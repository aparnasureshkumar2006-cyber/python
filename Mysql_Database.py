import mysql.connector
from tabulate import tabulate

con = mysql.connector.connect(host ="localhost", user = "root", password = "Anu@0104", database = "data_db")

while True:
    print("---Contact Management System---")
    print("1.Insert")
    print("2.Select")
    print("3.Update")
    print("4.Delete")
    print("5.Exit")
    choice = int(input("Enter your Choice:"))

    if choice == 1:
        name = input("Enter your Name:")
        age = int(input("Enter your Age:"))
        address = input("Enter your Address:")
        contact = input("Enter your Mobile Number:")
        email = input("Enter your email:")
        sql = "insert into data(name,age,address,contact,email) values (%s,%s,%s,%s,%s)"
        cursor = con.cursor()
        cursor.execute(sql,(name,age,address,contact,email))
        con.commit()
        print("---Insert Successfully---")
    
    elif choice == 2:
        cursor = con.cursor()
        sql = "Select * from data"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(tabulate(result, headers=["ID", "NAME", "AGE", "ADDRESS","CONTACT","MAIL"]))

    elif choice == 3:
        print("1.Name.")
        print("2.Age.")
        print("3.Address.")
        print("4.Contact.")
        print("5.Email.")
        option = int(input("What do you want to Update? "))

        if option == 1:
            id = int(input("Enter Id:"))
            name = input("Enter Name:")
            cur = con.cursor()
            sql = "update data set name=%s where id=%s"
            cur.execute(sql, (name, id))
            con.commit()
            print("---Update Successfully---")
        
        elif option == 2:
            id = int(input("Enter Id:"))
            age = input("Enter Age:")
            cur = con.cursor()
            sql = "update data set age=%s where id=%s"
            cur.execute(sql,(age,id))
            con.commit()
            print("---Update Successfully---")

        elif option == 3:
            id = int(input("Enter Id:"))
            address = input("Enter Address:")
            cur = con.cursor()
            sql = "update data set address = %s where id = %s"
            cur.execute(sql,(address,id))
            con.commit()
            print("---Update Successfully---")

        elif option == 4:
            id = int(input("Enter Id:"))
            contact = input("Enter Contact:")
            cur = con.cursor()
            sql = "update data set contact = %s where id = %s"
            cur.execute(sql,(contact,id))
            con.commit()
            print("---Update Successfully---")

        elif option == 5:
            id = int(input("Enter Id:"))
            email = input("Enter Email:")
            cur = con.cursor()
            sql = "update data set email = %s where id = %s"
            cur.execute(sql,(email,id))
            con.commit()
            print("---Update Successfully---")

        else:
            print("---Invalid Option---")

    elif choice == 4:
        id = input("Enter Id:")
        cursor = con.cursor()
        sql = "delete from data where id=%s"
        cursor.execute(sql,(id,))
        con.commit()
        print("---Deleted Successfully---")

    elif choice == 5:
        print ("...Thank you for using...")

    else:
        print("---Invalid Choice---")

        

