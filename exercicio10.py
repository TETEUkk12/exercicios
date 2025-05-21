import json
import os

data = "filmes.json"

def cadastrar_filmes():
    if os.path.exists(data):
        with open(data, "r", encoding="utf-8") as arq_json:
            return json.load(arq_json)
    else:
        return []
    
filmes = cadastrar_filmes()
for filme in filmes:
    print(filme["nome_filme"])