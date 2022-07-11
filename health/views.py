from pydoc import describe
from re import template
from cairo import Status
import django
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from health.models import service
from health.models import user

# Create your views here.

def set_service(self):
    service_name = self.POST.get('name')
    service_description = self.POST.get('description')
    service_status = self.POST.get('status')

    if (service_name is not None and service_description is not None or service_status is not None):
        service_model = service(
            name = service_name,
            description = service_description,
            status = True if service_status == 'on' else False
        )
        service_model.save()
    
        print(f"""Service Detail:
                Name: {service_model.name}
                Description: {service_model.description}
                Status: {service_model.status}
        """)
        
    #service_dic ={"services": service.objects.filter(status=True)}
    service_dic ={"services": service.objects.all()}

    template = loader.get_template('service_template.html')
    render = template.render(service_dic)

    return HttpResponse(render)

def set_user(self): 
    user_name = self.POST.get('name')
    user_lastname = self.POST.get('lastname')
    user_email = self.POST.get('email')
    user_phone = self.POST.get('phone')

    if (user_name is not None and user_lastname is not None or user_email is not None and user_phone is not None):
        user_model = user(
            name = user_name,
            last_name = user_lastname,
            email = user_email,
            phone = user_phone
        )
        user_model.save()
    
        print(f"""User Detail:
                Name: {user_model.name}
                Last Name: {user_model.last_name}
                Email: {user_model.email}
                Phone: {user_model.phone}
        """)

    user_dic ={"users":user.objects.all()}
    template = loader.get_template('user_template.html')
    render = template.render(user_dic)
    return HttpResponse(render)

def set_booking(self):

    booking_dic={"bookings":0}
    template = loader.get_template('booking_template.html')
    render = template.render(booking_dic)
    return HttpResponse(render)