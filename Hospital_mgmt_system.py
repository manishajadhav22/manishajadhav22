####HOSPITAL MANAGEMENT SYSTEM#####


class Patient:
    patientList=list()
    def __init__(self,pat_no,pat_name,pat_age,pat_gender,pat_rm):
        self.pat_no,self.pat_name=pat_no,pat_name
        self.pat_age,self.pat_gender,self.pat_rm=pat_age,pat_gender,pat_rm
    def AddNewPatient(self):
        Patient.patientList.append(self)
        print("Patient Data Added Successfully")
    def GetPatientList(self):
        return Patient.patientList
    def GetPatientByNo(pat_no):
        for i in Patient.patientList:
            if pat_no==i.GetPatientno():
               return i
        return False
    def GetPatientno(self):
        return self.pat_no
    def EditPatientData(self,pat_no,pat_name,pat_age,pat_gender,pat_rm):
        for i in Patient.patientList:
           
            if i.GetPatientno()== pat_no:
                i.pat_name=pat_name
                i.pat_age=pat_age
                i.pat_gender=pat_gender
                i.pat_rm=pat_rm
                return True
        return False
    def EditPatientName(Patient,pat_no):
        for pt in Patient.patientList:
            if pt.GetPatientno() == pat_no:
                name=input("Enter New Name : ")
                pt.pat_name=name
                return "Patient Name Updated Successfully for Patient No"+str(pat_no)
        return "Patient Not Found for patient No"+str(pat_no)
    def EditPatientAge(Patient,pat_no):
        for pt in Patient.patientList:
            if pt.GetPatientno() == pat_no:
                age=input("Enter New Age : ")
                pt.pat_age=age
                return "Patient Age Updated Successfully for Patient No"+str(pat_no)
        return "Patient Not Found for patient No  "+str(pat_no)           
        
    def EditPatientGender(Patient,pat_no):
        for pt in Patient.patientList:
            if pt.GetPatientno() == pat_no:
                gender=input("Enter New Gender : ")
                pt.pat_gender=gender
                return "Patient Gender Updated Successfully for Patient No"+str(pat_no)
        return "Patient Not Found for patient No  "+str(pat_no)           
        
    def EditPatientRoomno(Patient,pat_no):
        for pt in Patient.patientList:
            if pt.GetPatientno() == pat_no:
                rm=input("Enter New Room No : ")
                pt.pat_rm=rm
                return "Patient Room no Updated Successfully for Patient No"+str(pat_no)
        return "Patient Not Found for patient No  "+str(pat_no)           
    def DeletePatientDataByno(Patient,pat_no):
        for pt in Patient.patientList:
            if pt.GetPatientno() == pat_no:
                bill=input("Patient have paid all the bills(y/n) : ")
                if bill=="y":
                  Patient.patientList.remove(pt)
                  return True
               
        return False
   
class Doctor:
    doctorList=list()
    def __init__(self,doc_id,doc_name,doc_sp,doc_age,doc_mno,doc_fee):
        self.doc_id=doc_id
        self.doc_name,self.doc_sp,self.doc_age=doc_name,doc_sp,doc_age
        self.doc_mno,self.doc_fee=doc_mno,doc_fee
    def AddNewDoctor(self):
        Doctor.doctorList.append(self)
        print("Doctor's data Added Successfully")
    def GetDoctorList(self):
        return Doctor.doctorList
    def GetDoctorDataById(self,doc_id):
        for i in Doctor.doctorList:
            if i.GetDoctorid()==doc_id:
               return i
        return False

    def GetDoctorid(self):
        return self.doc_id

    def EditDoctorData(self,doc_id,doc_name,doc_sp,doc_age,doc_mno,doc_fee):
        for dt in Doctor.doctorList:
            if dt.GetDoctorid()==doc_id:
                dt.doc_name=doc_name
                dt.doc_sp=doc_sp
                dt.doc_age=doc_age
                dt.doc_mno=doc_mno
                dt.doc_fee=doc_fee
                return "Doctors Data Updated Successfully for Doctor id "+str(doc_id)
        return "Doctors Data Not Found For Doctor id  "+str(doc_id)
    def EditDoctorName(self,doc_id):
        for dt in Doctor.doctorList:
            if dt.GetDoctorid() == doc_id:
                name=input("Enter New Name : ")
                dt.doc_name=name
                return "Doctor Name Updated Successfully for doctor id "+str(doc_id)
        return "Doctor Data Not Found for Doctor id"+str(doc_id)
    def EditDoctorSp(self,doc_id):
        for dt in Doctor.doctorList:
            if dt.GetDoctorid() == doc_id:
                sname=input("Enter New Specialization : ")
                dt.doc_sp=sname
                return "Doctor Specialization Updated Successfully for doctor id "+str(doc_id)
        return "Doctor Data Not Found for Doctor id"+str(doc_id)
    def EditDoctorAge(self,doc_id):
        for dt in Doctor.doctorList:
            if dt.GetDoctorid() == doc_id:
                age=input("Enter New Age : ")
                dt.doc_age=age
                return "Doctor Age Updated Successfully for doctor id "+str(doc_id)
        return "Doctor Data Not Found for Doctor id"+str(doc_id)
    def EditDoctorMobileno(self,doc_id):
        for dt in Doctor.doctorList:
            if dt.GetDoctorid() == doc_id:
                mno=input("Enter New Mobile no : ")
                dt.doc_mno=mno
                return "Doctor Mobile No Updated Successfully for doctor id "+str(doc_id)
        return "Doctor Data Not Found for Doctor id"+str(doc_id)
    def EditDoctorFee(self,doc_id):
        for dt in Doctor.doctorList:
            if dt.GetDoctorid() == doc_id:
                fee=input("Enter New Fee : ")
                dt.doc_fee=fee
                return "Doctor Fees Updated Successfully for doctor id "+str(doc_id)
        return "Doctor Data Not Found for Doctor id"+str(doc_id)

    def DeleteDoctorDataByid(self,doc_id):
        for dt in Doctor.doctorList:
            if dt.GetDoctorid()==doc_id:
                Doctor.doctorList.remove(dt)
                return "Doctor Data is Deleted Successfully for doctor id "+str(doc_id)
        return "doctor not found for doctor id  "+str(doc_id)
   
            

print("                Wel-Come In Hospital Management System                    ")
while True:
    print("\n1.SignIn \n2.LogIn\n3.Logout")
    ch=int(input("Enter Choice  :"))
    if ch==1:
        while True:
            u_name=input("Set Username  :")
            u_pwd=input("Set Password  :")

            if len(u_pwd) >= 6:
              p=["@","#","$","&","_","*"]
              for i in p:
                   x=u_pwd.find(i)
                   if x != -1:
                     u_pass=u_pwd
                     print("Username And Password Created Successfully !! ")
                     break
                   else:
                     print("password should have atleast one spacial character")
                   break
            else:
              print("Password Should have atleast 6 Chracter ")
            break
        
        
    elif ch==2:
       while True:
           print("\n1.User Login \n2.Admin Login \n3.Back")
           ch1=int(input("Enter choice (1/2/3): "))
           if ch1==1:
               l_name=input("Enter Username  :")
               l_pass=input("Enter Password  :")
               if u_name==l_name and u_pass==l_pass:
                   while True:
                       print("\n1.Doctors Details \n2.Nurse Details\n3.others\n4.Back")
                       u_ch=input("Enter Choice (1/2/3): ")
                       if u_ch=="1":
                            while True:
                               print("\n1.Cardiology Department\n2.Orthopedics Department")
                               print("3.Pediatrics \n4.Gynaecology")
                               print("5.Logout")
                               u_ch1=input("\nEnter Choice :")
                               if u_ch1=="1":
                                  print("\nDoctors Available for Cardiology Department")
                                  print("Dr Abhijit Kulkarni    MBBS,MD,DM(Cardiology)  ")
                                  print("Dr Akhilesh Jain       MBBS,MD(Medicine),DM(Cardiology)")
                                  
                               elif u_ch1=="2":
                                  print("\nDoctors Available for Orthopedic Department")
                                  print("Dr Aditya Khemka       MBBS,MS Orthopaedics  ")
                                  print("Dr Sourabh Kulkarni    MBBS,MS Orthopaedics ")
                                  

                               elif u_ch1=="3":
                                  print("\nDoctors Available for Pediatric Department")
                                  print("Dr Maitreye Datta      pediatrics ")
                                  print("Dr Sourabh Kulkarni    MBBS,DCH")
                               elif u_ch1=="4":
                                  print("\nDoctors Available for Gynaecology Department")
                                  print("Dr Sulbha Arora        Infertility Specialist  ")
                                  print("Dr Sourabh Kulkarni    Gynaecologists and Obstetricians ")
                               elif u_ch1=="5":
                                  break
                               else:
                                   print("Invalid choice ")
                       elif u_ch=="2":
                          print("Kamal Sinha            Cardiology Department")
                          print("meena Patil            Cardiology Department")
                          print("jayashree Vaidya       Orthopedics Department")
                          print("jay Kumar              Orthopedics Department")
                          print("meera Jayanti          Pediatrics Department")
                          print("Navina Lad             Pediatrics Department")
                          print("Sandip Mishra          Gynaecology Department")
                          print("Sarita Mohite          Gynaecology Department")
                       elif u_ch=="3":
                           pass
                       elif u_ch=="4":
                          break
                       else:
                           print("Please Enter Valid Choice")

               else:
                   print("Invalid Username or Password")
           elif ch1==2:
                a_name="admin"
                a_pass="123"
                adm_name=input("Enter Username  :")
                adm_pass=input("Enter Password  :")
                if adm_name==a_name and adm_pass==a_pass:
                   print("Admin Login Successfully")
                   while True:
                        print("\n1.To Manage Patients Enter :\n2.To Manage Doctors Enter")
                        print("3.Discharge Summery\n4.Logout")
                        a_ch=input("Enter choice (1/2/3/4) : ")
                        if a_ch=="1":
                            while True:
                                print("\n1.Add New Patient\n2.Display Patients Detail")
                                print("3.Display Specific Patient by patient no")
                                print("4.Edit Patient data by patient no")
                                print("5.Edit Specific patient Data by patient no")
                                print("6.Logout")

                                p_ch=input("Enter Your Choice  :")
                                if p_ch=="1":
                                    pat_no=int(input("Enter Patient No :"))
                                    pat_name=input("Enter Patient Name :")
                                    pat_age=int(input("Enter Patient Age   :"))
                                    pat_gender=input("Enter Patient Gender :")
                                    pat_rm=int(input("Enter Patient Room No:"))

                                    p=Patient(pat_no,pat_name,pat_age,pat_gender,pat_rm)
                                    p.AddNewPatient()
                                elif p_ch=="2":
                                    for ps in Patient.GetPatientList(Patient):
                                        print()
                                        print("Patients Details ")
                                        print("Patient No     :",ps.pat_no)
                                        print("Patient Name   :",ps.pat_name)
                                        print("Patient Age    :",ps.pat_age)
                                        print("Patient Gender   :",ps.pat_gender)
                                        print("Patient Room No  :",ps.pat_rm)
                                        
                                elif p_ch=="3":
                                    pat_no=int(input("Enter Patients No :"))

                                    p1=Patient.GetPatientByNo(pat_no)

                                    if p1==False:
                                        print("\n Sorry .....Patient get Discharge")
                                    else:
                                        print("\nPatients Details ")
                                        print("Patient No     :",p1.pat_no)
                                        print("Patient Name   :",p1.pat_name)
                                        print("Patient Age    :",p1.pat_age)
                                        print("Patient Gender   :",p1.pat_gender)
                                        print("Patient Room No  :",p1.pat_rm)
                                               
                                elif p_ch=="4":
                                    pat_no=int(input("Enter Patient No :"))
                                    pat_name=input("Enter Patient Name :")
                                    pat_age=int(input("Enter Patient Age   :"))
                                    pat_gender=input("Enter Patient Gender :")
                                    pat_rm=int(input("Enter Patient Room No:"))

                                    p2=Patient.EditPatientData(Patient,pat_no,pat_name,pat_age,pat_gender,pat_rm)
                                    if p2 == True:
                                        print("Patient Data Updated Successfully")
                                    else:
                                        print("Patient Not found for Patient no",pat_no)

                                   
                                elif p_ch=="5":
                                    while True:
                                        print("1.Edit Name \n2.Edit Age\n3.Edit Gender\n4.Edit Room no")
                                        print("5.Back")
                                        e_ch=input("Enter Your Choice : ")
                                        if e_ch=="1":
                                             pat_no=int(input("Enter Patient No :"))
                                             print(Patient.EditPatientName(Patient,pat_no))
                                        elif e_ch=="2":
                                             pat_no=int(input("Enter Patient No :"))
                                             print(Patient.EditPatientAge(Patient,pat_no))
                                        
                                        elif e_ch=="3":
                                             pat_no=int(input("Enter Patient No :"))
                                             print(Patient.EditPatientGender(Patient,pat_no))  
                                        elif e_ch=="4":
                                             pat_no=int(input("Enter Patient No :"))
                                             print(Patient.EditPatientRoomno(Patient,pat_no))  
                                        elif e_ch=="5":
                                            break
                                        else:
                                            print("Invalid Choice")
                                    
                                     
                               
                                elif p_ch=="6":
                                   break
                                else:
                                    print("please Enter Valid choice")
                            
                        elif a_ch=="2":
                            while True:
                                print("\n1.Add New Doctor\n2.Display Doctor's Detail")
                                print("3.Display Specific Doctor by Doctor Id")
                                print("4.Edit Doctor's data by Doctor Id")
                                print("5.Edit Specific Doctor by Doctor Id")
                                print("6.delete Doctor by Doctor Id")
                                print("7.Logout")

                                d_ch=input("Enter Your Choice : ")
                                if d_ch=="1":
                                    doc_id=int(input("Enter Doctor Id : "))
                                    doc_name=input("Enter Doctor Name : ")
                                    doc_sp=input("Enter the Specialization : ")
                                    doc_age=int(input("Enter Doctor Age : "))
                                    while True:
                                        doc_mno=int(input("Enter Contact No : "))
                                        if len(str(doc_mno))==10:
                                            break
                                        
                                        else:
                                            print("Please enter 10 digit Mobile number")
                                           
                                    doc_fee=int(input("Enter The Fees : "))
                                    d=Doctor(doc_id,doc_name,doc_sp,doc_age,doc_mno,doc_fee)
                                    d.AddNewDoctor()
                                    
                                   
                                elif d_ch=="2":
                                    print()
                                    print("Doctor's  Details ")
                                    for d1 in Doctor.GetDoctorList(Doctor):
                                        print()
                                        print("Doctor Id  : ",d1.doc_id)
                                        print("Doctor Name :",d1.doc_name)
                                        print("Doctor Specialization : ",d1.doc_sp)
                                        print("Doctor Age : ",d1.doc_age)
                                        print("Doctor Mobile No :",d1.doc_mno)
                                        print("Doctor Fee :",d1.doc_fee)
                                elif d_ch=="3":
                                    doc_id=int(input("Enter Doctor Id  : "))
                                    ds=Doctor.GetDoctorDataById(Doctor,doc_id)

                                    if ds== False:
                                        print("\nSorry......Doctor Data not found")
                                    else:
                                        print("\nDoctor Id  : ",ds.doc_id)
                                        print("Doctor Name :",ds.doc_name)
                                        print("Doctor Specialization : ",ds.doc_sp)
                                        print("Doctor Age : ",ds.doc_age)
                                        print("Doctor Mobile No :",ds.doc_mno)
                                        print("Doctor Fee :",ds.doc_fee)
                                elif d_ch=="4":
                                    doc_id=int(input("Enter Doctor Id  : "))
                                    
                                    doc_name=input("Enter Doctor Name : ")
                                    doc_sp=input("Enter the Specialization : ")
                                    doc_age=int(input("Enter Doctor Age : "))
                                    doc_mno=int(input("Enter Contact No : "))
                                    doc_fee=int(input("Enter The Fees : "))

                                    print(Doctor.EditDoctorData(Doctor,doc_id,doc_name,doc_sp,doc_age,doc_mno,doc_fee))
                                elif d_ch=="5":
                                    while True:
                                           print()
                                           print("1.Edit Name\n2.Edit Specialization\n3.Edit Age\n4.Edit Mobile No")
                                           print("5.Edit Fee\n6.Back")

                                           d_ch1=input("Enter Your Choice  : ")
                                           if d_ch1=="1":
                                                doc_id=int(input("Enter Doctor id :"))
                                                print(Doctor.EditDoctorName(Doctor,doc_id))

                                           elif d_ch1=="2":
                                                doc_id=int(input("Enter Doctor id :"))
                                                print(Doctor.EditDoctorSp(Doctor,doc_id))
                                           elif d_ch1=="3":
                                                doc_id=int(input("Enter Doctor id :"))
                                                print(Doctor.EditDoctorAge(Doctor,doc_id))
                                           elif d_ch1=="4":
                                                doc_id=int(input("Enter Doctor id :"))
                                                print(Doctor.EditDoctorMobileno(Doctor,doc_id))
                                           elif d_ch1=="5":
                                                doc_id=int(input("Enter Doctor id :"))
                                                print(Doctor.EditDoctorFee(Doctor,doc_id))
                                           elif d_ch1=="6":
                                               break
                                           else:
                                               print("Invalid Choice  ")
                                       
                                elif d_ch=="6":
                                   doc_id=int(input("Enter Doctor id :"))
                                   print(Doctor.DeleteDoctorDataByid(Doctor,doc_id))
                                elif d_ch=="7":
                                    break
                                else:
                                    print("Invalid Choice......Enter Correct Choice")

                                
                        elif a_ch=="3":
                                   pat_no=int(input("Enter Patient No : "))
                                   ps=Patient.DeletePatientDataByno(Patient,pat_no)
                                   if ps==True:
                                       print("Patient paid all bills so, he have Get Discharged ")
                                   else:
                                       print("Patient have  get discharge")

                                   
                        elif a_ch=="4":
                               break
                        else:
                                print("please enter correct choice ")
                else:
                   print("Admin Username Or Password is Incorrect")
                    
               
           elif ch1==3:
             break
           else:
                print("Please Enter Valid choice ")
                
    elif ch==3:
        break
    else:
        print("Invalid Choice")
