import os

# Etapa 1: git add .
os.system("git add .")

# Etapa 2: pedir mensagem do commit
mensagem = input("Digite a mensagem do commit: ")

# Etapa 3: git commit
os.system(f'git commit -m "{mensagem}"')

# Etapa 4: git push
os.system("git push")
