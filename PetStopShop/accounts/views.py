from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.views.generic import CreateView
from django.urls import reverse_lazy
from accounts.form import UserAddressForm
from marketplace.models import Product
from .models import ServiceProvider, User, Vendor, RescueServices, Vet, UserAddress
from .form import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    return render(request, 'accounts/register.html')

# @login_required
# def add_product(request):
#     if request.method == 'POST':
#         add_form = AddNewProduct(request.POST)
#         if add_form.is_valid():
#             add_form.save()
#             messages.success(request, f'Your Product Has Been Added')
#             return redirect('profile')
#     else:
#         add_form = AddNewProduct()
#     context = {
#         'add_form' : add_form
#     }


    # return render(request, 'accounts/add_new_product.html', context)

@login_required
def profile(request):
    if request.user.is_vendor == True:
        c_user = "Vendor"
    elif request.user.is_serviceprovider == True:
        c_user = "Service Provider"
    elif request.user.is_rescue_service == True:
        c_user = "Rescue Servicer"
    elif request.user.is_vet == True:
        c_user = "Professional Vet"
    else:
        c_user = "Normal User"
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if request.user.is_vendor == True:
            form = VendorUpdateForm(request.POST, request.FILES, instance=request.user.vendor)
        elif request.user.is_serviceprovider == True:
            form = SPUpdateForm(request.POST, request.FILES, instance=request.user.serviceprovider)
        elif request.user.is_rescue_service == True:
            form = RSUpdateForm(request.POST, request.FILES, instance=request.user.rescueservices)
        elif request.user.is_vet == True:
            form = VetUpdateForm(request.POST, request.FILES, instance=request.user.vet)
        else:
            form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and form.is_valid():
            u_form.save()
            form.save()
            messages.success(request, f'Your Profile Information Has Been Updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        if request.user.is_vendor == True:
            form = VendorUpdateForm(instance=request.user.vendor)
        elif request.user.is_serviceprovider == True:
            form = SPUpdateForm(instance=request.user.serviceprovider)
        elif request.user.is_rescue_service == True:
            form = RSUpdateForm(instance=request.user.rescueservices)
        elif request.user.is_vet == True:
            form = VetUpdateForm(instance=request.user.vet)
        else:
            form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'form': form,
        'c_user':c_user
    }
    return render(request, 'accounts/profile.html', context)


class user_register(CreateView):
    model = User
    form_class = UserSignUpForm
    template_name = 'accounts/user_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'user'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class vendor_register(CreateView):
    model = Vendor
    form_class = VendorSignUpForm
    template_name = 'accounts/vendor_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'vendor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class service_provider(CreateView):
    model = ServiceProvider
    form_class = ServiceSignUpForm
    template_name = 'accounts/service_provider.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'service_provider'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return render(self.request, 'accounts/awaiting_confirmation.html')

class rescue_provider(CreateView):
    model = RescueServices
    form_class = RescueSignUpForm
    template_name = 'accounts/rescue.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'rescue_provider'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return render(self.request, 'accounts/awaiting_confirmation.html')

class vets(CreateView):
    model = Vet
    form_class = VetsSignUpForm
    template_name = 'accounts/vets.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'vet'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return render(self.request, 'accounts/awaiting_confirmation.html')


class add_product(CreateView):
    model = Product
    form_class = AddNewProduct
    template_name = 'accounts/add_new_product.html'
    success_url = reverse_lazy('marketplace')
    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)

def awaiting_confirmation(request):
    return render(request, 'blog/awaiting_confirmation.html')


def getServiceProviders(request):
    if request.method == 'GET':
        service_providers = ServiceProvider.objects.filter(is_approved=True).all()

        data = []
        for provider in service_providers:
            try:
                profile = Profile.objects.filter(user=provider.user).first()
                obj = {
                    "name" : f"{provider.user.first_name} {provider.user.last_name}",
                    "service_info" : provider.service_information,
                    "phone_num" : provider.user.phone_number,
                    "image" : profile.image,
                    "email" : provider.user.email
                }

                data.append(obj)
            except:
                pass

        context = {
            "service_providers" : data
        }
        return render(request,'accounts/list_service.html',context)

def getRescueProviders(request):
    if request.method == 'GET':
        rescue_providers = RescueServices.objects.filter(is_approved=True).all()

        data = []
        for provider in rescue_providers:
            try:
                profile = Profile.objects.filter(user=provider.user).first()
                obj = {
                    "name" : f"{provider.user.first_name} {provider.user.last_name}",
                    "service_info" : provider.service_information,
                    "phone_num" : provider.user.phone_number,
                    "image" : profile.image,
                    "email" : provider.user.email
                }

                data.append(obj)
            except:
                pass

        context = {
            "rescue_providers" : data
        }
        return render(request,'accounts/rescue_list.html',context)

def getVets(request):
    if request.method == 'GET':
        vets = Vet.objects.filter(is_approved=True).all()

        data = []
        for vet in vets:
            try:
                profile = Profile.objects.filter(user=vet.user).first()
                obj = {
                    "name" : f"{vet.user.first_name} {vet.user.last_name}",
                    "experience" : vet.experience,
                    "phone_num" : vet.user.phone_number,
                    "image" : profile.image,
                    "email" : vet.user.email
                }

                data.append(obj)
            except:
                pass

        context = {
            "vets" : data
        }
        return render(request,'accounts/vets_list.html',context)
