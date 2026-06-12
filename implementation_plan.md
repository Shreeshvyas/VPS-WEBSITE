# Implementation Plan - Vyas Public School Website

Implement a modern, high-performance website for **Vyas Public School** with a Django administration backend. The website will feature a highly premium user interface (UI) designed according to contemporary web design standards (glassmorphism, interactive states, micro-animations, customizable dark/light theme, and dynamic database-driven components). 

All content (images, slider banners, school configuration details, notices, events, facility details, and teacher profiles) will be fully editable through the Django Admin panel.

---

## User Review Required

> [!IMPORTANT]
> - **Python version**: We will use the system's Python 3.8.10.
> - **SQLite Database**: For ease of deployment and maintenance, we will use SQLite. If a production-grade database like PostgreSQL is needed later, the settings can be easily adjusted.
> - **Content Customization**: An easy-to-use Django Admin interface will be set up with custom forms and listings. We will register all models in the Django admin site and style/configure it to be easy to use.
> - **Image Assets**: We will generate initial high-quality images using the `generate_image` tool (e.g., logo, banner, school building, classroom, computer lab) to make the website feel complete and look professional immediately.

---

## Proposed Changes

We will create a standard Django project and application layout in the workspace `E:\VPHS WEBSITE`.

### 1. Project Setup
- **Virtual Environment**: Create a virtual environment `venv` in the workspace directory.
- **Dependencies**: Install `django`, `pillow` (for handling images), and create a `requirements.txt`.
- **Django Project**: Initialize a project named `vyas_school_project`.
- **Django App**: Create an app named `school`.

### 2. Database Models (`school/models.py`)
- **`SchoolConfig`** (Singleton):
  - `school_name` (char)
  - `logo` (image)
  - `favicon` (image)
  - `primary_color` (color code, optional)
  - `email` (email)
  - `phone` (char)
  - `address` (text)
  - `map_embed_url` (text - for Google Map iframe)
  - `principal_message` (text)
  - `principal_photo` (image)
  - `principal_name` (char)
  - `facebook_url`, `twitter_url`, `instagram_url`, `youtube_url` (urls)
  - `established_year` (int)
- **`HeroSlider`** (Banners):
  - `title` (char)
  - `subtitle` (char)
  - `image` (image)
  - `action_text` (char)
  - `action_url` (char)
  - `order` (int)
  - `is_active` (boolean)
- **`Facility`**:
  - `title` (char)
  - `description` (text)
  - `icon_class` (char - for SVG or FontAwesome icons, e.g., 'lab', 'library', 'sports')
  - `image` (image - backup/detail image)
  - `order` (int)
- **`Notice`** (Notice Board):
  - `title` (char)
  - `content` (text)
  - `attachment` (file - PDF/Docs)
  - `created_at` (datetime)
  - `is_active` (boolean)
  - `is_urgent` (boolean)
- **`Event`**:
  - `title` (char)
  - `description` (text)
  - `date` (date)
  - `location` (char)
  - `thumbnail` (image)
- **`Teacher`** (Staff Directory):
  - `name` (char)
  - `designation` (char)
  - `qualification` (char)
  - `photo` (image)
  - `order` (int)
- **`GalleryCategory`** and **`GalleryImage`**:
  - `category` (foreign key)
  - `image` (image)
  - `caption` (char)
- **`ContactQuery`** (Submitted via contact form):
  - `name` (char)
  - `email` (email)
  - `phone` (char)
  - `subject` (char)
  - `message` (text)
  - `created_at` (datetime)
  - `is_read` (boolean)

### 3. Frontend & Styling
We will build a single, highly refined CSS stylesheet (`school/static/css/style.css`) with:
- CSS variables for coloring, dark-mode adaptations, typography scales.
- Inter and Plus Jakarta Sans fonts.
- A dark/light mode toggle with state saving in `localStorage`.
- Glassmorphism navigation bar (blur filter, semi-transparent background).
- Multi-slide CSS or lightweight JS Hero Slider with animations.
- Interactive counters for stats (animated via JS).
- Notice board scrolling ticker or collapsible accordion.
- Filtering system for gallery (JS-based, zero dependencies).
- AJAX-powered contact form submission with custom toast notifications.

### 4. Admin Customizations (`school/admin.py`)
- Configure lists, search fields, filters, and custom displays.
- Enforce the Singleton pattern for `SchoolConfig` so only one instance exists and users are redirected to edit it directly.
- Add previews for images directly in the list views.

---

## Verification Plan

### Automated Checks
- Run Django migration checks: `python manage.py check`.
- Run database migrations: `python manage.py migrate`.
- Run Django development server: `python manage.py runserver` and inspect logs.

### Manual Verification
- Access the admin panel (`/admin`), create dummy data, upload files/images, and verify that changes reflect in real-time.
- Test responsive layout on mobile, tablet, and desktop viewports.
- Test form validation and successful AJAX submission of the contact form.
- Verify Light/Dark mode transitions.
- Validate lightbox modal and gallery filters.
