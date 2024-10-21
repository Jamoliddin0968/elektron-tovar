from django.core.management.base import BaseCommand

from apps.products.models import Category, Product


class Command(BaseCommand):
    help = 'Kategoriyalar va mahsulotlar qo\'shadi'

    def handle(self, *args, **kwargs):
        # 5 Kategoriya
        category_data = [
            {'name': 'Elektronika', 'description': 'Elektron qurilmalar va gadjetlar'},
            {'name': 'Maishiy texnika', 'description': 'Uyda ishlatiladigan texnikalar'},
            {'name': 'Kitoblar', 'description': 'Turli xil kitoblar va adabiyotlar'},
            {'name': 'Sport anjomlari',
                'description': 'Sport bilan shug\'ullanish uchun anjomlar'},
            {'name': 'Oziq-ovqat', 'description': 'Oziq-ovqat mahsulotlari va ichimliklar'},
        ]

        for category in category_data:
            obj, created = Category.objects.get_or_create(
                name=category['name'],
                defaults={'description': category['description']}
            )
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f"Kategoriya qo'shildi: {obj.name}"))
            else:
                self.stdout.write(self.style.WARNING(
                    f"Kategoriya allaqachon mavjud: {obj.name}"))

        # 20 Mahsulot
        product_data = [
            {'name': 'Smartfon', 'price': 900.00,
                'description': 'Eng so\'nggi model smartfon', 'category_name': 'Elektronika'},
            {'name': 'Televizor', 'price': 700.00,
                'description': 'Yuqori sifatli tasvirli televizor', 'category_name': 'Elektronika'},
            {'name': 'Noutbuk', 'price': 1200.00,
                'description': 'Yuqori quvvatli noutbuk', 'category_name': 'Elektronika'},
            {'name': 'Naushnik', 'price': 100.00,
                'description': 'Simli naushnik', 'category_name': 'Elektronika'},
            {'name': 'Uyali telefon zaryadkasi', 'price': 25.00,
                'description': 'Tezkor zaryadlash moslamasi', 'category_name': 'Elektronika'},

            {'name': 'Kir yuvish mashinasi', 'price': 500.00,
                'description': 'Avtomatik kir yuvish mashinasi', 'category_name': 'Maishiy texnika'},
            {'name': 'Muzlatgich', 'price': 800.00,
                'description': 'Katta hajmli muzlatgich', 'category_name': 'Maishiy texnika'},
            {'name': 'Changyutgich', 'price': 150.00,
                'description': 'Changyutish uchun texnika', 'category_name': 'Maishiy texnika'},
            {'name': 'Oshxona mikseri', 'price': 60.00,
                'description': 'Ko\'p funktsiyali oshxona mikseri', 'category_name': 'Maishiy texnika'},
            {'name': 'Mikroto\'lqinli pech', 'price': 120.00,
                'description': 'Yemak qizdirish uchun pech', 'category_name': 'Maishiy texnika'},

            {'name': 'Roman kitobi', 'price': 15.00,
                'description': 'Mashhur roman', 'category_name': 'Kitoblar'},
            {'name': 'Matematika darsligi', 'price': 10.00,
                'description': 'O\'rta maktab darsligi', 'category_name': 'Kitoblar'},
            {'name': 'Tarix kitobi', 'price': 12.00,
                'description': 'Tarixiy kitob', 'category_name': 'Kitoblar'},
            {'name': 'Ilmiy-fantastik kitob', 'price': 18.00,
                'description': 'Ilmiy-fantastik janrdagi kitob', 'category_name': 'Kitoblar'},
            {'name': 'Shaxsiy rivojlanish kitobi', 'price': 20.00,
                'description': 'O\'z-o\'zini rivojlantirish bo\'yicha qo\'llanma', 'category_name': 'Kitoblar'},

            {'name': 'Futbol to\'pi', 'price': 25.00,
                'description': 'Professional futbol to\'pi', 'category_name': 'Sport anjomlari'},
            {'name': 'Tennis raketkasi', 'price': 60.00,
                'description': 'Tennis o\'ynash uchun raketka', 'category_name': 'Sport anjomlari'},
            {'name': 'Velosiped', 'price': 300.00,
                'description': 'Oila uchun velosiped', 'category_name': 'Sport anjomlari'},
            {'name': 'Trenajyor', 'price': 1000.00,
                'description': 'Uy sharoitida foydalanish uchun trenajyor', 'category_name': 'Sport anjomlari'},
            {'name': 'Sport kiyimlari', 'price': 50.00,
                'description': 'Sport uchun maxsus kiyimlar', 'category_name': 'Sport anjomlari'},
        ]

        for product in product_data:
            try:
                category = Category.objects.get(name=product['category_name'])
                obj, created = Product.objects.get_or_create(
                    name=product['name'],
                    defaults={
                        'price': product['price'],
                        'description': product['description'],
                        'category': category
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(
                        f"Mahsulot qo'shildi: {obj.name}"))
                else:
                    self.stdout.write(self.style.WARNING(
                        f"Mahsulot allaqachon mavjud: {obj.name}"))
            except Category.DoesNotExist:
                self.stdout.write(self.style.ERROR(
                    f"Kategoriya topilmadi: {product['category_name']}"))
