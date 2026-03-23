# jornada-bootcamp-edu - Manual de Configuração de Ambiente Python

> Guia de referência para novos projetos utilizando **pyenv**, **Poetry**, **pre-commit**, **Black** e **isort**.

---

## Ferramentas

| Ferramenta | Finalidade |
|---|---|
| `pyenv` | Gerencia múltiplas versões do Python na mesma máquina, permitindo escolher a versão ideal por projeto. |
| `Poetry` | Gerencia dependências e ambientes virtuais do projeto com controle preciso de versões. |
| `pre-commit` | Executa verificações automáticas de qualidade de código antes de cada commit no Git. |
| `Black` | Formata o código Python automaticamente seguindo um estilo consistente e opinativo. |
| `isort` | Organiza e ordena os imports do Python automaticamente de forma padronizada. |

---

## Parte 1 — pyenv

O pyenv permite instalar e alternar entre versões do Python sem conflitos. Cada projeto pode usar uma versão diferente de forma isolada.

### 1.1 Instalação do pyenv

**Windows** (PowerShell como administrador):
```powershell
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

**macOS/Linux:**
```bash
curl https://pyenv.run | bash
```

> **Importante:** Após a instalação, reinicie o terminal e verifique com `pyenv --version`.

### 1.2 Instalação de uma versão do Python

```bash
# Listar versões disponíveis
pyenv install --list

# Instalar uma versão específica
pyenv install 3.12.3

# Verificar versões instaladas
pyenv versions
```

### 1.3 Definir a versão do projeto

Dentro da pasta do projeto, defina a versão local do Python:

```bash
# Dentro da pasta do projeto
pyenv local 3.12.3

# Isso cria o arquivo .python-version na raiz do projeto
# Verificar qual versão está ativa
python --version
```

> **Dica:** O arquivo `.python-version` garante que todos usem a mesma versão ao trabalhar no projeto. Commite este arquivo no Git.

---

## Parte 2 — Poetry

O Poetry gerencia as dependências do projeto e cria ambientes virtuais isolados, substituindo o `pip + requirements.txt` por uma abordagem mais robusta e reproduzível.

### 2.1 Instalação do Poetry

**Windows (PowerShell):**
```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```

**macOS/Linux:**
```bash
curl -sSL https://install.python-poetry.org | python3 -

# Verificar instalação
poetry --version
```

### 2.2 Configuração global recomendada

Configure o Poetry para sempre criar o ambiente virtual dentro da pasta do projeto:

```bash
poetry config virtualenvs.in-project true

# Verificar configuração
poetry config --list
```

> **Por que usar `in-project`?** Com essa configuração, a pasta `.venv` fica dentro do projeto, facilitando identificar o ambiente e integrá-lo com editores como VS Code.

### 2.3 Iniciar um novo projeto

```bash
# Criar um novo projeto
poetry new meu-projeto
cd meu-projeto

# OU inicializar Poetry em um projeto existente
cd meu-projeto-existente
poetry init
```

### 2.4 Criar o ambiente virtual e instalar dependências

```bash
# Instala dependências e cria o ambiente virtual (.venv)
poetry install

# Ativar o ambiente virtual
poetry shell

# Rodar um comando sem ativar o shell
poetry run python script.py
```

### 2.5 Adicionar e remover dependências

```bash
# Adicionar dependência de produção
poetry add requests

# Adicionar dependência de desenvolvimento
poetry add --dev pytest black isort

# Remover dependência
poetry remove requests

# Atualizar dependências
poetry update
```

> **Arquivo `pyproject.toml`:** Todas as dependências ficam registradas no `pyproject.toml`. Este arquivo deve ser commitado no Git. O `poetry.lock` garante que todos instalem exatamente as mesmas versões.

---

## Parte 3 — pre-commit com Black e isort

O pre-commit instala hooks que rodam automaticamente antes de cada `git commit`, garantindo que o código seja formatado e organizado de forma consistente por toda a equipe.

### 3.1 Instalar o pre-commit no projeto

```bash
poetry add --dev pre-commit
```

### 3.2 Criar o arquivo de configuração

Crie o arquivo `.pre-commit-config.yaml` na raiz do projeto (**atenção ao ponto no início do nome**):

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.3.0
    hooks:
      - id: black
        language_version: python3

  - repo: https://github.com/PyCQA/isort
    rev: 5.13.2
    hooks:
      - id: isort
        args: ["--profile", "black"]
```

> **Compatibilidade:** O argumento `--profile black` faz o isort respeitar o estilo do Black, evitando conflitos entre as duas ferramentas.

### 3.3 Instalar os hooks no repositório

```bash
poetry run pre-commit install

# Saída esperada:
# pre-commit installed at .git/hooks/pre-commit
```

### 3.4 Testar manualmente

```bash
# Rodar em todos os arquivos do projeto
poetry run pre-commit run --all-files

# Atualizar versões dos hooks para as mais recentes
poetry run pre-commit autoupdate
```

> **Comportamento esperado:** Se um arquivo for modificado pelo Black ou isort, o commit é bloqueado automaticamente. Basta fazer `git add` novamente e commitar para que o commit seja aceito com o código já formatado.

---

## Checklist — Resumo das Etapas

| # | Etapa | Comando |
|---|---|---|
| 1 | **Instalar pyenv** — Instale o pyenv para gerenciar versões do Python. | `pyenv install 3.12.3` |
| 2 | **Definir versão do projeto** — Dentro da pasta do projeto, defina a versão local do Python. | `pyenv local 3.12.3` |
| 3 | **Configurar Poetry globalmente** — Configure o Poetry para criar o `.venv` dentro do projeto (fazer apenas uma vez). | `poetry config virtualenvs.in-project true` |
| 4 | **Inicializar o projeto com Poetry** — Crie um novo projeto ou inicialize o Poetry em um projeto existente. | `poetry new meu-projeto` ou `poetry init` |
| 5 | **Instalar dependências** — Crie o ambiente virtual e instale as dependências do `pyproject.toml`. | `poetry install` |
| 6 | **Adicionar pre-commit, Black e isort** — Adicione as ferramentas de qualidade como dependências de desenvolvimento. | `poetry add --dev pre-commit black isort` |
| 7 | **Criar `.pre-commit-config.yaml`** — Crie o arquivo de configuração na raiz do projeto com as definições do Black e isort. | — |
| 8 | **Instalar os hooks no Git** — Ative os hooks para que rodem automaticamente a cada `git commit`. | `poetry run pre-commit install` |
| 9 | **Testar a configuração** — Rode manualmente para verificar se tudo está funcionando corretamente. | `poetry run pre-commit run --all-files` |

---

## Observações Importantes

- O arquivo `.python-version` (gerado pelo `pyenv local`) deve ser commitado no Git.
- O arquivo `pyproject.toml` deve ser commitado no Git.
- O arquivo `poetry.lock` deve ser commitado no Git para garantir reprodutibilidade.
- O arquivo `.pre-commit-config.yaml` deve ser commitado no Git.
- A pasta `.venv` **não** deve ser commitada — adicione ao `.gitignore`.

### .gitignore recomendado

```
.venv/
__pycache__/
*.pyc
.pytest_cache/
dist/
*.egg-info/
```


