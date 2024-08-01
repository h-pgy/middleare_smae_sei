from fastapi import APIRouter, Depends, HTTPException

from fastapi_pagination import Page, add_pagination, paginate

from typing import List

import core.dao.processos as dao
import core.schemas.processos as schemas

from fastapi.responses import PlainTextResponse

app = APIRouter()

@app.get("/link/", response_class=PlainTextResponse, tags=['processo'])
def get_link_processo(num_processo:str):

    link_processo = dao.get_link_processo(num_processo)
    return link_processo

app = add_pagination(app)