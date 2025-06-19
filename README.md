# 🏠 Asistente de Decoración Inteligente

Un sistema de IA que ayuda a encontrar productos de decoración y muebles perfectos para cualquier ambiente, con conversaciones inteligentes que mantienen el contexto.

## ✨ Características

- **Búsqueda inteligente de productos** por tipo, ambiente y necesidades específicas
- **Conversaciones con contexto** que recuerdan productos ya mostrados
- **Análisis de ambientes** para recomendar productos relevantes
- **Detección de continuaciones** ("tienes más ejemplos?")
- **Limpieza automática** de conversaciones antiguas
- **Interfaz web moderna** y responsive
- **API REST** con FastAPI
- **Integración con GROQ** para procesamiento de lenguaje natural

## 🚀 Instalación

### Prerrequisitos

- Python 3.8+
- PostgreSQL (para la base de datos)
- Cuenta en [GROQ](https://console.groq.com/) para obtener API key

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/asistente-decoracion.git
cd asistente-decoracion
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos y API

1. Crear una base de datos PostgreSQL
2. Obtener tu API key de GROQ desde [console.groq.com](https://console.groq.com/)
3. Configurar las variables de entorno en un archivo `.env`:

```env
DATABASE_URL=postgresql://usuario:password@localhost:5432/nombre_db
GROQ_API_KEY=tu_api_key_de_groq_aqui
```

### 5. Ejecutar migraciones

```bash
python db.py
```

## 🎯 Uso

### Iniciar el servidor

```bash
python main.py
```

El servidor estará disponible en `http://localhost:8000`

### Interfaz web

Abre `http://localhost:8000` en tu navegador para usar la interfaz web.

### API REST

#### Endpoint principal: `/chat`

```bash
curl -X POST "http://localhost:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "tienes sillas para oficina?",
    "session_id": "tu-session-id"
  }'
```

**Respuesta:**
```json
{
  "response": "Encontré 3 sillas perfectas para oficina...",
  "products": [
    {
      "id": "1",
      "sku": "OFI-CHAIR-001",
      "name": "Silla Ergonómica Ejecutiva",
      "description": "Silla ergonómica de alta calidad..."
    }
  ],
  "session_id": "tu-session-id",
  "last_products": ["1", "2", "3"]
}
```

## 📁 Estructura del Proyecto

```
├── main.py                 # Servidor FastAPI principal
├── db.py                   # Configuración y conexión a base de datos
├── product_analyzer.py     # Análisis inteligente de productos
├── llama_utils.py          # Utilidades para LLM (GROQ)
├── text_utils.py           # Utilidades de procesamiento de texto
├── design_template_analyzer.py  # Análisis de plantillas de diseño
├── index.html              # Interfaz web
├── requirements.txt        # Dependencias Python
├── .gitignore             # Archivos a ignorar en Git
├── README.md              # Este archivo
├── logs/                  # Logs del sistema
│   └── conversations/     # Archivos de conversaciones por sesión
└── static/                # Archivos estáticos
```

## 🔧 Configuración

### Variables de entorno

- `DATABASE_URL`: URL de conexión a PostgreSQL
- `GROQ_API_KEY`: Tu API key de GROQ para procesamiento de lenguaje natural
- `LOG_LEVEL`: Nivel de logging (INFO, DEBUG, etc.)

### Configuración del sistema

En `main.py` puedes modificar:

```python
CLEANUP_INTERVAL = 30 * 60        # Limpieza cada 30 minutos
SESSION_MAX_AGE = 2 * 60 * 60     # Sesiones expiran en 2 horas
MAX_SESSIONS = 1000               # Máximo 1000 archivos de sesión
MAX_CONVERSATIONS_SIZE_MB = 50    # Máximo 50MB total
```

### Configuración de GROQ

El sistema usa el modelo `llama3-70b-8192` de GROQ. Puedes cambiar el modelo en `llama_utils.py`:

```python
"model": "llama3-70b-8192",  # Cambiar por otro modelo disponible
```

## 🧪 Pruebas

Ejecuta el script de prueba para verificar el sistema de conversaciones:

```bash
python test_conversation_context.py
```

## 📝 Logs

El sistema genera logs detallados en:
- `logs/product_search_YYYYMMDD.log` - Logs de búsquedas
- `logs/conversations/` - Archivos de conversaciones por sesión

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 🆘 Soporte

Si tienes problemas o preguntas:

1. Revisa los [issues](https://github.com/tu-usuario/asistente-decoracion/issues)
2. Crea un nuevo issue con detalles del problema
3. Contacta al equipo de desarrollo

## 🚀 Roadmap

- [ ] Integración con más proveedores de LLM
- [ ] Análisis de imágenes de productos
- [ ] Recomendaciones personalizadas
- [ ] Integración con APIs de e-commerce
- [ ] Sistema de usuarios y preferencias
- [ ] Chatbot con voz
- [ ] Aplicación móvil

## 💡 Sobre GROQ

Este proyecto utiliza [GROQ](https://groq.com/) para el procesamiento de lenguaje natural. GROQ ofrece:
- **Velocidad**: Respuestas ultra-rápidas
- **Fiabilidad**: Alta disponibilidad
- **Escalabilidad**: Manejo de múltiples solicitudes simultáneas
- **Modelos de última generación**: Acceso a modelos como Llama 3

---

**¡Disfruta decorando tu espacio con IA! 🎨** 