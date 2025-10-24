from flask import Flask, jsonify
import math

app = Flask(__name__)

@app.route('/<int:n>', methods=['GET'])
def calcular_factorial(n):
    # Calcula el factorial del número
    factorial = math.factorial(n)

    # Determina si es par o impar
    etiqueta = "Par" if n % 2 == 0 else "Impar"

    # Crea la respuesta en formato JSON
    resultado = {
        "etiqueta": etiqueta,
        "factorial": factorial,
        "numero": n
    }

    return jsonify(resultado)

if __name__ == '__main__':
    # Ejecuta el servidor Flask en el puerto 8000
    app.run(host='0.0.0.0', port=8000, debug=True)
