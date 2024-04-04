from tkinter import *
from tkinter import messagebox
import sqlite3
with sqlite3.connect('database.db') as con:
    cur = con.cursor()
# pasteAndIndent.action

class window(Tk):
    def introduction_page():
        # from tkinter import *
        root = Tk()

        h,w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
                
        bus = PhotoImage(file = ".\\Bus_for_project.png")
        Label(root, image = bus).grid(row = 0, column = 0, columnspan = 3, padx = w//3)
        Label(root, text = "                            " ).grid(row = 1, column = 0)

        title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'skyblue', font = 'calibri 22 bold')
        title.grid(row = 2, column = 0, padx = w//3)

        Label(root, text = "                            " ).grid(row = 3, column = 0)
        Label(root, text = "                            " ).grid(row =4 , column = 0)
        Label(root, text = "                            " ).grid(row = 5, column = 0)

        name = Label(root, text = "Name : Nitin Chaudhary ", fg = "blue1",font='calibri 17 bold')
        name.grid(row = 6, column = 0, padx = w//3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 7, column = 0)

        er = Label(root, text =" Er: 211B199", fg = "blue1",font='calibri 17 bold')
        er.grid(row =8, column =0, padx = w//3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 9, column = 0)

        mobile = Label(root, text = "Mobile: 6395299945", fg = "blue1",font='calibri 15 bold')
        mobile.grid(row = 10, column =0 , padx = w//3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 11, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 12, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 13, column = 0)


        submitted_to  = Label(root, text = "Press any key start booking", fg = "maroon1", bg = "skyblue", font= 'calibri 15 bold')
        submitted_to.grid(row = 14, column =0, padx = w//3)

        project_learning = Label(root, text = "Project Based Learning" , fg ='maroon1')
        project_learning.grid(row = 15, column = 0, padx = w//3)
        def fun(e=0):
            root.destroy()
            ob.home_page()
        root.bind('<KeyPress>',fun)


        root.mainloop()
    def home_page():
        # from tkinter import *
        root = Tk()

        h,w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))

        def seatbooking():
            root.destroy()
            ob.bus_ticket()

        def checkbooked():
            root.destroy()
            ob.check_booking()

        def adddetails():
            root.destroy()
            ob.add_details()


        bus = PhotoImage(file = ".\\Bus_for_project.png")
        Label(root, image = bus).grid(row = 0, column = 0, columnspan = 3, padx = w//3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 1, column = 1)

        title = Label(root, text = "Online Bus Booking System" , fg = 'maroon1' , bg = 'skyblue', font = 'calibri 16 bold')
        title.grid(row = 2, column = 0, columnspan = 3, padx = w//3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 3, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 4, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 5, column = 0)

        seat_booking = Button(root, text ="Seat Booking " , fg = 'blue1', bg ='limegreen',command=seatbooking)
        seat_booking.grid(row = 6, column = 0)

        check_booked_seat = Button(root, text ="Check Booked Seat" , fg = 'blue1', bg ='limegreen',command=checkbooked)
        check_booked_seat.grid(row = 6, column = 1)

        add_bus = Button(root, text ="Add Bus Details" , fg = 'blue1', bg ='green2',command=adddetails)
        add_bus.grid(row = 6, column = 2)

        blank = Label(root, text = "                            " )
        blank.grid(row = 7, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 8, column = 0)

        admin = Label(root, text = "For Admin Only", fg = 'maroon1')
        admin.grid(row = 9, column =2)



        root.mainloop()
        
    def seatbooking():
        # from tkinter import *
        # from tkinter import messagebox
        root = Tk()

        h,w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))

        clicked = StringVar()
        clicked.set("Male")

        # def sure():
        #     messagebox.askyesno("bus confirmation", "Are you sure you want to book the bus?")


        def book():
            global booked_bus_id
            booked_bus_id=rv1.get()
            booked_bus = booked_bus_id
            # global booked_bus_id
            print(booked_bus_id)
            # import sqlite3
            # with sqlite3.connect('database.db') as con:
            #     cur = con.cursor()
            # cur.execute('''insert into passenger(bus_id) values(?)''',(booked_bus_id))
            # con.commit()
            # To=ent_To.get()
            # From=ent_From.get() 
            # import sqlite3
            # with sqlite3.connect('database.db') as con:
            #     cur = con.cursor()
            # cur.execute('''insert into ticket(source,destination,rv1,mobile) values(?,?,?,?)''',(To,From,booked_bus_id,phone))
            # con.commit()
            

            # def rv():
            #     booked_bus_id=rv1.get()

            

            if booked_bus_id=='None':
                messagebox.showwarning("Warning", "Please select a bus")
            else:

                blank = Label(root, text = "                            " )
                blank.grid(row = 11, column = 0)

                blank = Label(root, text = "                            " )
                blank.grid(row = 12, column = 0)

                blank = Label(root, text = "                            " )
                blank.grid(row = 13, column = 0)

                blank = Label(root, text = "                            " )
                blank.grid(row = 14, column = 0)

                fill_label = Label(root, text = "Fill Passenger Details to book the bus ticket" , fg = 'maroon1' , bg = 'skyblue', font = 'calibri 15 bold')
                fill_label.grid(row = 15, column = 0, columnspan = 8)

                blank = Label(root, text = "                            " )
                blank.grid(row = 16, column = 0)

                name_text = Label(root, text = "Name")
                name_text.grid(row = 17, column=0)

                name_ent = Entry(root)
                name_ent.grid(row =17, column=1)
                name = name_ent.get()

                gender_text = Label(root, text = "Gender")
                gender_text.grid(row = 17, column=2)

                gender_drop = OptionMenu(root, clicked , "Male", "Female", "Third Gender")
                gender_drop.grid(row = 17, column = 3)
                gender = clicked.get()

                seats_text = Label(root, text = "No of Seats")
                seats_text.grid(row = 17, column=4)

                seats_ent = Entry(root)
                seats_ent.grid(row =17, column=5)
                Capacity = seats_ent.get()

                mobile_text = Label(root, text = "Mobile No")
                mobile_text.grid(row = 17, column=6)

                mobile_ent = Entry(root)
                mobile_ent.grid(row =17, column=7)
                phone = mobile_ent.get()
                # if(len(int(phone))!=10):
                #     messagebox.showwarning("Warning", "Please Enter Valid Mobile")
                    
                    

                age_text = Label(root, text = "Age")
                age_text.grid(row = 17, column=8)

                age_ent = Entry(root)
                age_ent.grid(row =17, column=9)
                age = age_ent.get()

            # phone = mobile_ent.get()
            # To=ent_To.get()
            # From=ent_From.get() 
            # import sqlite3
            # with sqlite3.connect('database.db') as con:
            #     cur = con.cursor()
            # cur.execute('''insert into ticket(source,destination,rv1,mobile) values(?,?,?,?)''',(To,From,booked_bus_id,phone))
            # con.commit()

            
            def book_seat():
                phone = mobile_ent.get()
                Capacity = seats_ent.get()
                # with sqlite3.connect('database.db') as con:
                #     cur = con.cursor()
                if(len(phone)!=10):
                    messagebox.showwarning("Warning", "Please Enter Valid 10 digit Mobile NO.")
                age = age_ent.get()
                if(int(age)<0 or int(age)>120):
                    
                    messagebox.showwarning("Warning", "Please Enter Valid age.")
                # global booked_bus_id
                # booked_bus_id=rv1.get()
                # with sqlite3.connect('database.db') as con:
                #     cur = con.cursor()
                cur.execute('''select availaible_seats from bus where bus_id=?''',[booked_bus])
                i= cur.fetchone()
                compare = i[0]
                con.commit()
                if(int(Capacity)>compare):
                    messagebox.showwarning("Warning", "Seats entered are greater than seats available")
                
                else:
                    answer = messagebox.askyesno("bus confirmation", "Are you sure you want to book the bus?")
                    if answer:
                        age = age_ent.get()
                        phone = mobile_ent.get()
                        Capacity = seats_ent.get()
                        gender = clicked.get()
                        name = name_ent.get()
                        travel_date=ent_date.get()
                        booked_bus_id=rv1.get()
                        To=ent_To.get()
                        From=ent_From.get() 
                    # booked_date = cur.execute('''SELECT getdate()''')
                    # print(booked_date)
                        # import sqlite3
                        # with sqlite3.connect('database.db') as con:
                        #     cur = con.cursor()
                        cur.execute('''insert into passenger(name,gender,no_of_seats,mob_no,age,travelling_date,booking_date,bus_id) values(?,?,?,?,?,?,DATE(),?)''',[name,gender,Capacity,phone,age,travel_date,booked_bus_id])
                        cur.execute('''insert into ticket(source,destination,rv1,mobile) values(?,?,?,?)''',(To,From,booked_bus_id,phone))
                
                        con.commit()
                        root.destroy()
                    
                    

            book_button = Button(root, text = "Book Seat", bg ="limegreen", command = book_seat)
            book_button.grid(row = 17, column=10)

                




            

            


        def show():
            select_text = Label(root, text = "Select Bus", fg = "green2")
            select_text.grid(row = 8, column=0)

            opt_text = Label(root, text = "Operator", fg = "green2")
            opt_text.grid(row = 8, column=1)

            type_text = Label(root, text = "Bus Type", fg = "green2")
            type_text.grid(row = 8, column=2)

            available_text = Label(root, text = "Available/Capacity", fg = "green2")
            available_text.grid(row = 8, column=3)

            fare_text = Label(root, text = "Fare", fg = "green2")
            fare_text.grid(row = 8, column=4)
            
            
            blank = Label(root, text = "                            " )
            blank.grid(row = 9, column = 0)

            # import sqlite3
            with sqlite3.connect('database.db') as con:
                cur = con.cursor()
        #     cur.execute('''select max(passenger_id) from passenger''')
        #     a=cur.fetchone()
        #     maxid = a[0]
        #     cur.execute('''select bus_id from passenger where passenger_id=?''',[maxid])
        #     z=cur.fetchone()
        #     busid = z[0]
        #     cur.execute('''select no_of_seats from passenger where passenger_id=?''',[maxid])
        #     p=cur.fetchone()
        #     booked_seats = p[0]
        #     cur.execute('''select availaible_seats from bus where bus_id=?''',[busid])
        #     w=cur.fetchone()
        #     availaibleseats = w[0]
        #     updated_seats = availaibleseats - booked_seats
        # # cur.execute('''select bus_id from passenger where passenger_id=?''',[maxid])
        # # z=cur.fetchone()
        # # busid = z[0]

        #     cur.execute('''update bus set availaible_seats =? where bus_id=?''',(updated_seats,busid))
        #     con.commit()
            # cur.execute('''select availaibl''')



            To=ent_To.get() 
            From=ent_From.get() 
            Date=ent_date.get()
            if(To=='' or From=='' or Date==''):
                messagebox.showwarning("EMPTY DETAILS", "PLEASE ENTER ALL DETAILS")
            # else(To='Guna')
                
            elif((To=='Delhi' or To=='Mathura' or To=='Agra') and (From=='Agra' or From=='Mathura' or From=='Delhi')) :
                if(Date=='2022-12-01' or Date=='2022-12-02' or Date=='2022-12-03' or Date=='2022-12-04' or Date=='2022-12-05' or Date=='2022-12-06' or Date=='2022-12-07' ):

                
                    To=ent_To.get()
                    From=ent_From.get() 
                    Date=ent_date.get()
                    cur.execute('''Select name,bus_type,capacity,fare,bus_id,availaible_seats from bus as a,bus_operator as b,route as f, route as t where f.station_name=? and t.station_name=? and f.station_id<t.station_id and f.route_id=t.route_id and t.route_id=f.route_id and a.op_id=b.op_id''',(From,To))
                    res=cur.fetchall()
                    num=10
                    for i in res:   
                        r1=Radiobutton(root,variable=rv1,value=i[4])
                        r1.grid(row=num,column=0)

                        operator1=Label(root, text = i[0], fg = "blue1")
                        operator1.grid(row = num, column=1)
                        operator=Label(root, text = i[1], fg = "blue1")
                        operator.grid(row = num, column=2)
                        b_type=Label(root, text = str(i[5])+'/'+str(i[2]), fg = "blue1")
                        b_type.grid(row = num, column=3)
                        seat=Label(root, text = i[3], fg = "blue1")
                        seat.grid(row = num, column=4)
                        num=num+1
                    booked_bus_id=rv1.get()
            
                    con.commit()
                    book_button = Button(root, text="Proceed to Book", bg = "limegreen", command = book)
                    book_button.grid(row =10 , column= 6, columnspan=2)
                else:
                    messagebox.showwarning("BUS", "BUS NOT AVAILAIBLE ON THIS DATE")
                    
            
            else:
                messagebox.showwarning("BUS", "BUS NOT AVAILAIBLE ON THIS ROUTE")
                

                
                











            
            
        rv1=StringVar()
        rv1.set(None)
        mobile_ent = IntVar()


                    
        bus = PhotoImage(file = ".\\Bus_for_project.png")
        Label(root, image = bus).grid(row = 0, column = 0, columnspan = 8, padx = w//3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 1, column = 1)

        title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'calibri 15 bold')
        title.grid(row = 2, column = 0, columnspan = 8)

        blank = Label(root, text = "                            " )
        blank.grid(row = 3, column = 0)

        title1 =Label(root, text = "Enter Journey Details", bg="lightgreen", fg = "darkgreen", font = "calibri 15 bold" )
        title1.grid(row=4, column = 0, columnspan =8 )


        blank = Label(root, text = "                            " )
        blank.grid(row = 5, column = 0)

        To_text = Label(root, text = "From")
        To_text.grid(row = 6, column =0)


        ent_To = Entry(root, width=20)
        ent_To.grid(row = 6, column =1)



        From_text = Label(root, text = "To")
        From_text.grid(row = 6, column =2)

        ent_From = Entry(root, width=20)
        ent_From.grid(row = 6, column =3)

        date_text = Label(root, text = "Journey Date(yyyy-mm-dd)")
        date_text.grid(row = 6, column =4)

        ent_date = Entry(root, width=20)
        ent_date.grid(row = 6, column =5)
        travel_date=ent_date.get()




        show_button = Button(root, text = "Show Bus", fg = "blue1", bg ="green2", command = show)
        show_button.grid(row = 6, column =6)

        def home():
            root.destroy()
            ob.home_page()

        house = PhotoImage(file = ".\\home.png")
        home_button = Button(root, image = house,command=home)
        home_button.grid(row =6 , column= 7)

        blank = Label(root, text = "                            " )
        blank.grid(row = 7, column = 0)






















        # ob.bus_ticket(rv1)
        root.mainloop()
    def bus_ticket():
        # from tkinter import *
        # from tkinter import messagebox
        ob.seatbooking()
        root = Tk()

        h,w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))

        def fun(e=0):
            root.destroy()
            ob.home_page()

        house = PhotoImage(file = ".\\home.png")
        house_but = Button(root, image=house,command=fun)
        house_but.grid(row = 14, column =1 )


                    
        bus = PhotoImage(file = ".\\Bus_for_project.png")
        Label(root, image = bus).grid(row = 0, column = 1, columnspan = 3, padx = w//3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 1, column = 1)

        title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'calibri 15 bold')
        title.grid(row = 2, column = 1, columnspan = 3, padx = w//3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 3, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 4, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 5, column = 0)

        ticket_text = Label(root, text ="Bus Ticket")
        ticket_text.grid(row = 6, column=1, columnspan=3)

        final = LabelFrame(root)
        final.grid(row = 7, column =1, columnspan=3)

        passenger_text = Label(final, text = "Passenger: ")
        passenger_text.grid(row =8, column=0)

        seats_text = Label(final, text = "No of seats: ")
        seats_text.grid(row =10, column=0)

        age_text = Label(final, text = "Age: ")
        age_text.grid(row =12, column=0, columnspan=2)

        travel_text = Label(final, text = "Travel On: ")
        travel_text.grid(row =14, column=0)

        seats_text = Label(final, text = "No of Seats: ")
        seats_text.grid(row =16, column=0)

        g_text = Label(final, text = "Gender: ")
        g_text.grid(row =8, column=2)

        phone_text = Label(final, text = "Phone: ")
        phone_text.grid(row =10, column=2)

        flare_text = Label(final, text = "Fare Rs: ")
        flare_text.grid(row =12, column=2)

        detail_text = Label(final, text = "Bus Detail: ")
        detail_text.grid(row =14, column=2)

        booked_text = Label(final, text = "Booked On: ")
        booked_text.grid(row =16, column=2)

        point_text = Label(final, text = "Boarding Point: ")
        point_text.grid(row =18, column=2)













        # import sqlite3
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()
        # booked_bus_id=rv1.get()
        # phone = mobile_ent.get()
        #print(booked_bus_id)
        # print(phone)
        cur.execute('''select max(passenger_id) from passenger''')
        a=cur.fetchone()
        maxid = a[0]
        cur.execute('''select fare from bus where bus_id=?''',[booked_bus_id])
        m=cur.fetchone()
        Fare = m[0]
        cur.execute('''select no_of_seats from passenger where passenger_id=?''',[maxid])
        k=cur.fetchone()
        seats=k[0]
        totalfare = str(Fare*seats)



        cur.execute('''select name,gender,no_of_seats,mob_no,age,travelling_date,booking_date,source from passenger,ticket where passenger_id=? ''',[maxid])
        res = cur.fetchall()
        for i in res:
            Label(final,text = i[0]).grid(row=8,column = 1)
            Label(final,text = i[1]).grid(row=8,column = 3)
            Label(final,text = i[2]).grid(row=10,column = 1)
            Label(final,text = i[3]).grid(row=10,column = 3)
            Label(final,text = i[4]).grid(row=12,column = 1)
            Label(final,text = i[5]).grid(row=14,column = 1)
            Label(final,text = i[6]).grid(row=16,column = 3)
            Label(final,text = i[7]).grid(row=18,column = 3)
            Label(final,text = i[2]).grid(row=16,column = 1)

        cur.execute('''select name from bus as a,bus_operator as b where a.op_id = b.op_id and bus_id=? ''',(booked_bus_id) )
        temp = cur.fetchall()
        for i in temp:
            Label(final,text = i[0]).grid(row=14,column = 3)
        cur.execute('''select bus_id from passenger where passenger_id=?''',[maxid])
        z=cur.fetchone()
        busid = z[0]
        cur.execute('''select no_of_seats from passenger where passenger_id=?''',[maxid])
        p=cur.fetchone()
        booked_seats = p[0]
        cur.execute('''select availaible_seats from bus where bus_id=?''',[busid])
        w=cur.fetchone()
        availaibleseats = w[0]
        updated_seats = availaibleseats - booked_seats
        # cur.execute('''select bus_id from passenger where passenger_id=?''',[maxid])
        # z=cur.fetchone()
        # busid = z[0]

        cur.execute('''update bus set availaible_seats =? where bus_id=?''',(updated_seats,busid))
        con.commit()
        str(updated_seats)
        # Label(final,text = '/'+str(updated_seats)).grid(row=10,column = 1)

            
        Label(final,text = ''+totalfare).grid(row=12,column = 3)
        last_text = Label(final, text = "Total amount Rs  "+totalfare+ "  to be paid at the time of boarding the bus")
        last_text.grid(row =20, column=0)




        root.mainloop()
        

    def add_details():
        # from tkinter import *
        # from tkinter import messagebox
        root = Tk()

        h,w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))

                    
        bus = PhotoImage(file = ".\\Bus_for_project.png")
        Label(root, image = bus).grid(row = 0, column = 0, columnspan = 3, padx = w//3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 1, column = 1)

        title = Label(root, text = "Online Bus Booking System" , fg = 'maroon1' , bg = 'lightblue', font = 'calibri 15 bold')
        title.grid(row = 2, column = 0, columnspan = 3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 3, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 4, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 5, column = 0)

        detail = Label(root, text = "Add New Details to Database", fg ="green2", font = 'calibri 15 bold')
        detail.grid(row = 6, column = 0, columnspan = 3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 7, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 8, column = 0)

        def newoperator():
            root.destroy()
            ob.add_bus_operator()

        def newbus():
            root.destroy()
            ob.add_bus_details()

        def newroute():
            root.destroy()
            ob.add_bus_route()
        def newrun():
            root.destroy()
            ob.add_bus_run()
        def fun():
            root.destroy()
            ob.home_page()

        operator_but= Button(root, text ="New Operator", bg = "green2",command=newoperator)
        operator_but.grid(row= 9, column=0)

        bus_but= Button(root, text ="New Bus", bg = "orange",command=newbus)
        bus_but.grid(row= 9, column=1)

        route_but= Button(root, text ="New Route", bg = "yellow",command=newroute)
        route_but.grid(row= 9, column=2)

        run_but= Button(root, text ="New Run", bg = "maroon1",command=newrun)
        run_but.grid(row= 9, column=3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 13, column = 0)

        blank = Label(root, text = "                            " )
        blank.grid(row = 14, column = 0)

        house = PhotoImage(file = ".\\home.png")
        house_but = Button(root, image=house,command=fun)
        house_but.grid(row = 15, column = 3)

        root.mainloop()
    def add_bus_route():
        # from tkinter import *
        # from tkinter import messagebox
        root = Tk()

        h,w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
                    
        bus = PhotoImage(file = ".\\Bus_for_project.png")
        Label(root, image = bus).grid(row = 0, column = 0, columnspan = 10, padx = w//3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 1, column = 1)

        title = Label(root, text = "Online Bus Booking System" , fg = 'maroon1' , bg = 'lightblue', font = 'calibri 14 bold')
        title.grid(row = 2, column = 0, columnspan = 10)

        blank = Label(root, text = "                            " )
        blank.grid(row = 3, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 4, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 5, column = 0)

        title = Label(root, text = "Add Bus Route Details" , fg = 'green3' , font = 'calibri 14 bold')
        title.grid(row = 6, column = 0, columnspan = 10)

        blank = Label(root, text = "                            " )
        blank.grid(row = 7, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 8, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 9, column = 0)

        route_text = Label(root, text = "Route Id")
        route_text.grid(row=10, column=0)

        route_ent = Entry(root)
        route_ent.grid(row=10, column=1)
        route_id=route_ent.get()

        stname_text = Label(root, text = "Station name")
        stname_text.grid(row=10, column=2)

        stname_ent = Entry(root)
        stname_ent.grid(row=10, column=3)
        stname = stname_ent.get()


        stid_text = Label(root, text = "Station ID")
        stid_text.grid(row=10, column=4)

        stid_ent = Entry(root)
        stid_ent.grid(row=10, column=5)
        stid=stid_ent.get()

        # import sqlite3
        with sqlite3.connect('database.db') as bus:
            cur = bus.cursor()

        def add_busroute():
            route_id=route_ent.get()
            stname = stname_ent.get()
            stid=stid_ent.get()
            if(route_id=='' or stname=='' or stid==''):
                messagebox.showwarning("EMPTY DETAILS", "PLEASE ENTER ALL DETAILS")
            else:
                cur.execute('''insert into route(route_id,station_name,station_id) values(?,?,?)''',(route_id,stname,stid))
                bus.commit()
                messagebox.showinfo('BUS ENTRY','BUS ADDED SUCCESFULLY')

        def del_busroute():
            route_id=route_ent.get()
            stname = stname_ent.get()
            stid=stid_ent.get()
            if(route_id=='' or stname=='' or stid==''):
                messagebox.showwarning("EMPTY DETAILS", "PLEASE ENTER ALL DETAILS")
            else:
                
                cur.execute('''delete from route where route_id=? and station_id=?''',(route_id,stid))
                bus.commit()
                messagebox.showinfo('BUS DELETE','BUS DELETION SUCCESFULL')


        def text():
            Label(root,text=" "+route_ent.get()+"  "+stname_ent.get()+"  "+stid_ent.get()).grid(row=11,column=4)



        add_but = Button(root, text = "Add Route", bg ="lightgreen",command=lambda:[add_busroute(),text()])
        add_but.grid(row = 10, column = 7)

        edit_but = Button(root, text = "Delete Route", fg = "maroon1", bg = "limegreen",command=del_busroute)
        edit_but.grid(row = 10, column = 8)

        blank = Label(root, text = "                            " )
        blank.grid(row = 11, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 12, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 13, column = 0)

        def home():
            root.destroy()
            ob.home_page()

        house = PhotoImage(file = ".\\home.png")
        house_but = Button(root, image=house,command=home)
        house_but.grid(row = 14, column = 6)

        root.mainloop()
    def add_bus_run():
        # from tkinter import *
        # from tkinter import messagebox
        root = Tk()

        h,w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
                    
        bus = PhotoImage(file = ".\\Bus_for_project.png")
        Label(root, image = bus).grid(row = 0, column = 0, columnspan = 10, padx = w//3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 1, column = 1)

        title = Label(root, text = "Online Bus Booking System" , fg = 'maroon1' , bg = 'lightblue', font = 'calibri 14 bold')
        title.grid(row = 2, column = 0, columnspan = 10)

        blank = Label(root, text = "                            " )
        blank.grid(row = 3, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 4, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 5, column = 0)

        title = Label(root, text = "Add Bus Running Details" , fg = 'green3' , font = 'calibri 14 bold')
        title.grid(row = 6, column = 0, columnspan = 10)

        blank = Label(root, text = "                            " )
        blank.grid(row = 7, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 8, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 9, column = 0)

        route_text = Label(root, text = "Bus Id")
        route_text.grid(row=10, column=0)


        route_ent = Entry(root)
        route_ent.grid(row=10, column=1)
        #a=route_ent.get()

        station_text = Label(root, text = "Running Date")
        station_text.grid(row=10, column=2)

        station_ent = Entry(root)
        station_ent.grid(row=10, column=3)
        #b=station_ent.get()

        id_text = Label(root, text = "Seat Available")
        id_text.grid(row=10, column=4)

        id_ent = Entry(root)
        id_ent.grid(row=10, column=5)
        #c=id_ent.get()

        # import sqlite3
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()

        def add_busrun():
            a=route_ent.get()
            b=station_ent.get()
            c=id_ent.get()
            if(a==''or b==''or c==''):
                
                messagebox.showwarning("EMPTY DETAILS", "PLEASE ENTER ALL DETAILS")
            else:
                cur.execute('''insert into running_details(bus_id,running_date,seat_availaible) values(?,?,?)''',(a,b,c))
                con.commit()
                con.close()
                Label(root,text=" "+route_ent.get()+"  "+station_ent.get()+"  "+id_ent.get()+"  ").grid(row=11,column=4,columnspan=3)
                messagebox.showinfo("BUS RUN","RUNNING DETAILS ADDED SUCCESFULLY")

        def del_busrun():
            a=route_ent.get()
            b=station_ent.get()
            c=id_ent.get()
            if(a==''or b==''or c==''):
                
                messagebox.showwarning("EMPTY DETAILS", "PLEASE ENTER ALL DETAILS")
            else:
                cur.execute('''delete from running_details where running_date=? and bus_id=?''',(b,a))
                con.commit()
                con.close()
                messagebox.showinfo("BUS RUN DELETED","RUNNING DETAILS DELETED SUCCESFULLY")





        add_but = Button(root, text = "Add Run", bg ="lightgreen",command=add_busrun)
        add_but.grid(row = 10, column = 6)

        edit_but = Button(root, text = "Delete Run", bg = "lightgreen",command=del_busrun)
        edit_but.grid(row = 10, column = 7)

        blank = Label(root, text = "                            " )
        blank.grid(row = 11, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 12, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 13, column = 0)

        def home():
            root.destroy()
            ob.home_page()





        house = PhotoImage(file = ".\\home.png")
        house_but = Button(root, image=house,command=home)
        house_but.grid(row = 14, column = 6)

        root.mainloop()
    def add_bus_operator():
        root = Tk()



        h,w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))
                    
        bus = PhotoImage(file = ".\\Bus_for_project.png")
        Label(root, image = bus).grid(row = 0, column = 0, columnspan = 12, padx = w//3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 1, column = 0)

        title = Label(root, text = "Online Bus Booking System" , fg = 'maroon1' , bg = 'lightblue', font = 'calibri 20 bold')
        title.grid(row = 2, column = 0, columnspan = 12)

        blank = Label(root, text = "                            " )
        blank.grid(row = 3, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 4, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 5, column = 0)

        add_text = Label(root, text = "Add Bus Operator Details",  fg = "green3", font = 'calibri 20 bold')
        add_text.grid(row = 6, column = 0, columnspan = 12)

        blank = Label(root, text = "                            " )
        blank.grid(row = 7, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 8, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 9, column = 0)


        id_text = Label(root, text = "Operator id")
        id_text.grid(row = 10, column = 0)

        id_ent = Entry(root, width= 10)
        id_ent.grid(row = 10, column =1)
        op_id=id_ent.get()


        name_text = Label(root, text = "Name")
        name_text.grid(row = 10, column = 2)

        name_ent = Entry(root)
        name_ent.grid(row = 10, column =3)
        name=name_ent.get()


        address_text = Label(root, text = "Address")
        address_text.grid(row = 10, column = 4)

        address_ent = Entry(root)
        address_ent.grid(row = 10, column =5)
        address = address_ent.get()

        phone_text = Label(root, text = "Mobile No.")
        phone_text.grid(row = 10, column = 6)

        phone_ent = Entry(root)
        phone_ent.grid(row = 10, column =7)
        phone = phone_ent.get()

        email_text = Label(root, text = "Email")
        email_text.grid(row = 10, column = 8)

        email_ent = Entry(root)
        email_ent.grid(row = 10, column =9)
        email = email_ent.get()

        # import sqlite3
        with sqlite3.connect('database.db') as con:
            cur = con.cursor()

        def add_bus_operator():
            op_id=id_ent.get()
            name=name_ent.get()
            address = address_ent.get()
            phone = phone_ent.get()
            email = email_ent.get()
            if(op_id==''or name==''or address==''or phone==''or email==''):
                messagebox.showwarning("EMPTY DETAILS", "PLEASE ENTER ALL DETAILS")
            else:   
                cur.execute('''insert into bus_operator(op_id,name,address,phone,email) values(?,?,?,?,?)''',(op_id,name,address,phone,email))
                con.commit()
                messagebox.showinfo('OPERATOR','OPERATOR RECORD ADDED SUCCESFULLY')
                Label(root,text=" "+id_ent.get()+"  "+name_ent.get()+"  "+address_ent.get()+"  "+phone_ent.get()+"  "+email_ent.get()).grid(row=11,column=4,columnspan=3)
        

        def edit_bus_operator():
            op_id=id_ent.get()
            name=name_ent.get()
            address = address_ent.get()
            phone = phone_ent.get()
            email = email_ent.get()
            if(op_id==''or name==''or address==''or phone==''or email==''):
                
                messagebox.showwarning("EMPTY DETAILS", "PLEASE ENTER ALL DETAILS")
            else:   
                cur.execute('''update bus_operator set name=?,address=?,phone=?,email=? where op_id=?''',(name,address,phone,email,op_id))
                con.commit()
                messagebox.showinfo("OPERATOR RECORD UPTADE", "OPERATOR RECORD UPDATED SUCCESSFULLY")
            

        add_but = Button(root, text = "Add", bg= "lightgreen",command=add_bus_operator)
        add_but.grid(row =10, column = 10)

        edit_but = Button(root, text = "Edit", bg = "lightgreen", command = edit_bus_operator)
        edit_but.grid(row =10, column = 11)

        blank = Label(root, text = "                            " )
        blank.grid(row = 11, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 12, column = 0)

        def home():
            root.destroy()
            ob.home_page()
        houses = PhotoImage(file = ".\\home.png")
        Button(root, image = houses,command=home).grid(row = 13, column = 8)

        root.mainloop()
    def add_bus_details():
        # from tkinter import *
        # from tkinter import messagebox
        root = Tk()

        h,w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))

        clicked = StringVar()
        clicked.set("AC 2X2")
                    
        bus = PhotoImage(file = ".\\Bus_for_project.png")
        Label(root, image = bus).grid(row = 0, column = 0, columnspan = 10, padx = w//3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 1, column = 1)

        title = Label(root, text = "Online Bus Booking System" , fg = 'maroon1' , bg = 'lightblue', font = 'calibri 14 bold')
        title.grid(row = 2, column = 0, columnspan = 10)

        blank = Label(root, text = "                            " )
        blank.grid(row = 3, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 4, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 5, column = 0)

        title = Label(root, text = "Add Bus Details" , fg = 'green3' , font = 'calibri 14 bold')
        title.grid(row = 6, column = 0, columnspan = 10)

        blank = Label(root, text = "                            " )
        blank.grid(row = 7, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 8, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 9, column = 0)

        add_bus = Label(root, text = "Bus ID")
        add_bus.grid(row=10, column=0)

        ent_bus = Entry(root)
        ent_bus.grid(row=10, column=1)
        bus_id = ent_bus.get()

        type_bus = Label(root, text = "Bus Type")
        type_bus.grid(row=10, column=2)


        drop_bus = OptionMenu(root, clicked ,"AC 2X2", "AC 3X2", "Non AC2X2", "Non AC 3X2", "AC-Sleeper 2X1", "Non-AC SLeeper 2X1" )
        drop_bus.grid(row=10, column=3)
        bus_type = clicked.get()

        capacity_text = Label(root, text = "Capacity")
        capacity_text.grid(row=10, column=4)

        cap_ent = Entry(root)
        cap_ent.grid(row=10, column=5)
        capacity=cap_ent.get()

        fare_text = Label(root, text = "Fare Rs")
        fare_text.grid(row=10, column=6)

        fare_ent = Entry(root)
        fare_ent.grid(row=10, column=7)
        fare=fare_ent.get()

        opt_text = Label(root, text = "Operator ID")
        opt_text.grid(row=10, column=8)

        opt_ent = Entry(root)
        opt_ent.grid(row=10, column=9)
        op_id = opt_ent.get()

        route_text = Label(root, text = "Route ID")
        route_text.grid(row=10, column=10)

        route_ent = Entry(root)
        route_ent.grid(row=10, column=11)
        route_id = route_ent.get()

        blank = Label(root, text = "                            " )
        blank.grid(row = 11, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 12, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 13, column = 0)
        # import sqlite3
        with sqlite3.connect('database.db') as bus:
            cur = bus.cursor()

        def add_bus():
            bus_id = ent_bus.get()
            bus_type = clicked.get()
            route_id = route_ent.get()
            op_id = opt_ent.get()
            fare=fare_ent.get()
            capacity=cap_ent.get()
            if(bus_id==''or bus_type==''or route_id=='' or op_id=='' or fare=='' or capacity==''):
                
                messagebox.showwarning("EMPTY DETAILS", "PLEASE ENTER ALL DETAILS")
        # import sqlite3
            # con = sqlite3.Connection('database.db')
            # cur = con.cursor()
            # cur.execute("insert into bus values('"+bus_id+"','"+bus_type+"','"+capacity+"','"+fare+"','"+op_id+"','"+route_id+"')")
            # con.commit()
            # con.close()
            else:
                cur.execute('''insert into bus(bus_id,bus_type,capacity,fare,op_id,route_id)values(?,?,?,?,?,?)''',(bus_id,bus_type,capacity,fare,op_id,route_id))
                bus.commit()
                Label(root,text=" "+ent_bus.get()+"  "+clicked.get()+"  "+cap_ent.get()+"  "+fare_ent.get()+" "+opt_ent.get()+" "+route_ent.get()).grid(row=14,column=4)
                messagebox.showinfo("BUS RECORD", "BUS RECORD ADDED")
        def edit_bus():
            bus_id = ent_bus.get()
            bus_type = clicked.get()
            route_id = route_ent.get()
            op_id = opt_ent.get()
            fare=fare_ent.get()
            capacity=cap_ent.get()
            if(bus_id==''or bus_type==''or route_id=='' or op_id=='' or fare=='' or capacity==''):
                
                messagebox.showwarning("EMPTY DETAILS", "PLEASE ENTER ALL DETAILS")
        # import sqlite3
            # con = sqlite3.Connection('database.db')
            # cur = con.cursor()
            # cur.execute("insert into bus values('"+bus_id+"','"+bus_type+"','"+capacity+"','"+fare+"','"+op_id+"','"+route_id+"')")
            # con.commit()
            # con.close()
            else:
                cur.execute('''update bus set bus_type=?,capacity=?,fare=?,op_id=?,route_id=? where bus_id=?''',(bus_type,capacity,fare,op_id,route_id,bus_id))
                bus.commit()
                Label(root,text=" "+ent_bus.get()+"  "+clicked.get()+"  "+cap_ent.get()+"  "+fare_ent.get()+" "+opt_ent.get()+" "+route_ent.get()).grid(row=10,column=4,columnspan=3)
                messagebox.showinfo("BUS RECORD", "BUS RECORD UPDATED SUCCESSFULLY")


            

        add_but = Button(root, text = "Add Bus", command=add_bus)
        add_but.grid(row = 14, column = 6)

        edit_but = Button(root, text = "Edit Bus",command=edit_bus)
        edit_but.grid(row = 14, column = 7)

        def home():
            root.destroy()
            ob.home_page()


        house = PhotoImage(file = ".\\home.png")
        house_but = Button(root, image=house,command=home)
        house_but.grid(row = 14, column = 8)

        root.mainloop()
    def check_booking():
        # from tkinter import *
        # from tkinter import messagebox
        root = Tk()

        h,w = root.winfo_screenheight(), root.winfo_screenwidth()
        root.geometry('%dx%d+0+0'%(w,h))

        def check(e=0):
            root.destroy()
            ob.home_page()
        house = PhotoImage(file = ".\\home.png")
        house_but = Button(root, image=house,command=check)
        house_but.grid(row = 14, column =2 )





        mobile_text = Label(root, text = "Enter Your Mobile No: ")
        mobile_text.grid(row =7, column =0)

        mobile_ent = Entry(root)
        mobile = mobile_ent.get()
        mobile_ent.grid(row =7, column=1)

        def check():
            # import sqlite3
            with sqlite3.connect('database.db') as con:
                cur=con.cursor()
            mobile = mobile_ent.get()
            if(mobile==""):
                messagebox.showwarning("Warning","Please enter the details")
            else:
                cur.execute('''select name from passenger where mob_no=?''',[mobile] )
                res=cur.fetchall()
                if(res==[]):
                    messagebox.showwarning("Message","No record found ")
                else:

            



                    final = LabelFrame(root)
                    final.grid(row = 8, column =0, columnspan=3)

                    passenger_text = Label(final, text = "Passenger: ")
                    passenger_text.grid(row =9, column=0)

                    seats_text = Label(final, text = "No of seats: ")
                    seats_text.grid(row =10, column=0)

                    age_text = Label(final, text = "Age: ")
                    age_text.grid(row =12, column=0)

                    travel_text = Label(final, text = "Travel On: ")
                    travel_text.grid(row =14, column=0)

                    seats_text = Label(final, text = "No of Seats: ")
                    seats_text.grid(row =16, column=0)

                    g_text = Label(final, text = "Gender: ")
                    g_text.grid(row =8, column=2)

                    phone_text = Label(final, text = "Phone: ")
                    phone_text.grid(row =10, column=2)
            

                    flare_text = Label(final, text = "Fare Rs: ")
                    flare_text.grid(row =12, column=2)

                    detail_text = Label(final, text = "Bus Detail: ")
                    detail_text.grid(row =14, column=2)

                    booked_text = Label(final, text = "Booked On: ")
                    booked_text.grid(row =16, column=2)

                    point_text = Label(final, text = "Boarding Point: ")
                    point_text.grid(row =18, column=2)

            



            
            # import sqlite3
            with sqlite3.connect('database.db') as con:
                cur=con.cursor()
                
        # travel_date=ent_date.get()
        # To=ent_To.get()
        # From=ent_From.get()
            
            mobile= mobile_ent.get()
            cur.execute('''select name,gender,no_of_seats,mob_no,age,travelling_date,booking_date from passenger where mob_no=? ''',[mobile])
            res = cur.fetchall()
            for i in res:
                Label(final,text = i[0]).grid(row=9,column = 1)
                Label(final,text = i[1]).grid(row=8,column = 3)
                Label(final,text = i[2]).grid(row=10,column = 1)
                Label(final,text = i[3]).grid(row=10,column = 3)
                Label(final,text = i[4]).grid(row=12,column = 1)
                Label(final,text = i[5]).grid(row=14,column = 2)
                Label(final,text = i[6]).grid(row=16,column = 3)
                Label(final,text = i[2]).grid(row=16,column = 1)
            cur.execute('''select source,destination from ticket where mobile=? ''',[mobile] )
            red=cur.fetchall()
            for i in red:
                Label(final,text = i[0]).grid(row=18,column = 3)
                # Label(final,text = i[1]).grid(row=9,column = 1)

            cur.execute('''select fare from passenger as b,bus as a where mob_no=? and b.bus_id=a.bus_id''',[mobile])
            m=cur.fetchone()
            Fare = m[0]
            cur.execute('''select no_of_seats from passenger where mob_no=?''',[mobile])
            k=cur.fetchone()
            seats=k[0]
            totalfare = str(Fare*seats)
            Label(final,text = ''+totalfare).grid(row=12,column = 3)
            last_text = Label(final, text = "Total amount Rs  " +totalfare+ " to be paid at the time of boarding the bus")
            last_text.grid(row =20, column=0)
            con.commit()





















                    
        bus = PhotoImage(file = ".\\Bus_for_project.png")
        Label(root, image = bus).grid(row = 0, column = 0, columnspan = 3, padx = w//3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 1, column = 1)

        title = Label(root, text = "Online Bus Booking System" , fg = 'red' , bg = 'lightblue', font = 'calibri 15 bold')
        title.grid(row = 2, column = 0, columnspan = 3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 3, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 4, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 5, column = 0)


        title1 = Label(root, text = "Check Your Booking" , fg = 'darkgreen' , bg = 'lightgreen', font = 'calibri 15 bold')
        title1.grid(row = 4, column = 0, columnspan = 3)

        blank = Label(root, text = "                            " )
        blank.grid(row = 5, column = 0)
        blank = Label(root, text = "                            " )
        blank.grid(row = 6, column = 0)

        # mobile_text = Label(root, text = "Enter Your Mobile No: ")
        # mobile_text.grid(row =7, column =0)

        # mobile_ent = Entry(root)
        # moblie = mobile_ent.get()
        # mobile_ent.grid(row =7, column=1)


        check_but = Button(root, text = "Check Booking", command = check)
        check_but.grid(row = 7, column=2)



        root.mainloop()


if __name__== "__main__":
    ob = window
    ob.introduction_page()       
        
        
         
