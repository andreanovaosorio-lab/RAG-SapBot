# 🤖 RAG-SapBot

Sistema de **Retrieval-Augmented Generation (RAG)** diseñado para consultar, interpretar y responder preguntas sobre documentación SAP (y otros documentos técnicos), combinando **LLMs + búsqueda semántica + embeddings**.

---

## 🚀 ¿Qué es RAG-SapBot?

**RAG-SapBot** es un asistente inteligente que permite hacer preguntas en lenguaje natural sobre documentación técnica (como SAP) y obtener respuestas precisas basadas en el contenido real de los documentos.

En lugar de depender solo del conocimiento del modelo, el sistema:

1. 📄 Lee documentos (PDFs u otras fuentes)
2. ✂️ Los divide en fragmentos (chunking)
3. 🔎 Convierte el texto en embeddings
4. 🧠 Almacena vectores en una base de datos
5. 🤖 Recupera contexto relevante según la pregunta
6. ✍️ Genera respuestas con un modelo de lenguaje

---

## 🎯 Problema que resuelve

Los documentos SAP suelen ser:

- Muy extensos 📚  
- Técnicos y difíciles de buscar 🔍  
- Poco amigables para usuarios no expertos  

Este proyecto soluciona eso permitiendo:

- Buscar información semántica en lugar de solo palabras clave
- Obtener respuestas explicadas en lenguaje natural
- Ahorrar tiempo en consulta de manuales técnicos

---

## 🧠 Arquitectura del sistema

El flujo del sistema RAG es el siguiente:
Usuario → Pregunta
↓
Embedding de la pregunta
↓
Búsqueda en vector store (similaridad)
↓
Recuperación de chunks relevantes
↓
Contexto + Prompt
↓
LLM (Generación de respuesta)
↓
Respuesta final


---

## 🧱 Estructura del proyecto
RAG-SapBot/
│
├── app.py # Interfaz principal (Flask / API)
├── rag_engine.py # Motor RAG (retrieval + generación)
├── ingest.py # Ingesta y procesamiento de documentos
├── config.py # Configuración del sistema
├── requirements-rag.txt # Dependencias del proyecto
│
├── pdf/ # Documentos SAP (fuente de conocimiento)
│ └── TS460_2_ES_Col23.pdf
│
├── templates/ # Frontend HTML
│ └── index.html
│
├── static/ # CSS / estilos
│ └── styles.css
│
├── .gitignore
└── README.md


---

## ⚙️ Tecnologías utilizadas

- 🐍 Python 3.10+
- 🔗 LangChain (o lógica propia RAG)
- 📦 FAISS / ChromaDB (vector store)
- 🧠 Embeddings (OpenAI / HuggingFace / Groq compatible)
- 🌐 Flask (API / frontend web)
- 📄 PyPDF / loaders para documentos
- 🤖 LLM (OpenAI / Groq / Gemini opcional)

---

## 📦 Instalación

### 1. Clonar el repositorio
### 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

### 3. Instalar dependencias
pip install -r requirements-rag.txt

### 📥 Ingesta de documentos
python ingest.py

### Ejecutar la aplicación
python app.py

💬 Ejemplo de uso

Pregunta:

¿Cómo funciona el proceso de devoluciones en SAP SD?

Respuesta del sistema:

El proceso de devoluciones en SAP SD inicia con la creación de una orden de devolución, seguida por la entrega de retorno y la contabilización de mercancía...

🧪 Casos de uso
Consultas de documentación SAP SD
Asistente técnico para consultores SAP
Búsqueda semántica en manuales empresariales
Chatbot interno para empresas

