from django import forms
from .models import (
    Earnings, Expenses, Reserve,Room_Info,Room_Transactions,Room_Info
)

class DateInput(forms.DateInput):
    input_type='date'


class EarningsModelForm(forms.ModelForm):

    class Meta:
        model=Earnings
        widgets={
            'date':DateInput()
        }
        fields = ['prop_name','name','date','amount','comment','room_no']

class ExpensesModelForm(forms.ModelForm):
    class Meta:
        model=Expenses
        widgets={
            'date':DateInput(),
        }
        fields = ['prop_name','name','date','amount','comment','room_no']

class ReserveModelForm(forms.ModelForm):
    class Meta:
        model = Reserve 
        widgets={'date':DateInput()}
        fields = ['direction','name','date','amount','comment','prop_name']

class RoomTransactionsModelForm(forms.ModelForm):
    class Meta:
        model = Room_Transactions
        widgets ={'date':DateInput()}
        fields = ['prop_name','name','date','amount','comment','room_no']
class RoomAllTransactionsModelForm(forms.ModelForm):
    class Meta:
        model = Room_Transactions
        widgets ={'date':DateInput()}
        fields = ['prop_name','name','date','comment']

class RoomInformationsModelForm(forms.ModelForm):
    class Meta:
        model = Room_Info
        fields = [
            'room_no',
            'rent','key_deposit','last_month',
            'name','email','phone_no','prop_name','active_room'
            ]

