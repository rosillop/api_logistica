from modelo_transporte import UnidadTransporte


def ejecutar_pruebas_unitarias():
    # Umbral 1: < 30 km/h -> TRAFICO LENTO / RETRASO
    unidad_lenta = UnidadTransporte("TRK-01", 24.5, "Panamericana Norte - Km 775")
    assert unidad_lenta.estado_velocidad == "TRAFICO LENTO / RETRASO", "Error en umbral < 30 km/h"

    # Umbral 2: 30 - 80 km/h -> VELOCIDAD SEGURA
    unidad_limite_inf = UnidadTransporte("TRK-02", 30.0, "Chiclayo - Lambayeque")
    assert unidad_limite_inf.estado_velocidad == "VELOCIDAD SEGURA", "Error en límite 30 km/h"

    unidad_segura = UnidadTransporte("TRK-03", 68.0, "Chiclayo - Trujillo")
    assert unidad_segura.estado_velocidad == "VELOCIDAD SEGURA", "Error en rango 30 - 80 km/h"

    unidad_limite_sup = UnidadTransporte("TRK-04", 80.0, "Piura - Chiclayo")
    assert unidad_limite_sup.estado_velocidad == "VELOCIDAD SEGURA", "Error en límite 80 km/h"

    # Umbral 3: > 80 km/h -> INFRACCION: EXCESO DE VELOCIDAD
    unidad_exceso = UnidadTransporte("TRK-05", 96.0, "Panamericana Norte - Km 640")
    assert unidad_exceso.estado_velocidad == "INFRACCION: EXCESO DE VELOCIDAD", "Error en umbral > 80 km/h"

    # Validación defensiva: velocidad negativa
    fallo_validacion = False
    try:
        UnidadTransporte("TRK-99", -10, "Ruta de Prueba")
    except ValueError:
        fallo_validacion = True
    assert fallo_validacion, "Error: debió rechazarse una velocidad negativa"

    print("==============================================")
    print(">>> TODAS LAS PRUEBAS UNITARIAS PASARON EXITOSAMENTE <<<")
    print("==============================================")


if __name__ == "__main__":
    ejecutar_pruebas_unitarias()
