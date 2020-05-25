from . import date_util
def calculateMonthlyEarnings(my_dict,earnings,expenses):
    monthly_summary = {**my_dict}
    total_income=0
    total_expense = 0
    
    for earning in earnings:
        month = date_util.getMonthName(earning.date)
        total_income += earning.amount
        #month exists
        if month in monthly_summary:
            #month exists and earnings exist
            if 'income' in monthly_summary[month].keys():
                monthly_summary[month]['income'] += earning.amount
            #month exists but no earnings yet
            else:
                monthly_summary[month]['income'] = earning.amount
            #month does not exist
        else: 
            monthly_summary[month] = {'month':month,'income':earning.amount}
    
    for expense in expenses:
        month = date_util.getMonthName(expense.date)
        total_expense += expense.amount
        #month exists
        if month in monthly_summary:
            #month exists and earnings exist
            if 'expense' in monthly_summary[month].keys():
                monthly_summary[month]['expense'] += expense.amount
            #month exists but no earnings yet
            else:
                monthly_summary[month]['expense'] = expense.amount
            #month does not exist
        else: 
            monthly_summary[month] = {'month':month,'expense':expense.amount}
    
    total_profit = total_income-total_expense

    return [total_income,total_expense,total_profit,{**monthly_summary}]
