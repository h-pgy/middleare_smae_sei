
import re

from core.exceptions.processo import DadosForaDoPadrao

def s_n_to_bool(val:str)->bool:

    val = str(val).lower().strip()
    if val == 's':
        return True
    elif val == 'n':
        return False
    #casos em que ja esta booleano
    elif val == 'false':
        return False
    elif val == 'true':
        return True
    else:
        raise ValueError(f'Unexpected S/N val: {val}. Type: {type(val)}')
    

def regex_numero_processo(val:str)->str:

    #o SEMVALOR é porque essa flag existe no ambiente de homolog
    patt = r'\d{4}\.\d{4}\/\d{7}-\d(?=-SEMVALOR)?'
    haystack = str(val)
    needle = re.search(patt, haystack)
    if needle is None:
        raise DadosForaDoPadrao(500, f'Número processo fora do padrão: {val}')
    return needle.group()

def regex_data_dia_mes_ano(val:str)->str:

    patt = r'^\d{2}\/\d{2}\/\d{4}$'
    haystack = str(val)
    needle = re.search(patt, haystack)
    if needle is None:
        raise DadosForaDoPadrao(500, f'Data fora do padrão: {val}')
    return needle.group()


def regex_link_web(val:str)->str:

    patt = r'^https?://(?:www\.)?[^\s/$.?#].[^\s]*$'
    haystack = str(val)
    needle = re.search(patt, haystack)
    if needle is None:
        raise DadosForaDoPadrao(500, f'Link fora do padrão: {val}')
    return needle.group()