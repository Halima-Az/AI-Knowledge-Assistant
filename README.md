# AI Knowledge Assistant

Un projet RAG développé avec :

- Python
- LangChain
- ChromaDB
- Ollama
- HuggingFace Embeddings

## Fonctionnalités

- Chargement de PDF
- Découpage en chunks
- Génération d'embeddings
- Stockage dans ChromaDB
- Recherche par similarité
- Génération de réponses avec Ollama

## Installation

```bash
pip install -r requirements.txt
```

## Lancer Ollama

```bash
ollama serve
```

## Télécharger le modèle

```bash
ollama pull llama3.2
```

## Lancer le projet

```bash
python main.py
```