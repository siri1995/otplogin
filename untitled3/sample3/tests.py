from django.test import TestCase
from django.test import Client
from .forms import *
class Setup_Class(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(first_name="user", last_name="customer",mobile_number=9990002221,phone_number=8885556666,email_id ="user@mp.com")
class Customer_Form_Test(TestCase):
    def test_CustomerForm_valid(self):
        form = CustomerForm(data={'first_name':"user", 'last_name': 'customer',  'mobile_number':9990002221,'phone_number':8885556666,'email_id' :"user@mp.com"})
        self.assertTrue(form.is_valid())
    def test_CustomerForm_invalid(self):
        form = CustomerForm(data={'first_name': "las%1", 'last_name': "Cu tu",'mobile_number':'9999sdfd','phone_number':'999 888','email_id' :""})
        self.assertFalse(form.is_valid())
class Address_Form_Test(TestCase):
    def setUp(self):
        self.Address = Address.objects.create(customer='self.Customer', address1='h.no-212', address2='2nd lane',city='secunderabad', state='telangana', landmark='secondlane',pincode=500024)
        def test_AddressForm_valid(self):
            form = AddressForm(data={'customer':'self.Customer','address1': 'h.no-212','address2': '2nd lane', 'city': 'secunderabad', 'state': 'telangana','landmark': 'secondlane', 'pincode': 500024})
            self.assertTrue(form.is_valid())
        def test_AddressForm_invalid(self):
            form = AddressForm(data={'customer':'','address1': '', 'address2': '', 'city': 'secund@rabad2', 'state': 'telan&ana1','landmark': '', 'pincode': ''})
            self.assertFalse(form.is_valid())


class SignUp_Form_Test(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='harika',password1='hamsini@1',password2='hamsini@1',)
        def test_SignUpForm_valid(self):
            form = SignUpForm(data={'username':'harika','password1':'hamsini@1','password2':'hamsini@1',})
            self.assertTrue(form.is_valid())
        def test_SignUpForm_invalid(self):
            form = SignUpForm(data={'username':'','password1':'','password2':'',})
            self.assertFalse(form.is_valid())
