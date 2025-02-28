## ALURA-WSL-Scripting-automacao-tarefas

CURSO na ALURA: _Scripting: Automação de tarefas com Python e criação de Pipelines no Jenkins_

**Tópicos abordados no curso**

*   Utilize o Python na construção de scripts para automatização de processos
*   Compreenda o que são pipelines de entrega contínua
*   Construa pipelines de entrega contínua utilizando o Jenkins
*   Automatize processos de teste e análise de código usando ferramentas como Pytest e Flake8
*   Gere a documentação do projeto de modo automatizado com o Sphinx
*   Crie scripts para análise de dados usando a biblioteca Pandas

---

### Execução do Projeto

Antes de realizar o teste, é necessário garantir que o projeto esteja em execução em segundo plano, ou seja, que o servidor dash esteja rodando na nossa máquina.  
Portanto, é importante executar _**python3 main.py**_ no terminal.  
A aplicação de teste roda na porta **8081**.

### Instaladores

Neste curso instalamos o Jenkins ![alt text for screen readers](https://img.icons8.com/?size=48&id=39292&format=png)

O start do Jenkins foi realizado com:

```plaintext
sudo service jenkins start  
```

Pare o servico com:

```plaintext
sudo service jenkins stop
```

A URL do Jenkins é [http://localhost:8080/](http://localhost:8080/)
