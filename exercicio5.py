from exercicio4 import calcular_media

alunos = []

def obter_dados_aluno():
    nome_aluno = input("Informe seu nome completo: ")
    idade_aluno = input("Informe sua idade: ")
    email = input("Informe o email do aluno: ")
    serie = input("Informe a serie do aluno: ")
    nota01 = float(input("Informe a primeira nota do aluno"))
    nota02 = float(input("Informe a segunda nota do aluno"))
    nota03 = float(input("Informe a terceira nota do aluno"))

def cadastrar_aluno(nome, email, serie, nota01=0, nota02=0, nota03=0):
    

    notas = [nota01, nota02, nota03]

    aluno = {
            "nome": nome,
            "email": email,
            "serie": serie,
            "notas": notas,
            "media": calcular_media(notas)
}
    alunos.append(aluno)
    media = calcular_media()
    return aluno

def mostrar_dados_alunos(dados_alunos):
    return print(dados_alunos)

mostrar_dados_alunos(alunos)
