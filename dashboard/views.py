# dashboard/views.py

from django.http import HttpResponse

def dashboard_home(request):
    return HttpResponse("🎯 لوحة التحكم جاهزة وتعمل بنجاح!")
