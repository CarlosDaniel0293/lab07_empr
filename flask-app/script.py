 
from flask import Flask, request, render_template 
import redis

app = Flask(____name___)
redis_client = redis.StrictRedis (host='redis', port=6379, decode_responses=True)
# Ruta para renderizar la página de votación
@app.route('/')
def index():
    return render_template('index.html') # Llamará a un archivo index.html
# Ruta para procesar los votos
@app.route('/vote', methods=['POST'])
def vote():
    option = request.form.get('option') # Obtiene la opción seleccionada desde el formulario # Incrementa el conteo de la opción en Redis
    redis_client.incr(option)
    return f" ¡Voto contado para {option}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)