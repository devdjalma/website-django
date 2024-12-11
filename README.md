# Simple-Website

# 🌟 Beco dos Códigos - Django Site 🌟

Bem-vindo ao repositório do **Beco dos Códigos**, um projeto feito com **Django** para explorar funcionalidades de formulários e registros de usuários. 🚀

## 📂 Estrutura do Projeto

- **App `formulario`**: Gerencia os formulários e o armazenamento de dados do usuário.
- **App `registrados`**: Exibe os usuários registrados e outros detalhes.
- **Templates**: HTML estilizado com navegação e footer compartilhados entre as páginas.

## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/beco-dos-codigos.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd beco-dos-codigos
   ```

3. Crie um ambiente virtual e ative:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Realize as migrações do banco de dados:
   ```bash
   python manage.py migrate
   ```

6. Crie um arquivo .env na raiz do repositorio e adicione as variaveis:
   SECRET_KEY = "sua_secrect_key"
   ALLOWED_HOSTS = localhost
   DEBUG=True

7. Inicie o servidor:
   ```bash
   python manage.py runserver
   ```

## 🌐 Funcionalidades

- 📋 **Formulário de Usuários**: Adicione novos usuários com campos validados.
- 📜 **Lista de Registrados**: Visualize usuários registrados dinamicamente.
- 🖌️ **Estilo Moderno**: Interface estilizada com HTML e CSS responsivo.
- 🌍 **Navegação Completa**: Links rápidos para acessar todas as páginas.

## 🖥️ Tecnologias Utilizadas

- Python 🐍
- Django 🌐
- HTML5 & CSS3 🎨
- Bootstrap 5 (opcional para estilos adicionais) 💄

## 📝 Licença

Este projeto está sob a licença **MIT**. 🌟 

---

Made with ❤️ by **Beco dos Códigos** 🚀
