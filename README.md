# Project Health Up

En este proyecto podrán encontrar un app de reservas de turnos para el gimnasio Health UP.

## Authors

- [@jhosymijares](https://www.github.com/jhosymijares)

## Demo

Para ejecutar esta app debe seguir los siguientes pasos:

1. Clonar el repositorio a tu máquina local
2. Abrir el proyecto desde Visual Studio Code
3. Abrir la terminal desde IDE y ejecutar el siguiente comando

```bash
python manage.py runserver
```

4. Ir al navegador y abrir el siguente enlace: [App: Healp Up](http://localhost:8000/)

5. Encontrarás 3 vistas en la web de la app (ver en la sección Features)

## Features

- Ingresar al modelo de [Client Detail](http://localhost:8000/client)
 Modelo con la lista de clientes y sus datos personales para registrar la reserva posteriormente, en esta sección se pueden agregar registros.

-  Ingresar al modelo de [Service Detail](http://localhost:8000/service) 
Modelo con la lista de servicios para las reservas, en esta seción se pueden agregar registros de clientes por los momentos no cuenta con validaciones.

- Ingresar al modelo de [Booking Detail](http://localhost:8000/booking) 
Modelo con las lista de reservas realizadas por el usuario administrador, para los servicios disponibles en el gimnasio, en esta sección se pueden agregar y eliminar registros.

Desde este modelo también podrás realizar búsquedas de las reservas [Booking Detail](http://localhost:8000/booking) por alguno de los siguientes campos: 'Creation Date' and 'Note'. Este buscador lo podrá encontrar desde cualquier ubicación en la app.

## Healp Up


