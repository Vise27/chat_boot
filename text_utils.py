import unicodedata
import re

COLOR_VARIANTS = {
    # Gris
    "grises": "gris",
    "plateado": "gris",
    "plateada": "gris",
    # Negro
    "negra": "negro",
    "negros": "negro",
    "negras": "negro",
    # Blanco
    "blanca": "blanco",
    "blancos": "blanco",
    "blancas": "blanco",
    # Madera
    "maderas": "madera",
    "natural": "madera",
    "naturales": "madera",
    # Beige
    "beiges": "beige",
    "crema": "beige",
    "cremas": "beige",
    # Azul
    "azules": "azul",
    "celeste": "azul",
    "celestes": "azul",
    # Rojo
    "roja": "rojo",
    "rojos": "rojo",
    "rojas": "rojo",
    # Verde
    "verdes": "verde",
    "esmeralda": "verde",
    # Amarillo
    "amarilla": "amarillo",
    "amarillos": "amarillo",
    "amarillas": "amarillo",
    # Rosa
    "rosas": "rosa",
    "fucsia": "rosa",
    # Dorado
    "dorada": "dorado",
    "dorados": "dorado",
    "doradas": "dorado",
    # Marrón
    "marron": "marrón",
    "cafe": "marrón",
    "café": "marrón",
    "marrones": "marrón",
    "marrónes": "marrón"
}

def normalize_color(color: str) -> str:
    """Normaliza variantes de colores a su forma canónica"""
    color = normalize_text(color)
    return COLOR_VARIANTS.get(color, color)

def normalize_text(text: str) -> str:
    """
    Normaliza texto completo para búsquedas:
    1. Elimina TODOS los signos de puntuación
    2. Normaliza espacios (incluyendo espacios especiales)
    3. Elimina tildes y diacríticos
    4. Convierte a minúsculas
    """
    if not text:
        return ""

    # Paso 1: Eliminar signos de puntuación (conserva letras, números y espacios)
    text = re.sub(r'[^\w\s]|_', '', text)
    
    # Paso 2: Normalizar espacios (incluye no-break spaces, tabs, etc.)
    text = ' '.join(text.split())  # Esto también elimina espacios duplicados
    
    # Paso 3: Eliminar tildes y convertir a minúsculas
    text = text.lower()
    text = ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    )
    
    return text.strip()

def contains_word(text: str, word: str) -> bool:
    """Verifica si un texto contiene una palabra (sin sensibilidad a tildes)"""
    return normalize_text(word) in normalize_text(text)



def clean_query(text: str) -> str:
    """Limpia el texto removiendo signos de puntuación y normalizando"""
    if not text:
        return ""
    # Remover signos de puntuación
    text = re.sub(r'[^\w\s]', '', text)
    # Normalizar como antes
    text = text.lower().strip()
    text = ''.join(c for c in unicodedata.normalize('NFD', text) 
              if unicodedata.category(c) != 'Mn')
    return text    

   
def detect_query_type(query: str) -> str:
    """Detecta el tipo de consulta basado en palabras clave"""
    query = normalize_text(query)
    
    # Palabras clave para atributos
    attribute_keywords = [
        "color", "material", "tamaño", "medida", "dimension", 
        "alto", "ancho", "largo", "estilo", "acabado"
    ]
    
    # Lista simplificada de colores base (sin variantes)
    color_keywords = ["gris", "negro", "blanco", "madera", "beige", "azul", 
                     "rojo", "verde", "amarillo", "rosa", "dorado", "marrón"]
    
    # 1. Primero verificar colores (incluyendo variantes)
    query_words = query.split()
    for word in query_words:
        normalized_color = normalize_color(word)
        if normalized_color in color_keywords:
            return "attributes"
    
    # 2. Luego verificar otros atributos
    if any(attr in query for attr in attribute_keywords):
        return "attributes"
    
    # 3. Verificar espacios
    spaces = ["comedor", "sala", "living", "dormitorio", "habitacion", "cocina", 
              "oficina", "jardin", "terraza", "baño", "cuarto", "espacio"]
    if any(espacio in query for espacio in spaces):
        return "style"
    
    # 4. Verificar palabras de estilo
    style_keywords = ["para", "estilo", "ambiente", "look", "diseño", "decoración"]
    if any(kw in query for kw in style_keywords):
        return "style"
    
    # 5. Verificar productos específicos
    product_keywords = ["lámpara", "silla", "sofá", "mesa", "mueble"]
    if any(re.search(rf"\b{kw}\b", query) for kw in product_keywords):
        return "product"
    
    # 6. Si no coincide con nada anterior
    return "generic"   