from django.shortcuts import render,redirect,get_object_or_404
import json
import random
import string
from .models import URL,UserUsage
import datetime
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm
from django.http import JsonResponse
from django.contrib.auth import authenticate,login,logout

def registration_page(request):
    form = CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        else:
            messages.error(request, 'Error in registration')
    return render(request, 'registration/register.html', {'form': form})


def login_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password= request.POST.get('password')

        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request, 'You have been successfully logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        original_url = data.get("original_url")
        
        if not original_url:
            messages.error(request, 'error: No URL provided')
            return JsonResponse({'error': 'No URL provided'}, status=400)
        
        # Handle authenticated user
        usage, created = UserUsage.objects.get_or_create(user=request.user)
        
        # Reset count if it's a new day
        if usage.last_reset < timezone.now().date():  # Compare date with date
            usage.usage_count = 0
            usage.last_reset = timezone.now().date()
        
        if usage.usage_count >= 10:
            messages.error(request, 'error: Daily limit reached')
            return JsonResponse({'error': 'Daily limit reached'}, status=400)
        
        # Create short URL
        short_code, created = URL.objects.get_or_create(
            original_url=original_url,
            defaults={'short_code': generate_short_code(), 'created': timezone.now(), 'user': request.user}
        )
        
        # Increment usage count
        usage.usage_count += 1
        usage.save()
        
        short_url = request.build_absolute_uri(f'/{short_code.short_code}/')
        return JsonResponse({'short_url': short_url})
    
    return render(request, "main/home.html", {'user': request.user})

def redirect_to_original(request, short_code):
    url_entry = get_object_or_404(URL, short_code=short_code)
    return redirect(url_entry.original_url)

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(length))
    
    while URL.objects.filter(short_code=short_code).exists():
        short_code = ''.join(random.choice(characters) for _ in range(length))
    
    return short_code
