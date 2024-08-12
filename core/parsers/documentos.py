
def parse_link_documento(dados_doc:dict)->dict:

    return {'link' : dados_doc['link_acesso']}


def parse_resumo_documento(dados_doc:dict)->dict:

    parsed = {
            'id' : dados_doc['id_documento'],
            'doc_num' : dados_doc['documento_formatado'],
            'processo_num' : dados_doc['procedimento_formatado'],
            'link_acesso' : dados_doc['link_acesso'],
            'tipo_doc' : dados_doc['serie'],
            'unidade_elaborado' : dados_doc['unidade_elaboradora'],
            'nome' : dados_doc['nome_arvore'] or ''
        }

    return parsed

