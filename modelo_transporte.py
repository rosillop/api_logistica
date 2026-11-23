class UnidadTransporte:
    def __init__(self, codigo_unidad, velocidad_kmh, ruta):
        if not isinstance(codigo_unidad, str) or not codigo_unidad.strip():
            raise ValueError("El codigo_unidad es obligatorio y debe ser texto.")
        if not isinstance(ruta, str) or not ruta.strip():
            raise ValueError("La ruta es obligatoria y debe ser texto.")
        if isinstance(velocidad_kmh, bool) or not isinstance(velocidad_kmh, (int, float)):
            raise ValueError("La velocidad_kmh debe ser un valor numérico.")
        if float(velocidad_kmh) < 0:
            raise ValueError("La velocidad_kmh no puede ser negativa.")

        self.codigo_unidad = str(codigo_unidad).strip()
        self.velocidad_kmh = float(velocidad_kmh)
        self.ruta = str(ruta).strip()
        self.estado_velocidad = self.evaluar_velocidad()

    def evaluar_velocidad(self):
        if self.velocidad_kmh < 30:
            return "TRAFICO LENTO / RETRASO"
        elif self.velocidad_kmh <= 80:
            return "VELOCIDAD SEGURA"
        return "INFRACCION: EXCESO DE VELOCIDAD"

    def convertir_a_diccionario(self):
        return {
            "codigo_unidad": self.codigo_unidad,
            "velocidad_kmh": self.velocidad_kmh,
            "ruta": self.ruta,
            "estado": self.estado_velocidad
        }
