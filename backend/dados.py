import os

ARQUIVO_EVENTOS = 'eventos.csv'
CAMPOS_EVENTOS = ['id', 'nome', 'data', 'orcamento', 'tipo', 'local']

def _inicializar_arquivo():
    if not os.path.exists(ARQUIVO_EVENTOS):
        with open(ARQUIVO_EVENTOS, 'w', encoding='utf-8') as f:
            cabecalho = ",".join(CAMPOS_EVENTOS)
            f.write(cabecalho + "\n")

def gerar_novo_id():
    eventos = ler_eventos()
    if not eventos:
        return 1

    ultimo_evento = eventos[-1]
    return int(ultimo_evento['id']) + 1

def ler_eventos():
    _inicializar_arquivo()
    lista_eventos = []
    
    with open(ARQUIVO_EVENTOS, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
        
        if len(linhas) < 2:
            return []
        for linha in linhas[1:]:
            linha = linha.strip()
            if not linha: continue
            dados = linha.split(',')
            evento = {
                'id': int(dados[0]),
                'nome': dados[1],
                'data': dados[2],
                'orcamento': float(dados[3]),
                'tipo': dados[4],
                'local': dados[5]
            }
            lista_eventos.append(evento)
            
    return lista_eventos

def salvar_evento(evento):
    _inicializar_arquivo()
    nome = str(evento['nome']).replace(',', ' ')
    tipo = str(evento['tipo']).replace(',', ' ')
    local = str(evento['local']).replace(',', ' ')
    nova_linha = f"{evento['id']},{nome},{evento['data']},{evento['orcamento']},{tipo},{local}\n"
    with open(ARQUIVO_EVENTOS, 'a', encoding='utf-8') as f:
        f.write(nova_linha)
