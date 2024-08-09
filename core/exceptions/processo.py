
from fastapi import HTTPException

class ProcessoNaoEncontrado(HTTPException):
    '''Raises quando o processo buscado não foi encontrado'''
    pass

class DadosForaDoPadrao(HTTPException):
    '''Raises quando os dados retornados estão fora do padrão'''