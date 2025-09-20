    # Oráculo de Receitas - Backend 📜

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-4.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-A30000?style=for-the-badge&logo=django&logoColor=white)

Backend da aplicação Oráculo de Receitas, responsável por gerenciar os dados e se comunicar com a API do Google Gemini para a geração de receitas.

---

### 🎥 Demonstração

[INSERIR AQUI UM GIF CURTO DA APLICAÇÃO COMPLETA FUNCIONANDO. Ferramentas como 'ScreenToGif' (Windows) ou 'Kap' (Mac) são ótimas para isso.]

---

### ✨ Sobre o Projeto

Este projeto é a espinha dorsal do Oráculo de Receitas. É uma API RESTful construída com Django e Django REST Framework que fornece endpoints para a criação e visualização de receitas, ingredientes e passos. Seu principal recurso é um endpoint especializado que recebe uma lista de ingredientes e utiliza a inteligência artificial do Google Gemini para gerar uma receita criativa e completa em tempo real.

Este repositório contém apenas o **Backend**. O repositório do Frontend pode ser encontrado [aqui](https://github.com/vecelic/oraculo-receitas-frontend.git).

### 🛠️ Tecnologias Utilizadas

* **Python 3.12**
* **Django & Django REST Framework:** Para a construção da API.
* **Google Generative AI:** Para a integração com o modelo de IA Gemini.
* **Django-CORS-Headers:** Para permitir a comunicação com o frontend.
* **Python-Decouple:** Para a segurança das chaves de API.
* **Gunicorn:** Para preparação do ambiente de produção.
* **SQLite3:** Banco de dados utilizado em desenvolvimento.

### 🔮 Endpoints da API

* `GET /api/recipes/`: Lista todas as receitas.
* `POST /api/recipes/`: Cria uma nova receita completa.
* `GET /api/recipes/{id}/`: Detalha uma receita específica.
* ... (e todos os outros endpoints criados pelo `ViewSet` para `ingredients` e `steps`)
* `POST /api/generate/`: Endpoint especializado que recebe `{ "ingredients": "..." }` e retorna uma receita gerada pela IA.

### 🚀 Como Executar Localmente

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/vecelic/oraculo-Receitas-backend.git](https://github.com/vecelic/oraculo-Receitas-backend.git)
    cd SEU_REPOSITORIO_BACKEND
    ```
2.  **Crie e ative o ambiente virtual:**
    ```bash
    python -m venv venv
    # Windows
    .\venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```
3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure as variáveis de ambiente:**
    * Crie um arquivo `.env` na raiz do projeto.
    * Adicione sua chave da API Gemini: `GEMINI_API_KEY='SUA_CHAVE_AQUI'`
5.  **Execute as migrações do banco de dados:**
    ```bash
    python manage.py migrate
    ```
6.  **(Opcional) Crie um superusuário para acessar o Admin:**
    ```bash
    python manage.py createsuperuser
    ```
7.  **Inicie o servidor:**
    ```bash
    python manage.py runserver
    ```
O servidor estará rodando em `http://127.0.0.1:8000`.

---

### 👤 Autor

**[Bruno Vecelic]**
* LinkedIn: [link](https://www.linkedin.com/in/bruno-vecelic/)
* GitHub: [link](https://github.com/vecelic)