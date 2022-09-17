import mysql.connector as mysql
conn=mysql.connect(user="root",password="",host="localhost")

cursor=conn.cursor()
cursor.execute("use project")

def md():
   print("Available Train:Rajdhani express")

def mc():
   print("Available Train:Chennai Express")

def mr():
   print("Available Train:Saurashtra Express")

def pd():
   print("Available Train:Jhelum Express")

def pk():
   print("Available Train:Lucknow Express")

select=int(input("Select your starting city\n1:Mumbai\n2:Pune"))
select2=int(input("Select your Destination\n3:Delhi\n4:Chennai\n5:Rajkot\n6:Kanpur"))


if(select==1 and select2==3):
   md()
elif(select==1 and select2==4):
   mc()
elif(select==1 and select2==5):
   mr()
elif(select==2 and select2==3):
   pd()
elif(select==2 and select2==6):
   pk()
elif(select==2 and select2==4):
   print("No train Available")
elif(select==2 and select2==5):
   print("No train Available")
elif(select==1 and select2==6):
   print("No train Available")

def save():
    a=input("Enter the Passenger Name:")
    b=int(input("Enter the Passenger Age:"))
    c=input("Enter the Passenger Gender:")
    d=input("Enter the Passenger ID:")
    e=int(input("Enter the Passenger Contact:"))
    f=input("Enter the Passenger Address:")

    q="insert into info(Name,Age,Gender,ID,Contact,Address) values('"+a+"','"+str(b)+"','"+c+"','"+d+"','"+str(e)+"','"+f+"')"
    cursor.execute(q)
    conn.commit()
    print("Save success")

def raj():
   a=input("Enter the Travelling class in words,Ex:First,Second,Third:")
   b=int(input("Enter the the Seat No.:"))
   c=int(input("Enter the Coach no.:"))
   d=input("Enter the Journey Date in YYYY/MM/DD Format:")

   q="insert into rajdhani(class,seat,coach,date) values('"+a+"','"+str(b)+"','"+str(c)+"','"+d+"')"
   cursor.execute(q)
   conn.commit()
   print("Save success")

def che():
   a=input("Enter the Travelling class in words,Ex:First,Second,Third:")
   b=int(input("Enter the the Seat No.:"))
   c=int(input("Enter the Coach no.:"))
   d=input("Enter the Journey Date in YYYY/MM/DD Format:")

   q="insert into chennai(class,seat,coach,date) values('"+a+"','"+str(b)+"','"+str(c)+"','"+d+"')"
   cursor.execute(q)
   conn.commit()
   print("Save success")

def sau():
   a=input("Enter the Travelling class in words,Ex:First,Second,Third:")
   b=int(input("Enter the the Seat No.:"))
   c=int(input("Enter the Coach no.:"))
   d=input("Enter the Journey Date in YYYY/MM/DD Format:")

   q="insert into saurashtra(class,seat,coach,date) values('"+a+"','"+str(b)+"','"+str(c)+"','"+d+"')"
   cursor.execute(q)
   conn.commit()
   print("Save success")

def jhe():
   a=input("Enter the Travelling class in words,Ex:First,Second,Third:")
   b=int(input("Enter the the Seat No.:"))
   c=int(input("Enter the Coach no.:"))
   d=input("Enter the Journey Date in YYYY/MM/DD Format:")

   q="insert into jhelum(class,seat,coach,date) values('"+a+"','"+str(b)+"','"+str(c)+"','"+d+"')"
   cursor.execute(q)
   conn.commit()
   print("Save success")

def luc():
   a=input("Enter the Travelling class in words,Ex:First,Second,Third:")
   b=int(input("Enter the the Seat No.:"))
   c=int(input("Enter the Coach no.:"))
   d=input("Enter the Journey Date in YYYY/MM/DD Format:")

   q="insert into lucknow(class,seat,coach,date) values('"+a+"','"+str(b)+"','"+str(c)+"','"+d+"')"
   cursor.execute(q)
   conn.commit()
   print("Save success")

if(select==1 and select2==3):
 select3=int(input("Continue to Booking process for Rajdhani Express:\n1.Yes\n2.No"))
 if(select3==1):
   save()
   raj()
elif(select==1 and select2==4):
   select3=int(input("Continue to Booking process for Chennai Express:\n1.Yes\n2.No"))
   if(select3==1):
    save()
    che()
elif(select==1 and select2==5):
   select3=int(input("Continue to Booking process for Saurashtra Express:\n1.Yes\n2.No"))
   if(select3==1):
    save()
    sau()
elif(select==2 and select2==3):
   select3=int(input("Continue to Booking process for Jhelum Express:\n1.Yes\n2.No"))
   if(select3==1):
    save()
    jhe()
elif(select==2 and select2==6):
   select3=int(input("Continue to Booking process for Lucknow Express:\n1.Yes\n2.No"))
   if(select3==1):
    save()
    luc()
else:
   print("Exit")

def show():
    q="select * from info"
    cursor.execute(q)
    res=cursor.fetchall()
    for i in res:
      print("   PASSENGER INFORMATION\n\n"
             "   Name \ Age \ Gender \ ID \ Contact \ Address\n\n",i)

def show1():
    q="select * from rajdhani"
    cursor.execute(q)
    res=cursor.fetchall()
    for i in res:
      print("######################################################################\n"
                "  ________________________________________________________________\n "
                "|JOURNEY AND TICKET DETAILS FOR RAJDHANI EXPRESS                |\n" 
                " |  HAPPY JOURNEY          HELP LINE NO.138                      |\n"
                " |  CLASS \ SEAT NO. \ COACH NO. \ DATE \ PNR NO. \n\n"" |",i,"      |\n |"
                "                                        AMOUNT PAID: 450Rs.    |\n |"
                " _____________________________________________________________ |")

def show2():
    q="select * from chennai"
    cursor.execute(q)
    res=cursor.fetchall()
    for i in res:
      print("######################################################################\n"
                "  ________________________________________________________________\n "
                "|JOURNEY AND TICKET DETAILS FOR CHENNAI EXPRESS                 |\n" 
                " |  HAPPY JOURNEY          HELP LINE NO.138                      |\n"
                " |  CLASS \ SEAT NO. \ COACH NO. \ DATE \ PNR NO. \n\n"" |",i,"      |\n |"
                "                                        AMOUNT PAID: 450Rs.    |\n |"
                " _____________________________________________________________ |")

def show3():
    q="select * from saurashtra"
    cursor.execute(q)
    res=cursor.fetchall()
    for i in res:
      print("######################################################################\n"
                "  ________________________________________________________________\n "
                "|JOURNEY AND TICKET DETAILS FOR SUARASHTRA EXPRESS              |\n" 
                " |  HAPPY JOURNEY          HELP LINE NO.138                      |\n"
                " |  CLASS \ SEAT NO. \ COACH NO. \ DATE \ PNR NO. \n\n"" |",i,"      |\n |"
                "                                        AMOUNT PAID: 450Rs.    |\n |"
                " _____________________________________________________________ |")

def show4():
    q="select * from jhelum"
    cursor.execute(q)
    res=cursor.fetchall()
    for i in res:
      print("######################################################################\n"
                "  ________________________________________________________________\n "
                "|JOURNEY AND TICKET DETAILS FOR JHELUM EXPRESS                  |\n" 
                " |  HAPPY JOURNEY          HELP LINE NO.138                      |\n"
                " |  CLASS \ SEAT NO. \ COACH NO. \ DATE \ PNR NO. \n\n"" |",i,"      |\n |"
                "                                        AMOUNT PAID: 450Rs.    |\n |"
                " _____________________________________________________________ |")

def show5():
    q="select * from lucknow"
    cursor.execute(q)
    res=cursor.fetchall()
    for i in res:
      print("######################################################################\n"
                "  ________________________________________________________________\n "
                "|JOURNEY AND TICKET DETAILS FOR LUCKNOW EXPRESS                 |\n" 
                " |  HAPPY JOURNEY          HELP LINE NO.138                      |\n"
                " |  CLASS \ SEAT NO. \ COACH NO. \ DATE \ PNR NO. \n\n"" |",i,"      |\n |"
                "                                        AMOUNT PAID: 450Rs.    |\n |"
                " _____________________________________________________________ |")


if(select==1 and select2==3):
 select3=int(input("Show Your Booked Ticket for Rajdhani Express:\n1.Yes\n2.No"))
 if(select3==1):
   show()
   show1()
elif(select==1 and select2==4):
   select3=int(input("Show Your Booked Ticket for Chennai Express:\n1.Yes\n2.No"))
   if(select3==1):
    show()
    show2()
elif(select==1 and select2==5):
   select3=int(input("Show Your Booked Ticket for Saurashtra Express:\n1.Yes\n2.No"))
   if(select3==1):
    show()
    show3()
elif(select==2 and select2==3):
   select3=int(input("Show Your Booked Ticket for Jhelum Express:\n1.Yes\n2.No"))
   if(select3==1):
    show()
    show4()
elif(select==2 and select2==6):
   select3=int(input("Show Your Booked Ticket for Lucknow Express:\n1.Yes\n2.No"))
   if(select3==1):
    show()
    show5()
else:
   print("Exit")

                



   







   






   


    






    

    
    

    
  
