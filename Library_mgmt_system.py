import datetime
import os

class Library:
        def __init__(self,list_of_books,lib_name):
            self.list_of_books="list_of_books.txt"
            self.lib_name=lib_name
            self.books_dict={}
            id=101
            with open(self.list_of_books) as bk:
                contents=bk.readlines()
            for line in contents:
                self.books_dict.update({str(id):{'books_title':line.replace("\n",""),'lender_name':"",'Issue date':"",'Status':"Available"}})
                id=id+1
        def display_books(self):
            print("-----------------------List of Books--------------------")
            print("Books Id","\t","Title")
            print("----------------------------------------------------------")
            for key,value in self.books_dict.items():
                print(key,"\t",value.get("books_title"),"-[",value.get("Status"),"]")

        def issue_books(self):
            books_id=input("Enter books id :")
            current_date=datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
            if books_id in self.books_dict.keys():
                if not self.books_dict[books_id]["Status"]=="Available":
                    print(f"This books is already issued to{self.books_dict[books_id]['lender_name']}\
                    on {self.books_dict[books_id]['Issue_date']}")
                    return self.issue_books()
                elif self.books_dict[books_id]['Status']=="Available":
                    your_name=input("Enter your name :")
                    self.books_dict[books_id]['lender_name']=your_name
                    self.books_dict[books_id]['Issue_date']=current_date
                    self.books_dict[books_id]['Status']="Already Issued"
                    print("Books issued Successsfully!!!")
                else:
                    print("Book Id not found!!")
                    return self.issue_books()
        def add_books(self):
            new_books=input("Enter Books title : ")
            if new_books=="":
                return self.add_books()
            elif len(new_books)>25:
                print("Books title length is too long!!title length should be 20 character")
                return self.add_books()
            else:
                with open(self.list_of_books,"a")as bk:
                    bk.writelines(f"{new_books}\n")
                    self.books_dict.update({str(int(max(self.books_dict))+1):{'books_title':new_books,'lender_name':"",'Issue_date':"",'Status':"Available"}})
                    print(f"This books'{new_books}'has been added successfully!!!!")
        def return_books(self):
            books_id=input("Enter books Id : ")
            if books_id in self.books_dict.keys():
                if self.books_dict[books_id]["Status"]=="Available":
                    print("This book is already available in library.please check your book id")
                    return self.return_books()
                elif not self.books_dict[books_id]["Status"]=="Available":
                    self.books_dict[books_id]['lender_name']=""
                    self.books_dict[books_id]['Issue_date']=""
                    self.books_dict[books_id]['Status']="Available"
                    print("Successsfully Return!!!!")

        def remove_books(self):
             books_id=input("Enter books Id : ")
             if books_id in self.books_dict.keys():
                self.books_dict




#l=Library("list_of_books.txt","Technology Library")
#print(l.display_books())
#class Books:
#class User:

try:
    mylms=Library("list_of_books.txt","Technology Library")
    press_key_list={"D":"Display Books","I":"Issue Books","A":"Add Books","R":"Return Books","B":"Remove Books","Q":"Quit"}
    key_press=False
    while not(key_press=="q"):
        print("\n--------Welcome To Library Management System---------------\n")
        for key,value in press_key_list.items():
            print("Press",key,"To",value)
        key_press=input("Press_key :").lower()
        if key_press=="i":
                print("\nCurrent Selection : Issue Books\n")
                mylms.issue_books()
        elif key_press=="a":
                print("\nCurrent Selection : Add Books\n")
                mylms.add_books()
        elif key_press=="d":
                print("\nCurrent Selection : Display Books\n")
                mylms.display_books()
        elif key_press=="r":
                print("\nCurrent Selection : Return Books\n")
                mylms.return_books()
        elif key_press=="b":
                print("\nCurrent Selection : Remove Books\n")
                mylms.remove_books()
        elif key_press=="q":
                break
        else:
                continue
except Exception as e:
        print("Something went wrong.please check your input!!")

       