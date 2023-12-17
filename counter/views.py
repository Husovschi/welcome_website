import requests
from django.shortcuts import render
from django.http import JsonResponse
from .models import Count, Country

def index(request):
    # Increment view count
    count, created = Count.objects.get_or_create(id=1)
    count.views += 1
    count.save()

    # Get country from user's IP
    country_name = get_country_from_ip(request.META.get('HTTP_CF_CONNECTING_IP'))
    country, created = Country.objects.get_or_create(name=country_name)
    country.visits += 1
    country.save()
    top_countries = Country.objects.order_by('-visits')[:10]

    context = {
        'view_count': count.views,
        'button_count': count.button_presses,
        'country': country_name,
        'country_count': country.visits,
        'top_countries': top_countries,
    }
    return render(request, 'counter/index.html', context)

def increment_button(request):
    count = Count.objects.get(id=1)
    count.button_presses += 1
    count.save()
    return JsonResponse({'button_count': count.button_presses})

def get_country_from_ip(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        response.raise_for_status()
        return response.json()['country']
    except Exception:
        return 'Unknown'
