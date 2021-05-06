from random import shuffle

alunos = []

i = 0
while i < 4:
    aluno = str(input("Enter the student's name: "))
    i += 1
    alunos.append(aluno)
shuffle(alunos)

print(alunos)
