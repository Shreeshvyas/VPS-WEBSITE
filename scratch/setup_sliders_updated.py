import os
import sys
import django

sys.path.append(os.getcwd())
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vyas_school_project.settings')
django.setup()

from school.models import HeroSlider

def update_sliders():
    print("Recreating HeroSlider records in order...")
    HeroSlider.objects.all().delete()
    
    slides = [
        ("slider/slide0.jpg", 1),
        ("slider/slide1.jpg", 2),
        ("slider/slide2.jpg", 3),
        ("slider/slide3.png", 4),
        ("slider/slide4.jpg", 5),
        ("slider/slide5.jpg", 6),
        ("slider/slide6.jpg", 7),
    ]
    
    for path, order in slides:
        HeroSlider.objects.create(
            title=f"School Slider {order}",
            subtitle="",
            image=path,
            action_text="Learn More",
            action_url="#",
            order=order
        )
        print(f"Created slide order {order} at {path}")

if __name__ == '__main__':
    update_sliders()
