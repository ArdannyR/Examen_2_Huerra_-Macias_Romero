import os
import time
import requests

def split_data():
    url = "http://nginx/datos"
    max_retries = 10

    os.makedirs("splits", exist_ok=True)
    
    for i in range(max_retries):
        try:
            print(f"Intentando conectar a {url} (Intento {i+1})...")
            response = requests.get(url)
            if response.status_code == 200:
                data = response.text.strip().split('\n')
                data = [line for line in data if line.strip()]
                
                print(f"Recibidos {len(data)} registros.")
                
                # Se divide en 3 partes
                chunks = 3
                chunk_size = len(data) // chunks + 1
                
                for j in range(chunks):
                    start = j * chunk_size
                    end = start + chunk_size
                    part_data = data[start:end]
                    
                    with open(f"splits/part_0{j+1}.txt", 'w') as f:
                        f.write('\n'.join(part_data))
                
                print("Datos divididos y guardados en splits/")
                return
            else:
                print(f"Error en API (HTTP {response.status_code}): {response.text}")
                time.sleep(5)
                continue
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(5)
    
    print("No se pudo obtener la informacion despues de varios intentos.")

if __name__ == '__main__':
    split_data()
