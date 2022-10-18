from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from accounts.forms import SignUpForm
from accounts.models import CustomUser, UserPermissions


# Create your views here.


# class SignUpView(generic.CreateView):
#     form_class = SignUpForm
#     success_url = reverse_lazy("login")
#     template_name = 'registration/signup.html'





def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        if request.POST.get("organizer"):
            user.permission = UserPermissions.objects.get(id=2)
            user.save()
        login(request, user)
        return redirect('home')
    return render(request, 'registration/signup.html', {'form': form})


