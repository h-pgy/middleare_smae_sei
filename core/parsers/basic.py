from .utils import s_n_to_bool

def parse_tipo_unidade(unidade:dict)->dict:

    mapper = {
        'sin_protocolo' : 'protocolo',
        'sin_arquivamento' : 'arquivo',
        'sin_ouvidoria' : 'ouvidoria',
    }

    for key, val in mapper.items():

        if s_n_to_bool(unidade[key]):
            return val
    return 'regular'

def parser_unidade(unidade:dict)->dict:

    tipo_unidade = parse_tipo_unidade(unidade)

    parsed = {
        'id_unidade' : unidade['id_unidade'],
        'sigla' : unidade['sigla'],
        'descricao' : unidade['descricao'],
        'tipo_unidade' : tipo_unidade
    }

    return parsed