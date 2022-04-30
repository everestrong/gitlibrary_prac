from flask import redirect, render_template, request
import sqlite3


con=sqlite3.connect("library.db", check_same_thread=False)
cur=con.cursor()

class Customer:
    def __init__(self):
        pass

    def displayCustomers(self):
        if request.method=='POST':
            pass
        sqlCustomers = '''SELECT * FROM customers'''
        cur.execute(sqlCustomers)
        customers = cur.fetchall()
        return render_template("/customers/displaycustomers.html", customers=customers)

    def addnewcustomer(self):
        if request.method=='POST':
            customerID = request.form.get('customerID')
            cusname = request.form.get('cusname')
            cuscity = request.form.get('cuscity')
            cusage = request.form.get('cusage')
            cur.execute(f'''INSERT INTO customers VALUES("{customerID}", "{cusname}", "{cuscity}", {int(cusage)})''')
            con.commit()
        return render_template("/customers/addnewcustomer.html")
    
    def removeCustomer(self):
        if request.method=='POST':
            cusname = request.form.get('cusname')
            customerID=request.form.get('customerID')
            sqlRem = (f'''DELETE FROM customers where cusname="{cusname}" and customerID="{customerID}"''')
            cur.execute(sqlRem)
            con.commit()
            cRem="Customer removed!"
            goToBookDatabase="Click here"
            goBack="to go back."
            return render_template("/customers/removecustomer.html", cRem=cRem, goToBookDatabase=goToBookDatabase, goBack=goBack)
        return render_template("/customers/removecustomer.html")
    
    def findCustomer(self):
        if request.method=="POST":
            cusname=request.form.get("cusname")
            findCust = (f'''SELECT * FROM customers where cusname like "%{cusname}%"''')
            cur.execute(findCust)
            cust = cur.fetchall()
            return render_template("/customers/findcustomer.html", cust=cust)
        return render_template("/customers/findcustomer.html")