import os
import platform
import mysql.connector as s
import datetime

class AirBooking:
    def __init__(self):
        #creating the connection string between mysql and python
        #if not connected handling the error through exception handling
        try:
            self.mydb=s.connect(host="dbpanel.squadinfotech.in",user="testuser",password="testuser",database="testingdb")
            print("Connected to Mysql")
            
        except:
            print("Not connected")

        #creating tables
        self.pdata="create table if not exists passengerdetails(custno varchar(15),custname varchar(20),addr varchar(200),jrdate date,source varchar(20),destination varchar(30))"
        self.tkt="create table if not exists tkt(custno varchar(25),tkt_tot int,lug_tot int,g_tot int)"
        
        #creating cursor
        self.mycursor=self.mydb.cursor()
        self.mycursor.execute(self.pdata)
        #print("Passengerdetails table created")

        #executing query from python to mysql through connectivity
        self.mycursor.execute(self.tkt)
        #print("Table created tkt")
        
        #permanantly saving the changes in mysql table
        self.mydb.commit()
        #print("saved the changes")

            
    def registercust(self):
        L=[]
        custno=int(input('Enter customer no='))
        L.append(custno)
        name=input('Enter name:')
        L.append(name)
        addr=input('Enter address:')
        L.append(addr)
        jr_date=input('Enter date of journey:')
        L.append(jr_date)
        source=input('Enter source:')
        L.append(source)
        destination=input('Enter destination:')
        L.append(destination)
        
        cust=(L)
        sql='insert into pdata(custno,custname,addr,jrdate,source,destination) values(%s,%s,%s,%s,%s,%s)'
        self.mycursor.execute(sql,cust)
        self.mydb.commit()


    def ticketprice(self):
        L=[]
        cno=int(input('Enter custoner no='))
        L.append(cno)
        print('We have the following rooms for you:-')
        print('1. type First class--->rs 6000 PN\-')
        print('2. type Business class--->rs 4000 PN\-')
        print('3. type Economy class--->rs 2000 PN\-')
        x=int(input('Enter your choice:'))
        n=int(input('Enter No. of Passengers:'))
        if x==1:
            print('you have opted First class.')
            s=6000*n
            L.append(s)
        elif x==2:
            print('you have opted Business class.')
            s=4000*n
            L.append(s)
        elif x==3:
            print('you have opted Economy class.')
            s=2000*n
            L.append(s)
        else:
            print('Please select a class type.')
        print('your ticket charge is =',s,'\n')
        print('Extra luggage charge 100 rs per kg')
        
        y=int(input('Enter your weight,of extra luggage:'))
        z=y*100
        L.append(z)
        tkt=(L)
        print('Your Totalbill:',s+z,'\n')
        g_tot=s+z
        L.append(g_tot)
        sql="insert into tkt (custno,tkt_tot,lug_tot,g_tot) values (%s,%s,%s,%s)"
        self.mycursor.execute(sql,tkt)
        self.mydb.commit()
        
    def dis(self):
        custno=int(input("Enter the customer number whose bill to be viewed : "))
        sql="Select pdata.custno, pdata.custname, pdata.addr,pdata.source,pdata.destination,tkt.tkt_tot,tkt.lug_tot, g_tot from pdata INNER JOIN tkt ON pdata.custno=tkt.custno and tkt.custno = %s"
        rl=(custno,)
        self.mycursor.execute(sql,rl)
        res=self.mycursor.fetchall()
        for x in res:
            print(x)

    def dispall(self):
        sql="Select pdata.custno, pdata.custname, pdata.addr,pdata.source,pdata.destination,tkt.tkt_tot,tkt.lug_tot, g_tot from pdata INNER JOIN tkt ON pdata.custno=tkt.custno" 
        self.mycursor.execute(sql)   
        res=self.mycursor.fetchall()
        print("The Customer details are as follows : ")
        
        for x in res:
            print(x)
        
Indian_Airline = AirBooking()


def Menuset():
    print('Enter 1: To enter customer data.')
    print('Enter 2: For ticketamount.')
    print('Enter 3: Display customerwise Details.')
    print('Enter 4: Display All Details.')
    print('Enter 5: Exit')
    
    userinput=int(input('Enter your choice:'))
    if userinput==1:
        Indian_Airline.registercust()
    elif userinput==2:
        Indian_Airline.ticketprice()
    elif userinput==3:
        Indian_Airline.dis()
    elif userinput==4:
        Indian_Airline.dispall()
    elif userinput==5:
        quit()
    else:
        print('Enter correct choice.')

Menuset()

def runagain():
    runagn=input('\nWant to run again? y/n:')
    while runagn=='y':
        if platform.system=='windows':
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menuset()
        runagn=input('\nWant to run again? y/n:')
runagain()
