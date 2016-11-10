from django.test import TestCase

# Create your tests here.

from account.models import User
import tools.dealData as fun

u = User(name='lu',password='12312444',email='123')