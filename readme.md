# 🚀 Encontros AI Platform

&#x20;

**Aplicação web em Flask para organizar encontros (aulas, workshops) com vídeos hospedados no YouTube e busca híbrida (texto + semântica).**

---

## 📋 Funcionalidades

- 📂 **Sidebar hierárquica** por período e grupo de estudo
- 🎥 **Vídeos** embedados via YouTube `<iframe>` (sem carregar arquivos locais)
- 🔍 **Busca híbrida**:
  - **FuzzyWuzzy** para similaridade de texto
  - **Sentence-Transformers (BERT)** + **NearestNeighbors** para busca semântica
- 🎨 **Layout customizado** inspirado em mockup corporativo

---

## 📁 Estrutura do Projeto

```
├── app.py              # Aplicação Flask (WSGI entrypoint)
├── requirements.txt    # Dependências Python
├── meetings/           # Dados dos encontros (JSON)
│   └── 2024-1/
│       └── Machine_Learning/
│           └── encontro1.json
├── static/             # Arquivos estáticos (CSS, JS, imagens)
│   └── style.css       # CSS principal
└── templates/          # Templates Jinja2
    ├── base.html       # Layout base
    ├── index.html      # Página inicial
    └── encontro.html   # Detalhe do encontro
```

---

## ⚙️ Tecnologias

| Ferramenta                      | Versão | Uso                   |
| ------------------------------- | ------ | --------------------- |
| Python                          | 3.8+   | Linguagem principal   |
| Flask                           | latest | Microframework web    |
| Jinja2                          | latest | Templates HTML        |
| sentence-transformers           | latest | Embeddings BERT       |
| scikit-learn                    | latest | NearestNeighbors      |
| fuzzywuzzy & python-Levenshtein | latest | Similaridade de texto |
| HTML5 & CSS3                    | n/a    | Interface e estilo    |

---

## 🚀 Instalação e Execução Local

1. **Clone o repositório**

   ```bash
   git clone https://github.com/PedroHRocha23/streaming-mackai.git
   cd encontros-ai
   ```

2. **Crie e ative o virtualenv**

   - **Windows (PowerShell)**
     ```powershell
     python -m venv venv
     .\venv\Scripts\Activate.ps1
     ```
   - **Linux/macOS**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Instale as dependências**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure os encontros**

   - Estrutura de pastas: `meetings/<período>/<grupo>/encontroX.json`
   - Exemplo de `encontro1.json`:
     ```json
     {
       "title": "Encontro 1 – Perceptron e sua história",
       "description": "Visão geral sobre o Perceptron…",
       "youtube_id": "SEU_YOUTUBE_ID",
       "period": "2024-1",
       "group": "Machine Learning"
     }
     ```

5. **Execute a aplicação**

   ```bash
   python app.py
   ```

6. Acesse `http://127.0.0.1:5000/` no navegador.

---

## 🔍 Busca Híbrida

```python
from fuzzywuzzy import fuzz
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors

# FuzzyWuzzy
score = fuzz.token_set_ratio(query, texto)

# Embeddings + NN
model = SentenceTransformer('all-MiniLM-L6-v2')
embs = model.encode(lista_de_docs)
nn = NearestNeighbors(n_neighbors=5, metric='cosine').fit(embs)

# Pesquisa semântica
dist, idxs = nn.kneighbors(model.encode([query]))
results = [docs[i] for i in idxs[0]]
```

---

## 🎨 Customização de Estilo

Edite `static/style.css` para:

- Cores (variáveis hexadecimais)
- Fontes e tamanhos
- Layout (grid, flex, paddings)

---

## 🛠️ Deploy em PythonAnywhere

1. Crie Web App (Flask) no painel do PythonAnywhere.
2. Aponte o WSGI file para `app.py`.
3. Selecione o virtualenv e instale dependências.
4. Configure pastas `static/` e `templates/`.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se livre para:

- Melhorar UI/UX
- Adicionar autenticação
- Suportar upload de vídeos
- Conectar banco de dados externo

---

## 📄 Licença

Este projeto é distribuído sob a **MIT License**. Veja `LICENSE` para detalhes.

