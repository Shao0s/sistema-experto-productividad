# ==========================================================
# REPRESENTACIÓN DE HECHOS EN PYTHON
# SISTEMA EXPERTO DE PRODUCTIVIDAD PERSONAL
# ==========================================================

# 1. Base de hechos del estado del usuario
hechos_usuario = {
    "desconoce_uso_tiempo": True,
    "tiene_multiples_tareas": True,
    "existen_tareas_urgentes_e_importantes": True,
    "sufre_interrupciones_frecuentes": True,
    "requiere_alta_concentracion": True,
    "fatiga_mental": True,
    "cumplio_planificacion_diaria": False
}


# 2. Función para evaluar las reglas
def evaluar_sistema_experto(hechos):

    recomendaciones = []

    # Regla 1: Priorización por Matriz de Eisenhower
    if (hechos.get("tiene_multiples_tareas") and
            hechos.get("existen_tareas_urgentes_e_importantes")):

        recomendaciones.append(
            "Aplicar la Matriz de Eisenhower para "
            "clasificar y priorizar las tareas."
        )

    # Regla 2: Registro de actividades
    if hechos.get("desconoce_uso_tiempo"):

        recomendaciones.append(
            "Llevar una bitácora diaria durante tres días "
            "para identificar patrones de uso del tiempo."
        )

    # Regla 3: Control de distracciones
    if hechos.get("sufre_interrupciones_frecuentes"):

        recomendaciones.append(
            "Reducir las notificaciones y otras distracciones "
            "durante los bloques de trabajo."
        )

    # Regla 4: Técnica Pomodoro
    if (hechos.get("requiere_alta_concentracion") and
            hechos.get("fatiga_mental")):

        recomendaciones.append(
            "Aplicar la técnica Pomodoro: 25 minutos "
            "de trabajo enfocado y 5 minutos de descanso."
        )

    # Regla 5: Evaluación y ajuste diario
    if not hechos.get("cumplio_planificacion_diaria"):

        recomendaciones.append(
            "Analizar los obstáculos de la jornada y "
            "reorganizar las tareas del día siguiente."
        )

    return recomendaciones


# 3. Ejecución de prueba del sistema
if __name__ == "__main__":

    print("=== DIAGNÓSTICO DEL SISTEMA EXPERTO ===")

    diagnostico = evaluar_sistema_experto(hechos_usuario)

    for numero, recomendacion in enumerate(diagnostico, 1):
        print(f"{numero}. {recomendacion}")