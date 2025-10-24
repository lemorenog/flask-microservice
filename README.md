# flask-microservice

Si el microservicio necesitara comunicarse con otro servicio encargado de almacenar el historial de cálculos en una base de datos externa, el diseño se modificaría de la siguiente manera:

1. El microservicio actual seguiría siendo el servicio de cálculo (responsable de recibir el número y generar el resultado).

2. Agregaría un segundo microservicio, llamado servicio de historial, encargado de guardar los datos en la base de datos.

3. Este servicio de cálculo realizaría una llamada HTTP POST al servicio de historial después de generar el resultado.

4. Enviaría un JSON con los datos del cálculo, por ejemplo:
```
{
  "numero": 5,
  "factorial": 120,
  "etiqueta": "impar",
  "timestamp": "2025-10-24T12:00:00Z"
}
```
5. El servicio de historial recibiría esta información y la almacenaría en su base de datos

-----

Una posible modificacion de codigo sería:
```
import requests

# Después de crear el JSON "resultado"
try:
    requests.post("http://servicio-historial:5000/historial", json=resultado)
except Exception as e:
    print("No se pudo registrar el historial:", e)
```
