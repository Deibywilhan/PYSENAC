alunos={}
alunos[1]={"Nome":"Ana ","Turma":"201","Notas":[7.5,8.6,9.2]}
alunos[2]={"Nome":"João ","Turma":"201","Notas":[6.5,7.6,5.2]}
alunos[3]={"Nome":"Maria ","Turma":"201","Notas":[5.5,9.6,3.2]}

for id_aluno, info in alunos.items():
    notas =info["Notas"]
    media=sum(notas)/len(notas)
    info["media"]=round(media,2)

print(f'{alunos}')