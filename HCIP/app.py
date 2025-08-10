import joblib
import pandas as pd
from fastapi import FastAPI, Request
from pydantic import BaseModel

# Cargar el modelo entrenado
model = joblib.load("modelo_ensemble1.joblib")

# Definir la aplicación FastAPI
app = FastAPI()

# Esquema de entrada con Pydantic
class EntradaDatos(BaseModel):
    vidas: int
    puntaje: int
    tiempo: int
    nivel: int

@app.get("/")
def leer_raiz():
    return {"mensaje": "✅ API funcionando correctamente."}

@app.post("/predecir")
async def predecir_dificultad(datos: EntradaDatos):
    entrada_df = pd.DataFrame([{
        "vidas": datos.vidas,
        "puntaje": datos.puntaje,
        "tiempo": datos.tiempo,
        "nivel": datos.nivel
    }])

    prediccion = model.predict(entrada_df)[0]
    resultado_redondeado = max(0, min(round(prediccion), 2))  # limita entre 0 y 2
    return {"resultado": int(resultado_redondeado)}
