from pmMain.models import (Owner, Prop_Name, Reserve, Room_Info,  Expenses, Earnings ,Room_Transactions)
from pmMain.utilities.csv_util import *
                                                                          
reserves = Reserve.objects.all()
rooms = Room_Info.objects.all()                                                                                                             
expenses = Expenses.objects.all()
earnings = Earnings.objects.all()
room_ts =Room_Transactions.objects.all()
csv_rooms_transactions(room_ts)                                                                                                             
csv_reserve_info(reserves)                                                                                                                  
csv_expenses(expenses)
csv_earnings(earnings)
csv_rooms_info(rooms)



