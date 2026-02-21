# GUIA DE CONFIGURAÇÃO E USO DO `uv`

---
---

O `uv` é um gerenciador de pacotes e projetos Python extremamente rápido, escrito em _Rust Lang_. Ele substitui ferramentas como `pip`, `pip-tools`, `venv` e `poetry`.

---

## 1. Instalação (Linux/macOS)

Se você ainda não instalou, o comando oficial é:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

*Certifique-se de que `~/.local/bin` está no seu PATH.*

---

## 2. Configurando em um projeto existente

### Caso 1: O projeto já tem um `pyproject.toml`

Basta sincronizar as dependências para criar o ambiente virtual:

```bash
uv sync
```

### Caso 2: O projeto **NÃO** tem um `pyproject.toml` (apenas scripts)

Inicie o suporte ao `uv` no diretório:

```bash
uv init
```

Isso criará os arquivos base (`pyproject.toml`, `.python-version`).

### Caso 3: Migrando de um `requirements.txt`

Se você já possui uma lista de dependências:

```bash
uv add -r requirements.txt
```

---

## 3. Fluxo de trabalho diário

### Gerenciando dependências

- **Adicionar um pacote:** `uv add requests`
- **Adicionar para desenvolvimento:** `uv add --dev pytest`
- **Remover um pacote:** `uv remove requests`

### Executando o projeto

O `uv` gerencia o ambiente virtual automaticamente através do comando `run`:

```bash
uv run seu_script.py
```

*Isso garante que o script use as bibliotecas instaladas no `.venv` do projeto.*

---

## 4. Integração com Git e GitHub

### O que commitar?

- ✅ **`pyproject.toml`**: Define as dependências e metadados.
- ✅ **`uv.lock`**: Garante que todos os desenvolvedores usem **exatamente** as mesmas versões.

### O que ignorar?

Adicione ao seu `.gitignore`:

```text
.venv/
```

---

## 5. Dicas Extras

- **Trocar versão do Python:** `uv python pin 3.12`
- **Limpar cache:** `uv cache clean`
- **Atualizar todos os pacotes:** `uv lock --upgrade`