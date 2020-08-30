from django.test import TestCase
from .models import flowers
# Create your tests here.
class FlowersModelTest(TestCase):
    def setUpTestData(cls):
        flowers.objects.create(name='rose')
        flowers.object.create(description='rose is a flower')
    
    def test_title_content(self):
        flw = flowers.objects.get(id=1)
        expected_object_name = f'{flowers.name}'
        self.assertEquals(expected_object_name, 'first flower')
