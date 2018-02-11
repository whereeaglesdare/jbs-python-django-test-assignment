from django.apps import AppConfig


class DbLoggerConfig(AppConfig):
    name = 'db_logger'

    def ready(self):
        import db_logger.signals.signals