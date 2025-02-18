#iteracao com sistema operacional
import os
#criar supprocessos
import subprocess
#o que faz o sys???
import sys


def criarAmbiente(diretorioProjeto):
    if not os.path.exists(diretorioProjeto):
        #os.makedirs(diretorioProjeto)
        print(f'Pasta {diretorioProjeto} nao existe')
        return
    venvPath = os.path.join(diretorioProjeto, '.venv')

    if os.path.exists(venvPath):
        print(f'Pasta {venvPath} existe')
        return
    
    try:
        subprocess.run(['python3', '-m', 'venv', venvPath], check=True)
        #subprocess.run(['venv', venvPath], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Erro ao criar ambiente: {e}')
        return
    
    print(f'Ambiente criado em {venvPath}')


def instalarDependencias(diretorio_projeto, requirements_file):
    if not os.path.exists(requirements_file):
        print(f'Arquivo {requirements_file} nao existe')
        return
    
    venvPath = os.path.join(diretorio_projeto, '.venv','bin','activate')
    if not os.path.exists(venvPath):
        print(f'Arquivo {venvPath} nao existe')
        return
    
    try:
        subprocess.run([venvPath, 'activate'], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Erro ao ativar ambiente virtual: {e}')
        return
    
    try:
        subprocess.run(['pip', 'install', '-r', requirements_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f'Erro ao instalar dependencias: {e}')
        return
    
    print(f'Dependencias instaladas com sucesso')


def main():
    diretorioProjeto = sys.argv[1]
    requirementsFile = os.path.join(diretorioProjeto, 'requirements.txt')
    criarAmbiente(diretorioProjeto)
    instalarDependencias(diretorioProjeto, requirementsFile)


#PS C:\WORKSPACES\python-workspace\ALURA-Scripting-automacao-tarefas> & python .\cria_ambiente.py C:\WORKSPACES\python-workspace\ALURA-Scripting-automacao-tarefas\dash
if __name__ == '__main__':
    main()
