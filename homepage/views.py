from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from school.models import ContactQuery, Teacher

def home(request):
    teachers_list = Teacher.objects.filter(designation__icontains='Teacher').order_by('order')
    director = Teacher.objects.filter(designation__iexact='Director').first()
    vice_principal = Teacher.objects.filter(designation__icontains='Vice Principal').first()
    
    context = {
        'teachers_list': teachers_list,
        'director_teacher': director,
        'vice_principal_teacher': vice_principal,
    }
    return render(request, 'home.html', context)

@require_POST
def contact_submit(request):
    name = request.POST.get('name', '').strip()
    email = request.POST.get('email', '').strip()
    subject = request.POST.get('subject', '').strip()
    message = request.POST.get('message', '').strip()

    if not name or not email or not subject or not message:
        return HttpResponse('All fields are required.', status=400)

    try:
        ContactQuery.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        return HttpResponse('OK')
    except Exception as e:
        return HttpResponse(f'Error saving message: {str(e)}', status=500)

@require_POST
def newsletter_submit(request):
    # Simply return OK as required by standard newsletter php-email-form JS
    return HttpResponse('OK')

def offline(request):
    return render(request, 'offline.html')
