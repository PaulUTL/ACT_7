from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class compra(BaseModel):
    precio: float
    descuento: float

@app.post("/compra")
def procesar_compra(compra: compra):
    if compra.precio < 0:
        raise HTTPException(status_code=400, detail="El precio no puede ser negativo")

    if not 0 <= compra.descuento <= 100:
        raise HTTPException(status_code=400, detail="El descuento debe estar entre 0 y 100")

    subtotal = compra.precio * (1 - compra.descuento / 100)

    total = round(subtotal * 1.16, 2)  # Aplicar IVA del 16% y redondear a 2 decimales
    return {"subtotal": round(subtotal, 2), "total": total}