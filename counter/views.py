from django.shortcuts import render
from django.http import JsonResponse
from .models import Count

def index(request):
    # Increment view count
    count, created = Count.objects.get_or_create(id=1)
    count.views += 1
    count.save()

    # Get country from user's IP
    # You would use a service like ip-api.com or similar
    # country = get_country_from_ip(request.META.get('REMOTE_ADDR'))

    context = {
        'view_count': count.views,
        'button_count': count.button_presses,
        # 'country': country
    }
    return render(request, 'counter/index.html', context)

def increment_button(request):
    count = Count.objects.get(id=1)
    count.button_presses += 1
    count.save()
    return JsonResponse({'button_count': count.button_presses})
