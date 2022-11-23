from django.shortcuts import render


# Create your views here.
def jinja(request):
    d=context={'name':'Tarak','age':36}
    return render(request,'jinja_print.html',d)