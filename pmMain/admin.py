from django.contrib import admin
from .models import Owner, Prop_Name, Reserve, Room_Info,  Expenses, Earnings ,Room_Transactions
# Register your models here.
admin.site.register(Owner)
admin.site.register(Prop_Name)
admin.site.register(Reserve)
admin.site.register(Room_Info)
admin.site.register(Expenses)
admin.site.register(Earnings)
admin.site.register(Room_Transactions)

