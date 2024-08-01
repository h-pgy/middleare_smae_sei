from .decorators import set_client, processo_nao_encontrado
from zeep.exceptions import Fault

@processo_nao_encontrado
@set_client
def get_link_processo(client, num_proc:str)->list:

    dados_proc = client('consultar_procedimento', 
                        id_unidade='', 
                        protocolo_procedimento=num_proc, 
                        sin_retornar_assuntos='N', 
                        sin_retornar_interessados='N',
                        sin_retornar_observacoes ='N', 
                        sin_retornar_andamento_geracao='N', 
                        sin_retornar_andamento_conclusao='N', 
                        sin_retornar_ultimo_andamento='N',
                        sin_retornar_unidades_procedimento_aberto='N', 
                        sin_retornar_procedimentos_relacionados='N', 
                        sin_retornar_procedimentos_anexados='N', 
                        array_return=False
                        )
    
    return dados_proc['link_acesso']