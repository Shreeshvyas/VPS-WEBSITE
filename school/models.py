from django.db import models

class SchoolConfig(models.Model):
    school_name = models.CharField(max_length=200, default="Vyas Public School")
    logo = models.ImageField(upload_to="school/", blank=True, null=True, help_text="Best size: 200x60px (PNG with transparency)")
    favicon = models.ImageField(upload_to="school/", blank=True, null=True)
    email = models.EmailField(default="info@vyaspublicschool.com")
    phone = models.CharField(max_length=50, default="+91 98765 43210")
    address = models.TextField(default="Vyas Public School, Campus Area, City, State, India")
    map_embed_url = models.TextField(
        blank=True, 
        null=True, 
        help_text="Google Maps Embed iframe src URL. Extract the src attribute from the Google Maps share embed code."
    )
    
    # Principal's Section
    principal_name = models.CharField(max_length=100, default="Dr. R. K. Vyas")
    principal_title = models.CharField(max_length=100, default="Principal's Message")
    principal_message = models.TextField(
        default="Welcome to Vyas Public School. We are dedicated to fostering academic excellence and character building. Our goal is to prepare students to face global challenges with confidence and integrity."
    )
    principal_photo = models.ImageField(upload_to="school/", blank=True, null=True)
    
    # School Stats
    stat_students = models.IntegerField(default=1200, verbose_name="Number of Students")
    stat_teachers = models.IntegerField(default=80, verbose_name="Number of Teachers")
    stat_labs = models.IntegerField(default=5, verbose_name="Number of Labs")
    stat_experience = models.IntegerField(default=25, verbose_name="Years of Excellence")
    
    # Social Media Links
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    
    # Vision & Mission
    vision = models.TextField(default="To empower students to become life-long learners and productive members of a dynamic global society.")
    mission = models.TextField(default="To provide a nurturing environment that fosters academic excellence, innovation, collaborative learning, and ethical values.")

    class Meta:
        verbose_name = "School Configuration"
        verbose_name_plural = "School Configuration"

    def save(self, *args, **kwargs):
        self.id = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.school_name

    @classmethod
    def get_solo(cls):
        obj, created = cls.objects.get_or_create(id=1)
        return obj


class HeroSlider(models.Model):
    title = models.CharField(max_length=200, help_text="Primary heading on the slider")
    subtitle = models.CharField(max_length=200, blank=True, null=True, help_text="Secondary descriptive subtitle")
    image = models.ImageField(upload_to="slider/", help_text="High resolution background image (Recommended 1920x800px)")
    action_text = models.CharField(max_length=50, default="Explore More", help_text="Text shown on the call-to-action button")
    action_url = models.CharField(max_length=200, default="#", help_text="URL or section ID that button points to")
    order = models.IntegerField(default=0, help_text="Determines the display order (lower values show first)")
    is_active = models.BooleanField(default=True, help_text="Toggle visibility on website")

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Hero Slider"
        verbose_name_plural = "Hero Sliders"

    def __str__(self):
        return self.title


class Facility(models.Model):
    ICON_CHOICES = [
        ('book', 'Library / Reading Room'),
        ('microscope', 'Science Labs (Physics/Chemistry/Biology)'),
        ('desktop', 'Computer & IT Lab'),
        ('volleyball', 'Sports Complex & Playground'),
        ('bus', 'Safe School Transport'),
        ('music', 'Music, Dance & Art Studio'),
        ('heartbeat', 'Infirmary / Health Clinic'),
        ('chalkboard-teacher', 'Smart Classrooms'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_name = models.CharField(
        max_length=50, 
        choices=ICON_CHOICES, 
        default='book', 
        help_text="Select a pre-configured icon to represent this facility"
    )
    image = models.ImageField(upload_to="facilities/", blank=True, null=True, help_text="Detail photo of the facility")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "School Facility"
        verbose_name_plural = "School Facilities"

    def __str__(self):
        return self.title


class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True, null=True, help_text="Notice content details")
    attachment = models.FileField(upload_to="notices/", blank=True, null=True, help_text="Optional PDF or document download")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_urgent = models.BooleanField(default=False, help_text="Displays with an urgent badge and floats to top")

    class Meta:
        ordering = ['-is_urgent', '-created_at']
        verbose_name = "Notice / Announcement"
        verbose_name_plural = "Notices & Announcements"

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField(help_text="Date of the event")
    location = models.CharField(max_length=200, default="School Campus")
    thumbnail = models.ImageField(upload_to="events/", help_text="Event cover photo")

    class Meta:
        ordering = ['-date']
        verbose_name = "School Event"
        verbose_name_plural = "School Events"

    def __str__(self):
        return self.title


class GalleryCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True, help_text="Used for URL filtering (e.g. 'sports-day')")

    class Meta:
        verbose_name = "Gallery Category"
        verbose_name_plural = "Gallery Categories"

    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="gallery/", help_text="Upload high resolution photo")
    caption = models.CharField(max_length=200, blank=True, null=True, help_text="Brief description/tag for the photo")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"

    def __str__(self):
        return self.caption or f"Gallery Image {self.id} in {self.category.name}"


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, help_text="e.g. TGT Science, HOD Mathematics, Principal")
    qualification = models.CharField(max_length=150, help_text="e.g. M.Sc. B.Ed.")
    photo = models.ImageField(upload_to="teachers/", help_text="Professional headshot of the teacher")
    order = models.IntegerField(default=0, help_text="Order in staff list")

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Teacher / Staff Member"
        verbose_name_plural = "Teachers & Staff"

    def __str__(self):
        return f"{self.name} ({self.designation})"


class ContactQuery(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
