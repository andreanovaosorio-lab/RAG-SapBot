from flask import Flask, jsonify, render_template, request

from rag_engine import ReglamentoRAG


app = Flask(__name__)
rag = ReglamentoRAG()


@app.get("/")
def home():
    """Muestra la interfaz web del asistente."""
    return render_template("index.html")


@app.post("/ask")
def ask():
    """Recibe la pregunta del usuario y devuelve la respuesta del RAG."""
    data = request.get_json(silent=True) or {}
    question = data.get("question", "")

    try:
        result = rag.ask(question)
        return jsonify(
            {
                "answer": result.answer,
                "pages": result.pages,
                "chunks": result.chunks,
            }
        )
    except Exception as exc:
        return jsonify({"error": str(exc)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
