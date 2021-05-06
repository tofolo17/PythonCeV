from random import choice

alunos = []

i = 0
while i < 4:
    aluno = str(input("Enter the student's name: "))
    i += 1
    alunos.append(aluno)

print(choice(alunos))
