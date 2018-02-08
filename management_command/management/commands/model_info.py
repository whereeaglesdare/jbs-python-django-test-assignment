from django.core.management.base import BaseCommand
import django.apps


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        for model_instance in django.apps.apps.get_models():
            try:
                table_name = model_instance._meta.db_table
                rows_count = model_instance.objects.count()

            except Exception as e:
                self.stdout.write('error: ' + str(e))
                self.stderr.write('error: ' + str(e))
                continue
            self.stdout.write(self.style.SUCCESS(table_name), ending=' ')
            self.stdout.write(str(rows_count), ending='\n')
