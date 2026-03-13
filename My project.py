import pickle


def insertInfo():
    print("------------------------------BASIC INFO----------------------------------------")
    patientid=input("Enter Patient ID:")
    name=input("Enter Patient Name:")
    age=input("Enter Patient Age:")
    gender=input("Enter Patient Gender:")
    contact=input("Enter Patient Contact:")
    address=input("Enter Patient Address:")
    print("--------------------------------MEDICAL INFO------------------------------------")
    allergies=input("Enter Patients Allergies Record:")
    medications=input("Enter Medications Record:")
    medicalhistory=input("Enter Medical History Record:")
    print("------------------------------APPOINTMENT HISTORY-------------------------------")
    pastappointments=input("Enter Past Patients Record:")
    upcomingappointments=input("Enter Upcoming Patients Appointments:")
    print("--------------------------------INSURANCE DETAILS-------------------------------")
    policynumber=input("Enter Poilicy Number:")
    provider=input("Enter Provider Name:")
    print("------------------------------EMERGENCY CONTACT---------------------------------")
    emergencycontactname=input("Enter Name:")
    relation=input("Enter Relation:")
    emergencycontact=input("Enter Contact:")

    info={"PatientID":patientid,
          "Name":name,
          "Age":age,
          "Gender":gender,
          "Contact":contact,
          "Address":address,
          "Allergies":allergies,
          "Medications":medications,
          "Medical History":medicalhistory,
          "Past Appointments":pastappointments,
          "Upcoming Appointments":upcomingappointments,
          "Policy Number":policynumber,
          "Provider":provider,
          "Emergency Contact Name":emergencycontactname,
          "Relation":relation,
          "Emergency Contact":emergencycontact}

    f=open("patient2.dat","ab")
    pickle.dump(info,f)
    f.close()

    

def readInfo():
    f=open("patient2.dat","rb")
    while True:
        try:
            info=pickle.load(f)
            print("--------------------------------------------------------------------------------")
            print("-----------")
            print("BASIC INFO")
            print("-----------")
            print("Patient ID:",info["PatientID"])
            print("Name:",info["Name"])
            print("Age:",info["Age"])
            print("Gender:",info["Gender"])
            print("Contact:",info["Contact"])
            print("Address:",info["Address"])
            print("------------")
            print("MEDICAL INFO")
            print("-------------")
            print("Allergies:",info["Allergies"])
            print("Medications:",info["Medications"])
            print("Medical History:",info["Medical History"])
            print("-------------------")
            print("APPOINTMENT HISTORY")
            print("--------------------")
            print("Past Appointments:",info["Past Appointments"])
            print("Upcomig Appointments:",info["Upcoming Appointments"])
            print("-----------------")
            print("INSURANCE DETAILS")
            print("------------------")
            print("Policy Number:",info["Policy Number"])
            print("Provider:",info["Provider"])
            print("-----------------")
            print("EMERGENCY CONTACT")
            print("------------------")
            print("Emergency Contact Name:",info["Emergency Contact Name"])
            print("Relation:",info["Relation"])
            print("Emergency Contact:",info["Emergency Contact"])
            print("--------------------------------------------------------------------------------")
        except EOFError:
            break
    f.close()

def searchPatientID(p):
    f=open("patient2.dat","rb")
    flag=False
    while True:
        try:
            info=pickle.load(f)
            if info["PatientID"]==p:
                print("--------------------------------------------------------------------------------")
                print("----------")
                print("BASIC INFO")
                print("----------")
                print("PatientID:",info["PatientID"])
                print("Name:",info["Name"])
                print("Age:",info["Age"])
                print("Gender:",info["Gender"])
                print("Contact:",info["Contact"])
                print("Address:",info["Address"])
                print("------------")
                print("MEDICAL INFO")
                print("------------")
                print("Allergies:",info["Allergies"])
                print("Medications:",info["Medications"])
                print("Medical History:",info["Medical History"])
                print("------------------")
                print("APPONTMENT HISTORY")
                print("------------------")
                print("Past Appointments:",info["Past Appointments"])
                print("Upcoming Appointments:",info["Upcoming Appointments"])
                print("-----------------")
                print("INSURANCE DETAILS")
                print("-----------------")
                print("Policy Number:",info["Policy Number"])
                print("Provider:",info["Provider"])
                print("-----------------")
                print("EMERGENCY CONTACT")
                print("-----------------")
                print("Emergency Contact Name:",info["Name"])
                print("Relation:",info["Relation"])
                print("Emergency Contact:",info["Contact"])
                print("--------------------------------------------------------------------------------")
                flag=True
        except EOFError:
                break
    if flag==False:
        print("No Records Found")
    f.close()


def updateName(p,n):
    f=open("patient2.dat","rb")
    infolst=[]
    while True:
        try:
            info=pickle.load(f)
            infolst.append(info)
        except EOFError:
            break
    f.close()
    for i in range(len(infolst)):
        if infolst[i] ["PatientID"]==p:
            infolst[i] ["Name"]=n
    f=open("patient2.dat","wb")
    for x in infolst:
        pickle.dump(x,f)
    f.close()


def deleteInfo(p):
    f=open("patient2.dat","rb")
    infolst=[]
    while True:
        try:
            info=pickle.load(f)
            infolst.append(info)
        except EOFError:
            break
    f.close()
    f=open("patient2.dat","wb")
    for x in infolst:
        if x["PatientID"]==p:
            continue
        pickle.dump(x,f)
    f.close()

while True:
    print("                             --------------------                               ")
    print("------------------------------PATIENT MANAGEMENT--------------------------------")
    print("                             --------------------                               ")               
    print("1. Insert Info.")
    print("2. Display Info.")
    print("3. Serach Info.")
    print("4. Update Info.")
    print("5. Delete Info.")
    print("6. Exit.")
    print("--------------------------------------------------------------------------------")
    print("")
    choice=int(input("Enter Your Choice:"))
    print("")
    if choice==1:
        insertInfo()
    if choice==2:
        readInfo()
    if choice==3:
        p=input("Enter Patient Id you want to search:")
        searchPatientID(p)
    if choice==4:
        p=input("Enter Patient Id:")
        n=input("Enter new Name:")
        updateName(p,n)
    if choice==5:
        p=input("Enter Patient ID:")
        deleteInfo(p)
    if choice==6:
        exit()
        
    
            
                
            
    

                      
        
                  
                  

    
    
    
