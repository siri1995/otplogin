from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from .forms import *
from rest_framework import viewsets
from .serializers import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
import http.client
import random

conn = http.client.HTTPConnection("2factor.in")
randomOTP = random.randint(1111,9999)
conn.request("GET", "https://2factor.in/API/R1/?module=SMS_OTP&apikey=7ef37c63-a1dd-11e7-94da-0200cd936042&to=&otpvalue="+str(randomOTP))
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CustomerList(ListView):
    model = Customer


class CustomerCreate(CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'mobile_number', 'phone_number', 'email_id']


class CustomerAddressCreate(CreateView):
    model = Customer
    fields = ['first_name', 'last_name', 'mobile_number', 'phone_number', 'email_id']
    success_url = reverse_lazy('customer-list')

    def get_context_data(self, **kwargs):
        data = super(CustomerAddressCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['address'] = AddressFormSet(self.request.POST)
        else:
            data['address'] = AddressFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        address = context['address']
        with transaction.atomic():
            self.object = form.save()

            if address.is_valid():
                address.instance = self.object
                address.save()
        return super(CustomerAddressCreate, self).form_valid(form)


class CustomerUpdate(UpdateView):
    model = Customer
    success_url = '/'
    fields = ['first_name', 'last_name',  'mobile_number', 'phone_number', 'email_id']


class CustomerAddressUpdate(UpdateView):
    model = Customer
    fields = ['first_name', 'last_name',  'mobile_number', 'phone_number', 'email_id']
    success_url = reverse_lazy('customer-list')

    def get_context_data(self, **kwargs):
        data = super(CustomerAddressUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['address'] = AddressFormSet(self.request.POST, instance=self.object)
        else:
            data['address'] = AddressFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        address = context['address']
        with transaction.atomic():
            self.object = form.save()

            if address.is_valid():
                address.instance = self.object
                address.save()
        return super(CustomerAddressUpdate, self).form_valid(form)


class CustomerDelete(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer-list')





### Login process


@login_required
def customer_list(request):
    return render(request, 'sample3/customer_list.html')

def signup(request):
    if request.method == 'POST':
        #text = request.POST['text']
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.contact_number= form.cleaned_data.get('contact_number')
            user.profile.iam_name = form.cleaned_data.get('iam_name')
            username = form.cleaned_data.get('username')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



