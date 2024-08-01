
from fastapi import APIRouter, Depends, HTTPException

from fastapi_pagination import Page, add_pagination, paginate

from typing import List

import core.dao.basic as dao
import core.schemas.basic as schemas


app = APIRouter()

@app.get("/unidades", response_model=Page[schemas.Unidade], tags=['categorias'])
def get_unidades():

    unidades = dao.lst_unidades()
    return paginate(unidades)

@app.get("/processos/tipos", response_model=Page[schemas.TipoProcesso], tags=['categorias', 'processo'])
def get_tipos_processo():

    tipos = dao.lst_tipos_processo()
    return paginate(tipos)

@app.get("/documentos/tipos", response_model=Page[schemas.TipoDocumento], tags=['categorias'])
def get_tipos_doc():

    tipos = dao.lst_tipos_documento()
    return paginate(tipos)

app = add_pagination(app)


