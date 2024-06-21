from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def visitor_view(request):
    return render(request, 'visitor.html')

def visitor_dashboard(request):
    return render(request, 'visitor_dashboard.html')

def qr_page(request):
    return render(request, 'qr_page.html')

def qr_code_generator(request):
    return render(request, 'qr_code_generator.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login  # Import Django's login function as auth_login

def login(request):
    if request.method == 'POST':
        username = request.POST.get('userid')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use Django's login function (auth_login) to log in the user
            return redirect('dashboard')  # Redirect to dashboard upon successful login
        else:
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
@login_required
def submit_report(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        # Here you would save the report to the database
        # For example:
        # report = Report(title=title, content=content, user=request.user)
        # report.save()
        messages.success(request, 'Report submitted successfully.')
        return redirect('dashboard')
    return redirect('dashboard')
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

