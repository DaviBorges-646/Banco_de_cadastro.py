#  Sistema de Cadastro de Clientes (CRUD) em Python

Bem-vindo(a) ao meu projeto de **Sistema de Cadastro de Clientes**! Desenvolvido inteiramente em **Python**, este é um sistema que roda direto no terminal e simula um ambiente real de gerenciamento de dados (CRUD: *Create, Read, Update, Delete*). 

O grande diferencial deste projeto é o foco na **experiência do usuário e na integridade dos dados**, contando com diversas funções de validação para garantir que nenhuma informação seja salva de maneira errada.

---

##  Funcionalidades Principais

O sistema conta com um menu interativo e robusto que oferece as seguintes opções:

*   **1 - Cadastrar Cliente:** Permite a inserção de novos clientes solicitando dados completos (Nome, CPF, Data de Nascimento, Telefone e Endereço).
*   **2 - Pesquisar Cliente:** Busca flexível! Você pode localizar um cliente tanto digitando o **Nome Completo** quanto informando o **CPF**.
*   **3 - Excluir Cliente:** Remove o cadastro de um cliente do sistema com base no CPF informado.
*   **4 - Atualizar Cliente:** Um menu cirúrgico dentro do sistema que permite alterar um dado específico do cliente (ex: apenas o telefone ou apenas o bairro) sem a necessidade de reescrever todo o cadastro.
*   **5 - Sair do programa:** Encerra a aplicação de forma segura.

---

##  Validações Inteligentes (Anti-Erro)

Para evitar dados corrompidos ou mal digitados, o código conta com verificações automáticas em tempo real:

| Campo | Regra de Validação | Objetivo |
| :--- | :--- | :--- |
| **Nome** | Exige pelo menos nome e sobrenome. | Evita cadastros incompletos ou apenas com o primeiro nome. |
| **CPF** | Verifica se tem exatamente 11 dígitos, se são apenas números e se já não foi cadastrado. | Impede CPFs duplicados e formatos inválidos. |
| **Data de Nascimento** | Valida o tamanho e a presença obrigatória das barras (`DD/MM/AAAA`). | Padroniza a formatação das datas no sistema. |
| **Telefone** | Exige exatamente 9 dígitos numéricos. | Garante o padrão atual de números celulares brasileiros. |
| **Entradas do Menu** | Tratamento de exceções com `try/except`. | Evita que o programa quebre se o usuário digitar uma letra onde deveria ser um número. |

---

##  Tecnologias Utilizadas

*   **Linguagem:** Python 3
*   **Estrutura de Dados:** Dicionários (para representar os clientes) e Listas (para gerenciar o banco de dados em memória).
*   **Módulos Nativos:** `os` (utilizado para limpar a tela e deixar o terminal visualmente limpo).

---

##  Como Executar o Projeto

Para rodar o sistema na sua máquina, você só precisa ter o Python instalado. 

1. Baixe o arquivo do código ou clone este repositório:
   ```bash
   git clone https://github.com
   ```
2. Acesse a pasta do projeto no terminal e execute o script:
   ```bash
   python nome_do_arquivo.py
   ```

---

##  Aprendizados e Evolução

Este projeto foi excelente para consolidar conceitos fundamentais de programação, tais como:
*   Manipulação avançada de **estruturas de dados** (`list` e `dict`).
*   Modularização de código através de **funções específicas** para cada tarefa.
*   Uso do controle de fluxo moderno do Python, como o operador estruturado `match/case`.
*   Tratamento e prevenção de erros em tempo de execução.

Desenvolvido com muito café e dedicação! Sinta-se à vontade para clonar, sugerir melhorias ou abrir uma Issue. 🚀
