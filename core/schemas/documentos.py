from pydantic import BaseModel, validator
from typing import Literal

from .basic import TipoDocumento
from .validators import (regex_numero_processo, regex_data_dia_mes_ano, regex_numero_doc, 
                         regex_link_web, none_to_string)

class ResumoDocumento(BaseModel):

    id : str
    numero_documento : str
    numero_processo : str
    tipo_doc : TipoDocumento
    data_criacao : str
    link_acesso : str
    nome : str

    #validators

    _numero_documento = validator('numero_documento',
                                  allow_reuse=True, pre=True, always=True)(regex_numero_doc)
    _numero_processo = validator('numero_processo', 
                            allow_reuse=True, pre=True, always=True)(regex_numero_processo)
    _link_acesso = validator('link_acesso', 
                            allow_reuse=True, pre=True, always=True)(regex_link_web)
    _data_criacao = validator('data_criacao', 
                            allow_reuse=True, pre=True, always=True)(regex_data_dia_mes_ano)
    _nome = validator('nome', 
                            allow_reuse=True, pre=True, always=True)(none_to_string)
