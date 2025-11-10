import random
from datetime import datetime, time


class AstrologiaChina:
    """
    Clase para generar lecturas de astrología china basadas en la fecha de nacimiento
    y la hora actual del sistema.
    """
    
    def __init__(self):
        # Animales del zodiaco chino (ciclo de 12 años)
        self.animales_zodiaco = {
            0: "Mono",
            1: "Gallo",
            2: "Perro",
            3: "Cerdo",
            4: "Rata",
            5: "Buey",
            6: "Tigre",
            7: "Conejo",
            8: "Dragón",
            9: "Serpiente",
            10: "Caballo",
            11: "Cabra"
        }
        
        # Elementos (ciclo de 5 elementos, cada uno dura 2 años)
        self.elementos = {
            0: "Metal",
            1: "Metal",
            2: "Agua",
            3: "Agua",
            4: "Madera",
            5: "Madera",
            6: "Fuego",
            7: "Fuego",
            8: "Tierra",
            9: "Tierra"
        }
        
        # Horas chinas (cada hora china equivale a 2 horas occidentales)
        self.horas_chinas = {
            0: {"animal": "Rata", "significado": "tiempo de descanso y renovación"},
            1: {"animal": "Buey", "significado": "momento de trabajo duro y perseverancia"},
            2: {"animal": "Tigre", "significado": "período de valentía y acción"},
            3: {"animal": "Conejo", "significado": "tiempo de calma y reflexión"},
            4: {"animal": "Dragón", "significado": "momento de poder y transformación"},
            5: {"animal": "Serpiente", "significado": "período de sabiduría e intuición"},
            6: {"animal": "Caballo", "significado": "tiempo de energía y movimiento"},
            7: {"animal": "Cabra", "significado": "momento de creatividad y armonía"},
            8: {"animal": "Mono", "significado": "período de ingenio y adaptabilidad"},
            9: {"animal": "Gallo", "significado": "tiempo de confianza y determinación"},
            10: {"animal": "Perro", "significado": "momento de lealtad y protección"},
            11: {"animal": "Cerdo", "significado": "período de generosidad y abundancia"}
        }
        
        # Características de cada animal
        self.caracteristicas_animales = {
            "Rata": {
                "personalidad": ["inteligente", "astuta", "adaptable", "carismática"],
                "fortalezas": ["perspicacia", "ingenio", "ambición", "encanto"],
                "desafios": ["puede ser codiciosa", "a veces oportunista"]
            },
            "Buey": {
                "personalidad": ["trabajador", "confiable", "fuerte", "determinado"],
                "fortalezas": ["perseverancia", "honestidad", "paciencia", "metodología"],
                "desafios": ["puede ser terco", "a veces inflexible"]
            },
            "Tigre": {
                "personalidad": ["valiente", "competitivo", "impredecible", "confiado"],
                "fortalezas": ["coraje", "liderazgo", "pasión", "dinamismo"],
                "desafios": ["puede ser impulsivo", "a veces rebelde"]
            },
            "Conejo": {
                "personalidad": ["elegante", "amable", "responsable", "tranquilo"],
                "fortalezas": ["diplomacia", "sensibilidad", "compasión", "refinamiento"],
                "desafios": ["puede ser tímido", "a veces indeciso"]
            },
            "Dragón": {
                "personalidad": ["poderoso", "enérgico", "carismático", "intrépido"],
                "fortalezas": ["confianza", "entusiasmo", "inteligencia", "tenacidad"],
                "desafios": ["puede ser arrogante", "a veces impaciente"]
            },
            "Serpiente": {
                "personalidad": ["sabio", "enigmático", "intuitivo", "discreto"],
                "fortalezas": ["sabiduría", "elegancia", "determinación", "refinamiento"],
                "desafios": ["puede ser reservado", "a veces desconfiado"]
            },
            "Caballo": {
                "personalidad": ["enérgico", "independiente", "alegre", "aventurero"],
                "fortalezas": ["entusiasmo", "sociabilidad", "optimismo", "versatilidad"],
                "desafios": ["puede ser impaciente", "a veces inquieto"]
            },
            "Cabra": {
                "personalidad": ["creativo", "gentil", "compasivo", "tranquilo"],
                "fortalezas": ["empatía", "imaginación", "bondad", "perseverancia"],
                "desafios": ["puede ser pesimista", "a veces indeciso"]
            },
            "Mono": {
                "personalidad": ["ingenioso", "inteligente", "curioso", "juguetón"],
                "fortalezas": ["adaptabilidad", "creatividad", "ingenio", "sociabilidad"],
                "desafios": ["puede ser inquieto", "a veces poco serio"]
            },
            "Gallo": {
                "personalidad": ["observador", "trabajador", "valiente", "talentoso"],
                "fortalezas": ["confianza", "honestidad", "determinación", "puntualidad"],
                "desafios": ["puede ser crítico", "a veces vanidoso"]
            },
            "Perro": {
                "personalidad": ["leal", "honesto", "amigable", "fiel"],
                "fortalezas": ["lealtad", "responsabilidad", "honestidad", "empatía"],
                "desafios": ["puede ser ansioso", "a veces pesimista"]
            },
            "Cerdo": {
                "personalidad": ["generoso", "compasivo", "diligente", "sociable"],
                "fortalezas": ["bondad", "generosidad", "paciencia", "sinceridad"],
                "desafios": ["puede ser ingenuo", "a veces materialista"]
            }
        }
        
        # Predicciones generales
        self.predicciones_amor = [
            "El amor florecerá en tu vida de manera inesperada",
            "Es un buen momento para fortalecer tus relaciones existentes",
            "La comunicación será clave en tus relaciones sentimentales",
            "Podrías conocer a alguien especial en un lugar inusual",
            "Tu carisma natural atraerá nuevas oportunidades románticas",
            "Es momento de ser honesto sobre tus sentimientos",
            "La paciencia será recompensada en asuntos del corazón",
            "Las relaciones del pasado pueden traer lecciones valiosas",
            "Tu intuición te guiará hacia la persona correcta",
            "El amor propio es el primer paso hacia el amor verdadero"
        ]
        
        self.predicciones_trabajo = [
            "Nuevas oportunidades profesionales están en el horizonte",
            "Tu esfuerzo y dedicación serán reconocidos pronto",
            "Es un buen momento para iniciar proyectos ambiciosos",
            "La colaboración con otros traerá éxito profesional",
            "Confía en tu intuición para tomar decisiones laborales",
            "Tu creatividad abrirá puertas inesperadas",
            "Es momento de demostrar tus habilidades de liderazgo",
            "La perseverancia te llevará al éxito deseado",
            "Podrías recibir una propuesta interesante en el trabajo",
            "Aprovecha las oportunidades de aprendizaje que se presenten"
        ]
        
        self.predicciones_salud = [
            "Es un buen momento para enfocarte en tu bienestar físico",
            "La meditación y el descanso serán especialmente beneficiosos",
            "Presta atención a las señales que tu cuerpo te envía",
            "Una dieta balanceada mejorará tu energía vital",
            "El ejercicio regular fortalecerá tu cuerpo y mente",
            "Es importante mantener un equilibrio entre trabajo y descanso",
            "Tu salud emocional requiere atención en este momento",
            "Las actividades al aire libre renovarán tu espíritu",
            "Es un buen período para establecer hábitos saludables",
            "La conexión mente-cuerpo está especialmente fuerte ahora"
        ]
        
        self.predicciones_fortuna = [
            "La abundancia fluirá hacia ti de formas inesperadas",
            "Es un buen momento para hacer inversiones inteligentes",
            "La generosidad que muestres volverá multiplicada",
            "Ten cuidado con los gastos impulsivos en este período",
            "Nuevas fuentes de ingresos podrían presentarse",
            "La fortuna favorece a los audaces en este momento",
            "Es momento de ahorrar para el futuro",
            "Tu situación financiera mejorará gradualmente",
            "Podrías recibir ayuda financiera de donde menos lo esperas",
            "La gratitud atraerá más prosperidad a tu vida"
        ]
    
    def obtener_animal_zodiaco(self, año_nacimiento):
        """
        Calcula el animal del zodiaco chino basado en el año de nacimiento.
        
        Args:
            año_nacimiento (int): Año de nacimiento
            
        Returns:
            str: Animal del zodiaco correspondiente
        """
        # El año chino comienza aproximadamente en febrero, pero para simplicidad usamos el año occidental
        indice = año_nacimiento % 12
        return self.animales_zodiaco[indice]
    
    def obtener_elemento(self, año_nacimiento):
        """
        Calcula el elemento chino basado en el año de nacimiento.
        
        Args:
            año_nacimiento (int): Año de nacimiento
            
        Returns:
            str: Elemento correspondiente
        """
        indice = año_nacimiento % 10
        return self.elementos[indice]
    
    def obtener_hora_china(self, hora_actual):
        """
        Determina la hora china basada en la hora actual del sistema.
        
        Args:
            hora_actual (datetime): Hora actual del sistema
            
        Returns:
            dict: Información de la hora china
        """
        hora = hora_actual.hour
        # Cada hora china equivale a 2 horas occidentales
        indice_hora_china = hora // 2
        return self.horas_chinas[indice_hora_china]
    
    def calcular_compatibilidad_hora(self, animal_nacimiento, animal_hora):
        """
        Calcula una descripción de compatibilidad entre el animal de nacimiento y el animal de la hora.
        
        Args:
            animal_nacimiento (str): Animal del zodiaco de nacimiento
            animal_hora (str): Animal de la hora actual
            
        Returns:
            str: Descripción de la compatibilidad
        """
        if animal_nacimiento == animal_hora:
            return "La energía de la hora actual resuena perfectamente con tu esencia natural. Es un momento especialmente poderoso para ti."
        
        # Animales compatibles (triángulo de afinidad)
        triangulos_compatibilidad = [
            ["Rata", "Dragón", "Mono"],
            ["Buey", "Serpiente", "Gallo"],
            ["Tigre", "Caballo", "Perro"],
            ["Conejo", "Cabra", "Cerdo"]
        ]
        
        for triangulo in triangulos_compatibilidad:
            if animal_nacimiento in triangulo and animal_hora in triangulo:
                return "La hora actual es altamente favorable para ti. Las energías se alinean de manera armoniosa."
        
        return "La hora actual presenta una energía interesante que te invita a salir de tu zona de confort."
    
    def generar_consejo_personal(self, animal, elemento):
        """
        Genera un consejo personalizado basado en el animal y elemento.
        
        Args:
            animal (str): Animal del zodiaco
            elemento (str): Elemento chino
            
        Returns:
            str: Consejo personalizado
        """
        consejos = {
            "Metal": "cultiva la disciplina y la claridad mental",
            "Agua": "fluye con las circunstancias y mantén tu flexibilidad",
            "Madera": "crece con paciencia y nutre tus relaciones",
            "Fuego": "canaliza tu pasión con propósito y dirección",
            "Tierra": "mantén tu estabilidad mientras te abres a nuevas posibilidades"
        }
        
        caracteristica = random.choice(self.caracteristicas_animales[animal]["fortalezas"])
        consejo_elemento = consejos[elemento]
        
        return f"Como {animal} de {elemento}, tu {caracteristica} es notable. En este momento, es importante que {consejo_elemento}."
    
    def generar_lectura(self, fecha_nacimiento):
        """
        Función principal que genera una lectura completa de astrología china.
        
        Args:
            fecha_nacimiento (str o datetime): Fecha de nacimiento en formato 'YYYY-MM-DD' o objeto datetime
            
        Returns:
            str: Lectura completa de astrología china
        """
        # Procesar la fecha de nacimiento
        if isinstance(fecha_nacimiento, str):
            try:
                fecha_nac = datetime.strptime(fecha_nacimiento, "%Y-%m-%d")
            except ValueError:
                return "Error: El formato de fecha debe ser 'YYYY-MM-DD'"
        else:
            fecha_nac = fecha_nacimiento
        
        # Obtener la hora actual del sistema
        hora_actual = datetime.now()
        
        # Calcular los componentes astrológicos
        animal_zodiaco = self.obtener_animal_zodiaco(fecha_nac.year)
        elemento = self.obtener_elemento(fecha_nac.year)
        hora_china = self.obtener_hora_china(hora_actual)
        
        # Obtener características
        caracteristicas = self.caracteristicas_animales[animal_zodiaco]
        
        # Calcular compatibilidad con la hora
        compatibilidad = self.calcular_compatibilidad_hora(animal_zodiaco, hora_china["animal"])
        
        # Generar consejo personal
        consejo = self.generar_consejo_personal(animal_zodiaco, elemento)
        
        # Seleccionar predicciones aleatorias
        prediccion_amor = random.choice(self.predicciones_amor)
        prediccion_trabajo = random.choice(self.predicciones_trabajo)
        prediccion_salud = random.choice(self.predicciones_salud)
        prediccion_fortuna = random.choice(self.predicciones_fortuna)
        
        # Construir la lectura completa
        lectura = f"""
╔══════════════════════════════════════════════════════════════════╗
║          LECTURA DE ASTROLOGÍA CHINA PERSONALIZADA               ║
╚══════════════════════════════════════════════════════════════════╝

📅 FECHA DE NACIMIENTO: {fecha_nac.strftime("%d de %B de %Y")}
🕐 HORA DE CONSULTA: {hora_actual.strftime("%H:%M:%S del %d de %B de %Y")}

═══════════════════════════════════════════════════════════════════

🐉 TU SIGNO DEL ZODIACO CHINO:

Animal: {animal_zodiaco} de {elemento}
Año de nacimiento: {fecha_nac.year}

Personalidad: {", ".join(caracteristicas["personalidad"])}
Fortalezas: {", ".join(caracteristicas["fortalezas"])}
Desafíos: {", ".join(caracteristicas["desafios"])}

═══════════════════════════════════════════════════════════════════

⏰ INFLUENCIA DE LA HORA ACTUAL:

Hora China: {hora_china["animal"]} ({hora_china["significado"]})

{compatibilidad}

═══════════════════════════════════════════════════════════════════

💫 TUS PREDICCIONES:

❤️  AMOR Y RELACIONES:
{prediccion_amor}

💼 TRABAJO Y CARRERA:
{prediccion_trabajo}

🌿 SALUD Y BIENESTAR:
{prediccion_salud}

💰 FORTUNA Y PROSPERIDAD:
{prediccion_fortuna}

═══════════════════════════════════════════════════════════════════

🎯 CONSEJO PERSONAL:

{consejo}

═══════════════════════════════════════════════════════════════════

✨ Que la sabiduría ancestral china ilumine tu camino ✨

"""
        return lectura


# Función auxiliar para uso directo
def obtener_lectura_astrologica(fecha_nacimiento):
    """
    Función auxiliar para obtener una lectura astrológica rápidamente.
    
    Args:
        fecha_nacimiento (str): Fecha de nacimiento en formato 'YYYY-MM-DD'
        
    Returns:
        str: Lectura astrológica completa
    """
    astrologia = AstrologiaChina()
    return astrologia.generar_lectura(fecha_nacimiento)


# Ejemplo de uso
if __name__ == "__main__":
    print("═══════════════════════════════════════════════════════════════════")
    print("         GENERADOR DE LECTURAS DE ASTROLOGÍA CHINA")
    print("═══════════════════════════════════════════════════════════════════\n")
    
    # Ejemplo 1: Usando la clase directamente
    astrologia = AstrologiaChina()
    lectura = astrologia.generar_lectura("1990-05-15")
    print(lectura)
    
    # Ejemplo 2: Usando la función auxiliar
    # lectura2 = obtener_lectura_astrologica("1995-08-20")
    # print(lectura2)
    
    # Ejemplo 3: Entrada del usuario
    # fecha_usuario = input("\nIngresa tu fecha de nacimiento (YYYY-MM-DD): ")
    # lectura3 = obtener_lectura_astrologica(fecha_usuario)
    # print(lectura3)
