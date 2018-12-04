from django.shortcuts import render
from .models import SampleForm

# Create your views here.
def index(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST.get('name'))
        name_r = request.POST.get('name')
        phone_r = request.POST.get('phone')
        email_r = request.POST.get('email')
        address_r = request.POST.get('address')
        about_r = request.POST.get('about')

        c = SampleForm(name=name_r, phone=phone_r, email=email_r, address=address_r, about=about_r)
        c.save()

        return render(request, 'mysite/form.html')
    else:
        return render(request, 'mysite/form.html')

