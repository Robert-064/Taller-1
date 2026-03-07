from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class reserva(BaseModel):
    id_reserva : int
    id_sala : int
    id_usuario : int
    fecha : str
    hora_incio : str
    hora_fin : str
    personas: int
    estado: str

reservas = []

@app.get("/")
def inicio():
    return{"mensaje":"API de reservas funcionado"}

@app.post("/reservas")
def crear_reservas(reserva:reserva):
    reservas.append(reserva)
    return {"mensaje":"Reserva registrada con exito"}

@app.get("/reservas")
def mostrar_reservas():
        return reservas

@app.get("/saludo")
def saludo():
    return {"mensaje": "Hola desde otra ruta"}