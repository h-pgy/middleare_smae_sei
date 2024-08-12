
from .basic import parse_tipo_doc

def parse_link_documento(dados_doc:dict)->dict:

    return {'link' : dados_doc['link_acesso']}


def parse_resumo_documento(dados_doc:dict)->dict:

    parsed = {
            'id' : dados_doc['id_documento'],
            'numero_documento' : dados_doc['documento_formatado'],
            'numero_processo' : dados_doc['procedimento_formatado'],
            'tipo_doc' : parse_tipo_doc(dados_doc['serie']),
            'link_acesso' : dados_doc['link_acesso'],
            'data_criacao' : dados_doc['data'],
            'nome' : dados_doc['nome_arvore']
        }

    return parsed

