from django.core.management.base import BaseCommand

from apps.warehouses.models import Warehouse


class Command(BaseCommand):
    help = 'Kategoriyalar, mahsulotlar va omborlar qo\'shadi'

    def handle(self, *args, **kwargs):
        # Omborlarni qo'shish
        warehouse_data = [
            {'name': 'Markaziy ombor', 'description': 'Shahar markazidagi katta ombor'},
            {'name': 'Sharqiy ombor', 'description': 'Sharqiy hududlar uchun ombor'},
            {'name': 'G\'arbiy ombor', 'description': 'G\'arbiy hududlar uchun ombor'},
            {'name': 'Janubiy ombor', 'description': 'Janubdagi kichik ombor'},
            {'name': 'Shimoliy ombor', 'description': 'Shimoliy viloyatlar uchun ombor'},
        ]

        for warehouse in warehouse_data:
            obj, created = Warehouse.objects.get_or_create(
                name=warehouse['name'],
                defaults={'description': warehouse['description']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Ombor qo'shildi: {obj.name}"))
            else:
                self.stdout.write(self.style.WARNING(
                    f"Ombor allaqachon mavjud: {obj.name}"))

        # Oldingi kategoriya va mahsulot qo'shish qismi bu yerda qoladi
        # ...
