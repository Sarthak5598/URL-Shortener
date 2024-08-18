from django.shortcuts import render,redirect,get_object_or_404
import json
import random
import string
from .models import URL
import datetime

from django.http import JsonResponse

def home(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        original_url = data.get("original_url")
        if original_url:
            short_code, created = URL.objects.get_or_create(
                original_url=original_url,
                defaults={'short_code': generate_short_code(), 'created': datetime.datetime.now()}
            )
            if created:
                short_url = request.build_absolute_uri(f'/{short_code}/')
            else:
                short_url = request.build_absolute_uri(f'/{short_code.short_code}/')
            
            return JsonResponse({'short_url': short_url})
        else:
            return JsonResponse({'error': 'No URL provided'}, status=400)
    return render(request, "home.html")


def redirect_to_original(request, short_code):
    url_entry = get_object_or_404(URL, short_code=short_code)
    return redirect(url_entry.original_url)

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(length))
    
    while URL.objects.filter(short_code=short_code).exists():
        short_code = ''.join(random.choice(characters) for _ in range(length))
    
    return short_code
