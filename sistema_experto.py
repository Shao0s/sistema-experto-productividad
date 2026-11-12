# ==========================================================
# SISTEMA EXPERTO DE PRODUCTIVIDAD PERSONAL
# Motor de inferencia mediante encadenamiento hacia adelante
# ==========================================================

# 1. Base de hechos iniciales del usuario
hechos_usuario = {
    "desconoce_uso_tiempo": True,
    "tiene_multiples_tareas": True,
    "existen_tareas_urgentes_e_importantes": True,
    "sufre_interrupciones_frecuentes": True,
    "requiere_alta_concentracion": True,
    "fatiga_mental": True,
    "cumplio_planificacion_diaria": False,
}


# 2. Base de conocimiento: reglas de producción
# Cada regla contiene:
# - condiciones: hechos que deben coincidir con el valor esperado.
# - conclusiones: nuevos hechos que se incorporan a la base de hechos.
# - recomendacion: explicación que se presenta cuando se activa la regla.
reglas = [
    {
        "id": "R1",
        "nombre": "Priorización por Matriz de Eisenhower",
        "condiciones": {
            "tiene_multiples_tareas": True,
            "existen_tareas_urgentes_e_importantes": True,
        },
        "conclusiones": {"debe_priorizar_tareas": True},
        "recomendacion": (
            "Aplicar la Matriz de Eisenhower para clasificar las tareas "
            "según su importancia y urgencia."
        ),
    },
    {
        "id": "R2",
        "nombre": "Registro de actividades",
        "condiciones": {"desconoce_uso_tiempo": True},
        "conclusiones": {"requiere_registro_tiempo": True},
        "recomendacion": (
            "Llevar una bitácora diaria durante tres días para identificar "
            "patrones de uso del tiempo."
        ),
    },
    {
        "id": "R3",
        "nombre": "Control de distracciones",
        "condiciones": {"sufre_interrupciones_frecuentes": True},
        "conclusiones": {"requiere_control_distracciones": True},
        "recomendacion": (
            "Reducir las notificaciones y otras distracciones durante "
            "los bloques de trabajo."
        ),
    },
    {
        "id": "R4",
        "nombre": "Técnica Pomodoro",
        "condiciones": {
            "requiere_alta_concentracion": True,
            "fatiga_mental": True,
        },
        "conclusiones": {"se_recomienda_pomodoro": True},
        "recomendacion": (
            "Aplicar la técnica Pomodoro: 25 minutos de trabajo enfocado "
            "y 5 minutos de descanso."
        ),
    },
    {
        "id": "R5",
        "nombre": "Evaluación y ajuste diario",
        "condiciones": {"cumplio_planificacion_diaria": False},
        "conclusiones": {"requiere_ajuste_diario": True},
        "recomendacion": (
            "Analizar los obstáculos de la jornada y reorganizar las tareas "
            "del día siguiente."
        ),
    },
]


# 3. Motor de inferencia: encadenamiento hacia adelante (Forward Chaining)
def evaluar_sistema_experto(hechos_iniciales, base_reglas):
    """
    Evalúa las reglas repetidamente hasta que ya no se puedan activar más.

    Devuelve:
        hechos: base de hechos iniciales más los hechos inferidos.
        reglas_activadas: identificadores de las reglas ejecutadas.
        recomendaciones: recomendaciones generadas por las reglas.
    """
    hechos = hechos_iniciales.copy()
    reglas_activadas = []
    recomendaciones = []
    reglas_ejecutadas = set()

    hubo_inferencia = True

    while hubo_inferencia:
        hubo_inferencia = False

        for regla in base_reglas:
            regla_id = regla["id"]

            # Evita ejecutar una misma regla más de una vez.
            if regla_id in reglas_ejecutadas:
                continue

            # Todas las condiciones deben existir y coincidir con su valor.
            condiciones_cumplidas = all(
                nombre_hecho in hechos and hechos[nombre_hecho] is valor_esperado
                for nombre_hecho, valor_esperado
                in regla["condiciones"].items()
            )

            if condiciones_cumplidas:
                reglas_ejecutadas.add(regla_id)
                reglas_activadas.append(regla_id)
                recomendaciones.append({
                    "regla": regla_id,
                    "nombre": regla["nombre"],
                    "texto": regla["recomendacion"],
                })

                # Incorporación de nuevos hechos a la base de conocimiento.
                for nombre_hecho, valor in regla["conclusiones"].items():
                    if nombre_hecho not in hechos:
                        hechos[nombre_hecho] = valor
                        hubo_inferencia = True

    return hechos, reglas_activadas, recomendaciones


# 4. Ejecución de prueba del sistema
if __name__ == "__main__":
    print("=== DIAGNÓSTICO DEL SISTEMA EXPERTO ===")
    print("\nHechos iniciales:")
    for nombre, valor in hechos_usuario.items():
        print(f"- {nombre}: {valor}")

    hechos_finales, activadas, diagnostico = evaluar_sistema_experto(
        hechos_usuario, reglas
    )

    print("\n=== REGLAS ACTIVADAS ===")
    if activadas:
        for regla_id in activadas:
            print(f"- {regla_id}")
    else:
        print("No se activó ninguna regla.")

    print("\n=== RECOMENDACIONES ===")
    if diagnostico:
        for numero, resultado in enumerate(diagnostico, 1):
            print(
                f"{numero}. [{resultado['regla']}] "
                f"{resultado['nombre']}: {resultado['texto']}"
            )
    else:
        print("No hay recomendaciones para los hechos proporcionados.")

    print("\n=== BASE DE HECHOS FINAL ===")
    for nombre, valor in hechos_finales.items():
        print(f"- {nombre}: {valor}")
