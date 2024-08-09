

def parse_resumo_processo(dados_processo:dict)->dict:

    parsed = {
    'numero_processo' : dados_processo['procedimento_formatado'],
    'especificacao' : dados_processo['especificacao'],
    'data_autuacao' : dados_processo['data_autuacao'],
    'link' : dados_processo['link_acesso'],
    'assuntos' : [{'codigo' : assunto['CodigoEstruturado'], 'descricao' : assunto['Descricao']}
                  for assunto in dados_processo['assuntos']]
    }

    return parsed
