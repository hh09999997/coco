from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


# 🧩 إنشاء حساب جديد
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, _("تم إنشاء الحساب بنجاح!"))
            login(request, user)
            return redirect('home')  # يعيد المستخدم للصفحة الرئيسية
        else:
            messages.error(request, _("حدث خطأ أثناء إنشاء الحساب."))
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


# 🔑 تسجيل الدخول
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, _("مرحبًا بك، تم تسجيل الدخول بنجاح!"))
                return redirect("home")
            else:
                messages.error(request, _("اسم المستخدم أو كلمة المرور غير صحيحة."))
        else:
            messages.error(request, _("تحقق من صحة البيانات المدخلة."))
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})
