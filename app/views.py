from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms  import UserForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.views.generic import View





def register(request):
    
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return render(request, 'registration/login.html')

    else:
        form = UserForm()
    return render(request, 'app/register.html', {'form': form})          




