from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomRegisterForm

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account created successfully!')
            return redirect('index')
    else:
        form = CustomRegisterForm()
    return render(request, 'register.html', {'form': form})

