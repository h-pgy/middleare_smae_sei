from pydantic import BaseModel, validator
from typing import Literal, List

from .validators import (s_n_to_bool, regex_numero_processo, regex_data_dia_mes_ano, 
                         regex_link_web)


class LinkProcesso(BaseModel):

    link : str

    #validators
    _link_processo = validator('link',
                               allow_reuse=True, pre=True, always=True)(regex_link_web)

class Assunto(BaseModel):

    codigo : str
    descricao : str

class ResumoProcesso(BaseModel):

    numero_processo : str
    especificacao : str
    data_autuacao : str
    link : str
    assuntos : List[Assunto]

    #validators

    _numero_processo = validator('numero_processo', 
                                   allow_reuse=True, pre=True, always=True)(regex_numero_processo)

    _data_autuacao = validator('data_autuacao',
                                allow_reuse=True, pre=True, always=True)(regex_data_dia_mes_ano)
    _link = validator('link',
                    allow_reuse=True, pre=True, always=True)(regex_link_web)
    

