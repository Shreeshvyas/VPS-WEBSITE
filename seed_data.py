import os
import shutil
import django

# Setup Django Environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'vyas_school_project.settings')
django.setup()

from django.utils import timezone
from school.models import (
    SchoolConfig, 
    HeroSlider, 
    Facility, 
    Notice, 
    Event, 
    GalleryCategory, 
    GalleryImage, 
    Teacher
)

def copy_generated_images():
    print("Copying generated images from cache to media folders...")
    
    # Target media subdirectories
    os.makedirs('media/school', exist_ok=True)
    os.makedirs('media/slider', exist_ok=True)
    os.makedirs('media/facilities', exist_ok=True)
    os.makedirs('media/teachers', exist_ok=True)
    os.makedirs('media/gallery', exist_ok=True)
    os.makedirs('media/events', exist_ok=True)

    # Image source locations (Gemini Cache)
    cache_dir = r"C:\Users\shree\.gemini\antigravity\brain\5423f1bf-0124-4a7c-8fcc-e9c199054a2c"
    
    # Find generated files in cache directory
    logo_src = None
    principal_src = None
    campus_src = None
    classroom_src = None
    
    for filename in os.listdir(cache_dir):
        if filename.startswith("school_logo_") and filename.endswith(".png"):
            logo_src = os.path.join(cache_dir, filename)
        elif filename.startswith("principal_portrait_") and filename.endswith(".png"):
            principal_src = os.path.join(cache_dir, filename)
        elif filename.startswith("school_campus_") and filename.endswith(".png"):
            campus_src = os.path.join(cache_dir, filename)
        elif filename.startswith("modern_classroom_") and filename.endswith(".png"):
            classroom_src = os.path.join(cache_dir, filename)

    # Helper function to copy
    def safe_copy(src, dest):
        if src and os.path.exists(src):
            shutil.copy(src, dest)
            print(f"Successfully copied {os.path.basename(src)} -> {dest}")
            return dest
        else:
            print(f"Warning: Source not found for copy to {dest}")
            return None

    # Copy files
    safe_copy(logo_src, 'media/school/logo.png')
    safe_copy(principal_src, 'media/school/principal.png')
    safe_copy(campus_src, 'media/slider/banner1.png')
    safe_copy(classroom_src, 'media/slider/banner2.png')

    # Copy some backups for other model relations
    safe_copy(campus_src, 'media/events/event1.png')
    safe_copy(classroom_src, 'media/events/event2.png')
    safe_copy(campus_src, 'media/facilities/campus_fac.png')
    safe_copy(classroom_src, 'media/facilities/classroom_fac.png')
    safe_copy(logo_src, 'media/school/favicon.png')


def seed_database():
    print("Seeding database models...")
    
    # 1. School Configuration (Singleton)
    config = SchoolConfig.get_solo()
    config.school_name = "Vyas Public School"
    config.logo = "school/logo.png"
    config.favicon = "school/favicon.png"
    config.email = "admissions@vyaspublicschool.edu.in"
    config.phone = "+91 98765 43210"
    config.address = "Vyas Public School Campus, Sector 12, Dwarka, New Delhi - 110075, India"
    config.map_embed_url = "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3503.7483669149026!2d77.04018317619044!3d28.577322975697666!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x390d1ad39bcce8ab%3A0xe54d9c79cc5cfcb6!2sDwarka%20Sector%2012!5e0!3m2!1sen!2sin!4v1700000000000!5m2!1sen!2sin"
    
    config.principal_name = "Dr. R. K. Vyas"
    config.principal_title = "Principal's Welcome Address"
    config.principal_message = (
        "Dear Students, Parents, and Well-wishers,\n\n"
        "Welcome to Vyas Public School (VPS). We believe that education is not merely the acquisition of academic knowledge, "
        "but a journey of self-discovery, character building, and creative growth. Our objective is to design a nurturing ecosystem "
        "where curiosity is celebrated, and children are encouraged to ask questions.\n\n"
        "At VPS, we emphasize a child-centric, smart-learning curriculum. Our modern smart classrooms, comprehensive "
        "laboratories, and extensive sports infrastructure ensure that every child finds their passion. We inspire students to "
        "strive for academic excellence while remaining grounded in strong ethical values.\n\n"
        "We are proud of our legacy of nurturing young minds. Together with our passionate teaching faculty, we look forward to "
        "helping your child build a bright future.\n\n"
        "Warm regards,\nDr. R. K. Vyas"
    )
    config.principal_photo = "school/principal.png"
    
    config.stat_students = 1250
    config.stat_teachers = 82
    config.stat_labs = 6
    config.stat_experience = 25
    
    config.facebook_url = "https://facebook.com/vyaspublicschool"
    config.twitter_url = "https://x.com/vyaspublicschool"
    config.instagram_url = "https://instagram.com/vyaspublicschool"
    config.youtube_url = "https://youtube.com/vyaspublicschool"
    
    config.vision = "To empower students to become life-long learners, critical thinkers, and productive members of a dynamic global society, rooted in academic excellence and moral values."
    config.mission = "To provide a modern, nurturing environment that fosters scientific inquiry, collaborative learning, physical development, and ethical values through child-centric teaching methodologies."
    config.save()
    print("[OK] Seeded SchoolConfig")

    # 2. Hero Sliders
    HeroSlider.objects.all().delete()
    HeroSlider.objects.create(
        title="Empowering Minds, Shaping Futures",
        subtitle="Dwarka's premier co-educational school offering smart classrooms and holistic curriculum.",
        image="slider/banner1.png",
        action_text="Explore Campus Life",
        action_url="/about/",
        order=1
    )
    HeroSlider.objects.create(
        title="Smart Pedagogy & Advanced Science Labs",
        subtitle="Fostering practical inquiry through modern computer center, science setups, and robotics labs.",
        image="slider/banner2.png",
        action_text="Academics & Labs",
        action_url="/academics/",
        order=2
    )
    print("[OK] Seeded HeroSliders")

    # 3. Facilities
    Facility.objects.all().delete()
    Facility.objects.create(
        title="Modern Smart Classrooms",
        description="Every classroom is equipped with high-speed internet, acoustic insulation, and interactive smartboards, making daily lessons visually rich and engaging.",
        icon_name="chalkboard-teacher",
        image="facilities/classroom_fac.png",
        order=1
    )
    Facility.objects.create(
        title="Advanced Science Labs",
        description="State-of-the-art laboratory infrastructure for Physics, Chemistry, and Biology to facilitate practical experimentation and deep inquiry.",
        icon_name="microscope",
        image="facilities/campus_fac.png",
        order=2
    )
    Facility.objects.create(
        title="Advanced IT & Computer Center",
        description="Air-conditioned laboratory with 40+ computers, digital databases, coding platforms, and robotics kits for developing future ready technological skills.",
        icon_name="desktop",
        image="facilities/classroom_fac.png",
        order=3
    )
    Facility.objects.create(
        title="Comprehensive Resource Library",
        description="Over 12,000 reference books, encyclopedias, children's literature, daily journals, and e-learning terminals with a peaceful reading arena.",
        icon_name="book",
        image="facilities/campus_fac.png",
        order=4
    )
    Facility.objects.create(
        title="Sports Complex & Playgrounds",
        description="Multiple synthetic courts for basketball, volleyball, grass football pitch, and indoor game arenas for table tennis, gymnastics, and chess.",
        icon_name="volleyball",
        image="facilities/campus_fac.png",
        order=5
    )
    Facility.objects.create(
        title="Safe Transport Service",
        description="A fleet of modern GPS-enabled school buses covering major city routes, staffed by trained drivers and supervised female conductors.",
        icon_name="bus",
        image="facilities/campus_fac.png",
        order=6
    )
    print("[OK] Seeded Facilities")

    # 4. Notices
    Notice.objects.all().delete()
    Notice.objects.create(
        title="Summer Vacation Announcement 2026",
        content="The school will remain closed for summer holidays starting from June 10th, 2026, and will reopen on July 16th, 2026. Summer homework worksheets are uploaded on the online student portal.",
        is_urgent=True
    )
    Notice.objects.create(
        title="Registration Open for Session 2026-27",
        content="Registrations are open for Pre-Nursery, Nursery, and Grades I to IX. Registration forms can be collected from the administration helpdesk between 9:00 AM and 1:30 PM.",
        is_urgent=False
    )
    Notice.objects.create(
        title="Annual IT & Robotics Exhibition 2026",
        content="Vyas Science & Coding Fair will take place on July 25th in the main school auditorium. Students from Grades 6 to 12 can submit their science models and software project ideas by July 5th.",
        is_active=True,
        is_urgent=False
    )
    print("[OK] Seeded Notices")

    # 5. Events
    Event.objects.all().delete()
    Event.objects.create(
        title="Annual Athletics Meet 2026",
        description="A grand inter-house track & field event showcasing hurdles, relay races, long jump, and gymnastics. Medals will be awarded by Chief Guest, Olympic sprinter.",
        date=timezone.now().date() + timezone.timedelta(days=20),
        location="Main Sports Ground",
        thumbnail="slider/banner1.png"
    )
    Event.objects.create(
        title="Vyas Coding and Robotics Fair",
        description="Interactive student exhibition showcasing coding games, IoT automation projects, and line-following robots built by the VPS IT Club.",
        date=timezone.now().date() + timezone.timedelta(days=45),
        location="IT Center Lab",
        thumbnail="slider/banner2.png"
    )
    print("[OK] Seeded Events")

    # 6. Teachers
    Teacher.objects.all().delete()
    Teacher.objects.create(
        name="Dr. R. K. Vyas",
        designation="Principal & Founder",
        qualification="Ph.D. Education, M.Sc. Physics, B.Ed.",
        photo="school/principal.png",
        order=1
    )
    Teacher.objects.create(
        name="Mrs. Anita Sharma",
        designation="HOD English Literature",
        qualification="M.A. English, B.Ed. (15 years experience)",
        photo="school/principal.png",
        order=2
    )
    Teacher.objects.create(
        name="Mr. Vikram Adiga",
        designation="TGT Mathematics & Robotics Coordinator",
        qualification="M.Sc. Mathematics, B.Ed. (10 years experience)",
        photo="school/principal.png",
        order=3
    )
    Teacher.objects.create(
        name="Dr. Preeti Verma",
        designation="PGT Chemistry & Lab Superintendent",
        qualification="Ph.D. Chemistry, M.Sc. (12 years experience)",
        photo="school/principal.png",
        order=4
    )
    print("[OK] Seeded Teachers")

    # 7. Gallery Categories & Images
    GalleryCategory.objects.all().delete()
    cat_sports = GalleryCategory.objects.create(name="Sports Meet", slug="sports")
    cat_science = GalleryCategory.objects.create(name="Science & IT", slug="science")
    cat_cultural = GalleryCategory.objects.create(name="Cultural Events", slug="cultural")
    cat_campus = GalleryCategory.objects.create(name="Campus Life", slug="campus")
    
    GalleryImage.objects.all().delete()
    GalleryImage.objects.create(
        category=cat_sports,
        image="slider/banner1.png",
        caption="Annual House Athletics Champions 2026",
        order=1
    )
    GalleryImage.objects.create(
        category=cat_science,
        image="slider/banner2.png",
        caption="Robotics club students showcasing their prototype",
        order=2
    )
    GalleryImage.objects.create(
        category=cat_cultural,
        image="slider/banner2.png",
        caption="Smart Classroom interactive learning session",
        order=3
    )
    GalleryImage.objects.create(
        category=cat_campus,
        image="slider/banner1.png",
        caption="Front view of the main school building campus",
        order=4
    )
    print("[OK] Seeded Gallery Images")


if __name__ == '__main__':
    copy_generated_images()
    seed_database()
    print("All seed data created successfully!")
