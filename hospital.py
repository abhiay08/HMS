from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector


class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="orange",bg="grey",font=("monospace",40,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        # ****************** Use DataFrame **********************************************************************************                     
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=90,width=1530,height=400)
        
        DataframeLeft=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,
                                 font=("monospace",20,"bold"),text="Patient Information")  

        DataframeLeft.place(x=0,y=8,width=940,height=350)
        
        
        DataframeRight=LabelFrame(Dataframe,bd=10,padx=20,relief=RIDGE,
                                 font=("arial",20,"bold"),text="Patient Prescription")  

        DataframeRight.place(x=950,y=5,width=380,height=350)
        
        
            # ****************** Use ButtonFrame ************************************
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        
        
        
        
            # ****************** Use DetailsFrame ************************************
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=200)
        
        
        
            # ****************** Use DataFrameLeft ************************************

        lblNameTablet=Label(DataframeLeft,text='Tablet Name',font=('times new roman',15,'bold'),padx=2,pady=5)
        lblNameTablet.grid(row=0,column=0)
        
        comNametablet=ttk.Combobox(DataframeLeft,font=('times new roman',15,'bold'),width=22)
        comNametablet['values']=('Nice',
                                                'Acetaminophen',
                                                'Adderall',
                                                'Amitriptyline',
                                                'Amlodipine',
                                                'Amoxicillin',
                                                'Ativan',
                                                'Atorvastatin',
                                                'Azithromycin')
        comNametablet.grid(row=0,column=1)
        
        lblref=Label(DataframeLeft,text='Reference no: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=('arial',12,'bold'),width=25)
        txtref.grid(row=1,column=1)
        
        
        comref=ttk.Combobox(DataframeLeft,font=('times new roman',15,'bold'),width=22)
        comref['values']=(
            'Ref14500',
            'Ref14501',
            'Ref14502',
            'Ref14503',
            'Ref14504',
            'Ref14505',
            'Ref14506'
        
            
        )
        comref.grid(row=1,column=1)
        
        lblDose=Label(DataframeLeft,text='Dose: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lblDose.grid(row=2,column=0,sticky=W)
        txtDose=Entry(DataframeLeft,font=('arial',12,'bold'),width=25)
        txtDose.grid(row=2,column=1)
        
        
        comDose=ttk.Combobox(DataframeLeft,font=('times new roman',15,'bold'),width=22)
        comDose['values']=(
            'No Dose',
            '1',
            '2',
            '3',
            '4',
            '5',
            '6')
        comDose.grid(row=2,column=1)
        
        lblNo_of_Tablets=Label(DataframeLeft,text='Number of Tablets: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lblNo_of_Tablets.grid(row=3,column=0,sticky=W)
        txtNo_of_Tablets=Entry(DataframeLeft,font=('arial',12,'bold'),width=25)
        txtNo_of_Tablets.grid(row=3,column=1)
        
        comNo_of_Tablets=ttk.Combobox(DataframeLeft,font=('times new roman',15,'bold'),width=22)
        comNo_of_Tablets['values']=(
            '1',
            '2',
            '3',
            '4',
            '5',
            '6',
            '7',
            '8',
            '9',
            '10')
        comNo_of_Tablets.grid(row=3,column=1)
        
        
        lblLots=Label(DataframeLeft,text='Lots: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lblLots.grid(row=4,column=0,sticky=W)
        txtLots=Entry(DataframeLeft,font=('arial',12,'bold'),width=25)
        txtLots.grid(row=4,column=1)
        
        lblissue=Label(DataframeLeft,text='Issue Date: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lblissue.grid(row=5,column=0,sticky=W)
        txtissue=Entry(DataframeLeft,font=('arial',12,'bold'),width=25)
        txtissue.grid(row=5,column=1)
        
        lblexp=Label(DataframeLeft,text='Expiry Date: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lblexp.grid(row=6,column=0,sticky=W)
        txtexp=Entry(DataframeLeft,font=('arial',12,'bold'),width=25)
        txtexp.grid(row=6,column=1)
        
        
        lbldailyDose=Label(DataframeLeft,text='Daily Dose: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lbldailyDose.grid(row=7,column=0,sticky=W)
        txtdailyDose=Entry(DataframeLeft,font=('arial',12,'bold'),width=25)
        txtdailyDose.grid(row=7,column=1)
          
        lblEffects=Label(DataframeLeft,text='Side Effects: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lblEffects.grid(row=8,column=0,sticky=W)
        txtEffects=Entry(DataframeLeft,font=('arial',12,'bold'),width=25)
        txtEffects.grid(row=8,column=1)
        
        lblFurtherinfo=Label(DataframeLeft,text='Further Info: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lblFurtherinfo.grid(row=0,column=2,sticky=W)
        txtFurtherinfo=Entry(DataframeLeft,font=('arial',12,'bold'),width=25)
        txtFurtherinfo.grid(row=0,column=5)
        
        
        lblBloodPressure=Label(DataframeLeft,text='Blood Pressure: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=('arial',12,'bold'),width=25)
        txtBloodPressure.grid(row=1,column=5)
        
        
        lblStorage=Label(DataframeLeft,text='Storage Advice: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lblStorage.grid(row=2,column=2,sticky=W)
        txtStorage=Entry(DataframeLeft,font=('arial',12,'bold'),width=25)
        txtStorage.grid(row=2,column=5)
        
        
        lblMedicine=Label(DataframeLeft,text='Safety Measures: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lblMedicine.grid(row=3,column=2,sticky=W)
        txtMedicine=Entry(DataframeLeft,font=('arial',12,'bold'),width=25)
        txtMedicine.grid(row=3,column=5)
        
        
        lblPatientId=Label(DataframeLeft,text='Patient ID: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=('arial',12,'bold'),width=25)
        txtPatientId.grid(row=4,column=5)
        
        
        lblNhsNumber=Label(DataframeLeft,text='NHS Number: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lblNhsNumber.grid(row=5,column=2,sticky=W)
        txtNhsNumber=Entry(DataframeLeft,font=('arial',12,'bold'),width=25)
        txtNhsNumber.grid(row=5,column=5)
        
        lblPatientName=Label(DataframeLeft,text='Patient Name: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataframeLeft,font=('arial',12,'bold'),width=25)
        txtPatientName.grid(row=6,column=5)
        
        lblPatientDOB=Label(DataframeLeft,text='Date of Birth: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lblPatientDOB.grid(row=7,column=2,sticky=W)
        txtPatientDOB=Entry(DataframeLeft,font=('arial',12,'bold'),width=25)
        txtPatientDOB.grid(row=7,column=5)
        
        
        lblAdd=Label(DataframeLeft,text='Patient Address: ',font=('times new roman',15,'bold'),padx=2,pady=4)
        lblAdd.grid(row=8,column=2,sticky=W)
        txtAdd=Entry(DataframeLeft,font=('arial',15,"bold"),width=25)
        txtAdd.grid(row=8,column=5)
        
        
        # ****** Data Frame Right For Prescription*******
        
        self.txtPrescription=Text(DataframeRight, font=('arial',12,'bold'),width=35,height=15,padx=2,pady=4)
        
        self.txtPrescription.grid(row=0,column=0)
        
        
        #  ***************** Buttons *****************************
        
        btnPrescription=Button(Buttonframe,text="Prescription",bg='green',fg='white',font=("arial",18,'bold'),width=14)
        btnPrescription.grid(row=0,column=0)
        
        btnPrescriptionData=Button(Buttonframe,text="Save",bg='green',fg='white',font=("arial",18,'bold'),width=15)
        btnPrescriptionData.grid(row=0,column=2)
        
        btnUpdate=Button(Buttonframe,text="Update",bg='green',fg='white',font=("arial",18,'bold'),width=14)
        btnUpdate.grid(row=0,column=3)
        
        btnDelete=Button(Buttonframe,text="Delete",bg='green',fg='white',font=("arial",18,'bold'),width=14)
        btnDelete.grid(row=0,column=4)
        
        btnClear=Button(Buttonframe,text="Clear",bg='green',fg='white',font=("arial",18,'bold'),width=14)
        btnClear.grid(row=0,column=5)
        
        btnExit=Button(Buttonframe,text="Exit",bg='green',fg='white',font=("arial",18,'bold'),width=14)
        btnExit.grid(row=0,column=6)
        
        
        
        # ************Scroll Bar ***************************
        
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        
        # ******Table creation for Hider ************
        
        self.hospital_table=ttk.Treeview(Detailsframe,column=('NameofTable','Ref','Dose','NoofTablet','Lot','IssueDate','Expdate','DailyDose','Stroage','nhsnumber','pname','dob','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading('NameofTable',text='Name of Tablets')
        self.hospital_table.heading('Ref',text='Reference no:')
        self.hospital_table.heading('Dose',text='Dose')
        self.hospital_table.heading('NoofTablet',text='No of Tablets')
        self.hospital_table.heading('Lot',text='Lot')
        self.hospital_table.heading('IssueDate',text='Issue Date')
        self.hospital_table.heading('Expdate',text='Expiry Date')
        self.hospital_table.heading('DailyDose',text='Daily Date')
        self.hospital_table.heading('Stroage',text='Stroage')
        self.hospital_table.heading('nhsnumber',text='NHS No')
        self.hospital_table.heading('pname',text='Patient Name')
        self.hospital_table.heading('dob',text='D/o/B')
        self.hospital_table.heading('address',text='Patient Address')
        
        self.hospital_table["show"]="headings"
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        
        
        self.hospital_table.column('NameofTable',width=90)
        self.hospital_table.column('Ref',width=90)
        self.hospital_table.column('Dose',width=90)
        self.hospital_table.column('NoofTablet',width=90)
        self.hospital_table.column('Lot',width=90)
        self.hospital_table.column('IssueDate',width=90)
        self.hospital_table.column('Expdate',width=90)
        self.hospital_table.column('DailyDose',width=90)
        self.hospital_table.column('Stroage',width=100)
        self.hospital_table.column('nhsnumber',width=90)
        self.hospital_table.column('pname',width=90)
        self.hospital_table.column('address',width=90)
        
        #************************Functionality Declaration **************
        
    def iPrescriptionData(self):
           if self.Nameoftablets.get()=="" or self.ref.get()=="":
              messagebox.showerror("Error !","All fields are Required")
              
           else:
               conn=mysql.connector.connect(host="localhost",username="root",passwords="Puja@1997",database="Mydata")
               my_cursor=conn.cursor()
               my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                   self.Nametablet.get(),
                   self.ref.get(),
                   self.Dose.get(),
                   self.Lots.get(),
                   self.issue.get(),
                   self.exp.get(),
                   self.Effects.get(),
                   self.Furtherinfo.get(),
                   self.BloodPressure.get(),
                   self.Storage.get(),
                   self.Medicine.get(),
                   self.PatientId.get(),
                   self.NhsNumber.get(),
                   self.PatientName.get(),
                   self.PatientDOB.get(),
               ))
               
               conn.commit()
               conn.close()
        
root=Tk()
ob=Hospital(root)
root.mainloop()