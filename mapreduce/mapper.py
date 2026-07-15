import sys
import os

def run_mapper(filename):
    if not os.path.exists(filename):
        print(f"Archivo {filename} no encontrado.")
        return

    out_filename = f"{filename}.out"
    
    with open(filename, 'r') as f_in, open(out_filename, 'w') as f_out:
        for line in f_in:
            line = line.strip()
            if not line:
                continue
                
            parts = [p.strip() for p in line.split(',')]
            if len(parts) >= 5:
                usuario, accion, fecha, hora, video = parts[0], parts[1], parts[2], parts[3], parts[4]
                
                # 1. Metricas de video
                f_out.write(f"VIDEO_STAT\t{video}\t{accion}\t1\n")
                
                # 2. Usuario recurrente
                f_out.write(f"USER_STAT\t{usuario}\t1\n")
                
                # 3. Hora con mas interaccion
                hora_corta = hora.split(':')[0]
                f_out.write(f"HOUR_STAT\t{hora_corta}\t1\n")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Uso: python mapper.py <archivo_entrada>")
        sys.exit(1)
        
    archivo = sys.argv[1]
    run_mapper(archivo)
