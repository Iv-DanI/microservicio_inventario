from flask import Flask, request, jsonify
import datetime
from pyngrok import ngrok

port_no = 5000

app = Flask(__name__)

ngrok.set_auth_token("2mZS1eePX5yA4kBWXLnUiEdztqD_6orQzRLHYRpMiAwqyEw8q")
public_url = ngrok.connect(port_no).public_url

@app.route('/api/ventas', methods=['POST'])
def recibir_ventas():

    datos_venta = request.json
    if not datos_venta:
        return jsonify({"error": "No se enviaron detalles de la venta"}), 400

    # Extraer datos de la factura
    cod_factura = datos_venta.get("cod_factura")
    id_producto = datos_venta.get("id_producto")
    nombre_producto = datos_venta.get("nombre_producto")
    precio_unitario = datos_venta.get("precio_unitario")
    q_producto = datos_venta.get("q_producto")
    monto_total = datos_venta.get("monto_total")

    resultados_venta = []
    for producto_id, cantidad in zip(id_producto, q_producto):
        resultados_venta.append({
            "producto_id": producto_id,
            "cantidad": int(cantidad)
        })

    print(f"Venta recibida: {datos_venta}")
    print(f"Resultados de la venta: {resultados_venta}")


    return jsonify({"mensaje": "Venta procesada exitosamente", "resultados": resultados_venta}), 200

print(f"to acces {public_url}")

app.run(port=port_no)