# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 15:28:50 2022

@author: user
"""

import tkinter as tk
import tkinter.messagebox
import pandas as p
from tkinter import *

import mysql.connector

import mysql.connector as mysql

#from tkinter import filedialog as fd 
import tkinter.filedialog
from tkinter import ttk

from datetime import date 
import datetime
import os

from dateutil import relativedelta

from PIL import ImageTk,Image  

import pandas as p
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from array import *
from pandas import DataFrame
import matplotlib.pyplot as plt
class NewWin():
    
   def __init__(self):
       self.win = tk.Tk()

       self.win.geometry("863x505+300+100");
       self.win.title(" Brain Tumor Analysis And Prediction System ")
       self.win.configure(bg="#912388")
       self.canvas = tk.Canvas(self.win, width = 863, height = 505)  
       self.canvas.place(x=0,y=0);


       self.img3 = ImageTk.PhotoImage(Image.open("b2.png"))  
       l22 = tk.Label(self.win, image=self.img3,width=863,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
       l22.place(x=00,y=0)


       self.img2 = ImageTk.PhotoImage(Image.open("b2.png"))  
       l11 = tk.Label(self.win, image=self.img2,width=863,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
       l11.place(x=0,y=0)

#       self.l1 = tk.Label(self.win,text=" Cancer Disease Prediction System  ",width=55,bg="darkblue",fg="white",relief="raised",font=("magenta",15,"bold"))
 #      self.l1.place(x=0,y=00)

#       self.img3 = ImageTk.PhotoImage(Image.open("can3.jpg"))  
#       l33 = tk.Label(self.win, image=self.img3,width=450,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
 #      l33.place(x=0,y=150)

       self.b2 = tk.Button(self.win,text=" Select Data Set File  ",width=25,bg="#092193",fg="white",relief="raised",font=("cambria",13,"bold"),command=self.callback)
       self.b2.place(x=310,y=190)
       
  #     self.l12 = tk.Label(self.win,text=" Cancer Disease Prediction System  ",width=55,bg="darkblue",fg="white",relief="raised",font=("magenta",15,"bold"))
   #    self.l12.place(x=0,y=430)
       
       self.win.mainloop()

   def callback(self):
       self.name=tkinter.filedialog.askopenfilename()
       #name=fd.askopenfilename() 
       print(self.name)
       self.t1 = tk.Label(self.win,text="",width=35,relief="raised",bg="#092193",fg="white",font=("cambria",12,"bold"))
       self.t1.place(x=290,y=260)
       self.t1.configure(text=self.name)

       self.b1 = tk.Button(self.win,text=" Read Data Values  ",width=25,bg="red",fg="white",relief="raised",font=("cambria",13,"bold"),command=self.loading)
       self.b1.place(x=310,y=320)

#       fname=self.name
 #      print("File Name="+fname)
  #     if(fname==""):       
   #        tkinter.messagebox.showinfo(" Lung Cancer Prediction System "," Please Enter File Name....");
    #   else:
     #      tkinter.messagebox.showinfo(" Lung Cancer Prediction System "," Data set of File="+fname+" is Loading ...Please Wait...");
      #     self.loading()
#             

   def loading(self):
       
       fname=self.name
       print("File Name="+fname)
       if(fname==""):       
           tkinter.messagebox.showinfo(" Brain Tumor Analysis And Prediction System"," Please Enter File Name....");
       else:
           tkinter.messagebox.showinfo(" Brain Tumor Analysis And Prediction System "," Data set of File="+fname+" is Loading ...Please Wait...");
           self.dataload()
#       self.win.destroy()
 #      app=Test()
 
   def dataload(self):
       tkinter.messagebox.showinfo(" Brain Tumor Analysis And Prediction System "," Data Loading Functio is Called...");
       fname=self.name
       data=p.read_csv(fname)
#       print(data);
       data.columns=[col.lower() for col in data];  # Makes all columns To Lower Case
#       print(data[['employee_name','ssn','dept','salary','doj','no_of_project_assigned','completed']]);
       n=data.shape
       print(" Total Record=")
       max=n[0]
       print(max)
       
  #     for i in range(max):
#           print(i)
 #          print("\t Record")
    
       rec=data.iloc[3];
       print(rec)
       print(rec[0])
       
       #[['employee name','gender','age','location']]);
       
       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="braintumor",use_pure= "True",charset='utf8')
       cursor = mdb.cursor() 
       #mdb=mysql.connector.connect(user="root",password="mj",database="crop",host="localhost",charset='utf8')
       #cursor=mdb.cursor()
       cursor.execute("delete from braintumordata");
       mdb.commit()
#       sql="insert into emp values('jjj','222','Tester','12000','2015-2-2','40','25')";
 #      cursor.execute(sql);
 #      sql="select * from emp"



       for i in range(max):
           rec=data.iloc[i]
           f1=int(rec[0])
           f2=int(rec[1])
           f3=int(rec[2])
           f4=str(rec[3])
           f5=str(rec[4])
           f6=str(rec[5])
           f7=str(rec[6])
           f8=str(rec[7])
           f9=str(rec[8])
           f10=str(rec[9])
           f11=str(rec[10])
           f12=str(rec[11])
           f13=str(rec[12])
           f14=str(rec[13])
           f15=str(rec[14])
           
           print(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15);
           sql="insert into braintumordata values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
           cursor.execute(sql,(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15));
           mdb.commit()
     
       print(" All Data Transfered And Stored in Data Base....");    
       tkinter.messagebox.showinfo(" Tumor Prediction System "," All Brain Tumor Patients Data Transfered And Stored in Data Base....");
       self.win.destroy()
       app=Load();
       
     #  rows=cursor.fetchall()
      # total=cursor.rowcount
      # print("\n Total Data Records=\t"+str(total));


 
 
class Load():
   def __init__(self):
       self.load = tk.Tk()
       self.load.geometry("1200x600+100+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#812336")
       self.load.title(" Brain Tumor Analysis And Prediction System ")
     


       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="braintumor",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
       sql="select * from braintumordata"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")
       self.canvas.place(x=20,y=100);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Patients Data Set Details ",width=50,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"))
       l1.place(x=300,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15),show="headings",height="15")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#092193",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('15', minwidth=150, stretch=False)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="ID")
       self.tv.heading("#2",text="Age")
       self.tv.heading("#3",text="Gender")
       self.tv.heading("#4",text="	S1")
       self.tv.heading("#5",text=" S2")
       self.tv.heading("#6",text="S3")
       self.tv.heading("#7",text="S4")
       self.tv.heading("#8",text="S5")
       self.tv.heading("#9",text="S6")
       self.tv.heading("#10",text="S7") 
       self.tv.heading("#11",text="S8")
       self.tv.heading("#12",text="S9")
       self.tv.heading("#13",text="S10")
       self.tv.heading("#14",text="S11")
       self.tv.heading("#15",text="S12")

	
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")  
       self.canvas1.place(x=20,y=500);
       self.canvas1.pack();

       b1 = tk.Button(self.canvas1,text=" Analyse Data Set ",width=25,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"),command=self.dataload1)
       b1.place(x=500,y=14)

       self.load.mainloop()
 
   def dataload1(self):
       tkinter.messagebox.showinfo(" Brain Tumor Analysis And Prediction System "," The Process of Analyse and Prediction of Disease Begins");
       self.load.destroy();
       app=Analysis();

class Analysis():
   def __init__(self):

       self.ana = tk.Tk()
       self.ana.geometry("800x470+300+100");
       self.ana.title(" Brain Tumor Disease Prediction System ")
       self.ana.configure(bg="#912388")
                          
       self.canvas = tk.Canvas(self.ana, width = 800, height = 470)  
       self.canvas.place(x=0,y=0);

       self.img1 = ImageTk.PhotoImage(Image.open("b3.png"))  
       l1 = tk.Label(self.ana, image=self.img1,width=800,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
       l1.place(x=0,y=00)


       
       b1 = tk.Button(self.ana,text=" Extract Featured Attribute  ",width=30,bg="#092193",fg="white",relief="groove",font=("cambria",12,"bold"),command=self.featureextraction)
       b1.place(x=250,y=180)
       

       b4 = tk.Button(self.ana, text=" Exit ",width=30,bg="#092193",fg="white",relief="groove",font=("cambria",12,"bold"),command=self.exit)
       b4.place(x=250,y=290)

       self.ana.mainloop()

   def featureextraction(self):
       tkinter.messagebox.showinfo(" Brain Tumor Analysis And Prediction System"," Extraction of Required Data from Oveall Data Set Information...")

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="braintumor",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
       cursor.execute("delete from braintumordata1");

       sql="select * from braintumordata"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));
  
       for row in rows:
           
           f1=int(row[0])
           f2=int(row[1])
           f3=int(row[2])
           f4=str(row[3])
           f5=str(row[4])
           f6=str(row[5])
           f7=str(row[6])
           f8=str(row[7])
           f9=str(row[8])
           f10=str(row[9])
           f11=str(row[10])
           f12=str(row[11])
           f13=str(row[12])
           f14=str(row[13])
           f15=str(row[14])
           
           if(f3==1):
               gender="Male";
           else:
               gender="Female";
           
           print(f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15);
           sql="insert into braintumordata1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
           cursor.execute(sql,(f1,f2,gender,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15));
           mdb.commit()
  
       self.ana.destroy()
       app=Load1()
       

   def prediction(self):
       self.ana.destroy()
       app=Load()

   def exit(self):
       self.ana.destroy()

class Load1():
   def __init__(self):
       self.load1 = tk.Tk()
       self.load1.geometry("1200x600+100+100");
#       self.load.configure(bg="#912388")
       self.load1.configure(bg="#985676")
       self.load1.title(" Brain Tumor Predicction System ")


       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="braintumor",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()

       sql="select age,gender,s1,s2,s3,s4,s5,s6,s7 from braintumordata1"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load1, width = 1200, height = 60,bg="#232342")
       self.canvas.place(x=20,y=100);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Extracted Featured Attributes Details Of Brain Tumor Patients ",width=50,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"))
       l1.place(x=250,y=20)

       self.tv=ttk.Treeview(self.load1,column=(1,2,3,4,5,6,7,8,9),show="headings",height="15")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="green",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('9', minwidth=50, stretch=False)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
       self.tv.heading("#1",text="Age")
       self.tv.heading("#2",text="Gender")
       self.tv.heading("#3",text="S1")
       self.tv.heading("#4",text="	S2")
       self.tv.heading("#5",text=" S3")
       self.tv.heading("#6",text="S4")
       self.tv.heading("#7",text="S5")
       self.tv.heading("#8",text="S6")
       self.tv.heading("#9",text="S7")
       
 
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load1, width = 1200, height = 60,bg="#232342")  
       self.canvas1.place(x=20,y=500);
       self.canvas1.pack();

       b1 = tk.Button(self.canvas1,text=" Predict Brain Tumor Patients  ",width=40,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"),command=self.loading)
       b1.place(x=450,y=14)

       self.load1.mainloop()
 
   def loading(self):
       self.load1.destroy()
       app=Prediction()



class Prediction():
   def __init__(self):
       self.prediction = tk.Tk()
       self.prediction.geometry("401x110+400+200");
       self.prediction.title(" Brain Tumor Disease Prediction System ")

       self.canvas = tk.Canvas(self.prediction, width = 400, height = 500)  
       self.canvas.place(x=0,y=0);

       self.img1 = ImageTk.PhotoImage(Image.open("b4.png"))  

       
       b1 = tk.Button(self.prediction,image=self.img1,width=400,bg="cyan",fg="yellow",relief="raised",font=("cambria",12,"bold"),command=self.croppred)
       b1.place(x=0,y=0)
       


       self.prediction.mainloop()

   def croppred(self):
       tkinter.messagebox.showinfo(" Brain Tumor Disease Prediction"," Disease Prediction Begins...")
       tkinter.messagebox.showinfo(" Brain Tumor Disease Prediction "," Prediction of Brain Tumor Disease ...")

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="braintumor",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       cursor1 = mdb.cursor()
       
       cursor.execute("delete from braintumordisease");

       sql="select pid,age,gender,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12 from braintumordata1";
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));
  
       for row in rows:
           pid=int(row[0])
           age=int(row[1])
           gender=str(row[2])
           s1=float(row[3])
           s2=float(row[4])
           s3=float(row[5]) 
           s4=float(row[6]) 
           s5=float(row[7])
           s6=float(row[8])
           s7=float(row[9])
           s8=float(row[10])
           s9=float(row[11])
           s10=float(row[12])
           s11=float(row[13])
           s12=float(row[14])
           
           

           if((s1>11.3 or s1<13.3) and (s2>=8.1 or s2<=10.5) and (s3>6.9 or s3<9.1) and 
                   (s4>8 or s4<10.2) and (s5>4 or s5<5.5) and (s6>6.5 or s6<9.2) 
                   and (s7>5.9 or s7<7.2) and (s8>5.5 or s8<7.5) and (s9>5.1 or s9<7)
                   and (s10>4.5 and s10<6.7) and (s11>6.6 and s11<9.4) and (s12>8.2 and s12<8.9)):
                 res="Glioblastoma"
                   
                   
           elif((s1>10.1 and s1<11.3) and (s2>8.5 and s2<9.5) and (s3>6.2 and s3<6.6) and 
                 (s4>8.5 and s4<9.9) and (s5>4 and s5<5.7) and (s6>7 and s6<7.7) 
                  or (s7>6.1 and s7<6.9) and (s8>6.5 and s8<7.5) and (s9>5.1 and s9<6.5)
                  or (s10>4.5 and s10<5.5) and (s11>6.3 and s11<6.9) and (s12>8.1 and s12<7.5)):
               res= "Medulloblastoma"
                  
                  
           elif((s1>=12.4 and s1<=13.3) and (s2>8.2 and s2<8.8) and (s3>6.9 and s3<7.8) and 
                  (s4>=8.4 and s4<=10.5) and (s5>4.5 and s5<7.3) and (s6>7.7 and s6<9) 
                  and (s7>6.4 or s7<7.2) and (s8>6.3 and s8<6.9) and (s9>5.2 and s9<7.2)
                  and (s10>4.8 and s10<5.8) or (s11>7 and s11<8.3) and (s12>8 and s12<9.1)):
               res= "Pilocytic_astrocytoma"
               
               
           elif((s1>11.5 and s1<13.5) and (s2>7.0 and s2<9.5) and (s3>6.5 and s3<12.1) or 
                 (s4>8 and s4<10.2) and (s5>3.5 and s5<6.2) and (s6>7.2 and s6<10.2) 
                 and (s7>6 and s7<7.7) and (s8>5.5 and s8<7.9) and (s9>4.7 and s9<8.4)
                 and (s10>4.7 and s10<6.7) and (s11>6.3 and s11<10) and (s12>7.3 and s12<9.3)):
               res= "Ependymoma"
               
               
           else:
               
               res="Normal"

           print(pid,"===",res); 
           sql1="insert into braintumordisease values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
           cursor1.execute(sql1,(pid,age,gender,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12,res));
           mdb.commit()
     
       tkinter.messagebox.showinfo(" Brain Tumor Disease Prediction ","Brain Tumor Disease Prediction of a Patient Completed ....");
       self.prediction.destroy()
       app=Load2()
       
   def exit(self):
       self.prediction.destroy()
       app=Analysis()

class Load2():
   def __init__(self):
       self.load = tk.Tk()
       self.load.geometry("1200x600+100+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#812336")
       self.load.title(" Brain Tumor Prediction System ")
     


       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="braintumor",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
       sql="select * from braintumordisease"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")
       self.canvas.place(x=20,y=100);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Brain Tumor Disease Predicted Result Details ",width=50,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"))
       l1.place(x=300,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16),show="headings",height="15")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#213473",foreground="white", fieldbackground="red",font=('cambria', 10,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('16', minwidth=100, stretch=False)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="ID")
       self.tv.heading("#2",text="Age")
       self.tv.heading("#3",text="Gender")
       self.tv.heading("#4",text="	S1")
       self.tv.heading("#5",text=" S2")
       self.tv.heading("#6",text="S3")
       self.tv.heading("#7",text="S4")
       self.tv.heading("#8",text="S5")
       self.tv.heading("#9",text="S6")
       self.tv.heading("#10",text="S7") 
       self.tv.heading("#11",text="S8")
       self.tv.heading("#12",text="S9")
       self.tv.heading("#13",text="S10")
       self.tv.heading("#14",text="S11")
       self.tv.heading("#15",text="S12")
       self.tv.heading("#16",text="Result")
 
      
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 1200, height = 60,bg="#232342")  
       self.canvas1.place(x=20,y=500);
       self.canvas1.pack();

       b1 = tk.Button(self.canvas1,text=" Analyse The Result ",width=25,relief="raised",bg="red",fg="white",font=("cambria",14,"bold"),command=self.dataload1)
       b1.place(x=500,y=14)
 
       self.load.mainloop()
 
   def dataload1(self):
       tkinter.messagebox.showinfo(" Brain Tumor Prediction System "," The Process of Analyse and Prediction of Disease Begins");
       self.load.destroy();
       app=Classification();


class Classification():
   def __init__(self):
       
       self.classify = tk.Tk()
       self.classify.geometry("813x410+300+100");
       self.classify.title(" Brain Tumor Disease Prediction System ")
       self.classify.configure(bg="#912388")
                          
       self.canvas = tk.Canvas(self.classify, width = 813, height = 411)  
       self.canvas.place(x=0,y=0);

       self.img2 = ImageTk.PhotoImage(Image.open("b6.png"))  
       l2 = tk.Label(self.classify, image=self.img2,width=813,relief="groove",fg="#323223",font=("cambria",14,"bold"))
       l2.place(x=0,y=00)


 
       b1 = tk.Button(self.classify,text=" Brain Tumor Disease Class  ",width=30,height=1,bg="white",fg="red",relief="groove",font=("cambria",15,"bold"),command=self.diseaseclass)
       b1.place(x=50,y=120)
       
       b2 = tk.Button(self.classify,text=" Age ",width=30,height=1,bg="white",fg="red",relief="groove",font=("cambria",15,"bold"),command=self.day)
       b2.place(x=50,y=210)

       b3 = tk.Button(self.classify,text=" Exit ",width=30,height=1,bg="white",fg="darkblue",relief="groove",font=("cambria",15,"bold"),command=self.exit)
       b3.place(x=50,y=300)

       

       self.classify.mainloop()

   def diseaseclass(self):
       tkinter.messagebox.showinfo(" Brain Tumor Disease Data Analysis "," Brain Tumor Disease Patient Data Analysis On Disease Class ...")
       self.classify.destroy()
       app=DiseaseClass()
       
   def day(self):
       tkinter.messagebox.showinfo(" Brain Tumor Disease Data Analysis "," Brain Tumor Disease Patient Data Analysis On Age Group ...")
       self.classify.destroy()
       app=Day()

   def exit(self):
       self.classify.destroy()
      

class Day():
   def __init__(self):
       
       self.load = tk.Tk()
       self.load.geometry("700x400+250+100");
       self.load.configure(bg="#232342")
       self.load.title(" Brain Tumor Disease  Data Analysis Based on Age Group  ")
     

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="braintumor",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
 
       sql="select pid,age,res from braintumordisease";
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Brain Tumor Disease  Data Analysis Based on Age Group ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=50,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2,3),show="headings",height="10")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#768324",foreground="white", width="300" ,font=('cambria', 11,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('3', minwidth=100, stretch=False)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Patient ID")
       self.tv.heading("#2",text="Age")
       self.tv.heading("#3",text="Result")
                     
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")  
       self.canvas1.place(x= 0,y=300);
       self.canvas1.pack();

       b2 = tk.Button(self.canvas1,text=" Classify Age Group ",width=45,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.graph)
       b2.place(x=260,y=12)

       b3 = tk.Button(self.canvas1,text=" Back  ",width=20,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.back)
       b3.place(x=30,y=12)


       self.load.mainloop()
      
   def graph(self):
      # self.load.destroy()

       tkinter.messagebox.showinfo(" Brain Tumor Disease Data Data Analysis "," Brain Tumor Disease Data Processingn on Age Group Processing classification Begins ...")
       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="braintumor",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
 
       cursor.execute("delete from temp");

       sql="select pid,age,res from braintumordisease"
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       for rec in rows:
           id=str(rec[0])
           age=int(rec[1])
           res=str(rec[2])
           
           if(age>10 and age<20):
               ageclass="Age(10-20) Class"
           elif(age>20 and age<30):
               ageclass="Age(20-30) Class"
           elif(age>30 and age<40):
               ageclass="Age(30-40) Class"
           elif(age>40 and age<50):
               ageclass="Age(40-50) Class"
           elif(age>50 and age<60):
               ageclass="Age(50-60) Class"
           else:
               ageclass="Age(>60) Class"
        
           sql="insert into temp values(%s,%s)"
           cursor.execute(sql,(ageclass,res));
           mdb.commit()
           
       self.load.destroy()
       app=Age1()


   def back(self):
       self.load.destroy()
       app=Classification()

       
       
class Age1():
   def __init__(self):
       
       self.load = tk.Tk()
       self.load.geometry("700x400+250+100");

       self.load.configure(bg="#232342")
       self.load.title("Brain Tumor Disease  Data Analysis Based on Age Group  ")
     

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="braintumor",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
 
       sql="select age,count(*) from temp group by age";
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Brain Tumor Disease  Data Analysis Based on Age Group ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=50,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2),show="headings",height="5")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#768324",foreground="white", width="300" ,font=('cambria', 11,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('2', minwidth=100, stretch=False)
       self.tv.bind("<ButtonRelease-1>",self.selected)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Age")
       self.tv.heading("#2",text="No OF Patients")
                     
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")  
       self.canvas1.place(x= 0,y=300);
       self.canvas1.pack();

       b2 = tk.Button(self.canvas1,text=" Analyse using Graph  ",width=45,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.graph)
       b2.place(x=60,y=12)

       b3 = tk.Button(self.canvas1,text=" Back  ",width=20,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.back)
       b3.place(x=500,y=12)


       self.load.mainloop()
      
   def graph(self):
      # self.load.destroy()

       tkinter.messagebox.showinfo(" Brain Tumor Disease Data Analysis "," Brain Tumor Disease Data Analysis Using Graphical Representation ...")
       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="braintumor",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
 
       cursor.execute("delete from graph");

       sql="select age,res,count(*) from temp group by age,res order by age";
       cursor.execute(sql);
       rows=cursor.fetchall()

       for row in rows:
           age=str(row[0])
           res=str(row[1])
           cnt=int(row[2])
           sc=age+"-"+res;
           sql="insert into graph values(%s,%s)"
           cursor.execute(sql,(sc,cnt));
           mdb.commit()

       self.load.destroy()
       app=OverallAgeGraph88()
           

   def selected(self,a):
       print(" Item Clicke");
       self.data=self.tv.item(self.tv.selection())
       print(self.data)
       item=self.tv.selection()[0]
       print(item)
       self.age=str(self.tv.item(item)['values'][0])
       print(self.age)

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="braintumor",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
 
       cursor.execute("delete from graph");

       sql="select age,res,count(*) from temp where age='"+self.age+"' group by age,res order by age";
       cursor.execute(sql);
       rows=cursor.fetchall()

       for row in rows:
           age=str(row[0])
           res=str(row[1])
           cnt=int(row[2])
           sc=age+"-"+res;
           sql="insert into graph values(%s,%s)"
           cursor.execute(sql,(sc,cnt));
           mdb.commit()

       self.load.destroy()
       app=OverallAgeGraph88()
 

   def back(self):
       self.load.destroy()
       app=Classification()

class OverallAgeGraph88():
   def __init__(self):
       self.graph2= tk.Tk() 

       self.graph2.geometry("1600x1000+10+10")               
       self.graph2.title(" Graphical Representation of Data Analysis On Age Group Class");                      

       self.canvas = tk.Canvas(self.graph2, width = 1200, height = 60)
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Brain Tumor Disease Data Analysis Based On Age Group Class ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=150,y=20)

       b1 = tk.Button(self.canvas,text=" Back  ",width=35,relief="raised",bg="darkblue",fg="white",font=("cambria",13,"bold"),command=self.back)
       b1.place(x=750,y=20)

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="braintumor",use_pure= "True",charset='utf8')
       cursor = mdb.cursor() 

       sql="select * from graph";
       cursor.execute(sql);
       rows=cursor.fetchall()

       df = p.DataFrame( [[ij for ij in i] for i in rows] )
       df.rename(columns={0: 'dc',1: 'cnt'}, inplace=True);

       dc=df['dc']
       dc=dc.values

       print(dc)

       for i in range(0, len(dc)): 
           dc[i] = str(dc[i])

       print("\n------------------\n")
       print(dc)
       print("\n------------------\n")


       cnt=df['cnt']
       cnt=cnt.values
       print(cnt)
       
       for i in range(0, len(cnt)): 
           cnt[i] = float (cnt[i])
    
       print("\n------------------\n")
       print(cnt)
       print("\n------------------\n")

       xx1=cnt
       print(xx1)

       yy1=dc
       print(yy1)

       data2 = {'cnt': xx1,
                'dc': yy1
                }
 

       self.canvas1 = tk.Canvas(self.graph2, width = 1000, height =800,bg="#918289")
       self.canvas1.place(x=120,y=80);

       figure3 = plt.Figure(figsize=(18,7), dpi=100)
       ax1 = figure3.add_subplot(221)

   
       df2 = DataFrame(data2,columns=['cnt','dc'])
       df2 = df2[['cnt','dc']].groupby('dc').sum()
       df2.plot(kind='bar', legend=True, ax=ax1,color="cyan",fontsize=10)

       ax1.spines['bottom'].set_color('red')
       ax1.spines['top'].set_color('red')
       ax1.spines['left'].set_color('red')
       ax1.spines['right'].set_color('red')
       ax1.xaxis.label.set_color('red')
       ax1.yaxis.label.set_color('red')

       ax1.set_facecolor("#312094")
       ax1.set_title('Disease Class Vs Total No Of Patients',fontsize=10, fontweight='bold')
       ax1.set_xlabel(' Disease Class ',fontsize=10, fontweight='bold')
       ax1.set_ylabel(' Total Number Of Patients ',fontsize=10, fontweight='bold')
        
       bar1 = FigureCanvasTkAgg(figure3, self.canvas1)
       bar1.get_tk_widget().place(x=0,y=0);





       # self.canvas3 = tk.Canvas(self.graph2, width = 600, height =800,bg="#918289")
       # self.canvas3.place(x=650,y=70);
  
       # figure3 = plt.Figure(figsize=(13,9), dpi=70)
       # ax1 = figure3.add_subplot(111)
      
       # country_data =dc
       # medal_data = cnt

       # print(dc)

       # colors = ["#2ca02c","red", "#ff7f0e",  "#d62728", "#8c564b","#982363"]
       # explode = (0.1, 0, 0, 0, 0)  
       # ax1.pie(medal_data, labels=country_data, explode=None, colors=colors,
       # autopct='%1.1f%%', shadow=True, startangle=150)
       # ax1.axis('equal')  
       # pie2 = FigureCanvasTkAgg(figure3, self.canvas3)
       # pie2.get_tk_widget().pack()


       self.graph2.mainloop() 
   
   def back(self):
       self.graph2.destroy();
    
       app=Classification()


       self.load.mainloop()       
       


class DiseaseClass():
   def __init__(self):
       
       self.load = tk.Tk()
       self.load.geometry("700x400+250+100");
#       self.load.configure(bg="#912388")
       self.load.configure(bg="#232342")
       self.load.title(" Brain Tumor Disease Data Analysis Based on Disease Class  ")
     

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="braintumor",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
       
 #      select * from collegedataset where cname='BIET' order by sem,dept desc;

       sql="select res,count(*) from braintumordisease group by res order by age";
       cursor.execute(sql);
       rows=cursor.fetchall()
       total=cursor.rowcount
       print("\n Total Data Records=\t"+str(total));

       self.canvas = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Brain Tumor Disease Data Analysis Based on Disease Class ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=50,y=20)
       
 
       self.tv=ttk.Treeview(self.load,column=(1,2),show="headings",height="10")

       self.ysb = ttk.Scrollbar(self.tv, orient=tk.VERTICAL, command=self.tv.yview)
       self.xsb = ttk.Scrollbar(self.tv, orient=tk.HORIZONTAL, command=self.tv.xview)
       ttk.Style().configure("Treeview", background="#768324",foreground="white", width="300" ,font=('cambria', 11,'bold'))
       self.tv.configure(yscroll=self.ysb.set, xscroll=self.xsb.set)
       self.tv.column('2', minwidth=100, stretch=False)
#       self.tv.bind("<ButtonRelease-1>",self.selected)

       self.ysb.pack(anchor=tk.E, fill=tk.Y, side=tk.RIGHT)
       self.xsb.pack(anchor=tk.S, fill=tk.X, side=tk.BOTTOM)
       self.tv.pack(expand=True, fill=tk.BOTH)
    
    
       self.tv.heading("#1",text="Disease Class")
       self.tv.heading("#2",text=" Total Patient ")
                     
       for i in rows:
           self.tv.insert('','end',values=i)

       self.canvas1 = tk.Canvas(self.load, width = 700, height = 60,bg="#232342")  
       self.canvas1.place(x= 0,y=300);
       self.canvas1.pack();

       b2 = tk.Button(self.canvas1,text=" Analyse using Graph  ",width=45,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.graph)
       b2.place(x=60,y=12)

       b3 = tk.Button(self.canvas1,text=" Back  ",width=20,relief="raised",bg="darkred",fg="white",font=("cambria",12,"bold"),command=self.back)
       b3.place(x=500,y=12)


       self.load.mainloop()
      
   def graph(self):
      # self.load.destroy()

       tkinter.messagebox.showinfo(" Brain Tumor Disease Data Analysis "," Brain Tumor Disease Data Analysis Using Graphical Representation ...")
       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="braintumor",use_pure= "True",charset='utf8')
       cursor = mdb.cursor()
 
       cursor.execute("delete from graph");

       sql="select res,count(*) from braintumordisease group by res order by age";
       cursor.execute(sql);
       rows=cursor.fetchall()

       for row in rows:
           res=str(row[0])
           cnt=int(row[1])
           sc=res;
           sql="insert into graph values(%s,%s)"
           cursor.execute(sql,(sc,cnt));
           mdb.commit()

       self.load.destroy()
       app=OverallLocGraph88()
           

   def back(self):
       self.load.destroy()
       app=Classification()

class OverallLocGraph88():
   def __init__(self):
       self.graph2= tk.Tk() 
#       self.graph2.configure(bg="#912388")
       self.graph2.geometry("1600x1000+10+10")               
       self.graph2.title(" Graphical Representation of Data Analysis On Disease Class");                      

       self.canvas = tk.Canvas(self.graph2, width = 1200, height = 60)
       self.canvas.place(x=0,y=50);
       self.canvas.pack();

       l1 = tk.Label(self.canvas,text=" Brain Tumor Disease Data Analysis Based On Disease Class ",width=50,relief="raised",bg="darkred",fg="white",font=("cambria",14,"bold"))
       l1.place(x=150,y=20)

       b1 = tk.Button(self.canvas,text=" Back  ",width=35,relief="raised",bg="darkblue",fg="white",font=("cambria",13,"bold"),command=self.back)
       b1.place(x=750,y=20)

       mdb = mysql.connect(host = "localhost",user = "root",passwd = "mj",database="braintumor",use_pure= "True",charset='utf8')
       cursor = mdb.cursor() 

       sql="select * from graph";
#       sql="select city,count(*) from crimedataset1 group by city";
       cursor.execute(sql);
       rows=cursor.fetchall()

       df = p.DataFrame( [[ij for ij in i] for i in rows] )
       df.rename(columns={0: 'dc',1: 'cnt'}, inplace=True);

       dc=df['dc']
       dc=dc.values

       print(dc)

       for i in range(0, len(dc)): 
           dc[i] = str(dc[i])

       print("\n------------------\n")
       print(dc)
       print("\n------------------\n")


       cnt=df['cnt']
       cnt=cnt.values
       print(cnt)
       
       for i in range(0, len(cnt)): 
           cnt[i] = float (cnt[i])
    
       print("\n------------------\n")
       print(cnt)
       print("\n------------------\n")

       xx1=cnt
       print(xx1)

       yy1=dc
       print(yy1)

       data2 = {'cnt': xx1,
                'dc': yy1
                }
 

       self.canvas1 = tk.Canvas(self.graph2, width = 600, height =600,bg="#918289")
       self.canvas1.place(x=30,y=70);
#       self.canvas.pack();

       figure3 = plt.Figure(figsize=(10,7), dpi=100)
       ax1 = figure3.add_subplot(221)

   
       df2 = DataFrame(data2,columns=['cnt','dc'])
       df2 = df2[['cnt','dc']].groupby('dc').sum()
       df2.plot(kind='bar', legend=True, ax=ax1,color="cyan",fontsize=12)

       ax1.spines['bottom'].set_color('red')
       ax1.spines['top'].set_color('red')
       ax1.spines['left'].set_color('red')
       ax1.spines['right'].set_color('red')
       ax1.xaxis.label.set_color('red')
       ax1.yaxis.label.set_color('red')

       ax1.set_facecolor("#312094")
       ax1.set_title('Disease Class Vs Total No Of Patients',fontsize=10, fontweight='bold')
       ax1.set_xlabel(' Disease Class ',fontsize=10, fontweight='bold')
       ax1.set_ylabel(' Total Number Of Patients ',fontsize=10, fontweight='bold')
        
       bar1 = FigureCanvasTkAgg(figure3, self.canvas1)
       bar1.get_tk_widget().place(x=0,y=0);





       self.canvas3 = tk.Canvas(self.graph2, width = 600, height =600,bg="#918289")
       self.canvas3.place(x=700,y=70);

   
       figure3 = plt.Figure(figsize=(8,6), dpi=100)
       ax1 = figure3.add_subplot(111)
      
       country_data =dc
       medal_data = cnt

       print(dc)

       colors = ["#2ca02c","red", "#ff7f0e",  "#d62728", "#8c564b","#982363"]
       explode = (0.1, 0, 0, 0, 0)  
       ax1.pie(medal_data, labels=country_data, explode=None, colors=colors,
    
       autopct='%1.1f%%', shadow=True, startangle=150)
       ax1.axis('equal')  

       pie2 = FigureCanvasTkAgg(figure3, self.canvas3)
       pie2.get_tk_widget().pack()


       self.graph2.mainloop() 
   
   def back(self):
       self.graph2.destroy();
    
       app=Classification()

class Test():
   def __init__(self):
       self.root = tk.Tk()
       self.root.geometry("800x464+300+100");
       self.root.title(" brain tumor Prediction System ")
       self.root.configure(bg="green")
       self.canvas = tk.Canvas(self.root, width = 800, height = 464)  
       self.canvas.place(x=0,y=0);


       self.img1 = ImageTk.PhotoImage(Image.open("b1.png"))  
#       l1 = tk.Label(self.root, image=self.img1,width=1000,relief="ridge",fg="#323223",font=("cambria",14,"bold"))
 #      l1.place(x=0,y=00)



       b1 = tk.Button(self.root,image=self.img1,width=800,height=464,bg="green",fg="white",relief="raised",font=("cambria",14,"bold"),command=self.createNewWindow)
       b1.place(x=0,y=0) 
       

       self.root.mainloop()

   def createNewWindow(self):
       self.root.destroy()
       app=NewWin()
       

   def exit(self):
       self.root.destroy()

app=Test()