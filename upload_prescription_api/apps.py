from django.apps import AppConfig


class UploadPrescriptionApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'upload_prescription_api'

    def ready(self):
        import upload_prescription_api.signals
