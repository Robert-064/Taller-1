# API de Reservas de Salas

## Descripción

Este proyecto consiste en el desarrollo de una API sencilla utilizando **FastAPI** para registrar y consultar reservas de salas utilizadas en actividades académicas.

La API recibe y devuelve información en **formato JSON** y utiliza **Pydantic** para validar los datos enviados.

Para esta práctica no se utiliza una base de datos, por lo que las reservas se almacenan temporalmente en memoria dentro del servidor.

---

## Tecnologías utilizadas

- Python
- FastAPI
- Pydantic
- Uvicorn

---

## Modelo de datos

La API utiliza un modelo llamado **Reserva**, el cual contiene los siguientes campos:

- id_reserva
- id_sala
- id_usuario
- fecha
- hora_inicio
- hora_fin
- personas
- estado

---

## Endpoints

### Registrar una reserva

**POST /reservas**

Permite registrar una nueva reserva enviando los datos en formato JSON.
