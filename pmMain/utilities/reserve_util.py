from ..models import (
    Reserve
)
from . import date_util

def calculateReserve():
    all_res = Reserve.objects.all()
    myIn = 0
    myOut = 0
    for res in all_res:
        if res.direction == "IN":
            myIn += res.amount
        else:
            myOut += res.amount
    myNet= myIn-myOut
    return (myIn,myOut,myNet)

def calculateMonthlyReserve(monthly_summary,reserves):
    total_reserve = 0
    for reserve in reserves:
        month = date_util.getMonthName(reserve.date)
        if month in monthly_summary:   
            if reserve.direction == 'IN':
                monthly_summary[month]['reserve'] += reserve.amount
                total_reserve += reserve.amount
            else:
                total_reserve -= reserve.amount
                monthly_summary[month]['reserve'] -= reserve.amount
        else:
            if reserve.direction == 'IN':
                monthly_summary[month] = {'reserve':reserve.amount, 'month':month}
                total_reserve += reserve.amount
            else:
                total_reserve -= reserve.amount
                monthly_summary[month] = {'reserve':reserve.amount*-1, 'month':month}
    return [{**monthly_summary},total_reserve]
