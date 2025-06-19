# Asistente de Decoración Inteligente

Sistema de IA para encontrar productos de decoración y muebles con conversaciones inteligentes que mantienen el contexto.

## Características

- Búsqueda inteligente de productos por tipo y ambiente
- Conversaciones con contexto (recuerda productos mostrados)
- Detección de continuaciones ("tienes más ejemplos?")
- Limpieza automática de conversaciones antiguas
- Interfaz web con FastAPI
- Integración con GROQ API

## Instalación

1. **Clonar repositorio**
```bash
git clone https://github.com/Vise27/chat_boot.git
cd chat_boot
```

2. **Crear entorno virtual**
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**
Crear archivo `.env`:
```env
DATABASE_URL=postgresql://usuario:password@localhost:5432/nombre_db
GROQ_API_KEY=tu_api_key_de_groq
```

5. **Ejecutar servidor**
```bash
python -m uvicorn main:app --reload
```

## Uso

- Abrir `http://localhost:8000` en el navegador
- Hacer preguntas como "tienes sillas para oficina?"
- Usar "tienes más ejemplos?" para continuar la búsqueda

## API

```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "tienes sillas?", "session_id": "123"}'
``` 