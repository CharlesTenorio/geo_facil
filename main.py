from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from localizacao.localizacao_endereco import pegar_endereco
from model.endreco import Endereco

app = FastAPI()

@app.post("/endereco/")
async def get_pontos(endereco_data: Endereco, request: Request):
    endereco_completo = endereco_data.endereco_completo
    latitude, longitude = pegar_endereco(endereco_completo)

    if latitude is None or longitude is None:
        raise HTTPException(status_code=404, detail="Endereço não encontrado")

    result = {"latitude": latitude, "longitude": longitude}

    # You can access headers, cookies, etc., from the request object if needed
    user_agent = request.headers.get("user-agent", "unknown")
    result["user_agent"] = user_agent

    content = jsonable_encoder(result)
    return JSONResponse(content=content)
