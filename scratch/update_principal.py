import os
import sys
import shutil
import django

# Add project root directory to python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vyas_school_project.settings')
django.setup()

from school.models import SchoolConfig, Teacher

src_image = r"C:\Users\shree\.gemini\antigravity\brain\5423f1bf-0124-4a7c-8fcc-e9c199054a2c\media__1780948201868.jpg"
dest_school = r"E:\VPHS WEBSITE\media\school\principal_shreesh.jpg"
dest_teacher = r"E:\VPHS WEBSITE\media\teachers\principal_shreesh.jpg"

if os.path.exists(src_image):
    # Copy files
    os.makedirs(os.path.dirname(dest_school), exist_ok=True)
    os.makedirs(os.path.dirname(dest_teacher), exist_ok=True)
    shutil.copy(src_image, dest_school)
    shutil.copy(src_image, dest_teacher)
    print("Copied new principal image to media folders.")
    
    # 1. Update SchoolConfig
    config = SchoolConfig.get_solo()
    config.principal_name = "Shreesh Vyas"
    config.principal_photo = "school/principal_shreesh.jpg"
    config.save()
    print("Updated SchoolConfig principal details.")
    
    # 2. Update Teacher model listing
    # Find teacher that is principal
    principal_teachers = Teacher.objects.filter(designation__icontains="principal")
    if principal_teachers.exists():
        for t in principal_teachers:
            t.name = "Shreesh Vyas"
            t.photo = "teachers/principal_shreesh.jpg"
            t.designation = "Principal"
            t.save()
        print("Updated existing Principal listing in Teachers table.")
    else:
        Teacher.objects.create(
            name="Shreesh Vyas",
            designation="Principal",
            qualification="M.Sc. Physics, M.Ed.",
            photo="teachers/principal_shreesh.jpg",
            order=1
        )
        print("Created new Principal listing in Teachers table.")
else:
    print(f"Error: source image file {src_image} not found!")
