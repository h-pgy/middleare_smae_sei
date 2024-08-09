from fastapi import APIRouter, Depends, HTTPException

from fastapi_pagination import Page, add_pagination, paginate

from typing import List

import core.dao.processos as dao
import core.schemas.processos as schemas
from core.parsers.processos import parse_resumo_processo

app = APIRouter()

@app.get("/link/", response_model=schemas.LinkProcesso, tags=['processo'])
def get_link_processo(num_processo:str):

    link_processo = dao.get_link_processo(num_processo)
    return {'link' : link_processo}

app = add_pagination(app)

@app.get('/resumo', response_model = schemas.ResumoProcesso, tags=['processo'])
def get_resumo_processo(num_processo:str):

    dados_processo = dao.get_resumo_processo(num_processo)
    resumo = parse_resumo_processo(dados_processo)
    return resumo