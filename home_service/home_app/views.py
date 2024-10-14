from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect,redirect
from django.db import connection
from home_app.models import sermodel
from home_app.forms import serform
from datetime import date
import hashlib
# Create your views here.
def home(request):
    return render(request,'home.html')


def about(request):
    return render(request,'about.html')


def cregister(request):
    return render(request,'cregister.html')
 

def addstaff(request):
    cur=connection.cursor()
    list=[]
    spid=request.session['uid']
    s= "select * from staff where spid='%s'"%(spid)
    cur.execute(s)
    result=cur.fetchall()
    for row in result:
         data={'stfid':row[0],'name':row[1],'address':row[2],'place':row[3],'city':row[4],'landmark':row[5],'district':row[6],'state':row[7],'pincode':row[8],'phone':row[9],'dob':row[10],'gender':row[11],'experience':row[12],'doj':row[13],'email':row[14]}
         list.append(data)
    return render (request,'addstaff.html',{'list':list})



def spregister(request):
    return render(request,'spregister.html')


def ulogin(request):
    return render(request,'ulogin.html')


def cregisteraction(request):
    cursor=connection.cursor()
    name=request.GET['name'] 
    email=request.GET['email']
    password=request.GET['password'] 
    
    hpwd=hashlib.sha256(password.encode()).hexdigest()
    sql1="select * from userlogin where uname='%s'" %(email)
    cursor.execute(sql1)
    result=cursor.fetchall()
    if (cursor.rowcount) > 0:
       msg="<script>alert('Already Registered');window.location='/ulogin/';</script>"
    else:
       sql2="insert into customers(name,email) values('%s','%s')"%(name,email)
       cursor.execute(sql2)
       sql3="select max(cid) from customers"
       cursor.execute(sql3)
       result=cursor.fetchall()
       for row in result:
          uid=int(row[0])
       utype="Customer"
       sql4="insert into userlogin (uid, uname, upass, utype) values('%s','%s','%s','%s')"%(uid,email,hpwd,utype)
       cursor.execute(sql4)
       msg="<script>alert('Success');window.location='/ulogin/';</script>"

    return HttpResponse(msg)



def spregisteraction(request):
    cursor=connection.cursor()
    name=request.GET['name']
    address=request.GET['address']
    place=request.GET['place']
    city=request.GET['city']
    landmark=request.GET['landmark']
    district=request.GET['district']
    state=request.GET['state']  
    pincode=request.GET['pincode']
    phone=request.GET['phone']
    email=request.GET['email']
    password=request.GET['password']
    
    hpwd=hashlib.sha256(password.encode()).hexdigest()
    sql1="select * from userlogin where uname='%s'" %(email)
    cursor.execute(sql1)
    result=cursor.fetchall()
    if (cursor.rowcount) > 0:
       msg="<script>alert('Already Registered');window.location='/ulogin/';</script>"
    else:
       sql2="insert into serviceproviders(name,address,place,city,landmark,district,state,pincode,phone,email) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name,address,place,city,landmark,district,state,pincode,phone,email)
       cursor.execute(sql2)
       sql3="select max(id) from serviceproviders"
       cursor.execute(sql3)
       result=cursor.fetchall()
       for row in result:
          uid=int(row[0])
       utype="Service_Provider"
       sql4="insert into userlogin (uid, uname, upass, utype,status) values('%s','%s','%s','%s','Pending')"%(uid,email,hpwd,utype)
       cursor.execute(sql4)
       msg="<script>alert('Success');window.location='/ulogin/';</script>"

    return HttpResponse(msg)



def addstaffaction(request):
    cursor=connection.cursor()
    name=request.GET['name']
    address=request.GET['address']
    place=request.GET['place']
    city=request.GET['city']
    landmark=request.GET['landmark']
    district=request.GET['district']
    state=request.GET['state']  
    pincode=request.GET['pincode']
    phone=request.GET['phone']
    dob=request.GET['dob']
    gender=request.GET['gender']
    experience=request.GET['experience']
    doj=request.GET['doj'] 
    email=request.GET['email']
    password=request.GET['password']
    spid=request.session['uid']
    hpwd=hashlib.sha256(password.encode()).hexdigest()
    sql1="select * from userlogin where uname='%s'" %(email)
    cursor.execute(sql1)
    result=cursor.fetchall()
    if (cursor.rowcount) > 0:
       msg="<script>alert('Already Registered');window.location='/addstaff/';</script>"
    else:
       sql2="insert into staff(name,address,place,city,landmark,district,state,pincode,phone,dob,gender,experience,doj,email,spid) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name,address,place,city,landmark,district,state,pincode,phone,dob,gender,experience,doj,email,spid)
       cursor.execute(sql2)
       sql3="select max(stfid) from staff where spid='%s'"%(spid)
       cursor.execute(sql3)
       result=cursor.fetchall()
       for row in result:
          uid=int(row[0])
       utype="Staff"
       sql4="insert into userlogin (uid, uname, upass, utype,status) values('%s','%s','%s','%s','Pending')"%(uid,email,hpwd,utype)
       cursor.execute(sql4)
       msg="<script>alert('Success');window.location='/addstaff/';</script>"

    return HttpResponse(msg)

def remove_staff(request):
    cursor=connection.cursor()
    id=request.GET['id']
    sql1="delete from staff where stfid='%s'"%(id)
    cursor.execute(sql1)
    sql2="delete from userlogin where uid='%s' and utype='Staff'"%(id)
    cursor.execute(sql2)
    msg="<script>alert('Successfully Staff Deleted');window.location='/addstaff/';</script>"
    return HttpResponse(msg)


def loginaction(request):
    cursor=connection.cursor()
    name=request.POST['uname']
    password=request.POST['upass']
    
    hpwd=hashlib.sha256(password.encode()).hexdigest()
    sql1="select * from userlogin where uname='%s' and upass='%s'"%(name,hpwd)
    cursor.execute(sql1)
   
    if(cursor.rowcount)>0:
        result1=cursor.fetchall()
        for row in result1:
            request.session['uid']=row[1]
            request.session['uname']=row[2]
            request.session['upass']=row[3]
            request.session['utype']=row[4]
            request.session['status']=row[5]
        if(request.session['utype']=='admin'):
            return render (request,'admin_home.html')
        
        elif(request.session['utype']=='Customer'):
            return render (request,'cust_home.html')
        
        elif(request.session['utype']=='Service_Provider' and request.session['status']=='Approved'):
            return render (request,'sp_home.html')
        
        elif(request.session['utype']=='Staff' and request.session['status']=='Approved'):
            return render (request,'staff_home.html')
        
        else:
            msg="<script>alert('Your Request is Pending');window.location='/home/';</script>"
            return HttpResponse(msg)
        
    else:
        msg="<script>alert('Invalid password and username');window.location='/ulogin/';</script>"
        return HttpResponse(msg)



def view_cust(request):
    cursor=connection.cursor()
    list=[]
    sql1="select * from customers"
    cursor.execute(sql1)
    result=cursor.fetchall()
    for row in result:
        data={'cid':row[0],'name':row[1],'address':row[2],'place':row[3],'city':row[4],'landmark':row[5],'district':row[6],'state':row[7],'pincode':row[8],'phone':row[9],'dob':row[10],'gender':row[11],'email':row[12]}
        list.append(data)
    return render(request,'view_cust.html',{'list':list})



def view_staff(request):
    cursor=connection.cursor()
    id=request.GET['uid']
    list=[]
    sql1="select * from staff inner join userlogin on staff.stfid=userlogin.uid where userlogin.utype='Staff' and staff.stfid='%s'"%(id)
    cursor.execute(sql1)
    result=cursor.fetchall()
    for row in result:
        data={'stfid':row[0],'name':row[1],'address':row[2],'place':row[3],'city':row[4],'landmark':row[5],'district':row[6],'state':row[7],'pincode':row[8],'phone':row[9],'dob':row[10],'gender':row[11],'experience':row[12],'doj':row[13],'email':row[14],'status':row[21]}
        list.append(data)
    return render(request,'view_staff.html',{'list':list})


def view_sp(request):
    cursor=connection.cursor()
    list=[]
    sql1="select * from serviceproviders inner join userlogin on serviceproviders.id=userlogin.uid where userlogin.utype='Service_Provider'"
    cursor.execute(sql1)
    result=cursor.fetchall() 
    for row in result:
        data={'id':row[0],'name':row[1],'address':row[2],'place':row[3],'city':row[4],'landmark':row[5],'district':row[6],'state':row[7],'pincode':row[8],'phone':row[9],'email':row[10],'status':row[16]}
        list.append(data)
    return render(request,'view_sp.html',{'list':list})

def admin_home(request):
    return render(request,'admin_home.html')

def approve_staff(request):
    cursor=connection.cursor()
    id=request.GET['uid']
    sql="update userlogin set status='Approved' where uid='%s' and utype='Staff'"%(id)
    cursor.execute(sql)
    msg="<script>alert('Staff Approved Successfully');window.location='/viewstaff/';</script>"
    return HttpResponse(msg)

def reject_staff(request):
    cursor=connection.cursor()
    id=request.GET['uid']
    sql="update userlogin set status='Rejected' where uid='%s' and utype='Staff'"%(id)
    cursor.execute(sql)
    msg="<script>alert('Staff Rejected Successfully');window.location='/viewstaff/';</script>"
    return HttpResponse(msg)
    
    
def approve_sp(request):
    cursor=connection.cursor()
    id=request.GET['uid']
    sql="update userlogin set status='Approved' where uid='%s' and utype='Service_Provider'"%(id)
    cursor.execute(sql)
    msg="<script>alert('Service Provider Approved Successfully');window.location='/viewsp/';</script>"
    return HttpResponse(msg)

def reject_sp(request):
    cursor=connection.cursor()
    id=request.GET['uid']
    sql="update userlogin set status='Rejected' where uid='%s' and utype='Service_Provider'"%(id)
    cursor.execute(sql)
    msg="<script>alert('Service Provider Rejected Successfully');window.location='/viewsp/';</script>"
    return HttpResponse(msg)


def edit_custprofile(request):
    cursor=connection.cursor()
    list=[]
    id=request.session['uid']
    sql="select * from customers inner join userlogin on customers.cid=userlogin.uid where customers.cid='%s' and userlogin.utype='Customer'"%(id)
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:
        w={'name':row[1],'address':row[2],'place':row[3],'city':row[4],'landmark':row[5],'district':row[6],'state':row[7],'pincode':row[8],'phone':row[9],'dob':row[10],'gender':row[11],'email':row[12],'password':row[16]}
        list.append(w)

    return render(request,'edit_custprofile.html',{'list':list})

def cust_home(request):
    return render(request,'cust_home.html')
   

def edit_staffprofile(request):
    cursor=connection.cursor()
    list=[]
    id=request.session['uid']
    sql="select * from staff inner join userlogin on staff.stfid=userlogin.uid where staff.stfid='%s' and userlogin.utype='Staff'"%(id)
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:
        w={'name':row[1],'address':row[2],'place':row[3],'city':row[4],'landmark':row[5],'district':row[6],'state':row[7],'pincode':row[8],'phone':row[9],'dob':row[10],'gender':row[11],'experience':row[12],'doj':row[13],'email':row[14],'password':row[19]}
        list.append(w)
    return render(request,'edit_staffprofile.html',{'list':list})

def staff_home(request):
    return render(request,'staff_home.html')
   

def edit_spprofile(request):
    cursor=connection.cursor()
    list=[]
    id=request.session['uid']
    sql="select * from serviceproviders inner join userlogin on serviceproviders.id=userlogin.uid where serviceproviders.id='%s' and userlogin.utype='Service_Provider'"%(id)
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:
        w={'name':row[1],'address':row[2],'place':row[3],'city':row[4],'landmark':row[5],'district':row[6],'state':row[7],'pincode':row[8],'phone':row[9],'email':row[10],'password':row[14]}
        list.append(w)
    return render(request,'edit_spprofile.html',{'list':list})


def sp_home(request):
    return render(request,'sp_home.html')


def edit_cust_profileaction(request):
    cursor=connection.cursor()
    cid=request.session['uid']
    name=request.GET['name']
    address=request.GET['address']
    place=request.GET['place']
    city=request.GET['city']
    landmark=request.GET['landmark']
    district=request.GET['district']
    state=request.GET['state']
    pincode=request.GET['pincode'] 
    phone=request.GET['phone']
    dob=request.GET['dob']
    gender=request.GET['gender']
    email=request.GET['email']
    password=request.GET['password']
    sql1="update customers set name='%s', address='%s', place='%s', city='%s', landmark='%s', district='%s', state='%s',  pincode='%s', phone='%s',dob='%s',gender='%s',  email='%s' where cid='%s'"%(name,address,place,city,landmark,district,state,pincode,phone,dob,gender,email,cid)
    cursor.execute(sql1)   
    sql2="update userlogin set uname='%s', upass='%s' where uid='%s' and utype='Customer'"%(email,password,cid)
    cursor.execute(sql2)
    msg="<script>alert('Profile Successfully Edited');window.location='/editcustprofile/';</script>"
    return HttpResponse(msg)

def edit_sp_profileaction(request):
    cursor=connection.cursor()
    id=request.session['uid']
    name=request.GET['name']
    address=request.GET['address']
    place=request.GET['place']
    city=request.GET['city']
    landmark=request.GET['landmark']
    district=request.GET['district']
    state=request.GET['state']
    pincode=request.GET['pincode'] 
    phone=request.GET['phone']
    email=request.GET['email']
    password=request.GET['password']
    hpwd=hashlib.sha256(password.encode()).hexdigest()
    sql1="update serviceproviders set name='%s', address='%s', place='%s', city='%s',landmark='%s',  district='%s', state='%s',  pincode='%s', phone='%s', email='%s' where id='%s'"%(name,address,place,city,landmark,district,state,pincode,phone,email,id)
    cursor.execute(sql1)   
    sql2="update userlogin set uname='%s', upass='%s' where uid='%s' and utype='Service_Provider'"%(email,hpwd,id)
    cursor.execute(sql2)
    msg="<script>alert('Profile Successfully Edited');window.location='/editspprofile/';</script>"
    return HttpResponse(msg)

def edit_staff_profileaction(request):
    cursor=connection.cursor()
    id=request.session['uid']
    name=request.GET['name']
    address=request.GET['address']
    place=request.GET['place']
    city=request.GET['city']
    landmark=request.GET['landmark']
    district=request.GET['district']
    state=request.GET['state']
    pincode=request.GET['pincode'] 
    phone=request.GET['phone']
    dob=request.GET['dob']
    gender=request.GET['gender']
    experience=request.GET['experience']
    doj=request.GET['doj']
    email=request.GET['email']
    password=request.GET['password']
    sql1="update staff set name='%s', addre`ss='%s', place='%s', city='%s', landmark='%s', district='%s', state='%s',  pincode='%s', phone='%s',dob='%s',gender='%s', experience='%s',doj='%s', email='%s' where stfid='%s'"%(name,address,place,city,landmark,district,state,pincode,phone,dob,gender,experience,doj,email,id)
    cursor.execute(sql1)   
    sql2="update userlogin set uname='%s', upass='%s' where uid='%s' and utype='Staff'"%(email,password,id)
    cursor.execute(sql2)
    msg="<script>alert('Profile Successfully Edited');window.location='/editstaffprofile/';</script>"
    return HttpResponse(msg)


def services(request):
    cursor=connection.cursor()
    list=[]
    id=request.session['uid']
    sql="select * from services where spid='%s'"%(id)
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:
        w={'sid':row[0],'sname':row[2],'desc':row[3],'simg':row[4]}
        list.append(w)
    return render(request,'services.html',{'list':list})

def servicesaction(request):
    if request.method == "POST":
        ServiceForm = serform(request.POST, request.FILES)
        if ServiceForm.is_valid():
            services =sermodel()
            
            services.sname =ServiceForm.cleaned_data["sname"]
            services.desc =request.POST["desc"]

            services.simg =ServiceForm.cleaned_data["simg"]
            services.spid=request.session['uid']
            services.save()
            msg = "<script>alert('Services Successfully Added');window.location='/services/';</script>"
            saved = True
    else:
        ServiceForm = serform()
    return HttpResponse(msg)


def delete_services(request):
    cursor=connection.cursor()
    id=request.GET['sid']
    sql="delete from services where sid='%s'"%(id)
    cursor.execute(sql)
    msg="<script>alert('Successfully Deleted');window.location='/services/';</script>"
    return HttpResponse(msg)

def delete_custacc(request):
    cursor=connection.cursor()
    cid=request.session['uid']
    sql1="delete from customers where cid='%s'"%(id)
    cursor.execute(sql1)
    sql2="delete from userlogin where uid='%s' and utype='Customer' "%(cid)
    cursor.execute(sql2)
    msg="<script>alert('Successfully Account Deleted');window.location='/home/';</script>"
    return HttpResponse(msg)

def delete_spacc(request):
    cursor=connection.cursor()
    id=request.session['uid']
    sql1="delete from serviceproviders where spid='%s'"%(id)
    cursor.execute(sql1)
    sql2="delete from userlogin where uid='%s' and utype='Service_Provider' "%(id)
    cursor.execute(sql2)
    msg="<script>alert('Successfully Account Deleted');window.location='/home/';</script>"
    return HttpResponse(msg)

def view_services(request):
    cursor=connection.cursor()
    list=[]
    sql="select * from services inner join serviceproviders on services.spid=serviceproviders.id"
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:
        data={'id':row[5],'name':row[6],'sid':row[0],'sname':row[2],'desc':row[3],'simg':row[4]}
        list.append(data)
    return render(request,'view_services.html',{'list':list})


def subservices(request):
    sid=request.GET['sid']
    # id=request.session['uid']
    cursor=connection.cursor()
    list=[]
    sql="select * from subservice where sid='%s'"%(sid)
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:
        data={'ssid':row[0],'sid':row[1],'spid':row[2],'ssname':row[3],'descrip':row[4],'amount':row[5]}
        list.append(data)
   
    return render(request,'subservices.html',{'sid':sid,'list':list})

def subserviceaction(request):
    cursor=connection.cursor()
    sid=request.GET['sid']
    spid=request.session['uid']
    ssname=request.GET['ssname']
    am=request.GET['amount']
    desc=request.GET['desc']
    sql="insert into subservice (sid,spid,ssname,descrip,amount) values('%s','%s','%s','%s','%s')"%(sid,spid,ssname,desc,am)
    cursor.execute(sql)
    msg="<script>alert('Added SubService Successfully');window.location='/subservices?sid="+sid+"';</script>"
    return HttpResponse(msg)
                   

def servicelist(request):
    cursor=connection.cursor()
    list=[]
    sql="select * from services inner join serviceproviders on services.spid=serviceproviders.id"
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:
        data={'id':row[5],'name':row[6],'sid':row[0],'sname':row[2],'desc':row[3],'simg':row[4],'name':row[6]}
        list.append(data)
    return render(request,'service_list.html',{'list':list})


def searchaction(request):
    cursor=connection.cursor()
    var=request.GET['sname']

    list=[]
    sql="select * from services inner join serviceproviders on services.spid=serviceproviders.id where sname like '%%%s%%' "%(var)
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:
        data={'id':row[5],'name':row[6],'sid':row[0],'sname':row[2],'desc':row[3],'simg':row[4]}
        list.append(data)
    return render(request,'service_list.html',{'list':list})

def viewsub(request):
    sid=request.GET['sid']
    # id=request.session['uid']
    cursor=connection.cursor()
    list=[]
    sql="select * from subservice where sid='%s'"%(sid)
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:
        data={'ssid':row[0],'sid':row[1],'spid':row[2],'ssname':row[3],'descrip':row[4],'amount':row[5]}
        list.append(data)
   
    return render(request,'viewsub.html',{'list':list})
def book(request):
    id=request.GET['id']
  
    cursor=connection.cursor()
    sql30="select * from subservice where ssid='%s'"%(id)
    cursor.execute(sql30)
    rs=cursor.fetchall()
    cr=[]
    for row in rs:
        q={'ssid':row[0],'sid':row[1],'spid':row[2],'ssname':row[3],'descrip':row[4],'amount':row[5]}
        cr.append(q)
        
    return render(request,'book.html',{'cr':cr})
def bookaction(request):
    cursor=connection.cursor()
    bdate=date.today()
    uid=request.session['uid']
    sid=request.GET['ssid']
    spid=request.GET['spid']
    adat=request.GET['adate']
    tim=request.GET['time']
    amount=request.GET['amount']
   
    s="insert into booking(bkdate,cid,amount,bkstatus,pstatus,spid,ssid,adate,time) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(bdate,uid,amount,'pending','pending',spid,sid,adat,tim)
    cursor.execute(s)
    msg="<script>alert('success');window.location='/custhome/';</script>"
    return HttpResponse(msg)
def pendingservice(request):
    cursor = connection.cursor()
    uid = request.session['uid']
    sql = """
        SELECT 
            booking.bkid AS bkid, 
            subservice.ssname AS ssname, 
            customers.name AS name, 
            booking.amount AS amount, 
            booking.bkdate AS bkdate, 
            booking.adate AS adate, 
            booking.time AS time, 
            booking.bkstatus AS bkstatus, 
            booking.pstatus AS pstatus
            
        FROM booking 
        INNER JOIN subservice ON booking.ssid = subservice.ssid 
        INNER JOIN customers ON booking.cid = customers.cid  
        INNER JOIN serviceproviders ON serviceproviders.id = subservice.spid 
        WHERE serviceproviders.id = %s
    """
    cursor.execute(sql, [uid])
    rs = cursor.fetchall()
    cr = []
    for row in rs:
        q = {
            'bkid': row[0],
            'ssname': row[1],
            'name': row[2],
            'amount': row[3],
            'bkdate': row[4],
            'adate': row[5],
            'time': row[6],
            'bkstatus':row[7],
            'pstatus':row[8],
          
        }
        cr.append(q)
    return render(request, 'pendingservice.html', {'cr': cr})
def tapr(request):	
	cursor=connection.cursor()
	
	bkid=request.GET['bkid']

	sql="update booking set bkstatus='accept' where bkid=%s"%(bkid)
	cursor.execute(sql)
	msg="<script>alert('values updated successfully');window.location='/pendingservice/';</script>"
	return HttpResponse(msg)
def porder(request):
    cur = connection.cursor()
    uid = request.session['uid']
    
    # Fetch bookings and associated details
    s1="select b.bkid,b.bkdate,b.cid,b.amount * 0.5 as amount_50,b.bkstatus,b.pstatus,b.spid,b.adate,b.time,s.ssid,s.ssname,c.name,c.address,c.place,c.phone from booking as b inner join subservice as s on b.ssid=s.ssid inner join customers as c on b.cid=c.cid where s.spid='%s' "%(uid)
    # sql2 = "SELECT * FROM booking INNER JOIN subservice ON booking.ssid = subservice.ssid INNER JOIN customers ON booking.cid = customers.cid WHERE subservice.spid = '%s'" % (uid)
    cur.execute(s1)
    rs = cur.fetchall()
    cr = []
    
    for row in rs:
        q = {
            'bkid': row[0], 
            'bkdate': row[1],
            'cid': row[2],
            'amount_50': row[3],
            'bkstatus': row[4], 
            'pstatus': row[5], 
            'spid': row[6], 
            'ssid': row[7], 
            'adate': row[8], 
            'time': row[9], 
            'ssname': row[10], 
          
            'name': row[11], 
            'address': row[12], 
            'place': row[13],
            'phone':row[14]
            
        }
        cr.append(q)
    
    # Fetch staff details associated with the service provider
    s1 = "SELECT * FROM staff WHERE spid = '%s'" % (uid)
    cur.execute(s1)
    rs = cur.fetchall()
    cr1 = []
    
    for row in rs:
        w = {
            'stfid': row[0],
            'name': row[1],
            'address': row[2],
            'place': row[3],
            'city': row[4],
            'landmark': row[5],
            'district': row[6],
            'state': row[7],
            'pincode': row[8],
            'phone': row[9],
            'dob': row[10]
        }
        cr1.append(w)
    
    return render(request, 'porder.html', {'cr': cr, 'cr1': cr1})
def assign(request):
    cursor = connection.cursor()
    id = request.GET['bkid']
    st = request.GET['st']
    s = "INSERT INTO assign(bkid, stfid,remark) VALUES ('%s', '%s','pending')" %(id, st)
    cursor.execute(s)
    sql = "UPDATE booking SET bkstatus='assigned' WHERE bkid='%s'" % id
    cursor.execute(sql)
    h = "<script>alert('Assigned'); window.location='/sphome/'; </script>"
    return HttpResponse(h)
def cvbook(request):
    uid=request.session['uid']
    cursor=connection.cursor()
    sql="SELECT booking.bkid AS bkid, subservice.ssname AS ssname, customers.name AS name, booking.amount AS amount, booking.bkdate AS bkdate, booking.bkstatus,booking.pstatus FROM booking INNER JOIN subservice ON booking.ssid = subservice.ssid INNER JOIN customers ON booking.cid = customers.cid where booking.cid='%s'"%(uid)
    cursor.execute(sql)
    rs=cursor.fetchall()
    cr=[]
    for row in rs:
        q={'bkid':row[0],'ssname':row[1],'name':row[2],'amount':row[3],'bkdate':row[4],'bkstatus':row[5],'pstatus':row[6]}
        cr.append(q)
    return render(request,'cvbook.html',{'cr':cr})


# def pay(request):
#     cursor=connection.cursor()
#     sid=request.GET['id']
#     return render(request,'pay.html',{'bkid':sid})
def cpaid(request):
    cursor=connection.cursor()
    sid=request.GET['bkid']
    sql="update booking set pstatus='paid' where bkid='%s'"%sid
    cursor.execute(sql)
    msg="<script>alert('success');window.location='/custhome/';</script>"
    return HttpResponse(msg)
 
def aorder(request):
	cursor = connection.cursor()
	uid=request.session['uid']
	sql2=     """
              SELECT booking.bkid, booking.bkstatus, subservice.ssname, subservice.amount, customers.name, customers.phone, customers.address, customers.city, assign.remark,
assign.asid FROM booking
INNER JOIN subservice ON booking.ssid = subservice.ssid
INNER JOIN customers ON customers.cid = booking.cid
INNER JOIN assign ON assign.bkid = booking.bkid
INNER JOIN staff ON staff.stfid = assign.stfid
WHERE assign.stfid = %s
ORDER BY booking.bkid DESC
            """%(uid)
        
	cursor.execute(sql2)
	result=cursor.fetchall()
	list=[]
	for row in result:
		w = {
                'bkid': row[0],
                'bkstatus': row[1],
                'ssname': row[2],
                'amount': row[3],
                'name': row[4],
                'phone': row[5],
                'address': row[6],
                'city': row[7],
                'remark':row[8],
                'asid':row[9]
                
            }
		list.append(w)
	return render(request,'aorder.html',{'order': list})
def status(request):
	cursor = connection.cursor()
	oid=request.GET['bkid']
	sts=request.GET['s']
	sql="update booking set bkstatus='%s' WHERE bkid='%s'"%(sts,oid)
	cursor.execute(sql)
	h="<script>  window.location='/aorder/'; </script>"
	return HttpResponse(h)
def astatus(request):
	cursor = connection.cursor()
	oid=request.GET['bkid']
	sts=request.GET['s']
	sql="update booking set bkstatus='%s' WHERE bkid='%s'"%(sts,oid)
	cursor.execute(sql)
	h="<script>  window.location='/aorder/'; </script>"
	return HttpResponse(h)
def sstatus(request):
	cursor = connection.cursor()
	oid=request.GET['bkid']
	sts=request.GET['s']
	sql="update booking set bkstatus='%s' WHERE bkid='%s'"%(sts,oid)
	cursor.execute(sql)
	h="<script>  window.location='/aorder/'; </script>"
	return HttpResponse(h)
def myservice(request):
    uid = request.session['uid']
    cursor = connection.cursor()
    sql = """
        SELECT booking.bkid, booking.bkstatus, subservice.ssname, subservice.amount, staff.name
        FROM booking
        INNER JOIN subservice ON booking.ssid = subservice.ssid
        INNER JOIN customers ON customers.cid = booking.cid
        INNER JOIN assign ON assign.bkid = booking.bkid
        INNER JOIN staff ON staff.stfid = assign.stfid
        WHERE customers.cid = %s
    """
    cursor.execute(sql, [uid])
    result = cursor.fetchall()
    book = []
    for row in result:
        entry = {
            'bkid': row[0],
            'bkstatus': row[1],
            'ssname': row[2],
            'amount': row[3],
            'name': row[4]
        }
        book.append(entry)
    return render(request, 'myservice.html', {'book': book})
def feedback(request):
    return render(request,'feedback.html')
def faction(request):
	fb=request.GET['fb']
	uid=request.session['uid']
	cursor=connection.cursor()
	sql="insert into feedback(feedback,cid)values('%s','%s')"%(fb,uid)
	cursor.execute(sql)
	msg="<script>alert('success');window.location='/feedback/'</script>"
	return HttpResponse(msg)    
def vfeedback(request):
	cursor=connection.cursor()
	sql="select * from feedback inner join customers on feedback.cid=customers.cid"
	cursor.execute(sql)
	rs=cursor.fetchall()
	usr=[]
	for row in rs:
		y={'fid':row[0],'feedback':row[2],'name':row[4]}
		usr.append(y)
	return render(request,'vfeedback.html',{'usr':usr})
def updser(request):
    
    cursor=connection.cursor()
    cid=request.GET['id']
    sql="select * from subservice where ssid='%s'"%(cid)
    cursor.execute(sql)
    rs=cursor.fetchall()
    clist=[]
    for row in rs:
        x={'ssid':row[0],'sid':row[1],'spid':row[2],'ssname':row[3],'descrip':row[4],'amount':row[5]}
        clist.append(x)  
        
    return render(request,'updser.html',{'clist':clist}) 

def orderreport(request):
    cursor = connection.cursor()
    a = request.session['uid']
    
    if request.method == 'GET' and 'd1' in request.GET and 'd2' in request.GET:
        d1 = request.GET['d1']
        d2 = request.GET['d2']
        sql2 = """
            SELECT 
                subservice.ssname,
                booking.bkdate,
                booking.amount,
                booking.bkstatus,
                booking.pstatus,
                staff.name AS sname,
                customers.name AS cname,
                customers.phone,
                customers.email,
                serviceproviders.name AS spname
            FROM 
                booking
            INNER JOIN 
                assign ON assign.bkid = booking.bkid
            INNER JOIN 
                subservice ON subservice.ssid = booking.ssid
            INNER JOIN 
                customers ON customers.cid = booking.cid
            INNER JOIN 
                staff ON staff.stfid = assign.stfid
            INNER JOIN 
                serviceproviders ON serviceproviders.id = booking.spid -- Assuming 'id' is the primary key in serviceproviders
            WHERE 
                booking.bkdate BETWEEN %s AND %s
            ORDER BY 
                booking.bkid DESC
        """
        cursor.execute(sql2, [d1, d2])
    else:
        sql2 = """
            SELECT 
                subservice.ssname,
                booking.bkdate,
                booking.amount,
                booking.bkstatus,
                booking.pstatus,
                staff.name AS sname,
                customers.name AS cname,
                customers.phone,
                customers.email,
                serviceproviders.name AS spname
            FROM 
                booking
            INNER JOIN 
                assign ON assign.bkid = booking.bkid
            INNER JOIN 
                subservice ON subservice.ssid = booking.ssid
            INNER JOIN 
                customers ON customers.cid = booking.cid
            INNER JOIN 
                staff ON staff.stfid = assign.stfid
            INNER JOIN 
                serviceproviders ON serviceproviders.id = booking.spid -- Assuming 'id' is the primary key in serviceproviders
            ORDER BY 
                booking.bkid DESC
        """
        cursor.execute(sql2)

    result = cursor.fetchall()
    list = []

    for row in result:
        w = {
            'ssname': row[0],
            'bkdate': row[1],
            'amount': row[2],
            'bkstatus': row[3],
            'pstatus': row[4],
            'sname': row[5],
            'cname': row[6],
            'phone': row[7],
            'email': row[8],
            'spname': row[9]
        }
        list.append(w)
    
    return render(request, 'reports.html', {'order': list})
def updseract(request):
    cursor=connection.cursor()
    sn=request.GET['ssname']
    sd=request.GET['descrip']
    sm=request.GET['amount']
    cid=request.GET['ssid']
    
    sql="update subservice set ssname='%s',descrip='%s',amount='%s' where ssid='%s'"%(sn,sd,sm,cid)
    cursor.execute(sql)
    msg="<script>alert('updated');window.location='/services/';</script>"
    return HttpResponse(msg)
def vbstatus(request):
    cursor = connection.cursor()
    uid = request.session['uid']
    sql2 = """
        SELECT booking.bkid, booking.bkstatus, subservice.ssname, subservice.amount, 
               customers.cid, customers.name, customers.phone, customers.address, customers.city,
               staff.stfid, staff.name, staff.phone, staff.email,subservice.ssid
        FROM booking 
        INNER JOIN subservice ON booking.ssid = subservice.ssid
        INNER JOIN customers ON customers.cid = booking.cid
        INNER JOIN assign ON assign.bkid = booking.bkid
        INNER JOIN staff ON staff.stfid = assign.stfid
        WHERE customers.cid = %s
        ORDER BY booking.bkid DESC
    """
    
    cursor.execute(sql2, (uid,))
    result = cursor.fetchall()
    list = []
    for row in result:
        w = {
            'bkid': row[0],
            'bkstatus': row[1],
            'ssname': row[2],
            'amount': row[3],
            'cid': row[4],
            'customer_name': row[5],
            'customer_phone': row[6],
            'customer_address': row[7],
            'customer_city': row[8],
            'stfid': row[9],
            'staff_name': row[10],
            'staff_phone': row[11],
            'staff_email': row[12],
            'ssid':row[13]
        }
        list.append(w)
    return render(request, 'vbstatus.html', {'order': list})
def avbstatus(request):
    cursor = connection.cursor()
 
    sql2 = """
        SELECT booking.bkid, booking.bkstatus, subservice.ssname, subservice.amount, 
               customers.cid, customers.name, customers.phone, customers.address, customers.city,
               staff.stfid, staff.name, staff.phone, staff.email,assign.remark
        FROM booking 
        INNER JOIN subservice ON booking.ssid = subservice.ssid
        INNER JOIN customers ON customers.cid = booking.cid
        INNER JOIN assign ON assign.bkid = booking.bkid
        INNER JOIN staff ON staff.stfid = assign.stfid
       
    """
    
    cursor.execute(sql2)
    result = cursor.fetchall()
    list = []
    for row in result:
        w = {
            'bkid': row[0],
            'bkstatus': row[1],
            'ssname': row[2],
            'amount': row[3],
            'cid': row[4],
            'customer_name': row[5],
            'customer_phone': row[6],
            'customer_address': row[7],
            'customer_city': row[8],
            'stfid': row[9],
            'staff_name': row[10],
            'staff_phone': row[11],
            'staff_email': row[12],
            'remark':row[13]
        }
        list.append(w)
    return render(request, 'avbstatus.html', {'order': list})
def uReview(request):
    cursor=connection.cursor()
    list1=[]
    pid=request.GET['id']
    uid=request.session['uid']
    s="select * from review inner join customers on review.uid=customers.cid where review.pid='%s'"%(pid)
    print(s)
    cursor.execute(s)
    result=cursor.fetchall()
    for row in result:
        w={'rid':row[0],'review':row[1],'pid':row[2],'uid':row[3],'rating':row[4],'name':row[6]}
        list1.append(w)
    return render(request,'uReview.html',{'list1':list1,'uid':uid,'pid':pid})
from statistics import mean  # For calculating mean
def uReviewAct(request):
    # Fetch data from request
    pid = request.GET.get('ssid', None)
    uid = request.session.get('uid', None)
    rw = request.GET.get('rw', '')
    s1 = request.GET.get('s1', '')
    s2 = request.GET.get('s2', '')
    s3 = request.GET.get('s3', '')
    s4 = request.GET.get('s4', '')
    s5 = request.GET.get('s5', '')

    # Convert to integers or default to 0 if not selected
    s1 = int(s1) if s1 else 0
    s2 = int(s2) if s2 else 0
    s3 = int(s3) if s3 else 0
    s4 = int(s4) if s4 else 0
    s5 = int(s5) if s5 else 0

    # Calculate rate based on selected ratings
    rate = s1 + s2 + s3 + s4 + s5

    # Insert into database
    cursor = connection.cursor()
    sql = "INSERT INTO review (rw, pid, uid, rating) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (rw, pid, uid, rate))

    # Commit changes to the database
    connection.commit()

    # Redirect or display success message
    msg = "<script>alert('Successfully Reviewed');window.location='/custhome/';</script>"
    return HttpResponse(msg)

def uvReview(request):
    # Get the 'tid' parameter from the request
    tid = request.GET.get('tid')
    if not tid:
        return render(request, 'uvReview.html', {'list1': [], 'list2': []})

    cursor = connection.cursor()
    reviews = []
    avg_rating_info = []

    # Query to get reviews with customer and subservice info
    review_query = """
        SELECT review.rid, review.rw, review.pid, review.uid, review.rating, customers.cid, subservice.ssid,customers.name
        FROM review
        INNER JOIN customers ON review.uid = customers.cid
        INNER JOIN subservice ON review.pid = subservice.ssid
        WHERE review.pid = %s
    """
    cursor.execute(review_query, [tid])
    review_results = cursor.fetchall()
    
    for row in review_results:
        review = {
            'rid': row[0],
            'rw': row[1],
            'pid': row[2],
            'uid': row[5],  # customers.cid
            'rating': row[4],
            'name':row[7]
        }
        reviews.append(review)

    # Query to get the average rating for the specified 'tid'
    avg_rating_query = """
        SELECT pid, AVG(rating) AS avg_rating
        FROM review
        WHERE pid = %s
        GROUP BY pid
    """
    cursor.execute(avg_rating_query, [tid])
    avg_rating_results = cursor.fetchall()
    
    for r in avg_rating_results:
        avg_rating = {
            'tid': r[0],
            'avg_rating': round(r[1], 2)  # Round to 2 decimal places
        }
        avg_rating_info.append(avg_rating)

    # Debugging information
    print("Reviews: ", reviews)
    print("Average Rating Info: ", avg_rating_info)

    # Render the results in the template
    return render(request, 'uvReview.html', {'list1': reviews, 'list2': avg_rating_info})
def rstatus(request):
    cursor=connection.cursor()
    t1=request.GET['t1']
    rq=request.GET['asid']
    
    sql="update assign set remark='%s' where asid='%s'"%(t1,rq)
    
    cursor.execute(sql)
    msg="<script>alert('Remark Send');window.location='/aorder/';</script>"
    return HttpResponse(msg)
def sorderreport(request):
    cursor = connection.cursor()
    a = request.session['uid']
    
    if request.method == 'GET' and 'd1' in request.GET and 'd2' in request.GET:
        d1 = request.GET['d1']
        d2 = request.GET['d2']
        sql2 = """
            SELECT 
                subservice.ssname,
                booking.bkdate,
                booking.amount,
                booking.bkstatus,
                booking.pstatus,
                staff.name AS sname,
                customers.name AS cname,
                customers.phone,
                customers.email,
                serviceproviders.name AS spname
            FROM 
                booking
            INNER JOIN 
                assign ON assign.bkid = booking.bkid
            INNER JOIN 
                subservice ON subservice.ssid = booking.ssid
            INNER JOIN 
                customers ON customers.cid = booking.cid
            INNER JOIN 
                staff ON staff.stfid = assign.stfid
            INNER JOIN 
                serviceproviders ON serviceproviders.id = booking.spid
            WHERE 
                booking.bkdate BETWEEN %s AND %s AND booking.spid = %s
            ORDER BY 
                booking.bkid DESC
        """
        cursor.execute(sql2, [d1, d2, a])
    else:
        sql2 = """
            SELECT 
                subservice.ssname,
                booking.bkdate,
                booking.amount,
                booking.bkstatus,
                booking.pstatus,
                staff.name AS sname,
                customers.name AS cname,
                customers.phone,
                customers.email,
                serviceproviders.name AS spname
            FROM 
                booking
            INNER JOIN 
                assign ON assign.bkid = booking.bkid
            INNER JOIN 
                subservice ON subservice.ssid = booking.ssid
            INNER JOIN 
                customers ON customers.cid = booking.cid
            INNER JOIN 
                staff ON staff.stfid = assign.stfid
            INNER JOIN 
                serviceproviders ON serviceproviders.id = booking.spid
            WHERE 
                booking.spid = %s
            ORDER BY 
                booking.bkid DESC
        """
        cursor.execute(sql2, [a])

    result = cursor.fetchall()
    list = []

    for row in result:
        w = {
            'ssname': row[0],
            'bkdate': row[1],
            'amount': row[2],
            'bkstatus': row[3],
            'pstatus': row[4],
            'sname': row[5],
            'cname': row[6],
            'phone': row[7],
            'email': row[8],
        }
        list.append(w)
    
    return render(request, 'spreport.html', {'order': list})
def cancel(request):
    cursor = connection.cursor()
    bkid = request.GET['bkid']
    
    sql = "update booking set bkstatus='canceled' where bkid=%s" % (bkid)
    cursor.execute(sql)
    msg = "<script>alert('values updated successfully');window.location='/myservice/';</script>"
    return HttpResponse(msg)
def remark(request):
    cursor = connection.cursor()
    bkid = request.GET['bkid']
    remark = request.GET['remark']
    sql = "update booking set bkstatus='%s' where bkid='%s'" % (remark,bkid)
    cursor.execute(sql)
    msg = "<script>alert('values updated successfully');window.location='/pendingservice/';</script>"
    return HttpResponse(msg)


def bank(request):
    return render(request,"bank.html")
def bankaction(request):
    cursor = connection.cursor()
    a = request.session['uid']
    b = request.GET['bname']
    acc = request.GET['aco']
    cc = request.GET['co']
    cv = request.GET['cv']   
    ep = request.GET['ep'] 
    am = request.GET['amt']
    
    # Check if uid already exists in paccount
    check_sql = "SELECT COUNT(*) FROM paccount WHERE uid = %s"
    cursor.execute(check_sql, [a])
    result = cursor.fetchone()
    
    if result[0] > 0:
        # uid already exists, show alert message
        msg = "<script>alert('User bank details already added');window.location='/bank/';</script>"
    else:
        # uid does not exist, proceed with insertion
        sql = """
        INSERT INTO paccount (ano, bname, bamt, cno, cvv, edate, uid)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, [acc, b, am, cc, cv, ep, a])
        msg = "<script>alert('Values updated successfully');window.location='/bank/';</script>"
    
    return HttpResponse(msg)

def pay(request):
    cursor = connection.cursor()
    lid = request.GET.get('id')

    print(lid)

    list1 = []

    # Corrected SQL query with parameterized input to prevent SQL injection
    s = """
        SELECT b.bkid, ss.ssname, b.amount * 0.5 as amount
        FROM booking b
        INNER JOIN subservice ss ON b.ssid = ss.ssid
        WHERE b.bkid = %s
    """
    cursor.execute(s, [lid])
    result = cursor.fetchall()

    for row in result:
        w = {'bkid': row[0], 'ssname': row[1], 'amount': row[2]}
        list1.append(w)

    return render(request, 'pay.html', {'list1': list1})
def preBookingAct(request):
    import datetime

    if request.method == "POST":
        cur = connection.cursor()
        lid = request.POST.get('bkid')
        pamt = float(request.POST.get('amount', 0))  # Convert pamt to float if necessary, default to 0 if not present
        addr = request.POST.get('addr')
        cno = request.POST.get('cno').strip()  # Strip any leading/trailing spaces
        cvv = request.POST.get('cvv').strip()  # Strip any leading/trailing spaces
        edate = request.POST.get('exp').strip()  # Strip any leading/trailing spaces
        uid = request.session.get('uid')
        sql="update booking set pstatus='paid' where bkid='%s'"%lid
        cur.execute(sql)
        if not uid:
            msg = "<script>alert('User not logged in.');window.location='/login/'</script>"
            return HttpResponse(msg)

        today = datetime.date.today()  # Ensure you have imported datetime

        # Query to fetch bamt, cno, cvv, and edate from paccount table for the current user
        cur.execute("SELECT bamt, cno, cvv, edate FROM paccount WHERE uid = %s", [uid])
        row = cur.fetchone()
         
        if row:
            bamt = float(row[0])  # Assuming bamt is stored as a numeric type in the database
            stored_cno = str(row[1]).strip()  # Convert to string and strip spaces
            stored_cvv = str(row[2]).strip()  # Convert to string and strip spaces
            stored_edate = str(row[3]).strip()  # Convert to string and strip spaces

            if stored_cno != cno:
                msg = "<script>alert('Invalid Card Number');window.location='/pay?id="+lid+"'</script>"
                return HttpResponse(msg)

            if stored_cvv != cvv:
                msg = "<script>alert('Invalid CVV');window.location='/pay?id="+lid+"'</script>"
                return HttpResponse(msg)

            if stored_edate != edate:
                msg = "<script>alert('Invalid Expiry Date');window.location='/pay?id="+lid+"'</script>"
                return HttpResponse(msg)

            # Check if bamt is sufficient
            if bamt < pamt:
                msg = "<script>alert('Insufficient balance');window.location='/pay/'</script>"
                return HttpResponse(msg)
            else:
                # All checks passed, proceed with updating the balance
                sql1 = "UPDATE paccount SET bamt = bamt - %s WHERE uid = %s"
                cur.execute(sql1, [pamt, uid])
                msg = "<script>alert('Payment successful');window.location='/custhome/'</script>"
                return HttpResponse(msg)
        else:
            # Handle case where user's information is not found
            msg = "<script>alert('Error: User Account information not found');window.location='/custhome/'</script>"
            return HttpResponse(msg)
       
    # Handle case where request method is not POST
    msg = "<script>alert('Invalid request method');window.location='/pay/'</script>"
    return HttpResponse(msg)