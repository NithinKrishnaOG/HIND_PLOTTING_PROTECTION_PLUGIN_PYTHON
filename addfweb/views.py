
from django.shortcuts import render
import mysql.connector
from django.contrib import messages

from django.shortcuts import render_to_response
from django.conf import settings
import os
from django.conf import settings
from django.http import HttpResponse, Http404
import mimetypes
from django.core.files.storage import FileSystemStorage

from django.core.mail import send_mail
from django.conf import settings


  
    
def home(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    bc="select * from product where pro_cat='tv' limit 0,4"
    print(bc)
    cd=mycursor.execute(bc)
    rows1=mycursor.fetchall()
    print(rows1)
    bc="select * from product where pro_cat='music' limit 0,4"
    print(bc)
    cd=mycursor.execute(bc)
    rows2=mycursor.fetchall()
    print(rows2)   
    bc="select * from product where pro_cat='camera' limit 0,4"
    print(bc)
    cd=mycursor.execute(bc)
    rows3=mycursor.fetchall()
    print(rows3)
    bc="select * from product where pro_cat='mobile' limit 0,4"
    print(bc)
    cd=mycursor.execute(bc)
    rows4=mycursor.fetchall()
    print(rows4)           
    return render(request,'index.html',{'row1':rows1,'row2':rows2,'row3':rows3,'row4':rows4})  
def viewproductbl(request):
    rproductcode=request.GET.get("rproductcode")
    print(rproductcode)
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    bc="select * from product where product_code='"+rproductcode+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows1=mycursor.fetchall()
    print(rows1)
    return render(request,'product.html',{'row1':rows1})   
def signup(request):  
    return render(request,'signup.html') 
def signupvalidator(request):  
    name=request.POST.get("name")
    email=request.POST.get("email")
    contact=request.POST.get("contact")
    password=request.POST.get("pwd")
   
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    bc="select * from user_details where email='"+email+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows1=mycursor.fetchone()   
    if rows1!=None:
     return render(request,'signup.html',{'message': 'User is Already Exist.'})
    else:
     try:
      mn="INSERT INTO user_details(name,email,contact,password)VALUES('"+name+"','"+email+"','"+contact+"','"+password+"')"
      print(mn)
      mycursor.execute(mn)
      mydb.commit()
      return render(request,'signup.html',{'message': 'Successfully Added.'})
     except:
      return render(request,'signup.html',{'message': 'Some issue. Try after some time.'})    
def login(request):  
    return render(request,'login.html')
def loginvalidator(request):
    email=request.POST.get("email")
    password=request.POST.get("pwd")
    print("email"+email)
    print("password"+password)
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    bc="select * from user_details where email='"+email+"' and password='"+password+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows1=mycursor.fetchone()   
    if rows1!=None:
     request.session['id']=rows1[0]
     request.session['name']=rows1[1]
     request.session['email']=rows1[2]
     request.session['contact']=rows1[3]
     return render(request,'userho.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact']})
    else:
     return render(request,'login.html',{'message':'Invalid credentials'})     
def userhome(request):  
    return render(request,'userho.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact']})    
def myaccount(request):  
    return render(request,'myaccount.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact']})    
def edit_profile(request):  
    return render(request,'editprofile.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact']})    
def editprofilevalidator(request):
    userno=str(request.session['id'])
    name=request.GET.get("name")
    email=request.GET.get("email")
    contact=request.GET.get("contact")
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    try:
     mn="update user_details set name='"+name+"', email='"+email+"', contact='"+contact+"'  where ser_no="+userno
     print(mn)
     mycursor.execute(mn)
     mydb.commit()
     return render(request,'editprofile.html',{'id':request.session['id'],'name':name,'email':email,'contact':contact})    
    except:
     return render(request,'editprofile.html',{'id':request.session['id'],'name':name,'email':email,'contact':contact,'message':'There is some issue. Try after some time.'})
def changepaswd(request):  
    return render(request,'changepaswd.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact']})         
def changepaswdvalidator(request):
    userno=str(request.session['id'])
    newpwd=request.GET.get("newpwd")
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    try:
     mn="update user_details set password='"+newpwd+"'  where ser_no="+userno
     print(mn)
     mycursor.execute(mn)
     mydb.commit()
     return render(request,'changepaswd.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact'],'message':'Password changed successfully.'})    
    except:
     return render(request,'changepaswd.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact'],'message':'There is some issue. Try after some time.'})
def viewcart(request):
    email=request.session['email']
    print(email)
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    bc="select * from shopping_cart where email='"+email+"' and txn_status='movedtocart'"
    print(bc)
    cd=mycursor.execute(bc)
    rows1=mycursor.fetchall()
    print(rows1)
    amt=0
    cartnolist=[]
    for x in rows1:
     amt=amt+(int(x[5])*int(x[6]))
     cartnolist.append(x[0]);
    request.session['cartnolist']=cartnolist
    request.session['pamt']=amt
    return render(request,'viewcart.html',{'row1':rows1,'total':amt,'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact']})   
def search(request):
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    bc="select * from product where pro_cat='tv'"
    print(bc)
    cd=mycursor.execute(bc)
    rows1=mycursor.fetchall()
    print(rows1)
    bc="select * from product where pro_cat='music'"
    print(bc)
    cd=mycursor.execute(bc)
    rows2=mycursor.fetchall()
    print(rows2)   
    bc="select * from product where pro_cat='camera'"
    print(bc)
    cd=mycursor.execute(bc)
    rows3=mycursor.fetchall()
    print(rows3)
    bc="select * from product where pro_cat='mobile'"
    print(bc)
    cd=mycursor.execute(bc)
    rows4=mycursor.fetchall()
    print(rows4)           
    return render(request,'search.html',{'row1':rows1,'row2':rows2,'row3':rows3,'row4':rows4,'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact']})  
def searchbyname(request):
    searchname=request.GET.get("searchb")
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    bc="select * from product where pro_cat='tv' and product_code LIKE '"+searchname+"%'"
    print(bc)
    cd=mycursor.execute(bc)
    rows1=mycursor.fetchall()
    print(rows1)
    bc="select * from product where pro_cat='music' and product_code LIKE '"+searchname+"%'"
    print(bc)
    cd=mycursor.execute(bc)
    rows2=mycursor.fetchall()
    print(rows2)   
    bc="select * from product where pro_cat='camera' and product_code LIKE '"+searchname+"%'"
    print(bc)
    cd=mycursor.execute(bc)
    rows3=mycursor.fetchall()
    print(rows3)
    bc="select * from product where pro_cat='mobile' and product_code LIKE '"+searchname+"%'"
    print(bc)
    cd=mycursor.execute(bc)
    rows4=mycursor.fetchall()
    print(rows4)           
    return render(request,'search.html',{'row1':rows1,'row2':rows2,'row3':rows3,'row4':rows4,'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact']})      
def viewproductal(request):
    rproductcode=request.GET.get("rproductcode")
    print(rproductcode)
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    bc="select * from product where product_code='"+rproductcode+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows1=mycursor.fetchall()
    print(rows1)
    return render(request,'productal.html',{'row1':rows1,'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact']})        
def addtocart(request):  
    email=request.session['email']
    product_code=request.GET.get("aproduct_code")
    product_name=request.GET.get("aproduct_name")
    image1=request.GET.get("aimage1")
    quantity=request.GET.get("quantity")
    price=request.GET.get("aprice")
    
   
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    try:
     mn="INSERT INTO shopping_cart(email,product_code,product_name,image1,quantity,price)VALUES('"+email+"','"+product_code+"','"+product_name+"','"+image1+"','"+quantity+"','"+price+"')"
     print(mn)
     mycursor.execute(mn)
     mydb.commit()
     bc="select * from shopping_cart where email='"+email+"' and txn_status='movedtocart'"
     print(bc)
     cd=mycursor.execute(bc)
     rows1=mycursor.fetchall()
     print(rows1)
     cartnolist=[]
     amt=0
     for x in rows1:
      amt=amt+(int(x[5])*int(x[6]))
      cartnolist.append(x[0]);
     request.session['pamt']=amt 
     request.session['cartnolist']=cartnolist
     return render(request,'viewcart.html',{'row1':rows1,'total':amt,'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact']})      
    except:
     return render(request,'viewcart.html',{'row1':rows1,'total':amt,'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact'],'message': 'Some issue. Try after some time.'})  
def removecart(request):  
    email=request.session['email']
    cartno=request.GET.get("cartno")
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    try:
     mn="delete from shopping_cart where ser_no="+cartno
     print(mn)
     mycursor.execute(mn)
     mydb.commit()
     bc="select * from shopping_cart where email='"+email+"' and txn_status='movedtocart'"
     print(bc)
     cd=mycursor.execute(bc)
     rows1=mycursor.fetchall()
     print(rows1)
     cartnolist=[]
     amt=0
     for x in rows1:
      amt=amt+(int(x[5])*int(x[6]))
      cartnolist.append(x[0]);
     request.session['pamt']=amt 
     request.session['cartnolist']=cartnolist
     return render(request,'viewcart.html',{'row1':rows1,'total':amt,'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact']})      
    except:
     bc="select * from shopping_cart where email='"+email+"' and txn_status='movedtocart'"
     print(bc)
     cd=mycursor.execute(bc)
     rows1=mycursor.fetchall()
    return render(request,'viewcart.html',{'row1':rows1,'total':amt,'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact'],'message': 'Some issue. Try after some time.'})
def track(request):
    email=request.session['email']
    print(email)
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    bc="select * from shopping_cart where email='"+email+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows1=mycursor.fetchall()
    print(rows1)
    amt=0
    for x in rows1:
     amt=amt+(int(x[5])*int(x[6]))
    return render(request,'track.html',{'row1':rows1,'total':amt,'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact']}) 
def feedback(request):
    return render(request,'feedback.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact']})     
def feedbackhandler(request):  
    name=request.GET.get("name")
    email=request.GET.get("email")
    mnum=request.GET.get("mnum")
    msgg=request.GET.get("msg")
    
   
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    try:
     mn="INSERT INTO feedback(name,email,mnum,msgg)VALUES('"+name+"','"+email+"','"+mnum+"','"+msgg+"')"
     print(mn)
     mycursor.execute(mn)
     mydb.commit()
     return render(request,'feedback.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact'],'message':'Successfully Added'})     
    except:
     return render(request,'feedback.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact'],'message':'Some issue. Try after some time.'})     
def paymentlogin(request):
    request.session['numberofattempts']=1;
    return render(request,'paymentlogin.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact']})     
    
def paymentloginvalidator(request):
    email=request.POST.get("email")
    password=request.POST.get("pwd")
    request.session['bankemail']=email
    request.session['bankpassword']=password
    print("email"+email)
    print("password"+password)
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    bc="select * from bankregistration where email='"+email+"' and password='"+password+"' and status='active'"
    print(bc)
    cd=mycursor.execute(bc)
    rows1=mycursor.fetchone() 
    
    if rows1!=None:
     request.session['bankuserdetails']=rows1
     
     
     return render(request,'bankusercardentry.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact'],'x':rows1,'pamt':request.session['pamt']})
    else:
     if int(request.session['numberofattempts'])==3:
      sendmail(request)
      #block()
      request.session['numberofattempts']=0
      return render(request,'paymentlogin.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact'],'message':'Some suspecious activities in your Account'})      
     else: 
       request.session['numberofattempts']=int(request.session['numberofattempts'])+1;
       return render(request,'paymentlogin.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact'],'message':'Invalid User'})        
              

def paymentloginvalidator2(request):
      a=[]
      db = request.session['bankuserdetails']

      b=[db[9],db[10]]
      a.append(b)
      c=[db[11],db[12]]
      a.append(c)
      d=[db[13],db[14]]
      a.append(d)
      e=[db[16],db[17]]
      a.append(e)
      f=[db[18],db[19]]
      a.append(f)
      g=[db[20],db[21]]
      a.append(g)
      h=[db[22],db[23]]
      a.append(h)
      print(a)      
      import random
      random.shuffle(a)
      print(a)
      newl=[]
      count=0;
      while count<=2:
       jj=a[count]
       newl.append(jj[0])
       newl.append(jj[1])
       count=count+1
     
       
      print(newl)
      return render(request,'bankuservalidity.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact'],'x':request.session['bankuserdetails'],'qa':newl})

def paymentupdate(request):
     #update the carttable
     cartlist=request.session['cartnolist']
     mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
     mycursor=mydb.cursor()
     for cartnos in cartlist:
      mn="update shopping_cart set txn_status='paid' where ser_no="+str(cartnos)
      print(mn)
      mycursor.execute(mn)
      mydb.commit()      
              
     #update the payment table
     userid=str(request.session['id'])
     username=request.session['name']
     email=request.session['email']
     amount=str(request.session['pamt'])
     from datetime import datetime
     fdate=str(datetime.date(datetime.now()))
     print(fdate)
     mn="INSERT INTO payment(userid,username,useremail,amount,Date)VALUES('"+userid+"','"+username+"','"+email+"','"+amount+"','"+fdate+"')"
     print(mn)
     mycursor.execute(mn)
     mydb.commit()     
     
     
     email=request.session['email']
     print(email)
     mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
     mycursor=mydb.cursor()
     bc="select * from shopping_cart where email='"+email+"'"
     print(bc)
     cd=mycursor.execute(bc)
     rows1=mycursor.fetchall()
     print(rows1)
     amt=0
     for x in rows1:
      amt=amt+(int(x[5])*int(x[6]))
     return render(request,'track.html',{'row1':rows1,'total':amt,'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact']})      
       
def sendmail(request):
     import socket    
     hostname = socket.gethostname()    
     IPAddr = socket.gethostbyname(hostname)    
     print("Your Computer Name is:" + hostname)    
     print("Your Computer IP Address is:" + IPAddr)
     subject = 'Suspecious Attempt from you Account'
     message = 'There is an suspecious attack is happening from the IP address:'+IPAddr
     email_from = settings.EMAIL_HOST_USER
     recipient_list = [str(request.session['email'])]
     send_mail( subject, message, email_from, recipient_list )
        
################    

def bankhome(request):
    return render(request,'bank/index.html')  
def banksignup(request):  
    return render(request,'bank/signup.html')          
def banksignupvalidator(request):  
    name=request.POST.get("name")
    email=request.POST.get("email")
    contact=request.POST.get("contact")
    password=request.POST.get("pwd")
   
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    bc="select * from bankregistration where email='"+email+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows1=mycursor.fetchone()   
    if rows1!=None:
     return render(request,'bank/signup.html',{'message': 'User is Already Exist.'})
    else:
     try:
      mn="INSERT INTO bankregistration(name,email,contact,password,cardno,q1,a1,q2,a2,q3,a3)VALUES('"+name+"','"+email+"','"+contact+"','"+password+"','','','','','','','')"
      print(mn)
      mycursor.execute(mn)
      mydb.commit()
      return render(request,'bank/signup.html',{'message': 'Successfully Added.'})
     except:
      return render(request,'bank/signup.html',{'message': 'Some issue. Try after some time.'})     
    
def banklogin(request):  
    return render(request,'bank/login.html')    
def bankloginvalidator(request):
    email=request.POST.get("email")
    password=request.POST.get("pwd")
    print("email"+email)
    print("password"+password)
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    bc="select * from bankregistration where email='"+email+"' and password='"+password+"'"
    print(bc)
    cd=mycursor.execute(bc)
    rows1=mycursor.fetchone()   
    if rows1!=None:
     request.session['id']=rows1[0]
     request.session['name']=rows1[1]
     request.session['email']=rows1[2]
     request.session['contact']=rows1[3]
     em=rows1[6]
     ey=rows1[7]
     return render(request,'bank/bankuserho.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact'],'x':rows1,'em':em,'ey':ey})
    else:
     return render(request,'bank/login.html',{'message':'Invalid credentials'})
def editbankuser(request):
    userno=str(request.session['id'])
    cardno=request.POST.get("cardno")
    expirymonth=request.POST.get("expirymonth")
    expiryyear=request.POST.get("expiryyear")
    securitycode=request.POST.get("securitycode")
    q1=request.POST.get("q1")
    a1=request.POST.get("a1")
    q2=request.POST.get("q2")
    a2=request.POST.get("a2")
    q3=request.POST.get("q3")
    a3=request.POST.get("a3")
    
    q4=request.POST.get("q4")
    a4=request.POST.get("a4")
    q5=request.POST.get("q5")
    a5=request.POST.get("a5")
    q6=request.POST.get("q6")
    a6=request.POST.get("a6")
    q7=request.POST.get("q7")
    a7=request.POST.get("a7")
    
    
    mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
    mycursor=mydb.cursor()
    try:
     mn="update bankregistration set cardno='"+cardno+"',expirymonth='"+expirymonth+"',expiryyear='"+expiryyear+"',securitycode='"+securitycode+"', q1='"+q1+"', a1='"+a1+"', q2='"+q2+"', a2='"+a2+"', q3='"+q3+"', a3='"+a3+"', q4='"+q4+"', a4='"+a4+"', q5='"+q5+"', a5='"+a5+"', q6='"+q6+"', a6='"+a6+"', q7='"+q7+"', a7='"+a7+"'  where ser_no="+userno
     print(mn)
     mycursor.execute(mn)
     mydb.commit()
     bc="select * from bankregistration where ser_no="+userno
     print(bc)
     mycursor.execute(bc)
     rows1=mycursor.fetchone()   
     return render(request,'bank/bankuserho.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact'],'x':rows1,'message':'Successfully updated.'})
    except:
     bc="select * from bankregistration where ser_no="+userno
     print(bc)
     mycursor.execute(bc)
     rows1=mycursor.fetchone()
     return render(request,'bank/bankuserho.html',{'id':request.session['id'],'name':request.session['name'],'email':request.session['email'],'contact':request.session['contact'],'x':rows1,'message':'Some issue. Try after some time.'})    
################    

def adminhome(request):
     return render(request,'adm/index.html')
def adminloginvalidator(request):
     name=request.POST.get("name")
     password=request.POST.get("password")
     if name=='Admin' and password=='Admin':
      return render(request,'adm/sub.html')    
     else:
      return render(request,'adm/index.html',{'message':'invalid Credentials'})
def viewcus(request):
     mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
     mycursor=mydb.cursor()
     bc="SELECT * FROM user_details"
     print(bc)
     cd=mycursor.execute(bc)
     rows1=mycursor.fetchall()
     print(rows1)      
     return render(request,'adm/viewcus.html',{'rows1':rows1}) 
def viewpayment(request):
     mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
     mycursor=mydb.cursor()
     bc="SELECT * FROM payment"
     print(bc)
     cd=mycursor.execute(bc)
     rows1=mycursor.fetchall()
     print(rows1)      
     return render(request,'adm/viewpayment.html',{'rows1':rows1})  
def viewfeedback(request):
     mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
     mycursor=mydb.cursor()
     bc="SELECT * FROM feedback"
     print(bc)
     cd=mycursor.execute(bc)
     rows1=mycursor.fetchall()
     print(rows1)      
     return render(request,'adm/viewfeedback.html',{'rows1':rows1})      
def insert(request):
     return render(request,'adm/insert.html')   
def inserthandler(request):
     pcode=request.POST.get("pcode")
     print("pcode"+pcode)
     path="addfweb\static\images"
     if request.method == 'POST' and request.FILES['Iname']:
       file = request.FILES['Iname']
       fs = FileSystemStorage(location=path)
       #filename = fs.save(file.name, file)
       filename = fs.save(pcode+file.name, file)
       uploaded_file_url = fs.url(filename)
       b2=filename
       print(b2)
     pcode=request.POST.get("pcode")
     print("pcode"+pcode)
     pname=request.POST.get("pname")
     print("pname"+pname)
     pcat=request.POST.get("pcat")
     print("pcat"+pcat)
     price=request.POST.get("price")  
     print("price"+price)
     desc=request.POST.get("desc") 
     print("desc"+desc)
     brand=request.POST.get("brand")  
     print("brand"+brand)
     category=request.POST.get("category")
     print("category"+category)
     features=request.POST.get("features") 
     print("features"+features)
     plateform=request.POST.get("plateform")
     print("plateform"+plateform)
     model=request.POST.get("model") 
     print("model"+model)
     type=request.POST.get("type")  
     print("type"+type)
     display=request.POST.get("display")
     print("display"+display)
     waranty=request.POST.get("waranty")
     print("waranty"+waranty)
     shipping_time=request.POST.get("shipping_time")
     print("shipping_time"+shipping_time)
     price=request.POST.get("price")
     print("price"+price)
     save=request.POST.get("save")
     print("save"+save)
     offer_price=request.POST.get("offer_price")
     print("offer_price"+offer_price)
     image=b2
     mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
     mycursor=mydb.cursor()
     try:
      #bc="insert into product(product_code,product_name,pro_cat,product_price,description,brand,category,features,plateform,model,type,display,waranty,shipping_time,price,offer_price,save,image1) values('"+pcode+"','"+pname+"','"+pcat+"','"+price+"','"+desc+"','"+brand+"','"+category+"','"+features+"','"+plateform+"','"+model+"','"+type+"','"+display+"','"+waranty+"','"+shipping_time+"','"+price+"','"+offer_price+"','"+save+"','"+image+"')"
      bc="insert into product(product_code,product_name,pro_cat,product_price,description,brand,category,features,plateform,model,type,display,waranty,shipping_time,price,offer_price,save,image1) values('"+pcode+"','"+pname+"','"+pcat+"','"+price+"','"+desc+"','"+brand+"','"+category+"','"+features+"','"+plateform+"','"+model+"','"+type+"','"+display+"','"+waranty+"','"+shipping_time+"','"+price+"','"+offer_price+"','"+save+"','"+image+"')";
      print(bc)
      mycursor.execute(bc)
      mydb.commit()
      return render(request,'adm/insert.html',{'message': 'Successfully Added.'})
     except:
      return render(request,'adm/insert.html',{'message': 'Some issue. Try after some time.'})
def update(request):
     return render(request,'adm/update.html')
def update1(request):
     cate=request.POST.get("pcat")
     mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
     mycursor=mydb.cursor()
     bc="select * from product where pro_cat='"+cate+"'"
     print(bc)
     cd=mycursor.execute(bc)
     rows1=mycursor.fetchall()
     print(rows1)      
     return render(request,'adm/update1.html',{'rows1':rows1}) 
def update2(request):
     pcode=request.POST.get("productcode")
     mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
     mycursor=mydb.cursor()
     bc="select * from product where product_code='"+pcode+"'"
     print(bc)
     cd=mycursor.execute(bc)
     rows1=mycursor.fetchall()
     print(rows1)      
     return render(request,'adm/update2.html',{'rows1':rows1})
def update2handler(request):
     pcode=request.POST.get("productcode")
     pname=request.POST.get("pname")
     print("pname"+pname)
     price=request.POST.get("price")  
     print("price"+price)
     desc=request.POST.get("desc") 
     print("desc"+desc)
     brand=request.POST.get("brand")  
     print("brand"+brand)
     category=request.POST.get("category")
     print("category"+category)
     features=request.POST.get("features") 
     print("features"+features)
     plateform=request.POST.get("plateform")
     print("plateform"+plateform)
     model=request.POST.get("model") 
     print("model"+model)
     type=request.POST.get("type")  
     print("type"+type)
     display=request.POST.get("display")
     print("display"+display)
     waranty=request.POST.get("waranty")
     print("waranty"+waranty)
     shipping_time=request.POST.get("shipping_time")
     print("shipping_time"+shipping_time)
     price=request.POST.get("price")
     print("price"+price)
     save=request.POST.get("save")
     print("save"+save)
     offer_price=request.POST.get("offer_price")
     print("offer_price"+offer_price)
     mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
     mycursor=mydb.cursor()
     try:
      mn="Update product set product_name='"+pname+"',product_price='"+price+"',description='"+desc+"', brand='"+brand+"',category='"+category+"',features='"+features+"',plateform='"+plateform+"',model='"+model+"',type='"+type+"',display='"+display+"',waranty='"+waranty+"',shipping_time='"+shipping_time+"',price='"+price+"',offer_price='"+offer_price+"',save='"+save+"' where product_code='"+pcode+"'"
      print(mn)
      mycursor.execute(mn)
      mydb.commit()
      bc="select * from product where product_code='"+pcode+"'"
      print(bc)
      cd=mycursor.execute(bc)
      rows1=mycursor.fetchall()
      print(rows1)      
      return render(request,'adm/update2.html',{'rows1':rows1,'message':'Succesfully Updated'})
     except:
      bc="select * from product where product_code='"+pcode+"'"
      print(bc)
      cd=mycursor.execute(bc)
      rows1=mycursor.fetchall()
      print(rows1)      
      return render(request,'adm/update2.html',{'rows1':rows1,'message':'There is some issue. Try after some time.'})
def delete(request):
     return render(request,'adm/delete.html')
def delete1(request):
     cate=request.POST.get("pcat")
     mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
     mycursor=mydb.cursor()
     bc="select * from product where pro_cat='"+cate+"'"
     print(bc)
     cd=mycursor.execute(bc)
     rows1=mycursor.fetchall()
     print(rows1)      
     return render(request,'adm/delete1.html',{'rows1':rows1}) 
def delp(request):
     productno=request.POST.get("productno")
     cate=request.POST.get("pcat")
     mydb=mysql.connector.connect(host="localhost",user="root",password="",database="addfhomeunidb")
     mycursor=mydb.cursor()
     try:
      bc="delete from product where ser_no='"+productno+"'"
      print(bc)
      cd=mycursor.execute(bc)
      mydb.commit()
      bc="select * from product where pro_cat='"+cate+"'"
      print(bc)
      cd=mycursor.execute(bc)
      rows1=mycursor.fetchall()
      print(rows1)      
      return render(request,'adm/delete1.html',{'rows1':rows1,'message':'Deleted'})
     except:
      bc="select * from product where pro_cat='"+cate+"'"
      print(bc)
      cd=mycursor.execute(bc)
      rows1=mycursor.fetchall()
      print(rows1)      
      return render(request,'adm/delete1.html',{'rows1':rows1,'message':'There is some issue. Try after some time.'})