from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User  # <--- 1. Import User model

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        
        # 2. Create a standard user for testing
        self.user = User.objects.create_user(username='testUser', password='testPassword')
        
        # 3. Force the test client to "log in" as this user
        self.client.force_login(self.user)

        # Create menu items
        self.item1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = MenuItem.objects.create(title="Burger", price=50, inventory=50)

    def test_getall(self):
        items = MenuItem.objects.all()
        serializer = MenuSerializer(items, many=True)
        
        # Now this request will be "Authenticated" and return 200 OK
        response = self.client.get(reverse('menu-items'))
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)