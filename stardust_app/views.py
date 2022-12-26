from django.shortcuts import render, HttpResponse
from stardust_app.models import Feedback


# Create your views here.
def index(request):
    return render(request,'index.html')

def form(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        usn = request.POST.get('usn')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        feedback = request.POST.get('feedback')
        s = Feedback(name=name,usn=usn,email=email,phone=phone,feedback=feedback)
        s.save()

       


    return render(request,'forms.html')
