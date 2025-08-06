Encontros AI Platform

Aplicação web para organização de encontros (aulas, workshops) com vídeos hospedados no YouTube e busca híbrida (texto e semântica), implementada em Flask.

📌 Visão Geral

Este projeto oferece uma interface parecida com um LMS leve, onde:

Sidebar hierárquica por período e grupo de estudo.

Header customizado com logo, campo de busca e ícones.

Conteúdo apresenta título, descrição e vídeo em container estilizado.

Vídeos são embeddings do YouTube via <iframe>, evitando peso no servidor.

Busca híbrida combinando similaridade de string (FuzzyWuzzy) e embeddings BERT (Sentence-Transformers).

Ideal para organizar encontros acadêmicos, meetups e cursos online de forma simples.

⚙️ Tecnologias

Python 3.8+

Flask: microframework web

Jinja2: templates HTML

sentence-transformers: embeddings BERT

scikit-learn: indexação e vizinhança (NearestNeighbors)

fuzzywuzzy + python-Levenshtein: similaridade de texto

HTML/CSS com estilo moderno inspirado em mockup

🚀 Instalação e Execução

Clonar o repositório:

git clone https://github.com/seu-usuario/encontros-ai.git
cd encontros-ai

Criar e ativar Virtualenv (Windows PowerShell):

python -m venv venv
.\venv\Scripts\Activate.ps1

ou (Linux/macOS):

python3 -m venv venv
source venv/bin/activate

Instalar dependências:

pip install -r requirements.txt

Estrutura de reuniões:

Crie pastas dentro de meetings/ no formato PERIODO/GROUP/.

Adicione JSONs (encontroX.json) com campos: title, description, youtube_id, period, group.

Rodar localmente:

python app.py

Abra http://127.0.0.1:5000/ no navegador.

🗂️ Estrutura de Pastas

├── app.py              # Aplicação Flask
├── requirements.txt    # Dependências Python
├── meetings/           # Dados dos encontros
│   └── 2024-1/         # Período
│       └── Machine_Learning/
│           └── encontro1.json
├── static/             # Arquivos estáticos (CSS, JS)
│   └── style.css
└── templates/          # Templates Jinja2
    ├── base.html       # Layout principal
    ├── index.html      # Página inicial
    └── encontro.html   # Detalhe do encontro

🔍 Busca Híbrida

Fuzzy String (fuzzywuzzy.token_set_ratio): retorna resultados exatos/parecidos.

Embedding Semântico:

Modelo: all-MiniLM-L6-v2 do Sentence-Transformers.

Índice: NearestNeighbors(metric='cosine').

Busca por proximidade no espaço de embedding.

Fallback: se a similaridade por texto for baixa (<70), usa busca semântica.

results = hybrid_search(query)

🎨 Customização de Estilo

CSS principal em static/style.css:

Header vermelho (#D32F2F), logo e ícones com Font Awesome.

Sidebar branca, itens ativos em vermelho.

Vídeo em container 16:9 com fundo arredondado.

Para ajustar cores/tamanhos, edite o arquivo CSS.

📦 Deploy

PythonAnywhere:

Crie Web App, escolha Flask.

Configure o virtualenv e o WSGI apontando para app.py.

Aponte static/ e templates/ para WSGI.

Outros provedores (Heroku, AWS, etc.) seguem padrão WSGI.

🤝 Contribuições

Pull requests são bem-vindos! Sinta-se à vontade para:

Melhorar o CSS/UX

Adicionar autenticação de usuários

Suporte a upload de vídeo próprio

Integração com bancos de dados externos

📝 Licença

Este projeto está licenciado sob a MIT License. Consulte o arquivo LICENSE para mais detalhes.

