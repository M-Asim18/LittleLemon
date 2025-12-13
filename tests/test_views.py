from django.test import TestCase, Client
from django.urls import reverse  # Standard Django module for finding URLs
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.item1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = MenuItem.objects.create(title="Burger", price=50, inventory=50)

    def test_getall(self):
        # 1. Retrieve data from DB
        items = MenuItem.objects.all()
        # Serialize the data
        serializer = MenuSerializer(items, many=True)
        
        # 2. Make request using reverse()
        # This looks up "name='menu-items'" in your urls.py and calculates the correct path
        response = self.client.get(reverse('menu-items'))
        
        # 3. Check status
        # If this fails with 404, it means the URL is not connected in the project urls.py
        self.assertEqual(response.status_code, 200)

        # 4. Check data
        self.assertEqual(response.data, serializer.data)