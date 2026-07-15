import os
from flask import Flask, Response
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'db'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASS', 'rootpassword'),
        database=os.environ.get('DB_NAME', 'examenad')
    )

@app.route('/datos', methods=['GET'])
def obtener_datos():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT usuario, accion, fecha, hora, short FROM redes")
        rows = cursor.fetchall()
        
        # Salida en texto plano
        output = []
        for row in rows:
            # Se formatea fecha y hora a string
            usuario = str(row[0])
            accion = str(row[1])
            fecha = str(row[2])
            hora = str(row[3])
            video = str(row[4])
            
            line = f"{usuario}, {accion}, {fecha}, {hora}, {video}"
            output.append(line)
            
        cursor.close()
        conn.close()
        
        return Response("\n".join(output) + "\n", mimetype='text/plain')
    except Exception as e:
        return Response(f"Error: {str(e)}", status=500, mimetype='text/plain')

@app.route('/health', methods=['GET'])
def health_check():
    server_id = os.environ.get('SERVER_ID', 'unknown')
    return f"OK from {server_id}\n", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
