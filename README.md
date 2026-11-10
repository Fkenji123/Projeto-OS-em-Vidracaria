# Projeto OS em Vidraçaria - Sistema de Gestão de Ordens de Serviço

Software MVP desenvolvido para a automação e controle de Ordens de Serviço (OS) de uma vidraçaria parceira localizada no município de Ribeirão Preto - SP. O projeto tem como foco solucionar a desorganização decorrente dos controles manuais em agendas físicas, alinhando a eficiência operacional do pequeno negócio ao **ODS 8 (Trabalho Decente e Crescimento Econômico)**.

## 📌 Sobre o Projeto

O **Projeto OS em Vidraçaria** é uma aplicação web responsiva que substitui o uso de agendas de papel por um fluxo centralizado de abertura, acompanhamento e alteração de status de ordens de serviço.

### Problema Resolvido

Controle manual que ocasionava perda de prazos, esquecimentos, dificuldades na quantificação de serviços pendentes e falhas na identificação do nível de urgência das demandas.

### Solução Proposta

Uma interface enxuta e focada na rotina dos atendentes, gerentes e executores, permitindo rápida visualização de status, prazos de entrega e prioridades, sem a complexidade de módulos financeiros ou de estoque.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3.12+

* **Framework Web:** Flask

* **Banco de Dados:** PostgreSQL / SQLite (ORM via SQLAlchemy)

* **Autenticação:** Flask-Login & Werkzeug (PBKDF2-SHA256)

* **Front-end:** Jinja2, HTML5, CSS3, Bootstrap 5

* **Testes Automatizados:** Pytest

* **Integração Contínua:** GitHub Actions (`.github/workflows/ci.yml`)

## 🖥️ Demonstração das Telas Principais

### 1. Tela de Entrada e Autenticação (Login)

Permite o acesso seguro de usuários autenticados por perfil (Gerente, Atendente, Executor).

* **Destaques de Acessibilidade:** Foco visível via teclado (`Tab`), rótulos associados aos campos e botão principal ergonomicamente dimensionado.

```
+-------------------------------------------------------------+
|                 Gestão de OS - Vidraçaria                   |
|                                                             |
|  E-mail: [ exemplo@vidracaria.com.br                      ] |
|  Senha:  [ **********                                    ]  |
|                                                             |
|                     [  ENTRAR  ]                            |
|              Esqueci minha senha | Solicitar acesso         |
+-------------------------------------------------------------+

```

### 2. Painel Principal (Listagem e Acompanhamento de OS)

Oferece uma visão global dos indicadores de serviços (Ativas, Em Andamento, Concluídas) e tabela com detalhes das solicitações.

* **Destaques de Usabilidade:** Filtros por período, badges coloridas com texto explicativo de prioridades/status e botões de ação rápida.

```
+---------------------------------------------------------------------------------------------------------+
| ❖ Gestão de OS - Vidraçaria                                           👤 (Pedro Silva - Administrador)  |
+---------------------------------------------------------------------------------------------------------+
| Painel de Ordens de Serviço                                      [ 🔍 Buscar OS... ]  [ + Nova OS ]    |
|                                                                                                         |
| [ 142 ] Ativas  |  [ 65 ] Em Andamento  |  [ 12 ] Concluídas                                            |
+---------------------------------------------------------------------------------------------------------+
| N.º OS     | Cliente        | Prazo (Data) | Prioridade | Status (Indicadores)    | Ações             |
+------------+----------------+--------------+------------+-------------------------+-------------------+
| OS-10520   | TechNova Ltda. | 20 Out 2026  | Alta       | Aberta                  | [ Status ∨ ]      |
| OS-10519   | Loja Central   | 18 Out 2026  | Média      | Em Andamento            | [ Status ∨ ]      |
| OS-10517   | Loja Central   | 18 Out 2026  | Baixa      | Concluída               | [ Status ∨ ]      |
+---------------------------------------------------------------------------------------------------------+

```

### 3. Tela de Cadastro de Nova Ordem de Serviço

Formulário centralizado para registro dos dados do cliente, especificação do serviço de vidro, prazos de entrega e prioridade.

* **Destaques de Integridade:** Validações em tempo real no servidor e obrigatoriedade dos dados do cliente e prazos.

```
+---------------------------------------------------------------------------------------------------------+
| Dados do Cliente                                                                                        |
| Nome Completo: [ Ex: Maria Silva          ]  Telefone: [ (16) 99999-9999 ]  E-mail: [ mariasilva... ] |
+---------------------------------------------------------------------------------------------------------+
| Detalhes do Serviço                                                                                     |
| Descrição do Serviço de Vidro:                                                                         |
| [ Descreva o serviço, medidas, tipo de vidro, local de instalação, etc.                              ] |
+---------------------------------------------------------------------------------------------------------+
| Prazo e Prioridade                                                                                      |
| Prazo de Entrega: [ dd/mm/aaaa 📅 ]          Seleção de Prioridade: [ Média ∨ ]                        |
|                                                                                                         |
|                   [ Cadastrar Ordem de Serviço ]       [ Cancelar ]                                    |
+---------------------------------------------------------------------------------------------------------+

```

## ⚙️ Estrutura do Repositório

```
Projeto OS em Vidracaria/
├── .github/
│   └── workflows/
│       └── ci.yml             # Pipeline de Integração Contínua (GitHub Actions)
├── static/
│   ├── css/style.css          # Estilização customizada e acessibilidade
│   └── js/script.js           # Interações da interface (alertas e confirmações)
├── templates/
│   ├── base.html              # Layout base compartilhável
│   ├── login.html             # Tela 1: Autenticação
│   ├── painel.html            # Tela 2: Dashboard e Listagem de OS
│   └── nova_os.html           # Tela 3: Cadastro de OS
├── .gitignore                 # Arquivos ignorados pelo controle de versão
├── app.py                     # Inicialização das rotas e regras de negócio
├── models.py                  # Entidades ORM (Usuario, Cliente, OrdemServico)
├── forms.py                   # Validações e sanitização de entradas
├── pytest.ini                 # Configuração dos testes automatizados
├── requirements.txt           # Dependências do projeto Python
└── README.md                  # Documentação do repositório

```

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos

* Python 3.12+ instalado

### Passo a Passo

1. **Clonar o repositório e abrir a pasta:**

   ```
   cd "Projeto OS em Vidracaria"
   
   ```

2. **Criar e ativar o ambiente virtual (venv):**

   ```
   py -m venv venv
   # No Windows (PowerShell / CMD):
   venv\Scripts\activate
   
   ```

3. **Instalar as dependências:**

   ```
   pip install -r requirements.txt
   
   ```

4. **Executar a aplicação:**

   ```
   python app.py
   
   ```

   *(Ou caso o Windows solicite o interpretador direto do ambiente virtual: `.\venv\Scripts\python.exe app.py`)*

5. **Acessar o sistema:**
   Abra o navegador e acesse: `http://127.0.0.1:5000`

   > **Credenciais de Demonstração:**
   >
   > * **E-mail:** `gerente@vidracaria.com.br`
   >
   > * **Senha:** `123456`

## 🧪 Testes e Integração Contínua

Para executar os testes automatizados localmente com o **Pytest**:

```
pytest

```

Toda alteração enviada para o repositório remoto dispara automaticamente a esteira de validação contínua através do **GitHub Actions** (`ci.yml`).

## 👥 Autor

**Fabio Kenji Ichimura**

