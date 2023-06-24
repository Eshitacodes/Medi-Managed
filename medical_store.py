import mysql.connector as sqldb
mycon=sqldb.connect(host="localhost",user="root",passwd="mango",database="medical_shop")
if mycon.is_connected():
    print("Successfully connected to mysql database")
cursor=mycon.cursor()
print("========================INSTRUCTIONS==========================")

print()
print("Enter 1 for medicine menu ")
print("Enter 2 for customer menu ")
print("Enter 3 for supplier menu ")
print()
ch=int(input("Enter your choice "))
print()
if ch==1:
    print("Enter 1 to view medicines ")
    print("Enter 2 to add medicine ")
    print("Enter 3 to search medicine ")
    print("Enter 4 to update medicine info ")
    print("Enter 5 for medicines to be purchased list ")
    print()
    ch1=int(input("Enter your choice "))
    print()
    if ch1==1:
        inp="select * from medicines;"
        cursor.execute(inp)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)
            
    if ch1==2:
        a=input("Enter medicine name ")
        b=int(input("Enter medicine id "))
        c=int(input("Enter sale "))
        d=int(input("Enter unit "))
        e=int(input("Enter Quantity "))
        f=int(input("Enter minimum Quantity "))
        g=input("Enter Company name ")
        h=int(input("Enter supplier ID "))
        i=int(input("Enter Quantity to be purchased "))
        inp="insert into medicines values('%s',%s,%s,%s,%s,%s,'%s',%s,%s)"%(a,b,c,d,e,f,g,h,i)
        cursor.execute(inp)
        mycon.commit()
        inp1="select * from medicines;"
        cursor.execute(inp1)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)
        
    if ch1==3:
        print("Enter 1 to search by medicine name ")
        print("Enter 2 to search by medicine id ")
        print("Enter 3 to search by sale ")
        print("Enter 4 to search by unit ")
        print("Enter 5 to search by Quantity ")
        print("Enter 6 to search by minimum Quantity ")
        print("Enter 7 to search by Company name ")
        print("Enter 8 to search by supplier ID ")
        print("Enter 9 to search by Quantity to be purchased ")
        print()
        c1=int(input("Enter your choice "))
        print()
        if c1==1:
            a=input("Enter medicine name ")
            inp="select * from medicines where medicine_name='%s'"%a
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
        if c1==2:
            b=int(input("Enter medicine ID "))
            inp="select * from medicines where medicine_id=%s"%b
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
        if c1==3:
            c=int(input("Enter Sale "))
            inp="select * from medicines where sale=%s"%c
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
        if c1==4:
            d=int(input("Enter Unit "))
            inp="select * from medicines where unit=%s"%d
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
        if c1==5:
            e=int(input("Enter Quantity "))
            inp="select * from medicines where Quantity=%s"%e
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
        if c1==6:
            f=int(input("Enter minimum quantity "))
            inp="select * from medicines where minimum_quantity=%s"%f
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
        if c1==7:
            g=input("Enter Company name ")
            inp="select * from medicines where company_name='%s'"%g
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
        if c1==8:
            h=int(input("Enter supplier ID "))
            inp="select * from medicines where supplier_id=%s"%h
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
        if c1==9:
            i=int(input("Enter Quantity to purchase "))
            inp="select * from medicines where to_purchase=%s"%i
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)

    if ch1==4:
        st=input("Enter the name of the medicine whose content is to be updated ")
        print("Enter 1 to update medicine name ")
        print("Enter 2 to update medicine id ")
        print("Enter 3 to update sale ")
        print("Enter 4 to update unit ")
        print("Enter 5 to update Quantity ")
        print("Enter 6 to update minimum Quantity ")
        print("Enter 7 to update Company name ")
        print("Enter 8 to update supplier ID ")
        print("Enter 9 to update Quantity to be purchased ")
        print()
        c1=int(input("Enter your choice "))
        if c1==1:
            st1=input("Enter medicines's new name ")
            inp="update medicines set medicine_name='%s'where medicine_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from medicines;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)
        if c1==2:
            st1=int(input("Enter medicines's new ID "))
            inp="update medicines set medicine_id=%s where medicine_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from medicines;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)
        if c1==3:
            st1=int(input("Enter medicines's new Sale "))
            inp="update medicines set sale=%s where medicine_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from medicines;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)
        if c1==4:
            st1=int(input("Enter medicines's new unit "))
            inp="update medicines set unit= %s where medicine_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from medicines;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)
        if c1==5:
            st1=int(input("Enter medicines's new Quantity "))
            inp="update medicines set quantity=%s where medicine_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from medicines;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)
        if c1==6:
            st1=int(input("Enter medicines's new Minimum quantity "))
            inp="update medicines set Minimum_quantity=%s where medicine_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from medicines;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)
        if c1==7:
            st1=input("Enter Company's new name ")
            inp="update medicines set company_name='%s'where medicine_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from medicines;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)
        if c1==8:
            st1=int(input("Enter new supplier ID "))
            inp="update medicines set supplier_id=%s where medicine_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from medicines;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)
        if c1==9:
            st1=int(input("Enter new quantity to be purchased "))
            inp="update medicines set to_purchase=%s where medicine_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from medicines;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)
        print()
    if ch1==5:
        inp="select medicine_name from medicines"
        cursor.execute(inp)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)

if ch==2:
    print("Enter 1 to view customer menu ")
    print("Enter 2 to search customer ")
    print("Enter 3 to create new customer ")
    print("Enter 4 to update customer info ")
    ch2=int(input("Enter Your Choice! "))
    if ch2==1:
        inp="select * from customer;"
        cursor.execute(inp)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)
    if ch2==2:
        print("Enter 1 to search by customer name ")
        print("Enter 2 to search by customer id ")
        print("Enter 3 to search by customer phone no. ")
        print("Enter 4 to search by customer address ")
        print()
        c1=int(input("Enter your choice "))
        print()
        if c1==1:
            a=input("Enter customer name ")
            inp="select * from customer where customer_name='%s'"%a
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
        if c1==2:
            b=int(input("Enter customer ID "))
            inp="select * from customer where customer_id=%s"%b
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
        if c1==3:
            c=int(input("Enter customer Phone no "))
            inp="select * from customer where phone_no=%s"%c
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
        if c1==4:
            d=input("Enter customer Address ")
            inp="select * from customer where Address='%s'"%d
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
    if ch2==3:
        a=input("Enter customer name ")
        b=int(input("Enter customer ID "))
        c=int(input("Enter Phone no "))
        d=input("Enter Address ")
        inp="insert into customer values('%s',%s,%s,'%s')"%(a,b,c,d)
        cursor.execute(inp)
        mycon.commit()
        inp1="select * from customer;"
        cursor.execute(inp1)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)

    if ch2==4:
        st=input("Enter the name of the customer whose content is to be updated ")
        print("Enter 1 to update customer name ")
        print("Enter 2 to update customer id ")
        print("Enter 3 to update customer's phone no ")
        print("Enter 4 to update customer address ")
        print()
        c1=int(input("Enter your choice "))
        if c1==1:
            st1=input("Enter customers's new name ")
            inp="update customer set customer_name='%s'where customer_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from customer;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)
        if c1==2:
            st1=int(input("Enter customer's new ID"))
            inp="update customer set customer_id=%s where customer_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from customer;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)
        if c1==3:
            st1=int(input("Enter customer's new phone no"))
            inp="update customer set phone_no=%s where customer_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from customer;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)
        if c1==4:
            st1=input("Enter customers's new address")
            inp="update customer set address= '%s' where customer_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from customer;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)

if ch==3:
    print("Enter 1 to view supplier menu")
    print("Enter 2 to search supplier")
    print("Enter 3 to create new supplier")
    print("Enter 4 to update supplier info")
    ch2=int(input("Enter Your Choice!"))
    if ch2==1:
        inp="select * from supplier;"
        cursor.execute(inp)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)
    if ch2==2:
        print("Enter 1 to search by supplier name ")
        print("Enter 2 to search by supplier id")
        print("Enter 3 to search by supplier contact no")
        print("Enter 4 to search by supplier city")
        print("Enter 5 to search by supplier email ")
        print()
        c1=int(input("Enter your choice"))
        print()
        if c1==1:
            a=input("Enter supplier's name")
            inp="select * from supplier where supplier_name='%s'"%a
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
        if c1==2:
            b=int(input("Enter supplier ID"))
            inp="select * from supplier where supplier_id=%s"%b
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
        if c1==3:
            c=int(input("Enter supplier's Phone no"))
            inp="select * from supplier where contact_no=%s"%c
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
        if c1==4:
            d=input("Enter supplier's Address")
            inp="select * from supplier where supplier_city='%s'"%d
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
        if c1==5:
            e=input("Enter supplier's email")
            inp="select * from supplier where email='%s'"%e
            c=cursor.execute(inp)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
                print(row)
    if ch2==3:
        a=input("Enter supplier's name")
        b=int(input("Enter supplier's ID"))
        c=input("Enter suppliers city")
        d=int(input("Enter supplier's Phone no"))
        e=input("Enter supplier's email")
        inp="insert into supplier values('%s',%s,'%s',%s,'%s')"%(a,b,c,d,e)
        cursor.execute(inp)
        mycon.commit()
        inp1="select * from supplier;"
        cursor.execute(inp1)
        data=cursor.fetchall()
        count=cursor.rowcount
        for row in data:
            print(row)

    if ch2==4:
        st=input("Enter the name of the supplier whose content is to be updated")
        print("Enter 1 to update supplier's name ")
        print("Enter 2 to update supplier's id")
        print("Enter 3 to update supplier's city")
        print("Enter 4 to update suppliers's contact no ")
        print("Enter 5 to update supplier's email")
        print()
        c1=int(input("Enter your choice"))
        if c1==1:
            st1=input("Enter supplier's new name")
            inp="update supplier set supplier_name='%s'where supplier_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from supplier;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)
        if c1==2:
            st1=int(input("Enter supplier's new ID"))
            inp="update supplier set supplier_id=%s where supplier_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from supplier;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)
        if c1==3:
            st1=input("Enter supplier's new city")
            inp="update supplier set supplier_city='%s'where supplier_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from supplier;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)
        if c1==4:
            st1=int(input("Enter supplier's new contact no"))
            inp="update supplier set contact_no=%s where supplier_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from supplier;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)
        if c1==5:
            st1=input("Enter supplier's new email")
            inp="update supplier set email= '%s' where supplier_name='%s'"%(st1,st)
            cursor.execute(inp)
            mycon.commit()
            inp1="select * from supplier;"
            cursor.execute(inp1)
            data=cursor.fetchall()
            count=cursor.rowcount
            for row in data:
               print(row)