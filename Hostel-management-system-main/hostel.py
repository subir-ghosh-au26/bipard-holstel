
from tkinter.ttk import *
from tkinter import *




def date():
    from datetime import datetime
    # current date time
    now = datetime.now()
    t = now.strftime("%H:%M")
    s1 = now.strftime("%H:%M,%Y-%m-%d")
    s1 = str(s1)
    return s1 #returns Current Date And Time In String



base = Tk()
base.title("BIPARD HOSTEL MANAGEMENT SYSTEM")
base.geometry(f'{1535}x{790}+{0}+{0}')
heading = Label(base, text="BIPARD HOSTEL MANAGEMENT SYSTEM", font=("Arial 30 bold"), bg="skyblue", fg="black", padx=490, pady=20)
heading.pack()
canvas = Canvas(base, bg='silver', height=575, width=800)
canvas.place(x=330, y=130)
G = 1
def main():
    global G
    canvas = Canvas(base, bg='lightseagreen', height=675, width=310)
    canvas.place(x=-1, y=100)
    can = Canvas(base, bg='silver', height=675, width=1500)
    can.place(x=320, y=105)
    def add_stud():
        canvas = Canvas(base, bg='silver', height=675, width=1210)
        canvas.place(x=320, y=105)
        name = Label(base, text="Name", font=("Arial 15 bold"), bg='silver', fg="black")
        name.place(x=400, y=150)
        name_entry = Entry(base, width=20, font=("Arial 15"))
        name_entry.place(x=600, y=150)
        name_entry.focus()
        service = Label(base, text="Service", font=("Arial 15 bold"), bg="silver", fg="black")
        service.place(x=400, y=200)
        service_entry = Entry(base, width=20, font=("Arial 15"))
        service_entry.place(x=600, y=200)
            
        contact = Label(base, text="Mobile No", font=("Arial 15 bold"), bg="silver", fg="black")
        contact.place(x=400, y=250)
        cont_entry = Entry(base, width=20, font=("Arial 15 bold"))
        cont_entry.place(x=600, y=250)
        
        
        address = Label(base, text="Address", font=("Arial 15 bold"), bg="silver", fg="black")
        address.place(x=400, y=300)
        addrs_entry = Entry(base, width=30, font=("Arial 15 bold"))
        addrs_entry.place(x=600, y=300)
        
        date = Label(base, text="Date", font=("Arial 15 bold"), bg="silver", fg="black")
        date.place(x=400, y=350)
        date_entry = Entry(base, width="15", font=("Arial 15 bold"))
        date_entry.place(x=600, y=350)
        m2 = Label(base, text="(Date of Arrival)", font=("Arial 11 bold"), bg="silver", fg="black")
        m2.place(x=450, y=350)
              
       
        gender = Label(base, text="Gender", font=("Arial 15 bold"), bg="silver", fg="black")
        gender.place(x=400, y=400)
        G = 1
        def selected():
            global G
            if c1.get() == 1:
                G = 1
            elif c1.get() == 2:
                G = 2
            elif c1.get() == 0:
                G = 0
            else:
                G = 1
        c1 = IntVar()
        a = Radiobutton(base, text="Male", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=1, command=selected)
        b = Radiobutton(base, text="Female", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=2, command=selected)
        c = Radiobutton(base, text="Other", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=0, command=selected)
        a.place(x=580, y=400)
        b.place(x=680, y=400)
        c.place(x=800, y=400)
        def available_roome():
            rooms_availble = Label(base, text="Rooms Available", font=("Arial 20 bold"), bg="lightseagreen", fg="white", padx=140)
            rooms_availble.place(x=1005, y=110,)
            x = " Room No. | Beds"
            room = Label(base, text=x, font=("Arial 15 bold"), bg="dark slate grey", fg="white")
            room.place(x=1005, y=150,)
            global G
            bed1 = None
            bed2 = None
            bed3 = None
            if G == 1:
                f1 = open("room_info_boys.txt","r")
                bed1 = "B1"
                bed2 = "B2"
                bed3 = "B3"
            elif G==2:
                f1 = open("room_info_girls.txt","r")
                bed1 = "G1"
                bed2 = "G2"
                bed3 = "G3"
            elif G==0:
                f1 = open("room_info_others.txt","r")
                bed1 = "O1"
                bed2 = "O2"
                bed3 = "O3"
            else:
                file_name = "room_info_boys.txt"
                bed1 = "B1"
                bed2 = "B2"
                bed3 = "B3"
            all_lines = f1.readlines()
            count = 1
            rooms = []
            for i in all_lines:
                temp1 = str(i)
                one_line = temp1.split(',')
                if one_line[1] == bed1 and one_line[2] == bed2 and one_line[3] == bed3:
                    temp = []
                    count = 2
                    temp.append(one_line[0])
                    temp.append(bed1)
                    temp.append(bed2)
                    temp.append(bed3)
                    rooms.append(temp)
                if one_line[1] != bed1 and one_line[2] == bed2 and one_line[3] == bed3:
                    count = 2
                    temp = []
                    temp.append(one_line[0])
                    temp.append("NA")
                    temp.append(bed2)
                    temp.append(bed3)
                    rooms.append(temp)
                if one_line[1] == bed1 and one_line[2] != bed2 and one_line[3] == bed3:
                    temp = []
                    count = 2
                    temp.append(one_line[0])
                    temp.append(bed1)
                    temp.append("NA")
                    temp.append(bed3)
                    rooms.append(temp)
                if one_line[1] == bed1 and one_line[2] == bed2 and one_line[3] != bed3:
                    temp = []
                    count = 2
                    temp.append(one_line[0])
                    temp.append(bed1)
                    temp.append(bed2)
                    temp.append("NA")
                    rooms.append(temp)
                if one_line[1] == bed1 and one_line[2] != bed2 and one_line[3] != bed3:
                    temp = []
                    count = 2
                    temp.append(one_line[0])
                    temp.append(bed1)
                    temp.append("NA")
                    temp.append("NA")
                    rooms.append(temp)
                if one_line[1] != bed1 and one_line[2] == bed2 and one_line[3] != bed3:
                    temp = []
                    count = 2
                    temp.append(one_line[0])
                    temp.append("NA")
                    temp.append(bed2)
                    temp.append("NA")
                    rooms.append(temp)
                if one_line[1] != bed1 and one_line[2] != bed2 and one_line[3] == bed3:
                    temp = []
                    count = 2
                    temp.append(one_line[0])
                    temp.append("NA")
                    temp.append("NA")
                    temp.append(bed3)
                    rooms.append(temp)
                if one_line[1] != bed1 and one_line[2] != bed2 and one_line[3] != bed3:
                    temp = []
                    count = 2
                    temp.append("--")
                    temp.append("NA")
                    temp.append("NA")
                    temp.append("NA")
                    rooms.append(temp)
            if count == 1:
                y = "No Rooms Available"
                x = Label(base, text=y, font=("Arial", 40), bg="dark slate grey", fg="white")
                x.place(x=1020, y=300)
            else:
                x1co = 1150
                y1co = 200
                x2co = 1350
                y2co = 200
                flag = 1
                for i in rooms:
                    r_no = Label(base, text=i[0], font=("Arial", 15), bg="silver", fg="black")
                    r_no.place(x=x1co, y=y1co)
                    y = i[1] + " " + i[2] + " " + i[3]
                    r_bk_no = Label(base, text=y, font=("Arial", 15), bg="silver", fg="black")
                    r_bk_no.place(x=x2co, y=y2co)
                    y1co = y1co + 40
                    y2co = y2co + 40
                    count = 2
                    if flag >= 8:
                        break
                    flag = flag + 1
            f1.close()
            c1 = Canvas(base, height=2, width=600)
            c1.place(x=1000, y=550)
            r1 = Label(base, text="Room No.", font=("Arial 15 bold"), bg="silver", fg="black")
            r1.place(x=1040, y=570)
            r2 = Entry(base, width=15, font=("Arial 15 bold"))
            r2.place(x=1150, y=570)
            r3 = Label(base, text="Bed No.", font=("Arial 15 bold"), bg="silver", fg="black")
            r3.place(x=1040, y=610)
            r4 = Entry(base, width=15, font=("Arial 15 bold"))
            r4.place(x=1150, y=610)
            r5 = Label(base, text="(B1 B2 B3)", font=("Arial 10 bold"), bg="silver", fg="black")
            r5.place(x=1040, y=640)
            r6 = Label(base, text="( Girl = G1 )", font=("Arial 15 bold"), bg="silver", fg="black")
            r6.place(x=1350,y=570)
            r7 = Label(base, text="( Other = O1)",font=("Arial 15 bold"), bg="silver", fg="black")
            r7.place(x=1350,y=610)
            def student():
                global G
                bed1 = None
                bed2 = None
                bed3 = None
                file_name = None
                if G == 1:
                    file_name = "room_info_boys.txt"
                    bed1 = "B1"
                    bed2 = "B2"
                    bed3 = "B3"
                elif G == 2:
                    file_name = "room_info_girls.txt"
                    bed1 = "G1"
                    bed2 = "G2"
                    bed3 = "G3"
                elif G == 0:
                    file_name = "room_info_others.txt"
                    bed1 = "O1"
                    bed2 = "O2"
                    bed3 = "O3"
                else:
                    file_name = "room_info_boys.txt"
                    bed1 = "B1"
                    bed2 = "B2"
                    bed3 = "B3"
                f1 = open("student_info.txt", "a")
                f2 = open(file_name,"a")
                n = str(fir_name_entry.get()) + " "
                b = str(r4.get()).upper()
                ln = str(last_name_entry.get()).lower()
                f = str(fathr_name_entry.get()).lower()
                m = str(mther_name_entry.get()).lower()
                d = str(dob_entry.get()).lower()
                add = str(addrs_entry.get()).lower()
                c = str(cont_entry.get()).lower()
                e = str(email_entry.get())
                w = str(place_entry.get()).lower()
                v = str(vehicle_entry.get()).lower()
                da = date().lower()
                rom = str(r2.get()).lower()
                f1.write(
                c + "," + n + ln + "," + f + "," + m + "," + d + "," + e + "," + w + "," + v + "," + da + "," +
                b + "," + rom + "," + "\n")
                f1.close()
                fobj = open(file_name, "r")
                fdata_ls = fobj.readlines()
                fobj.close()
                rdate = date()
                fobj = open(file_name, "w")
                if b == bed1:
                    for oneline in fdata_ls:
                        if oneline.startswith(rom + ",") and oneline.__contains__(","+bed1):  # write date
                            new_oneline = oneline.replace(","+bed1+",", "," + c + ",")
                            new_oneline2 = new_oneline.replace(",NOT,", "," + rdate + ",")
                            fobj.write(new_oneline)
                        else:
                            fobj.write(oneline)
                else:
                    if b == bed2:
                        for oneline in fdata_ls:
                            if oneline.startswith(rom + ",") and oneline.__contains__(","+bed2): # write date
                                new_oneline = oneline.replace(","+bed2+"," , "," + c + ",")
                                new_oneline2 = new_oneline.replace(",NOT," , "," + rdate + ",")
                                fobj.write(new_oneline)
                            else:
                                fobj.write(oneline)
                    else:
                        for oneline in fdata_ls:
                            if oneline.startswith(rom + ",") and oneline.__contains__(","+bed3): # write date
                                new_oneline = oneline.replace(","+bed3+"," , "," + c + ",")
                                new_oneline2 = new_oneline.replace(",NOT," , "," + rdate + ",")
                                fobj.write(new_oneline)
                            else:
                                fobj.write(oneline)
                fobj.close()
                l = Label(base, text="Student Added Successfully....!", font=("Arial 15 bold"), bg='silver', fg="black")
                l.place(x=1150, y=650)
            add_student = Button(base, text="Save", font=("Arial 20 bold"), bg="white", fg="black" ,command=student)
            add_student.place(x=1050, y=700)
        
        submit = Button(base, text="Submit", font=("Arial 15 bold"), bg="white", fg="black", command=available_roome)
        submit.place(x=650, y=500)
        line = Canvas(base, height=670, width=2)
        line.place(x=1000, y=105)
    def add_room():
            canvas = Canvas(base, bg='silver', height=675, width=1210)
            canvas.place(x=320, y=105)
            h1 = Label(base, text="Add New Room", bg="dark slate grey", font=("Arial 20 bold"), fg="white", padx=500, pady=10)
            h1.place(x=320, y=105)
            n_rm_n = Label(base, text="New Room No.", font=("Arial 20 bold"), bg="silver", fg="black")
            n_rm_n.place(x=500, y=300)
            rm_n_entry = Entry(base, width=20, font=("Arial 15 bold"))
            rm_n_entry.place(x=750, y=303)
            gender = Label(base,text="Gender", font=("Arial 20 bold"), bg="silver", fg="black")
            gender.place(x=500,y=350)
            global G
            G = 1
            def selected():
                global G
                if c1.get() == 1:
                    G = 1
                if c1.get() == 2:
                    G = 2
                if c1.get() == 0:
                    G = 0
            c1 = IntVar()
            a = Radiobutton(base, text="Male", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=1, command=selected)
            b = Radiobutton(base, text="Female", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=2, command=selected)
            c = Radiobutton(base, text="Other", bg="silver", fg="black", font=("Arial 15 bold"), variable=c1, value=0, command=selected)
            a.place(x=750, y=350)
            b.place(x=840, y=350)
            c.place(x=950, y=350)
            def add():
                file_name = ""
                bed1 = bed2 = bed3 = None
                r = (rm_n_entry.get())
                if G==1:
                    bed1 = "B1"
                    bed2 = "B2"
                    bed3 = "B3"
                    file_name = "room_info_boys.txt"
                    f2 = open(file_name, "r")
                if G==2:
                    bed1 = "G1"
                    bed2 = "G2"
                    bed3 = "G3"
                    file_name = "room_info_girls.txt"
                    f2 = open(file_name, "r")
                if G==0:
                    bed1 = "O1"
                    bed2 = "O2"
                    bed3 = "O3"
                    file_name = "room_info_others.txt"
                    f2 = open(file_name, "r")
                all_lines = f2.readlines()
                count = 0
                for i in all_lines:
                    temp = str(i)
                    one_line = temp.split(',')
                    if one_line[0] == r:
                        l = Label(base, text="Room Is Already Addded....!", font=("Arial 25 bold"), bg='silver', fg="black")
                        l.place(x=650, y=600)
                        f2.close()
                        count = 2
                f2.close()
                if count != 2:
                    q = "NOT"
                    f1 = open(file_name, "a")
                    f1.write(r + "," + bed1 + "," + bed2 + "," + bed3 + "," + q + "," + "\n")
                    f1.close()
                    l = Label(base, text="ROOM Successfully Added....!", font=("Arial 25 bold"), bg='silver', fg="black")
                    l.place(x=650, y=600)
            ad_rm_btn = Button(base, text="Add Room", font=("Arial 20 bold"), bg="white", fg="black", command=add)
            ad_rm_btn.place(x=550, y=500)
    
    
    def view_info():
            canvas = Canvas(base, bg='silver', height=675, width=1215)
            canvas.place(x=320, y=105)
            def all_girl_info():
                canvas = Canvas(base, bg='silver', height=675, width=810)
                canvas.place(x=715, y=105)
                h1 = Label(base, text="Information Of Participants", font=("Arial 20 bold"), bg="dark slate grey", fg="white",padx=270, pady=5)
                h1.place(x=720, y=105)
                h = "Room NO.     Name     Contact     Service"
                h2 = Label(base, text=h, font=("Arial 20 bold"), bg="dark orange", fg="white")
                h2.place(x=723, y=150)
                students = []
                f1 = open("student_info.txt", "r")
                all_lines = f1.readlines()
                for i in all_lines:
                    temp = str(i)
                    one_line = temp.split(',')
                    t = []
                    t.append(one_line[11])
                    t.append(one_line[1])
                    t.append(one_line[0])
                    t.append(one_line[6])
                    students.append(t)
                x1co = 800
                y1co = 200
                x2co = 900
                x3co = 1160
                x4co = 1380
                flag = 1
                for i in students:
                    y = i
                    c = 0
                    while c <= 2:
                        label = Label(base, text=y[0], font=("Arial 15 bold"), bg="silver", fg="black")
                        label.place(x=x1co, y=y1co)
                        label2 = Label(base, text=y[1], font=("Arial 15 bold"), bg="silver", fg='black')
                        label2.place(x=x2co, y=y1co)
                        label3 = Label(base, text=y[2], font=('Arial 15 bold'), bg="silver", fg='black')
                        label3.place(x=x3co, y=y1co)
                        label4 = Label(base, text=y[3], font=("Arial 15 bold"), bg="silver", fg="black")
                        label4.place(x=x4co, y=y1co)
                        c = c + 1
                    y1co = y1co + 50
                    if flag > 8:
                        break
            def room_wise():
                canvas = Canvas(base, bg='silver', height=675, width=810)
                canvas.place(x=715, y=105)
                l1 = Label(base, text="Enter Room No.", font=("Arial 20 bold"), bg="silver", fg="black")
                l1.place(x=750, y=150)
                l1_entry = Entry(base, width=10, font=("Arial 20 bold"))
                l1_entry.place(x=1000, y=150)
                l1_entry.focus()
                def search():
                    r_no = str(l1_entry.get())
                    f1 = open("student_info.txt", "r")
                    all_lines = f1.readlines()
                    r_info = []
                    for i in all_lines:
                        temp = str(i)
                        one_line = temp.split(',')
                        if one_line[11] == r_no:
                            temp = []
                            temp.append(one_line[10])
                            temp.append(one_line[1])
                            temp.append(one_line[0])
                            temp.append(one_line[6])
                            r_info.append(temp)
                    h1 = Label(base, text="Information Of Students", font=("Arial 20 bold"), bg="dark slate grey",fg="white", padx=270, pady=5)
                    h1.place(x=720, y=250)
                    h = "Bed No. Name Contact Workplace"
                    h2 = Label(base, text=h, font=("Arial 20 bold"), bg="dark orange", fg="white")
                    h2.place(x=723, y=300)
                    x1co = 780
                    y1co = 400
                    x2co = 900
                    x3co = 1160
                    x4co = 1380
                    flag = 1
                    for i in r_info:
                        y = i
                        c = 0
                        while c <= 2:
                            label = Label(base, text=y[0], font=("Arial 15 bold"), bg="silver", fg="black")
                            label.place(x=x1co, y=y1co)
                            label2 = Label(base, text=y[1], font=("Arial 15 bold"), bg="silver", fg='black')
                            label2.place(x=x2co, y=y1co)
                            label3 = Label(base, text=y[2], font=('Arial 15 bold'), bg="silver", fg='black')
                            label3.place(x=x3co, y=y1co)
                            label4 = Label(base, text=y[3], font=("Arial 15 bold"), bg="silver", fg="black")
                            label4.place(x=x4co, y=y1co)
                            c = c + 1
                        y1co = y1co + 100
                        if flag > 2:
                            break
                search_btn = Button(base, text="Search", font=("Arial 20 bold"), command=search)
                search_btn.place(x=1200, y=140)
            stud_info = Button(base, text="Information Of All Participants", wraplength=180, justify=CENTER, font=("Arial 20 bold"), padx=50, pady=1, command=all_girl_info)
            stud_info.place(x=400, y=200)
            stud_room_wise = Button(base, text="Room Info", font=("Arial 20 bold"), padx=60, pady=5, command=room_wise)
            stud_room_wise.place(x=400, y=400)
            line = Canvas(base, height=680, width=5)
            line.place(x=710, y=105)
    
    add_std_btn = Button(base, text="Add Participants", font=("Arial 20 bold"), padx=13, bg="white", command=add_stud)
    add_std_btn.place(x=32, y=150)
    
    add_new_room = Button(base, text="Add New Room", font=("Arial 20 bold"), bg="white", command=add_room)
    add_new_room.place(x=32, y=250)
     
    view_info = Button(base, text="View Information", font=("Arial 18 bold"), bg="white", command=view_info)
    view_info.place(x=32, y=350)
    
    exit = Button(base, text="EXIT", font=("Arial 18 bold"), bg="white", padx=70, command=quit)
    exit.place(x=32, y=450)
    
username = Label(base, text="Username", font=("Arial 15 bold"), bg="silver", fg="black")
username.place(x=500, y=240)
user_entry = Entry(base, width=15, font=("Arial 15"))
user_entry.place(x=650, y=245)
user_entry.focus()
password = Label(base, text="Password", font=("Arial 15 bold"), bg="silver", fg="black")
password.place(x=500, y=300)
pass_entry = Entry(base, width=15, font="Arial 15")
pass_entry.place(x=650, y=300)
def login():
    id = str(user_entry.get())
    key = str(pass_entry.get())
    if id == "admin" and key == "1234":
        main()
    else:
        user_entry.focus()
        user_entry.delete(0, END)
        pass_entry.delete(0, END)
        fail = Label(base, text="Wrong Username Or Password...!", font=("Arial 30 bold"),bg="silver", fg="red")
        fail.place(x=450, y=540)
login_btn = Button(base, text="Login", font=("Arial 15 bold"), bg="lightseagreen", fg="white",command=login)
login_btn.place(x=550, y=400)

exit = Button(base, text="EXIT", font=("Arial 15 bold"), bg="lightseagreen", fg="white", command=quit)
exit.place(x=650, y=400)

base.mainloop()
