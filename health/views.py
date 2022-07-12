from pydoc import describe
from re import template
#from cairo import Status
import django
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template import loader
from health.models import service
from health.models import client
from health.models import booking
import datetime
from django.db.models import Q

def client_view(self): 
    client_name = self.POST.get('name')
    client_lastname = self.POST.get('lastname')
    client_email = self.POST.get('email')
    client_phone = self.POST.get('phone')

    if (client_name is not None and client_lastname is not None or client_email is not None and client_phone is not None):
        client_model = client(
            name = client_name,
            lastname = client_lastname,
            email = client_email,
            phone = client_phone
        )
        client_model.save()
    
        print(f"""Client Detail:
                Name: {client_model.name}
                Last Name: {client_model.lastname}
                Email: {client_model.email}
                Phone: {client_model.phone}""")

    client_dic ={"clients":client.objects.all()}
    client_template = loader.get_template("client.html")
    client_render = client_template.render(client_dic)
    return HttpResponse(client_render)

def service_view(self):
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
                Service Status: {service_status}""")
        
    service_dic ={"services": service.objects.all()}
    service_template = loader.get_template('service.html')
    service_render = service_template.render(service_dic)

    return HttpResponse(service_render)

def booking_view(self):
    id_client = self.POST.get("client")
    id_service = self.POST.get("service")
    note = self.POST.get("note")
  
    if (id_client is not None and id_client != "-1" and id_service is not None and id_service != "-1" and note is not None):
        booking_model = booking(
            id_client = id_client,
            id_service = id_service,
            creation = datetime.datetime.now(),
            note = note
        )
        booking_model.save()
        print(f"""Booking Detail:
                Client Seleted: {booking_model.id_client}
                Service Selected: {booking_model.id_service}
                Creation: {booking_model.creation}
                Note: {booking_model.note}""")

    booking_dic={
        "bookings": booking.objects.all(),
        "clients": client.objects.all(),
        "services": service.objects.filter(status=True)}

    booking_template = loader.get_template('booking.html')
    booking_render = booking_template.render(booking_dic)
    return HttpResponse(booking_render)

def search(self):
    value = self.POST.get("value")   
    if value is None: 
        return redirect('/booking')
    result_search=booking.objects.filter(Q(note__contains=value) | Q(creation__contains=value) | Q(iduser__contains=value) | Q(idservice__contains=value))
    for result in result_search:
        print(f"""Booking Search Detail:
                        Id: {result.id}
                        IdUser:{result.iduser}
                        IdService:{result.idservice}
                        Creation:{result.creation}
                        Note:{result.note}
                """)
    result_dic={"value":value,"search_result":result_search}
    template = loader.get_template('search.html')
    render = template.render(result_dic)
    return HttpResponse(render)