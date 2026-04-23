from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')

        authenticate_user = authenticate(request, username=user, password=password)
        if authenticate_user is not None:
            login(request, authenticate_user)
            return redirect('home')
        else:
            # Handle invalid login here
            return render(request, 'accounts/login.html', {'error': 'Usuario o contraseña incorrectos'})
            pass
    else:
        # Handle GET request here
        return render(request, 'accounts/login.html')

@login_required
def home(request):
    return render(request, 'accounts/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')