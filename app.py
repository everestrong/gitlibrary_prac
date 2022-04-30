import json
from flask import Flask , render_template, request
import sqlite3 
from sqlite3 import Error



con = sqlite3.connect('library.db', check_same_thread=False)
cur = con.cursor()


def initDB():
    try:
        pass
    # Create table
        cur.execute("CREATE TABLE books (ID int, bookname text, author text, yearpublished int, booktype int,loanstatus text )")
        cur.execute("CREATE TABLE customers (customerID int, cusname text, cuscity text, cusage int)")
        cur.execute("CREATE TABLE loans (customerID int, bookID int, loandate int, returndate int)")
        
        #added only one time  first patameters,only for exemple
        cur.execute('''INSERT INTO books VALUES(1, "The Transformers 1", "Optimus Prime", 1987, 1,"Available")''')
        cur.execute('''INSERT INTO books VALUES(2, "The Transformers 2", "Megatron", 1987, 2,"Available")''')
        cur.execute('''INSERT INTO books VALUES(3, "WWF", "Diezel", 1999, 3,"Available")''')
        cur.execute('''INSERT INTO customers VALUES(1, "Avi ron", "Netanya", 23)''')
        cur.execute('''INSERT INTO customers VALUES(2, "Mati fon", "Kadima", 32)''')
        cur.execute('''INSERT INTO customers VALUES(3, "Shuli chan ", "nahariya", 33)''')
        
    except:
        print("table already exist")
    else:
        print("table created sucessfuly")
    # Insert a row of data
    # cur.execute('''INSERT INTO books VALUES(1, "The Transformers 1", "Optimus Prime", 1987, 1,"Available")''')
    # cur.execute('''INSERT INTO books VALUES(2, "The Transformers 2", "Megatron", 1987, 2,"Available")''')
    # cur.execute('''INSERT INTO books VALUES(3, "WWF", "Diezel", 1999, 3,"Available")''')
    # cur.execute('''INSERT INTO customers VALUES(4, "Avi ron", "Netanya", 23)''')
    # cur.execute('''INSERT INTO customers VALUES(5, "Mati fon", "Kadima", 32)''')
    # cur.execute('''INSERT INTO customers VALUES(6, "Shuli chan ", "nahariya", 33)''')
    # Save (commit) the changes
    con.commit()
initDB()
api = Flask(__name__)
@api.route('/')
def hello(): #  from thr  method send string 
    return 'Hello, World!'
# index is : the home page
@api.route('/home', methods=['GET', 'POST'])
def get_about():    
    return render_template('home.html') 
# send string that was rendered from html file with books data parameter
@api.route('/books/books')
def books():
    return render_template('books/books.html')

@api.route('/books/displayallbooks')
def displayallbooks():    
    return libbooks.Book.displayallbooks(libbooks)

@api.route('/books/addnewbook', methods=['GET', 'POST'])
def addnewbook():
    return libbooks.Book.addNewBook(libbooks)

@api.route('/books/findbook',methods=['GET', 'POST'])
def findbook():
    return libbooks.Book.findBook(libbooks)

@api.route('/books/removebook',methods=['GET', 'POST'])
def removebook():
    return libbooks.Book.removeBook(libbooks)

# send string that was rendered from html file with customers data parameter
@api.route('/customers/customers')
def customers():
    return render_template('customers/customers.html')

@api.route('/customers/addnewcustomer', methods=['GET', 'POST'])
def addnewcustomer():
    return libcust.Customer.addnewcustomer(libcust)

@api.route('/customers/displaycustomers')
def displaycustomers():
    return libcust.Customer.displayCustomers(libcust)

@api.route('/customers/findcustomer', methods=['GET', 'POST'])
def findcustomer(): 
    return libcust.Customer.findCustomer(libcust)

@api.route('/customers/removecustomer', methods=['GET', 'POST'])
def removecustomer():
    return libcust.Customer.removeCustomer(libcust)
# send string that was rendered from html file with loans data parameter
@api.route('/loans/loans')   
def loans():    
    return render_template('loans/loans.html')

@api.route('/loans/loanbook', methods=['GET', 'POST'])   
def loanbook():    
    return libloans.Loan.loanbook(libloans)

@api.route('/loans/returnbook', methods=['GET', 'POST'])
def returnbook():    
    return libloans.Loan.returnbook(libloans)

@api.route('/loans/display_all_loans')
def display_all_loans():    
    return libloans.Loan.display_all_loans(libloans)

@api.route('/loans/display_late_loans', methods=['GET', 'POST'])
def display_late_loans():    
    return libloans.Loan.display_late_loans(libloans)



if __name__ == '__main__':
    api.run(debug=True,port=9000)
