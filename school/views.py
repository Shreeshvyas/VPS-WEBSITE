from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from .models import (
    HeroSlider, 
    Facility, 
    Notice, 
    Event, 
    GalleryCategory, 
    GalleryImage, 
    Teacher, 
    ContactQuery
)

def home(request):
    hero_sliders = HeroSlider.objects.filter(is_active=True)
    facilities = Facility.objects.all()
    notices = Notice.objects.filter(is_active=True)
    events = Event.objects.all()[:3]
    teachers = Teacher.objects.all()[:4]
    gallery_images = GalleryImage.objects.all()[:8]
    
    context = {
        'hero_sliders': hero_sliders,
        'facilities': facilities,
        'notices': notices,
        'events': events,
        'teachers': teachers,
        'gallery_images': gallery_images,
        'is_home': True,
    }
    return render(request, 'school/index.html', context)


def about(request):
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers,
        'title': 'About Us',
    }
    return render(request, 'school/about.html', context)


def academics(request):
    facilities = Facility.objects.all()
    context = {
        'facilities': facilities,
        'title': 'Academics & Facilities',
    }
    return render(request, 'school/academics.html', context)


def gallery(request):
    categories = GalleryCategory.objects.all()
    gallery_images = GalleryImage.objects.prefetch_related('category').all()
    context = {
        'categories': categories,
        'gallery_images': gallery_images,
        'title': 'Gallery',
    }
    return render(request, 'school/gallery.html', context)


def contact(request):
    context = {
        'title': 'Contact Us',
    }
    return render(request, 'school/contact.html', context)


@require_POST
def contact_submit(request):
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    phone = request.POST.get('phone', '').strip()
    subject = request.POST.get('subject', '').strip()
    message = request.POST.get('message', '').strip()

    if not name or not email or not subject or not message:
        return JsonResponse({
            'status': 'error',
            'message': 'Please fill in all required fields.'
        }, status=400)

    try:
        ContactQuery.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )
        return JsonResponse({
            'status': 'success',
            'message': 'Your message has been sent successfully! We will get back to you soon.'
        })
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': 'An error occurred while sending your message. Please try again later.'
        }, status=500)
