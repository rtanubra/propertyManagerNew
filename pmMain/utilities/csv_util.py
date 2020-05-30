#Used to pull data into an excel form
import os 
import csv


#output_path = os.getcwd()+'/csv_file_dump/'
output_path = os.getcwd()+'/static/csv/pm/'

def csv_rooms_transactions(transactions):
    fieldnames = [
        'name','date','amount','comment','room_no','prop_name'
    ]
    with open(output_path+'rooms_transactions.csv', 'w', newline='') as csvfile: 
        #Setup Writer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #Write header
        my_header = {}
        for fn in fieldnames:
                my_header[fn] = fn
        writer.writerow({**my_header})

        for rt in transactions:
            writer.writerow({
                'name':rt.name,
                'date':rt.date,
                'amount':rt.amount,
                'comment':rt.comment,
                'room_no':rt.room_no,
                'prop_name':rt.prop_name
            })

def csv_reserve_info(reserves):
    fieldnames = [
        'name','date','amount','comment','direction','prop_name'
    ]
    with open(output_path+'reserves.csv', 'w', newline='') as csvfile: 
        #Setup Writer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #Write header
        my_header = {}
        for fn in fieldnames:
                my_header[fn] = fn
        writer.writerow({**my_header})

        for rs in reserves:
            writer.writerow({
                'name':rs.name,
                'date':rs.date,
                'amount':rs.amount,
                'comment':rs.comment,
                'direction':rs.direction,
                'prop_name':rs.prop_name
            })



def csv_expenses(expenses):
    fieldnames = [
        'name','date','amount','comment','room_no','prop_name'
    ]
    with open(output_path+'expenses.csv', 'w', newline='') as csvfile: 
        #Setup Writer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #Write header
        my_header = {}
        for fn in fieldnames:
                my_header[fn] = fn
        writer.writerow({**my_header})

        for expense in expenses:
            writer.writerow({
                'name':expense.name,
                'date':expense.date,
                'amount':expense.amount,
                'comment':expense.comment,
                'room_no':expense.room_no,
                'prop_name':expense.prop_name
            })

def csv_earnings(earnings):
    fieldnames = [
        'name','date','amount','comment','room_no','prop_name'
    ]
    with open(output_path+'earnings.csv', 'w', newline='') as csvfile: 
        #Setup Writer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #Write header
        my_header = {}
        for fn in fieldnames:
                my_header[fn] = fn
        writer.writerow({**my_header})

        for ea in earnings:
            writer.writerow({
                'name':ea.name,
                'date':ea.date,
                'amount':ea.amount,
                'comment':ea.comment,
                'room_no':ea.room_no,
                'prop_name':ea.prop_name
            })

def csv_rooms_info(tenants):
    fieldnames = [
        'name', 'email','phone_no','room_no',
        'phone_no','rent','key_deposit','last_month','active_room'
    ]
    with open(output_path+'rooms_info.csv', 'w', newline='') as csvfile:    
        #Setup Writer
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #Write header
        my_header = {}
        for fn in fieldnames:
                my_header[fn] = fn
        writer.writerow({**my_header})
        for tenant in tenants:
            writer.writerow({
                'name':tenant.name,
                'email':tenant.email,
                'phone_no':tenant.phone_no,
                'room_no':tenant.room_no,
                'phone_no':tenant.phone_no,
                'rent':tenant.rent,
                'key_deposit':tenant.key_deposit,
                'last_month':tenant.last_month,
                'active_room':tenant.active_room
            })
   
