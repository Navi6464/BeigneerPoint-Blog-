from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from . models import Contact , Topic ,News,BlogComment
# Create your views here.

def home(request):
    if request.method == "POST":
       Email = request.POST['email'] 
       nsl = ['<','>','/','script','=','onload','svg']
       for i in nsl:
            if i in Email:
                messages.error(request," You cannot do any type of Harmfull activity on this site")
                break
            else:
                news = News(email=Email)
                messages.success(request,'your News request successfully send')
                news.save() 
                break
    return render(request,'blog/home.html/')

def free(request):
    return render(request,'blog/free.html/')

def contact(request):
    if request.method == "POST":
       Name = request.POST['name']
       Email = request.POST['email']
       Mesg = request.POST['mesg']
       
       nsl = ['<','>','/','script','=','onload','svg']
       for i in nsl:
            if i in Name or i in Email or i in Mesg:
                messages.error(request," You cannot do any type of Harmfull activity on this site")
                break
            elif len(Mesg) < 5 or len(Email)<4 or len(Name)<3:
                messages.error(request," 🙏️ please fill your info correctly ")
                break
            else:
                contact = Contact(name=Name,email=Email,mesg=Mesg)
                contact.save()
                messages.success(request,'your message successfully send 😎️☺️ thnq for visit on blog')
                break

       
       
    return render(request,'blog/contact.html/')


def more(request):          
    alltop = Topic.objects.all()
    return render(request,'blog/more.html',{"alltop":alltop})




def tor(request):
    if request.method == "POST":
       Name = request.POST['name']
       Comment = request.POST['comment']       
       
       nsl = ['<','>','/','script','=','onload','svg']
       for i in nsl:
            if i in Name or i in Comment:
                messages.error(request," You cannot do any type of Harmfull activity on this site")
                break
            elif len(Name) < 3:
                messages.error(request," 🙏️ please fill your info correctly ")
                break
            else:
                comm = BlogComment(user=Name,comment=Comment,post_name='tor')
                comm.save()
                messages.success(request,'your message successfully send 😎️☺️ thnq for visit on blog')
                break
       

    post = BlogComment.objects.filter(post_name = 'tor')
    return render(request,'blog/info.html',{'comment':post})

def nmap(request):
    if request.method == "POST":
       Name = request.POST['name']
       Comment = request.POST['comment']       
       
       nsl = ['<','>','/','script','=','onload','svg']
       for i in nsl:
            if i in Name or i in Comment:
                messages.error(request," You cannot do any type of Harmfull activity on this site")
                break
            elif len(Name) < 3:
                messages.error(request," 🙏️ please fill your info correctly ")
                break
            else:
                comm = BlogComment(user=Name,comment=Comment,post_name='nmap')
                comm.save()
                messages.success(request,'your message successfully send 😎️☺️ thnq for visit on blog')
                break
       

    post = BlogComment.objects.filter(post_name = 'nmap')
    return render(request,'blog/nmap.html',{'comment':post})

def proxies(request):
    if request.method == "POST":
       Name = request.POST['name']
       Comment = request.POST['comment']       
       
       nsl = ['<','>','/','script','=','onload','svg']
       for i in nsl:
            if i in Name or i in Comment:
                messages.error(request," You cannot do any type of Harmfull activity on this site")
                break
            elif len(Name) < 3:
                messages.error(request," 🙏️ please fill your info correctly ")
                break
            else:
                comm = BlogComment(user=Name,comment=Comment,post_name='proxie')
                comm.save()
                messages.success(request,'your message successfully send 😎️☺️ thnq for visit on blog')
                break
       

    post = BlogComment.objects.filter(post_name = 'proxie')
    return render(request,'blog/proxies.html',{'comment':post})


def aircrack(request):
    if request.method == "POST":
       Name = request.POST['name']
       Comment = request.POST['comment']       
       
       nsl = ['<','>','/','script','=','onload','svg']
       for i in nsl:
            if i in Name or i in Comment:
                messages.error(request," You cannot do any type of Harmfull activity on this site")
                break
            elif len(Name) < 3:
                messages.error(request," 🙏️ please fill your info correctly ")
                break
            else:
                comm = BlogComment(user=Name,comment=Comment,post_name='aircrack')
                comm.save()
                messages.success(request,'your message successfully send 😎️☺️ thnq for visit on blog')
                break
       

    post = BlogComment.objects.filter(post_name = 'aircrack')
    return render(request,'blog/aircrack.html',{'comment':post})



def search(request):
    search = request.GET['search']
    topic = Topic.objects.filter(desc__icontains=search)
    return render(request,'blog/search.html',{'alltop':topic}) 



  
