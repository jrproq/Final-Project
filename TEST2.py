from tkinter import * 
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
import tkinter
import random
import pymysql
import csv
from datetime import datetime
import numpy as np

# Your existing connectDB function
def connectDB ():
    conn=pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='itc_database_admin'
    )
    return conn

conn= connectDB()
cursor=conn.cursor()

# Existing functions go here...

def login():
    def check_login():
        username = username_entry.get()
        password = password_entry.get()

        cursor.connection.ping()
        sql = "SELECT * FROM admin WHERE username=%s AND password=%s"
        cursor.execute(sql, (username, password))

        result=cursor.fetchall()
        if result:
            messagebox.showinfo("Success", "Login Successful")
            login_window.destroy()  # Close login windo==AAw
            main_application()  # Call to open the inventory system window
        else:
            messagebox.showerror("Error", "Invalid Credentials")
        conn.close()

    login_window = tk.Tk()
    login_window.title("Login")

    tk.Label(login_window, text="Username").grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(login_window, text="Password").grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(login_window, show='*')
    password_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Button(login_window, text="Login", command=check_login).grid(row=2, column=0, columnspan=2, pady=10)

    login_window.mainloop()


def main_application():
    window = tkinter.Tk()
    window.title("Inventory System")
    window.geometry("720x640")
    btnColor ="#53d769"

    my_Tree = ttk.Treeview(window, show='headings', height=20)
    my_Tree['columns'] = ("Product ID", "Name", "Price", "Quantity", "Category", "Date")

    # Set column properties
    my_Tree.column("#0", width=0, stretch=NO)
    my_Tree.column("Product ID", anchor=W, width=100)
    my_Tree.column("Name", anchor=W, width=100)
    my_Tree.column("Price", anchor=W, width=100)
    my_Tree.column("Quantity", anchor=W, width=100)
    my_Tree.column("Category", anchor=W, width=150)
    my_Tree.column("Date", anchor=W, width=100)

    my_Tree.heading("Product ID", text="Product ID", anchor=W)
    my_Tree.heading("Name", text="Name", anchor=W)
    my_Tree.heading("Price", text="Price", anchor=W)
    my_Tree.heading("Quantity", text="Quantity", anchor=W)
    my_Tree.heading("Category", text="Category", anchor=W)
    my_Tree.heading("Date", text="Date", anchor=W)

    my_Tree.tag_configure('orow', background="#EEEEEE")
    my_Tree.pack()

    # Create the manage and entries frame
    frame = tkinter.Frame(window, bg="#0e62a0")
    frame.pack()

    manageFrame=tkinter.LabelFrame(frame, text="Manage", borderwidth=5)
    manageFrame.grid(row=0, column=0, sticky="w", padx=[10,250], pady=20, ipadx=[6])

    saveBtn =Button(manageFrame, text ="SAVE", width=10, borderwidth=3, bg=btnColor, fg ='#0C0404', command=add)
    updateBtn =Button(manageFrame, text ="UPDATE", width=10, borderwidth=3, bg=btnColor, fg ='#0C0404',command=update)
    deleteBtn =Button(manageFrame, text ="DELETE", width=10, borderwidth=3, bg=btnColor, fg ='#0C0404', command= delete)
    selectBtn =Button(manageFrame, text ="SELECT", width=10, borderwidth=3, bg=btnColor, fg ='#0C0404', command=select)
    findBtn =Button(manageFrame, text ="FIND", width=10, borderwidth=3, bg=btnColor, fg ='#0C0404', command=find)
    clearBtn =Button(manageFrame, text ="CLEAR", width=10, borderwidth=3, bg=btnColor, fg ='#0C0404', command=clear)
    exportBtn =Button(manageFrame, text ="EXPORT AS XSLX", width=15, borderwidth=3, bg=btnColor, fg ='#0C0404', command=exportExcel)

    saveBtn.grid(row=0, column=0,padx=5,pady=5)
    updateBtn.grid(row=0, column=1,padx=5,pady=5)
    deleteBtn.grid(row=0, column=2,padx=5,pady=5)
    selectBtn.grid(row=0, column=3,padx=5,pady=5)
    findBtn.grid(row=0, column=4,padx=5,pady=5)
    clearBtn.grid(row=0, column=5,padx=5,pady=5)
    exportBtn.grid(row=0, column=6, padx=5, pady=5)

    # FORM
    entriesFrame=tkinter.LabelFrame(frame, text="Form", borderwidth=5)
    entriesFrame.grid(row=1, column=0, sticky="w ", padx=[10 ,20], pady=[20,20], ipadx=6)

    itemIdLabel=Label(entriesFrame, text="PRODUCT ID", anchor="e", width=10)
    nameLabel=Label(entriesFrame, text="NAME", anchor="e", width=10	)
    priceLabel=Label(entriesFrame, text="PRICE", anchor="e", width=10	)
    quantiLabel=Label(entriesFrame, text="QUANTITY", anchor="e", width=10	)
    categoryLabel=Label(entriesFrame, text="CATEGORY", anchor="e", width=10	)

    # the format and layout of the label in the left side
    itemIdLabel.grid(row=0, column=0, padx=10)
    nameLabel.grid(row=1, column=0, padx=10)
    priceLabel.grid(row=2, column=0, padx=10)
    quantiLabel.grid(row=3, column=0, padx=10)
    categoryLabel.grid(row=4, column=0, padx=10)

    # category array
    categoryArray= ['Mainstream Laptops', 'Premium Laptops', 'Gaming Laptops', 'Peripherals']   

    # the box after the label
    itemIdEntry=Entry(entriesFrame, textvariable=placeholderArray[0], width=79)
    nameEntry=Entry(entriesFrame, textvariable=placeholderArray[1], width=79)
    priceEntry=Entry(entriesFrame, textvariable=placeholderArray[2], width=79)
    quantiEntry=Entry(entriesFrame, textvariable=placeholderArray[3], width=79)
    categoryCombo=ttk.Combobox(entriesFrame, textvariable=placeholderArray[4], width=75, values=categoryArray) # calls the label at the top

    # layout of the input box
    itemIdEntry.grid(row=0, column=2, padx=5 , pady=5)
    nameEntry.grid(row=1, column=2, padx=5 , pady=5)
    priceEntry.grid(row=2, column=2, padx=5 , pady=5)
    quantiEntry.grid(row=3, column=2, padx=5 , pady=5)
    categoryCombo.grid(row=4, column=2, padx=5 , pady=5)

    # generating button
    generateidBtn=Button(entriesFrame, text="GENERATE ID", borderwidth=3, bg=btnColor, fg='#0C0404', command=generateID)
    generateidBtn.grid(row=0, column=3, padx=5, pady=5)


    window.resizable(False, False)
    window.mainloop()

 

    # Keep window open
    # Function calls related to the inventory system
    def read():
        cursor.connection.ping()
        sql=f"SELECT `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM `stocks` ORDER BY `id` ASC"
        cursor.execute(sql)
        results=cursor.fetchall()
        conn.commit()
        conn.close()
        return results
    def refreshTable():
            for data in my_Tree.get_children():
                my_Tree.delete(data)
            for array in read(  ):
                my_Tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")
            my_Tree.tag_configure('orow', background="#EEEEEE")
            my_Tree.pack()              
        
        
    # generate unique id 
    def generateID():
        itemId=''
        for i in range(0,5):
            randno=random.randrange(0,(len(numeric)-1))
            itemId=itemId+str(numeric[randno])
        rando=random.randrange(0, (len(alpha)-1))
        itemId= itemId + '-' + str(alpha[randno])
        print("Generated: " + itemId)
        setph(itemId,0) 
    # uhm
    def setph(word, num):
        for ph in range(0,5):
            if ph == num:
                placeholderArray[ph].set(word)

    # the inputed data would be place in sqlyog/database
    def add():
        itemId=str(itemIdEntry.get())  # get the item id from the entry
        name=str(nameEntry.get()) # get the name from the entry
        price=str(priceEntry.get()) # get the price from the entry
        quanti=str(quantiEntry.get()) # get the quantity from the entry
        cat=str(categoryCombo.get()) # get the category from the entry
        valid=True
        if not(itemId and itemId.strip()) or not(name and name.strip()) or not(price and price.strip()) or not(quanti and quanti.strip()) or not(cat and cat.strip()):
            messagebox.showwarning("","Please fill up all entries")
            return
        if len(itemId) < 5:
            messagebox.showwarning("","Invalid Item Id")
            return
        if(not(itemId[3]=='-')):
            valid=False
        for i in range(0,3):
            if(not(itemId[i] in numeric)):
                valid=False
                break
        if(not(itemId[4] in alpha)):
            valid=False
        if not(valid):
            messagebox.showwarning("","Invalid Item Id")
            return
        try:
            cursor.connection.ping()
            sql=f"SELECT * FROM stocks WHERE `item_id` = '{itemId}' "
            cursor.execute(sql)
            checkItemNo=cursor.fetchall()
            if len(checkItemNo) > 0:
                messagebox.showwarning("","Item Id already used")
                return
            else:
                cursor.connection.ping()
                sql=f"INSERT INTO stocks (`item_id`, `name`, `price`, `quantity`, `category`) VALUES ('{itemId}','{name}','{price}','{quanti}','{cat}')"
                cursor.execute(sql)
            conn.commit()
            conn.close()
            for num in range(0,5):
                setph('',(num))
        except Exception as e:
            print(e)
            messagebox.showwarning("","Error while saving ref: "+str(e))
            return
        refreshTable()
        

    # update function
    def update():
        selectedItemId = ''
        try:
            selectedItem = my_Tree.selection()[0]
            selectedItemId = str(my_Tree.item(selectedItem)['values'][0])
        except:
            messagebox.showwarning("", "Please select a data row")
        print(selectedItemId)
        itemId = str(itemIdEntry.get())
        name = str(nameEntry.get())
        price = str(priceEntry.get())
        quanti = str(quantiEntry.get())
        cat = str(categoryCombo.get())
        if not(itemId and itemId.strip()) or not(name and name.strip()) or not(price and price.strip()) or not(quanti and quanti.strip()) or not(cat and cat.strip()):
            messagebox.showwarning("","Please fill up all entries")
            return
        if(selectedItemId!=itemId):
            messagebox.showwarning("","You can't change Item ID")
            return
        try:
            cursor.connection.ping()
            sql=f"UPDATE stocks SET `name` = '{name}', `price` = '{price}', `quantity` = '{quanti}', `category` = '{cat}' WHERE `item_id` = '{itemId}' "
            cursor.execute(sql)
            conn.commit()
            conn.close()
            for num in range(0,5):
                setph('',(num))
        except Exception as err:
            messagebox.showwarning("","Error occured ref: "+str(err))
            return
        refreshTable()
        
    # delete 
    def delete():
        try:
            if(my_Tree.selection()[0]):
                decision = messagebox.askquestion("Delete", "Delete the selected data?")
                if(decision != 'yes'):
                    return
                else:
                    selectedItem = my_Tree.selection()[0]
                    itemId = str(my_Tree.item(selectedItem)['values'][0])
                    try:
                        cursor.connection.ping()
                        sql=f"DELETE FROM stocks WHERE `item_id` = '{itemId}' "
                        cursor.execute(sql)
                        conn.commit()
                        conn.close()
                        messagebox.showinfo("","Data has been successfully deleted")
                    except:
                        messagebox.showinfo("","Sorry, an error occured")
                    refreshTable()
        except:
            messagebox.showwarning("", "Please select a data row")

    # select function
    def select():
        try:
            selectedItem = my_Tree.selection()[0]
            itemId = str(my_Tree.item(selectedItem)['values'][0])
            name = str(my_Tree.item(selectedItem)['values'][1])
            price = str(my_Tree.item(selectedItem)['values'][2])
            quanti = str(my_Tree.item(selectedItem)['values'][3])
            cat = str(my_Tree.item(selectedItem)['values'][4])
            setph(itemId,0)
            setph(name,1)
            setph(price,2)
            setph(quanti,3)
            setph(cat,4)
        except:
            messagebox.showwarning("", "Please select a data row")

    # find function
    def find():
        itemId = str(itemIdEntry.get())
        name = str(nameEntry.get())
        price = str(priceEntry.get())
        quanti = str(quantiEntry.get())
        cat = str(categoryCombo.get())
        cursor.connection.ping()
        if(itemId and itemId.strip()):
            sql = f"SELECT `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks WHERE `item_id` LIKE '%{itemId}%' "
        elif(name and name.strip()):
            sql = f"SELECT `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks WHERE `name` LIKE '%{name}%' "
        elif(price and price.strip()):
            sql = f"SELECT `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks WHERE `price` LIKE '%{price}%' "
        elif(quanti and quanti.strip()):
            sql = f"SELECT `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks WHERE `quantity` LIKE '%{quanti}%' "
        elif(cat and cat.strip()):
            sql = f"SELECT `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks WHERE `category` LIKE '%{cat}%' "
        else:
            messagebox.showwarning("","Please fill up one of the entries")
            return
        cursor.execute(sql)
        try:
            result = cursor.fetchall()
            for num in range(0,5):
                setph(result[0][num],(num))
            conn.commit()
            conn.close()
        except:
            messagebox.showwarning("","No data found")

    def clear():
        for num in range(0,3):
            setph('',(num))
    # export as excel function
    def exportExcel():
        cursor.connection.ping()
        sql=f"SELECT `item_id`, `name`, `price`, `quantity`, `category`, `date` FROM stocks ORDER BY `id` DESC"
        cursor.execute(sql)
        dataraw=cursor.fetchall()
        date = str(datetime.now())
        date = date.replace(' ', '_')
        date = date.replace(':', '-')
        dateFinal = date[0:16]
        with open("stocks_"+dateFinal+".csv",'a',newline='') as f:
            w = csv.writer(f, dialect='excel')
            for record in dataraw:
                w.writerow(record)
        print("saved: stocks_"+dateFinal+".csv")
        conn.commit()
        conn.close()
        messagebox.showinfo("","Excel file downloaded")
        window.mainloop()
        # Assuming all the provided attributes and functions are used within this function
    refreshTable()

    window.mainloop()


# Start the login process
if __name__ == "__main__":
    login()
