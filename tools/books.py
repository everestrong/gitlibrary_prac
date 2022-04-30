from flask import render_template, request
import sqlite3


con=sqlite3.connect("library.db", check_same_thread=False)
cur=con.cursor()

class Book:
     def __init__(self,bookID,bookname,author,yearpublished,booktype):
        self.bookID=bookID
        self.bookname=bookname
        self.author=author
        self.yearpublished=yearpublished
        self.booktype=booktype 

     def addNewBook(self):
                msg=[]
                if request.method=='POST':
                    self.ID=request.form.get('ID')
                    self.bookname =request.form.get('bookname')
                    self.author = request.form.get('author')
                    self.yearpublished = request.form.get('yearpublished')
                    self.booktype = request.form.get('booktype')
                    try:
                        cur.execute("INSERT INTO books (ID,bookname,author,yearpublished,booktype) VALUES (?,?,?,?,?)",((self.ID,self.bookname,self.author,self.yearpublished,self.booktype)))
                        cur.execute(f'''UPDATE books SET loanstatus = 'Available'  WHERE ID={self.ID}''')
                        con.commit()
                    except:
                        msg="book already exists" 
                    else:
                        msg="book added"    
                return render_template("/books/addnewbook.html",msg=msg)



     def displayallbooks(self):
        if request.method=='POST':
            pass
        SQL = "SELECT * FROM books"
        cur.execute(SQL)
        books = cur.fetchall()
        return render_template("/books/displayallbooks.html", books=books)

     def findBook(self):
        if request.method=='POST':
            bookname = request.form.get('bookname')
            author=request.form.get('author')
            SQL = (f'''select * from books where bookName like "%{bookname}%" and Author like "%{author}%"''')
            cur.execute(SQL)
            books = cur.fetchall()
            return render_template("/books/findbook.html", books=books)
        return render_template("/books/findbook.html")

     def removeBook(self):
        if request.method=='POST':
            bookname=request.form.get('bookname')
            ID=request.form.get('ID')
            sql=(f'''DELETE FROM books where bookname="{bookname}" and ID="{ID}"''')
            cur.execute(sql)
            con.commit()
            bRem="Book removed!"
            goToBookDatabase="Click here"
            goDB="to go to display all books."   
            return render_template("/books/removebook.html", bRem=bRem, goToBookDatabase=goToBookDatabase, goDB=goDB)
        return render_template("/books/removebook.html")