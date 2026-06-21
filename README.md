# 🤖 RAG-SapBot  
Andrea Jinet Nova Osorio  
Fecha: 20 de junio de 2026  

------------------------------------------------------------
### 📄 Documento seleccionado y justificación

Documento: TS460_2_ES_Col23.pdf

Justificación:
Se seleccionó este documento porque contiene información clave sobre procesos estándar de SAP SD, incluyendo ventas, devoluciones, organización comercial y gestión de documentos. Es un material técnico adecuado para demostrar la capacidad del sistema RAG en la recuperación de información estructurada y compleja.

------------------------------------------------------------
### 👤 Persona usuaria objetivo y caso de uso

Usuario objetivo:
Consultores SAP SD, analistas funcionales y usuarios sin experiencia técnica avanzada que necesitan consultar documentación SAP de forma rápida y en lenguaje natural.

Caso de uso:
Permitir la consulta inteligente de documentación SAP mediante preguntas en lenguaje natural, reduciendo el tiempo de búsqueda manual y facilitando la comprensión de procesos como ventas, devoluciones y estructura organizativa.

------------------------------------------------------------
### 🤖 Descripción del sistema

RAG-SapBot es un sistema basado en Retrieval-Augmented Generation (RAG) que permite responder preguntas usando documentación técnica real.

El sistema:
- Carga documentos PDF
- Divide el contenido en chunks
- Genera embeddings
- Almacena vectores en una base de datos
- Recupera información relevante según la pregunta
- Genera respuestas con un modelo de lenguaje

------------------------------------------------------------
### 🧠 Arquitectura del sistema

Usuario → Pregunta  
↓  
Embedding de la pregunta  
↓  
Búsqueda en vector store (similaridad)  
↓  
Recuperación de chunks relevantes  
↓  
Construcción de contexto  
↓  
LLM (generación de respuesta)  
↓  
Respuesta final  

------------------------------------------------------------
### 🧱 Estructura del proyecto

RAG-SapBot/
│
├── app.py                  # API / interfaz Flask  
├── rag_engine.py          # Motor RAG  
├── ingest.py              # Procesamiento de documentos  
├── config.py              # Configuración del sistema  
├── requirements-rag.txt   # Dependencias  
│
├── pdf/
│   └── TS460_2_ES_Col23.pdf
│
├── templates/
│   └── index.html
│
├── static/
│   └── styles.css
│
└── README.md  

------------------------------------------------------------
### ⚙️ Tecnologías utilizadas

- Python 3.10+
- Flask
- LangChain (o implementación propia RAG)
- FAISS / ChromaDB
- Embeddings (OpenAI / HuggingFace / Groq)
- LLM (OpenAI / Groq / Gemini opcional)
- PyPDF

------------------------------------------------------------
### 📦 Instalación y configuración

1. Clonar el repositorio

git clone <url-del-repositorio>
cd RAG-SapBot

2. Crear entorno virtual

python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Linux/Mac

3. Instalar dependencias

pip install -r requirements-rag.txt

------------------------------------------------------------
### 🔑 Configuración de API Key

Si usas Groq:
set GROQ_API_KEY=tu_api_key   # Windows
export GROQ_API_KEY=tu_api_key  # Linux/Mac

Si usas OpenAI:
set OPENAI_API_KEY=tu_api_key

------------------------------------------------------------
### 📥 Ingesta de documentos

python ingest.py

------------------------------------------------------------
### 🚀 Ejecución del sistema

python app.py

Luego abrir en el navegador:
http://localhost:5000

------------------------------------------------------------
### 🧪 Cinco preguntas y respuestas generadas por el sistema

1. ¿Cómo hago una venta en SAP SD?
El proceso de venta inicia con la consulta, seguida de la oferta, el pedido y finalmente el reparto del producto al cliente.

2. ¿Cuáles son los elementos de un área de ventas?
Los elementos son: organización de ventas, canal de distribución y sector.

3. ¿Qué controla el tipo de posición en SAP?
Controla la determinación de precios y la relación entre posiciones y subposiciones.

4. ¿Qué datos contiene un reparto?
Contiene información de expedición y aprovisionamiento como cantidades y plazos de entrega.

5. ¿Qué proceso se sigue en las devoluciones?
Incluye la creación de orden de devolución, entrega de retorno y contabilización de mercancía.

------------------------------------------------------------
### 🧠 Conclusión

RAG-SapBot permite transformar documentación SAP compleja en un sistema de consulta inteligente, mejorando la accesibilidad de la información mediante lenguaje natural y técnicas de recuperación semántica.
