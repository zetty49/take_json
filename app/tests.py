from django.test import TestCase
from .models import Filters, FiltredData

class YourModelTestCase(TestCase):
    def setUp(self):
        Filters.objects.create(f1='value1', f2='value2', f3='value3', f4='value4')

    def test_filters_attributes(self):
        filters_row = Filters.objects.first()

        self.assertEqual(filters_row.f1, 'value1')
        self.assertEqual(filters_row.f2, 'value2')
        self.assertEqual(filters_row.f3, 'value3')
        self.assertEqual(filters_row.f4, 'value4')

    def test_adding_data_to_db(self):
        filters_row = Filters.objects.create(f1='value1', f2='value2', f3='value3', f4='value4')

        FiltredData.objects.create(
            name='Product1',
            product_code='12345',
            price=10.0,
            image='http://example.com/image1.jpg',
            currency='USD',
            qty=5,
            f1=filters_row.f1,
            f2=filters_row.f2,
            f3=filters_row.f3,
            f4=filters_row.f4,
        )

        self.assertEqual(FiltredData.objects.count(), 1)
        self.assertEqual(FiltredData.objects.first().name, 'Product1')

