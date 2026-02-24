from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox
import random
from database_details import DatabaseDetails

class phonebook:
    def __init__(self,root):
        #=======================Application name & background Image=============
        self.root=root
        self.root.title("PHONEBOOK APPLICATION")
        self.root.geometry("1525x840")
        self.db=DatabaseDetails()
        #/===============Image++++++++++++
        mainp=Image.open(r"D:\python projects\CONTACT BOOK PROJECT FILE\photos & icon\P7.png")
        mainp=mainp.resize((1525,840),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(mainp)
        label=Label(self.root,image=self.photoimg,bg="#484e45")
        label.place(x=-200,y=-125,width=1920,height=1080)
        #===============difine_variabls=========================================
        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))
        self.var_name=StringVar()
        self.var_gender=StringVar()
        self.var_email=StringVar()
        self.var_mobile=StringVar()
        self.search_var=StringVar()
        #=============Enterys & Focus on off functions==========================
        def on_enter(e):
            Name.delete(0,"end")
        def on_leave(e):
            name=Name.get()
            if name=="":
                Name.insert(0,"Enter Name")
        ref=ttk.Entry(self.root, textvariable=self.var_ref,font=("Verdana",4),state="readonly")
        ref.place(x=775,y=242,width=80,height=15)
        Name=Entry(self.root,textvariable=self.var_name,font=("Verdana",13),bg="#ffffff",bd="0",fg="#081B26")
        Name.place(x=140,y=128,width=380,height=40)
        Name.insert(0,"Enter Name")
        Name.bind("<FocusIn>",on_enter)
        Name.bind("<FocusOut>",on_leave)
        def on_enter(e):
            gender.delete(0,"end")
        def on_leave(e):
            Gender=gender.get()
            if gender=="":
                gender.insert(0,"Enter gender")
        gender=ttk.Combobox(self.root,textvariable=self.var_gender,font=("Verdana",13),state="readonly")
        gender["value"]=("Male","Female","other")
        gender.current(0)
        gender.place(x=127,y=230,width=408,height=50)
        gender.insert(0," Select gender")
        gender.bind("<FocusIn>",on_enter)
        gender.bind("<FocusOut>",on_leave)
        def on_enter(e):
            Email.delete(0,"end")
        def on_leave(e):
            email=Email.get()
            if Email=="":
                Email.insert(0,"Email")
        Email=Entry(self.root,textvariable=self.var_email,font=("Verdana",13),bg="#ffffff",bd="0",fg="#081B26")
        Email.place(x=140,y=340,width=380,height=40)
        Email.insert(0,"Email")
        Email.bind("<FocusIn>",on_enter)
        Email.bind("<FocusOut>",on_leave)
        Mobile=Entry(self.root,textvariable=self.var_mobile,font=("Verdana",13),bg="#ffffff",bd="0",fg="#081B26")
        Mobile.place(x=140,y=447,width=380,height=40)
        Mobile.insert(0,"mobile number")
        def on_enter(e):
            Mobile.delete(0,"end")
        def on_leave(e):
            MO=Mobile.get()
            if Mobile=="":
                Mobile.insert(0,"mobile number")
        Mobile.bind("<FocusIn>",on_enter)
        Mobile.bind("<FocusOut>",on_leave)
        self.txt_view=StringVar()
        #====================================SEARCH ENTERY================================================
        search=Entry(self.root,textvariable=self.txt_view,font=("Verdana",11),bg="#EDF2F2",bd="0",fg="#081B26")
        search.place(x=837,y=87,width=300,height=40)
        search.insert(0,"Select search option")
        def on_enter(e):
            search.delete(0,"end")
        def on_leave(e):
            Search=search.get()
            if search=="":
                search.insert(0,"Search using mobile number")
        search.bind("<FocusIn>",on_enter)
        search.bind("<FocusOut>",on_leave)        
        self.txt_serch=StringVar()
        #=====================================Buttons=======================
        New_add=Button(self.root,text="ADD NEW",bg="#113C32",font=("Verdana",17,"bold"),bd="0",activebackground="#113c32",fg="white",command=self.add_data)
        New_add.place(x=270,y=542,width=135,height=40)
        Update=Button(self.root,text="UPDATE",bg="#113C32",font=("Verdana",17,"bold"),bd="0",activebackground="#113c32",fg="white",command=self.update)
        Update.place(x=142,y=636,width=135,height=40)
        DELETE=Button(self.root,text="DELETE",bg="#113C32",font=("Verdana",18,"bold"),bd="0",activebackground="#113c32",fg="white",command=self.mdelete)
        DELETE.place(x=396,y=636,width=135,height=40)
        SEARCH=Button(self.root,text="SEARCH",bg="#113C32",font=("Verdana",14,"bold"),bd="0",activebackground="#113c32",fg="white",command=self.search)
        SEARCH.place(x=1268,y=88,width=100,height=40)
        all_V=Button(self.root,text="ALL",bg="#113C32",font=("Verdana",14,"bold"),bd="0",activebackground="#113c32",fg="white",command=self.fetch_data)
        all_V.place(x=1427,y=88,width=46,height=40)
        self.search_var=StringVar()
        combo_search=ttk.Combobox(self.root,textvariable=self.search_var,font=("Verdana",11),state="readonly")
        combo_search["value"]=(" mobile","name","email")
        combo_search.current(0)
        combo_search.place(x=752,y=85,width=80,height=46)
        #=============================TABLE FARAME=================================================
        T_FRAME=Frame(self.root,bg="#113C32")
        T_FRAME.place(x=770,y=160,width=702,height=540)
        scroll_x=ttk.Scrollbar(T_FRAME,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(T_FRAME,orient=VERTICAL)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        self.contact=ttk.Treeview(T_FRAME,columns=("ref","name","gender","email","mobile"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        #self.contact.pack(fill=X)
        scroll_x.config(command=self.contact.xview)
        scroll_y.config(command=self.contact.yview)
        #=========================attributes_name_of_table==========================================
        self.contact.heading("ref",text="ref")
        self.contact.heading("name",text="Name")
        self.contact.heading("gender",text="Gender")
        self.contact.heading("email",text="Email")
        self.contact.heading("mobile",text="Mobile Number")
        self.contact["show"]="headings"
        self.contact.pack(fill=BOTH,expand=1)
        self.fetch_data()
        #===============size_of_table_columns=================================
        self.contact.column(0,width=100)
        self.contact.column(1,width=150)
        self.contact.column(2,width=150)
        self.contact.column(3,width=200)
        self.contact.column(4,width=180)
        self.contact.bind("<ButtonRelease-1>",self.get_cur)
    #=====================Add button working==================================   
    def add_data(self):
        #====================duplicate value check==========================
        conn=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
        val_email=conn.cursor()
        val_contact=conn.cursor()
##        val_email.execute("select email from phonebook")
##        print(val_email.fetchall())
##        val_contact.execute("select mobile from phonebook")
##        print(val_contact.fetchall())
##        conn.commit()
        conn.close()
        if len(self.var_mobile.get())!=10 or self.var_mobile.get().isdecimal()==False:
            messagebox.showerror("Error","The dial number does not valid! \n please enter again",parent=self.root)
        elif (self.var_name.get()=="" or self.var_mobile.get()==""):
            messagebox.showerror("Error","Please Fill All Sections",parent=self.root)
        elif self.var_name.get()=="Enter Name" and self.var_mobile.get()=="mobile number" and self.var_email.get()=="Email":
            messagebox.showerror("Error","Fill Details Carefully",parent=self.root)
        elif self.var_email.get().find("@")==-1 or self.var_email.get().endswith("gmail.com" or "outlook.com")!=True or self.var_email.get().find(" ")!=-1:
            messagebox.showerror("Error","Email address does not valid \n please check",parent=self.root)
        else:
            conn=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
            cur=conn.cursor()
            cur.execute("insert into phonebook values(%s,%s,%s,%s,%s)",(self.var_ref.get(),self.var_name.get(),self.var_gender.get(),self.var_email.get(),self.var_mobile.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            self.var_ref=StringVar()
            x=random.randint(1000,9999)
            self.var_ref.set(str(x))
            messagebox.showinfo("hurray!","Contact has been added successfully",parent=self.root)
    #=====================fetching data from database  table=============================
    def fetch_data(self):
        conn=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
        cur=conn.cursor()
        cur.execute("select * from  phonebook order by name asc")
        data=cur.fetchall()
        if len(data)!=0:
            self.contact.delete(*self.contact.get_children())
            for i in data:
                self.contact.insert("",END, value=i)
            conn.commit()
        conn.close()
    #====================fetching data in Entries from table=============================
    def get_cur(self,event=""):
        cur_row=self.contact.focus()
        content=self.contact.item(cur_row)
        row=content["values"]
        self.var_ref.set(row[0]),
        self.var_name.set(row[1]),
        self.var_gender.set(row[2]),
        self.var_email.set(row[3]),
        self.var_mobile.set(row[4])
    #====================update button function==========================================
    def update(self):
        if self.var_name.get()=="Enter Name" and self.var_mobile.get()=="mobile number" and self.var_email.get()=="Email":
            messagebox.showerror("Error","Select a contect and do some change",parent=self.root)
        else:
            conn=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
            cur=conn.cursor()
            cur.execute("update phonebook set name=%s,gender=%s,email=%s,mobile=%s where ref=%s ",(
                self.var_name.get(),self.var_gender.get(),self.var_email.get(),self.var_mobile.get(),self.var_ref.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("hurray!","Data has been updated successfully",parent=self.root)
        
    #========================delete button function====================================
    def mdelete(self):
        mdelete=messagebox.askyesno("Yes or No","Do you want delete this contact",parent=self.root)
        if mdelete>0:
            conn=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
            cur=conn.cursor()
            query="delete from  phonebook where mobile=%s"
            value=(self.var_mobile.get(),)
            cur.execute(query,value)
            messagebox.showinfo("Deleted","Contact has been Delete successfully",parent=self.root)
        else:
            if not mdelete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
    #=====================search button function working===============================
    def search(self):
        conn=mysql.connector.connect(host=self.db.host,user=self.db.user,password=self.db.password,database=self.db.database)
        cur=conn.cursor()
        cur.execute("SELECT * FROM phonebook where "+str(self.search_var.get())+" LIKE '%"+str(self.txt_view.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.contact.delete(*self.contact.get_children())
            for i in rows:
                self.contact.insert("",END, value=i)
            conn.commit()
        conn.close()            
if __name__=="__main__":
    root=Tk()
    obj=phonebook(root)
        
