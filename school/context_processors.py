from .models import SchoolConfig

def school_settings(request):
    return {
        'school_config': SchoolConfig.get_solo()
    }
