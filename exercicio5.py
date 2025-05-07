def cadastrar_aluno(aluno, email, serie):
    alunos = []

    aluno = {
            "aluno": aluno,
            "email": email,
            "serie": serie
}
    alunos.append(aluno)
    return aluno

print(cadastrar_aluno("Matheus", "matheusbastos12123@gmail.com", "2° TB", 10, 10, 10))