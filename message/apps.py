from django.apps import AppConfig


class MessageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'message'
    verbose_name = 'Administrar Mensagens'

    def ready(self):
        import message.signals
