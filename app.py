from flask import Flask, render_template, request, jsonify
import os, json
from fuzzywuzzy import fuzz
from sentence_transformers import SentenceTransformer
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)
BASE = "meetings"

# Carrega toda a base de docs em memória
def build_tree():
    tree = {}
    docs = []
    for period in sorted(os.listdir(BASE)):
        tree[period] = {}
        for group in sorted(os.listdir(f"{BASE}/{period}")):
            tree[period][group] = []
            for fname in sorted(os.listdir(f"{BASE}/{period}/{group}")):
                path = f"{BASE}/{period}/{group}/{fname}"
                data = json.load(open(path, encoding="utf-8"))
                tree[period][group].append(data)
                docs.append(data)
    return tree, docs

tree, all_docs = build_tree()

# Setup modelo e índice semântico
model = SentenceTransformer('all-MiniLM-L6-v2')
corpus = [d['title'] + " " + d['description'] for d in all_docs]
embeddings = model.encode(corpus, convert_to_numpy=True)
nn = NearestNeighbors(n_neighbors=5, metric='cosine').fit(embeddings)

def semantic_search(q):
    q_emb = model.encode([q])
    dist, idxs = nn.kneighbors(q_emb)
    return [all_docs[i] for i in idxs[0]]

def hybrid_search(q):
    # busca fuzzy nos títulos+descrições
    scored = [
        (d, fuzz.token_set_ratio(q, d['title'] + " " + d['description']))
        for d in all_docs
    ]
    scored.sort(key=lambda x: x[1], reverse=True)
    if scored[0][1] > 70:
        return [d for d,_ in scored[:5]]
    return semantic_search(q)

@app.route("/")
def index():
    return render_template("index.html",
                           tree=tree,
                           current=None)

@app.route("/encontro/<period>/<group>/<int:idx>")
def show_encontro(period, group, idx):
    encontro = tree[period][group][idx]
    return render_template("encontro.html",
                           tree=tree,
                           current=encontro,
                           e=encontro)

@app.route("/search")
def search():
    q = request.args.get("q", "")
    results = hybrid_search(q)
    # Retornamos só info básica para exibir
    return jsonify([{"title": r["title"], "period": r["period"], "group": r["group"]} for r in results])

if __name__ == "__main__":
    app.run(debug=True)
