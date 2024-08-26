from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import habitaciones
from .forms import CustomUserCreationForm 


@login_required
def catalogo(request):
    hab = habitaciones.objects.all()
    return render(request, 'core/catalogo.html', {'habitaciones':hab})

def home(request):
    return render(request, 'core/home.html')

def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
        
    return render(request, 'registration/register.html', {'form': form})