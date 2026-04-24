from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def login_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        user = request.POST.get('username')
        password = request.POST.get('password')
        next_url = request.POST.get('next')

        authenticate_user = authenticate(request, username=user, password=password)

        if next_url in [None, '', 'None']:
            next_url = None

        if authenticate_user is not None:
            # print(next_url)
            login(request, authenticate_user)
            return redirect(next_url or 'home')
        
        # Handle invalid login here
        return render(request, 'accounts/login.html', {'error': 'Usuario o contraseña incorrectos','next': next_url or ''})
    
    # Handle GET request here
    next_url = request.GET.get('next', '')
    # next_url = next_url.split('/')[-2] if next_url else None
    return render(request, 'accounts/login.html', {'next': next_url})

@login_required
def home(request):
    return render(request, 'accounts/home.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def lista_de_usuarios(request):
    from django.contrib.auth.models import User
    users = User.objects.all()
    return render(request, 'accounts/lista_usuarios.html', {'users': users})