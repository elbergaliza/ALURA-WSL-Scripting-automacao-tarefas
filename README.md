# ALURA-WSL-Scripting-automacao-tarefas
#CURSO: Scripting automação de tarefas com Python e criação de Pipelines no Jenkins
**Tópicos abordados no curso**
*	Utilize o Python na construção de scripts para automatização de processos
*	Compreenda o que são pipelines de entrega contínua
*	Construa pipelines de entrega contínua utilizando o Jenkins
*	Automatize processos de teste e análise de código usando ferramentas como Pytest e Flake8
*	Gere a documentação do projeto de modo automatizado com o Sphinx
*	Crie scripts para análise de dados usando a biblioteca Pandas

**Possivel solução para o problema de acesso do executavel e bibliotecas do Python pelo Jenkisn **
OBS: foi apolicada. Nao foi completada. Decidi usa o Docker.
Para que o Jenkins tivesse acesso ao PYENV e ao PYTHON, controlado pelo usuário egaliza, foi aplicada
uma solução de Reconfiguração de Permissões:

Passo 1: Verificar permissões atuais:

	ls -ld /home/egaliza/.pyenv
	ls -l /home/egaliza/.pyenv/shims/python3

Passo 2: Ajustar permissões para grupo jenkins:

	sudo usermod -a -G egaliza jenkins
	sudo chmod -R 755 /home/egaliza/.pyenv
	sudo chown -R egaliza:jenkins /home/egaliza/.pyenv

Passo 3: Validar acesso:

	sudo -u jenkins ls /home/egaliza/.pyenv/shims/python3

Vantagens:
	Implementação rápida
	Não requer alterações no pipeline

Riscos:
	Potencial brecha de segurança ao compartilhar diretórios de usuário
	Manutenção complexa em ambientes multi-node410


-----------------------------------------------------------------------------------

O start do Jenkins foi realizado com:
   sudo service jenkins start
Pare o servico com:
   sudo service jenkins stop

A URL do Jenkins é http://localhost:8080/

Antes de realizar o teste, é necessário garantir que o projeto esteja em execução em segundo plano, ou seja, 
que o servidor dash esteja rodando na nossa máquina. 
Portanto, é importante executar python3 main.py no terminal. 
No meu caso, o servidor já está rodando na porta 8081, conforme mudamos no código.
