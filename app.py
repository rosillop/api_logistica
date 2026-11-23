import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from modelo_transporte import UnidadTransporte

load_dotenv()

servidor_web = Flask(__name__)
historial_lecturas = []

nombre_empresa = os.environ.get("NOMBRE_EMPRESA", "Logística Panamericana Norte")
modo_sistema = os.environ.get("MODO_SISTEMA", "PRODUCCION")


@servidor_web.route('/', methods=['GET'])
def ruta_principal():
    return jsonify({
        "servicio": nombre_empresa,
        "modo": modo_sistema
    }), 200


@servidor_web.route('/flota', methods=['GET'])
def consultar_flota():
    lista_diccionarios = [
        unidad.convertir_a_diccionario() for unidad in historial_lecturas
    ]
    return jsonify(lista_diccionarios), 200


@servidor_web.route('/flota', methods=['POST'])
def registrar_flota():
    datos_recibidos = request.get_json(silent=True)

    if (
        not datos_recibidos
        or 'codigo_unidad' not in datos_recibidos
        or 'velocidad_kmh' not in datos_recibidos
        or 'ruta' not in datos_recibidos
    ):
        return jsonify({
            "error": "Datos incompletos. Se requiere codigo_unidad, velocidad_kmh y ruta."
        }), 400

    try:
        nueva_unidad = UnidadTransporte(
            codigo_unidad=datos_recibidos["codigo_unidad"],
            velocidad_kmh=datos_recibidos["velocidad_kmh"],
            ruta=datos_recibidos["ruta"]
        )
        historial_lecturas.append(nueva_unidad)

        return jsonify({
            "mensaje": "Lectura de unidad registrada con exito en el sistema",
            "datos_guardados": nueva_unidad.convertir_a_diccionario()
        }), 201

    except (ValueError, TypeError) as error:
        return jsonify({
            "error": "Formato o valor no valido",
            "detalle": str(error)
        }), 400


if __name__ == '__main__':
    puerto = int(os.environ.get("PORT", os.environ.get("PUERTO_LOCAL", 5000)))
    servidor_web.run(host="127.0.0.1", port=puerto, debug=True)
