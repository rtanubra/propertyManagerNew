from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import CreateView,DetailView,UpdateView
from django.http import HttpResponseRedirect
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import (
    Owner,
    Prop_Name,
    Room_Info,
    Earnings,
    Expenses,
    Reserve,
    Room_Transactions
)
from .forms import (
    EarningsModelForm,
    ExpensesModelForm,
    ReserveModelForm,
    RoomTransactionsModelForm,
    RoomInformationsModelForm,
    RoomAllTransactionsModelForm
)

from .utilities import(
    reserve_util,
    date_util,
    earnings_util,
    csv_util
)

# Create your views here.
            #Summaries
def earningsSummary(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    earnings= Earnings.objects.all()
    expenses = Expenses.objects.all()
    reserves = Reserve.objects.all()
    reserve_info = reserve_util.calculateMonthlyReserve({},reserves)
    total_reserve =reserve_info[1]
    monthly_summary = {**reserve_info[0]}
    
    earnings_info =earnings_util.calculateMonthlyEarnings(monthly_summary,earnings,expenses)
    monthly_summary = {**earnings_info[3]}
    total_income = earnings_info[0]
    total_expense = earnings_info[1]
    total_profit = earnings_info[2] 
    after_reserve = total_profit - total_reserve
    monthly_summary_list = []
    for m in monthly_summary:
        monthly_summary_list.append([m,0,0,0,0])
        if 'income' in monthly_summary[m].keys():
            monthly_summary_list[-1][1]= monthly_summary[m]['income']
        if 'expense' in monthly_summary[m].keys():
            monthly_summary_list[-1][2]= monthly_summary[m]['expense']
        if 'reserve' in monthly_summary[m].keys():
            monthly_summary_list[-1][3]= monthly_summary[m]['reserve']
        monthly_summary_list[-1][4] = monthly_summary_list[-1][1]-monthly_summary_list[-1][2]-monthly_summary_list[-1][3]

    return render(request, 'pmMain/summaries/earningsSummary.html',
        {   
            'monthly_summary':monthly_summary,
            'monthly_summary_list':monthly_summary_list,
            'total_income':total_income,
            'total_expense':total_expense,
            'total_reserve':total_reserve,
            'after_reserve':after_reserve
        }
    )

def reserveSummary(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    my_res = reserve_util.calculateReserve()
    reserves=[]
    reserves = Reserve.objects.all().order_by('-date')
    for res in reserves:
        res.month = date_util.getMonthName(res.date)
    return render(request,'pmMain/summaries/reserveSummary.html',
    {
        'resIn':my_res[0],
        'resOut':my_res[1],
        'resNet':my_res[2],
        'reserves':reserves
    })


def roomsTransSummary(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    room_trans = Room_Transactions.objects.all().order_by('-date')
    room_total = 0
    room_totals = {}
    room_totals_list = []
    for room_tran in room_trans:
        if room_tran.room_no in room_totals:
            room_totals[room_tran.room_no] += room_tran.amount
        else:
            room_totals[room_tran.room_no] = room_tran.amount
        room_total += room_tran.amount

    for k,v in room_totals.items():
        room_totals_list.append([k,v])
    

    return render(request,'pmMain/summaries/roomTransactions.html',{
        'room_total':room_total,
        'room_totals':room_totals_list
    })


def roomsInfoSummary(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    tenants = Room_Info.objects.all().order_by('room_no')
    active_tenants= []
    active_rooms= 0
    anticipated_rent = 0
    for tenant in tenants:
        if tenant.active_room:
            active_rooms += 1
            anticipated_rent += tenant.rent
            active_tenants.append(tenant)

    return render(request,'pmMain/summaries/roomInformation.html',{
        'tenants':active_tenants,
        'active_rooms':active_rooms-1,
        'anticipated_rent':anticipated_rent-1
    })

#List Views
def earningsList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    earnings= Earnings.objects.all().order_by('-date')
    for e in earnings:
        e.month = date_util.getMonthName(e.date)

    return render(request,'pmMain/list/listEarnings.html',{
        'earnings':earnings
    })

def expensesList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    expenses = Expenses.objects.all().order_by('-date')
    for e in expenses:
        e.month= date_util.getMonthName(e.date)
    return render(request,'pmMain/list/listExpenses.html',{
        'expenses':expenses
    })

def roomsTransList(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    room_transactions = Room_Transactions.objects.all().order_by('-date')
    for rt in room_transactions:
        rt.month= date_util.getMonthName(rt.date)
    return render(request,'pmMain/list/listRoomTransactions.html',{
        'room_transactions':room_transactions
    })
#Update Views
class ReserveUpdate(LoginRequiredMixin,UpdateView):
    model = Reserve
    fields= ['direction','name','comment','amount','date']
    template_name = 'pmMain/detail/detailReserve.html'
    
    def get_success_url(self):
        return '/reserve'

class EaerningsUpdate(LoginRequiredMixin,UpdateView):
    model = Earnings
    fields = ['name','date','amount','comment','room_no']
    template_name = 'pmMain/detail/detailEarning.html'
    
    def get_success_url(self):
        return '/earnings/list'

class ExpensesUpdate(LoginRequiredMixin,UpdateView):
    model = Expenses
    fields = ['name','date','amount','comment']
    template_name = 'pmMain/detail/detailExpense.html'

    def get_success_url(self):
        return '/expenses/list'

class RoomInfoUpdate(LoginRequiredMixin,UpdateView):
    model = Room_Info
    fields = [
        'room_no',
        'rent','key_deposit','last_month',
        'name','email','phone_no'
    ]
    template_name = 'pmMain/detail/detailRoomI.html'
    def get_success_url(self):
        return '/roomsi'
class RoomTranUpdate(LoginRequiredMixin,UpdateView):
    model = Room_Transactions
    fields = ['name','date','amount','comment','room_no']
    template_name = 'pmMain/detail/detailRoomT.html'
    def get_success_url(self):
        return '/roomst/list'

#Delete Views 
def reserve_delete_view(request,id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    obj = get_object_or_404(Reserve,id=id)
    context = {
        'object':obj
    }
    if request.method == "POST":
        obj.delete()
        return redirect('/reserve')

    return render(request,'pmMain/delete/deleteReserve.html',context)

def earning_delete_view(request,id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    obj = get_object_or_404(Earnings,id=id)
    context = {
        'object':obj
    }
    if request.method == "POST":
        obj.delete()
        return redirect('/earnings/list')
    
    return render(request,'pmMain/delete/deleteEarning.html',context)

def expense_delete_view(request,id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    obj = get_object_or_404( Expenses ,id=id)
    context = {
        'object':obj
    }
    if request.method == "POST":
        obj.delete()
        return redirect('/expenses/list')
    
    return render(request,'pmMain/delete/deleteExpense.html',context)

def roomTransaction_delete_view(request,id):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    obj = get_object_or_404(Room_Transactions,id=id)
    context = {
        'object':obj
    }
    if request.method == "POST":
        obj.delete()
        return redirect('/roomst/list')
    
    return render(request,'pmMain/delete/deleteRoomT.html',context)

#CREATE Views using simple class
class EarningsCreateView(LoginRequiredMixin,CreateView):
    model = Earnings
    form_class = EarningsModelForm
    template_name= 'pmMain/add/addEarnings.html'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        #Validation can be done here 
        self.object.save()
        #Save this into Room Transactions too
        Room_Transactions.objects.create(
            name = self.request.POST['name'],
            date = self.request.POST['date'],
            amount = self.request.POST['amount'],
            comment = self.request.POST['comment'],
            prop_name = Prop_Name.objects.get(id=self.request.POST['prop_name']),
            room_no = Room_Info.objects.get(id=self.request.POST['room_no'])
        ).save()

        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return '/earnings'

class RoomTCreateView(LoginRequiredMixin,CreateView):
    model = Room_Transactions
    form_class = RoomTransactionsModelForm
    template_name= 'pmMain/add/addRoomsT.html'
    def form_valid(self,form):
        self.object = form.save(commit=False)
        #Validation can be done here 
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return '/roomst'

class RoomAllTCreateView(LoginRequiredMixin,CreateView):
    model = Room_Transactions
    form_class = RoomAllTransactionsModelForm
    template_name='pmMain/add/addAllRoomsT.html'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        all_tenants = Room_Info.objects.filter(active_room=True)
        my_post = self.request.POST

        for tenant in all_tenants:
            #To Implicitly omit my expenses
            
            if tenant.rent > 2:
                """
                myObj = {
                    'name' :my_post["name"] + 'rm ' + str(tenant.room_no),
                    'date' : my_post['date'],
                    'amount' : tenant.rent *-1,
                    'comment' : my_post['comment'] + 'rm '+ str(tenant.room_no),
                    'prop_name' : tenant.prop_name,
                    'room_no':tenant.room_no
                }
                print(myObj)
            """
                Room_Transactions.objects.create(
                    name = self.request.POST['name'] + ' rm ' + str(tenant.room_no),
                    date = self.request.POST['date'],
                    amount = tenant.rent *-1,
                    comment = self.request.POST['comment'] + ' rm ' + str(tenant.room_no),
                    prop_name = tenant.prop_name,
                    room_no = Room_Info.objects.get(room_no=tenant.room_no)
                ).save()
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return '/roomst'

class RoomICreateView(LoginRequiredMixin,CreateView):
    model=Room_Info
    form_class = RoomInformationsModelForm
    template_name='pmMain/add/addRoomsI.html'
    
    def form_valid(self,form):
        self.object = form.save(commit=False)
        #Validation can be done here 
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return '/roomsi'

class ExpensesCreateView(LoginRequiredMixin,CreateView):
    model = Expenses
    form_class = ExpensesModelForm
    template_name= 'pmMain/add/addExpenses.html'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        #Validation can be done here 
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return '/earnings'

class ReserveCreateView(LoginRequiredMixin,CreateView):
    model = Reserve
    form_class = ReserveModelForm
    template_name = 'pmMain/add/addReserve.html'

    def form_valid(self,form):
        self.object = form.save(commit=False)
        #Validation can be done here 
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return '/reserve'

def analysis(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    #load csv files.
    reserves = Reserve.objects.all()
    rooms = Room_Info.objects.all()                                                                                                             
    expenses = Expenses.objects.all()
    earnings = Earnings.objects.all()
    room_ts =Room_Transactions.objects.all()
   
    csv_util.csv_reserve_info(reserves)                                                                                                                  
    csv_util.csv_expenses(expenses)
    csv_util.csv_earnings(earnings)
    csv_util.csv_rooms_info(rooms)
    csv_util.csv_rooms_transactions(room_ts)
    csv_util.csv_everything()
                                                                                                    
    expenses_j = list(Expenses.objects.values('amount','date'))
    earnings_j = list(Earnings.objects.values('amount','date'))
    reserve_j = list(Reserve.objects.values('amount','date','direction'))
    
    for e in earnings_j:
        e['date'] = date_util.getMonthName(e['date'])
        e['amount'] =  e['amount'] 
    
    for e in expenses_j:
        e['date'] = date_util.getMonthName(e['date'])
    
    for r in reserve_j:
        r['date'] = date_util.getMonthName(r['date'])
        if r['direction'] == 'OUT':
            r['amount'] = r['amount']*-1

    context = {
       'expenses':expenses_j,
       'earnings':earnings_j,
       'reserve':reserve_j
    }

    return render(request, 'pmMain/files/download.html',context)

    
