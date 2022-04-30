import sqlite3
from datetime import datetime
from flask import render_template,request

con=sqlite3.connect("library.db", check_same_thread=False)
cur=con.cursor()

class Loan:
    def __init__(self):
        pass

 
    def loanbook(self):
        res=[]
        if request.method == "POST":
            customerID=request.form.get("customerID")
            bookID=request.form.get("bookID")
            loandate=request.form.get("loandate")
            for row in cur.execute(f'''SELECT loanstatus from books WHERE ID={bookID} '''):
                    loanstatus=row[0]
                    if(loanstatus == 'Not Available'):
                        res.append("book isn't available")
                    else:
                        cur.execute("INSERT INTO loans (customerID,bookID,loandate) VALUES (?,?,?)",(customerID,bookID,loandate))
                        cur.execute(f"UPDATE books SET loanstatus ='Not Available' WHERE ID={bookID}")
                        con.commit()
                        res.append("Book is loaned")
                        return render_template("/loans/loanbook.html", res=res)
            return render_template("/loans/loanbook.html", res=res)
        return render_template("/loans/loanbook.html")
       

    def display_all_loans(self):
        if request.method=='POST':
            pass
        cur.execute('''SELECT * FROM loans''')
        loans = cur.fetchall()
        return render_template("/loans/display_all_loans.html", loans=loans)

    def returnbook(self):
        if request.method== "POST":
            self.bookID=request.form.get("bookID")
            self.returndate=datetime.now()
            cur.execute(f"DELETE FROM loans WHERE bookID={self.bookID}")
            cur.execute(f'''UPDATE books SET loanstatus = 'Available'  WHERE ID ={self.bookID}''')
            con.commit()
            return render_template("/loans/returnbook.html")
        return render_template("/loans/returnbook.html")


    def display_late_loans(self):
        global booktype,row
        dis=[]
        if request.method=='POST':
            self.bookID=request.form.get("bookID")
            for row in cur.execute(f'''SELECT loans.bookID, books.booktype, loans.loandate FROM loans
                                            INNER JOIN books ON loans.bookID = books.ID
                                            WHERE bookID={self.bookID}'''):
                            
                booktype=row[1]
                mdate1= datetime.now() - datetime.strptime(row[2], "%Y-%m-%d")
                Dtype1= (mdate1).days > 10
                Dtype2= (mdate1).days > 5
                Dtype3= (mdate1).days > 2
                if(booktype == 1 and Dtype1):
                    dis.append(("Book is late by" ,((mdate1).days-10),"days"))
                    return render_template('loans/display_late_loans.html',dis=dis)
                elif(booktype == 2 and Dtype2):
                    dis.append(("Book is late by" ,((mdate1).days-5),"days"))
                    return render_template('loans/display_late_loans.html',dis=dis)
                elif(booktype == 3 and Dtype3):
                    dis.append(("Book is late by" ,((mdate1).days-2),"days"))
                    return render_template('loans/display_late_loans.html',dis=dis)
                else:
                    dis.append(("Book isn't late"))
                    return render_template('loans/display_late_loans.html',dis=dis)
        return render_template('loans/display_late_loans.html',dis=dis)