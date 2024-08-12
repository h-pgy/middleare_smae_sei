from fastapi import APIRouter, Depends, HTTPException

from fastapi_pagination import Page, add_pagination, paginate

from typing import List

import core.dao.documentos as dao
import core.schemas.documentos as schemas
import core.schemas.basic as basic_schemas
from core.parsers.documentos import parse_link_documento

app = APIRouter()

@app.get("/link/", response_model=basic_schemas.Link, tags=['documento'])
def get_link_doc(num_doc:str):

    dados_doc = dao.get_resumo_documento(num_doc)
    
    return parse_link_documento(dados_doc)


app = add_pagination(app)
