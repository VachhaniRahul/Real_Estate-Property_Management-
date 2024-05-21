from django.apps import AppConfig


class RealEstateWebConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'real_estate_web'

    def ready(self):
        import real_estate_web.signals