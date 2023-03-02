from django.shortcuts import render, redirect
import random
from django.core.mail import send_mail
from django.conf import settings
from store.models.mail import userotp
from store.models.customer import Customer
from django.contrib.sessions.models import Session


def mail(request):
    if request.method=="POST":
        otp=request.POST.get('otp')
        userotp.objects.filter(otp=otp).last()
        return redirect('checkout')
        
	    		
    else:
        

        session_key = request.session._session_key
        print('------------------------------------')
        print(session_key)
        session = Session.objects.get(session_key=session_key)
        session_data = session.get_decoded()
        print(session_data,'============================',type(session_data))
        
        a=session_data.get('customer')
        print(session_data.get('customer'),'---------------------------------')
        
    
        usr= Customer.objects.get(id=a)
        print("===================email==================",type(usr))
        print(usr.email)
  
        # a="dyanandkumar4411@gmail.com"
        # print(a)
        otp2 = random.randint(100000, 999999)
        userotp.objects.create(otp = otp2 )
        mess = f"Hello ,\nYour OTP is {otp2}\nThanks!"
        send_mail(
	    	"welcom in online shopping -Orders confirmation mail",
	    	mess,
	    	settings.EMAIL_HOST_USER,
	    	[usr.email],
	    		fail_silently = False
	    		)

        return render(request,"mail.html")




