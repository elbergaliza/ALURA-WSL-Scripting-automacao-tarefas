#Começamos importando as bibliotecas necessárias para interagir com o sistema operacional e executar comandos no terminal. 
# Utilizamos as bibliotecas os, subprocess e sys.
import os
import subprocess
import sys


#Na sequência, definimos as funções para criação do ambiente virtual e instalação das dependências requeridas para execução do projeto.

# Recommended approach using venv (no external dependencies)
def criar_ambiente_virtual(diretorio_projeto):
    '''
    A função criar_ambiente_virtual recebe um parâmetro: o diretório do projeto.
    O primeiro passo é verificar se o diretório do projeto existe. Caso não exista, a função exibe uma mensagem de erro e retorna.
    Em seguida, a função monta o caminho do ambiente virtual e verifica se ele já existe. Caso exista, a função exibe uma mensagem de erro e retorna.
    Por fim, a função executa o comando virtualenv para criar o ambiente virtual.
    '''

    if not os.path.exists(diretorio_projeto):
        #print(f"O diretório '{diretorio_projeto}' não existe.")
        raise FileNotFoundError(f"O diretório '{diretorio_projeto}' não existe.")
        return

    venv_path = os.path.join(diretorio_projeto, '.venv')
    
    if os.path.exists(venv_path):
        print("O ambiente virtual já existe.")
        return
    
    try:
        subprocess.run([sys.executable, '-m', 'venv', venv_path], check=True)
        print("Ambiente virtual criado com sucesso.")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Erro ao CRIAR o ambiente virtual: {e}")



def ativar_ambiente_virtual(diretorio_projeto):
    '''
    A função ativar_ambiente_virtual recebe um parâmetro: o diretório do projeto.
    O primeiro passo é montar o caminho do arquivo activate dentro do ambiente virtual.
    Em seguida, a função executa o comando source para ativar o ambiente virtual.
    '''

    venv_path = os.path.join(diretorio_projeto, '.venv', 'bin', 'activate')

    try:
        # Use string command instead of list for shell commands
        subprocess.run(f'. {venv_path}', check=True, shell=True)
        print("Ambiente virtual ativado com sucesso.")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Erro ao ATIVAR o ambiente virtual: {e}")



def instalar_dependencias(diretorio_projeto, requirements_file):
    '''
    A função instalar_dependencias recebe dois parâmetros: o diretório do projeto e o caminho do arquivo requirements.txt.
    O primeiro passo é verificar se o diretório do projeto existe. Caso não exista, a função exibe uma mensagem de erro e retorna.
    Em seguida, a função monta o caminho do arquivo requirements.txt e verifica se ele existe. Caso não exista, a função exibe uma mensagem de erro e retorna.
    Depois, a função monta o caminho do arquivo activate dentro do ambiente virtual e executa o comando source para ativá-lo.
    Por fim, a função executa o comando pip install -r requirements.txt para instalar as dependências do projeto.
    '''    
    if not os.path.exists(requirements_file):
        raise FileNotFoundError(f"O arquivo '{requirements_file}' não existe.")

    # Get the virtual environment's pip path
    venv_pip = os.path.join(diretorio_projeto, '.venv', 'bin', 'pip')

    try:
        subprocess.run([venv_pip, 'install', '-r', requirements_file], check=True)
        print("Dependências instaladas com sucesso.")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Erro ao instalar as dependências: {e}")



def backup_dependencias_instaladas(backup_file):
    '''
    A função backup_dependencias_instaladas recebe um parâmetro: o caminho do arquivo de backup.
    O primeiro passo é verificar se o arquivo de backup já existe. Caso exista, a função exibe uma mensagem de erro e retorna.
    Em seguida, a função executa o comando pip freeze para listar as dependências instaladas e salva a saída no arquivo de backup.
    '''
    if os.path.exists(backup_file):
        print(f"O arquivo de backup '{backup_file}' já existe.")
        return

    try:
        with open(backup_file, 'w') as f:
            subprocess.run([sys.executable, '-m', 'pip', 'freeze'], stdout=f, check=True)
        print(f"Backup das dependências instaladas criado com sucesso em '{backup_file}'.")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Erro ao criar o backup das dependências instaladas: {e}")

#Por fim, escrevemos a função principal do código (main) e a condição de execução do script.
def main():
    if len(sys.argv) != 2:
        print("Uso: python3 nome.py /caminho/do/diretorio")
        sys.exit(1)

    diretorio_projeto = sys.argv[1]
    
    requirements_file = os.path.join(diretorio_projeto, 'requirements.txt')
    
    criar_ambiente_virtual(diretorio_projeto)
 
    ativar_ambiente_virtual(diretorio_projeto)

    backup_file = os.path.join(diretorio_projeto, 'requirements_instaladas.txt')
    backup_dependencias_instaladas(backup_file)


    instalar_dependencias(diretorio_projeto, requirements_file)

if __name__ == "__main__":
    main()

#EXECUTAR O SCRIPT
#python3 cria_ambiente.py dash
#NAO /bin/python3 /home/egaliza/WORKSPACE-PYTHON/ALURA-Scripting-automacao-tarefas/cria_ambiente.py /home/egaliza/WORKSPACE-PYTHON/ALURA-Scripting-automacao-tarefas/dash
#NAO source /home/egaliza/WORKSPACE-PYTHON/ALURA-Scripting-automacao-tarefas/dash/venv/bin/activate

#ativar ambiente virtual
#. .venv/bin/activate

#EXECUTAR o site
#python3 main.py
