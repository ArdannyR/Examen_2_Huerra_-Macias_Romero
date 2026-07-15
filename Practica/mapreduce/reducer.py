import os

def run_reducer():
    video_stats = {}
    user_stats = {}
    hour_stats = {}

    splits_dir = "splits"
    if not os.path.exists(splits_dir):
        print("No se encontró el directorio splits.")
        return

    # Fase de división
    for file in os.listdir(splits_dir):
        if file.endswith(".out"):
            with open(os.path.join(splits_dir, file), 'r') as f:
                for line in f:
                    parts = line.strip().split('\t')
                    if not parts:
                        continue
                        
                    tipo = parts[0]
                    
                    if tipo == "VIDEO_STAT":
                        video = parts[1]
                        accion = parts[2]
                        count = int(parts[3])
                        
                        if video not in video_stats:
                            video_stats[video] = {'view': 0, 'like': 0, 'comment': 0, 'shared': 0}
                        if accion in video_stats[video]:
                            video_stats[video][accion] += count
                            
                    elif tipo == "USER_STAT":
                        user = parts[1]
                        count = int(parts[2])
                        user_stats[user] = user_stats.get(user, 0) + count
                        
                    elif tipo == "HOUR_STAT":
                        hour = parts[1]
                        count = int(parts[2])
                        hour_stats[hour] = hour_stats.get(hour, 0) + count

    print("\n--- RESULTADOS DEL ANALISIS MAPREDUCE ---")
    
    # Video mas visto
    if video_stats:
        video_mas_visto = max(video_stats.keys(), key=lambda v: video_stats[v]['view'])
        print(f"Video mas visto: {video_mas_visto} (Views: {video_stats[video_mas_visto]['view']})")
        
        # Video con mas likes
        video_mas_likes = max(video_stats.keys(), key=lambda v: video_stats[v]['like'])
        print(f"Video con mas likes: {video_mas_likes} (Likes: {video_stats[video_mas_likes]['like']})")
        
        # Video mas comentado
        video_mas_comentado = max(video_stats.keys(), key=lambda v: video_stats[v]['comment'])
        print(f"Video mas comentado: {video_mas_comentado} (Comments: {video_stats[video_mas_comentado]['comment']})")
        
        # Mostrar el video con mayor cantidad de interacción
        mejor_video = None
        mejor_ratio = -1
        
        for video, stats in video_stats.items():
            views = stats['view']
            if views > 0:
                ratio = (stats['like'] + stats['comment'] + stats['shared']) / views
                if ratio > mejor_ratio:
                    mejor_ratio = ratio
                    mejor_video = video
                    
        print(f"Video con mayor Ratio de Interaccion: {mejor_video} (Ratio: {mejor_ratio:.2f})")
    
    # Usuario mas recurrente
    if user_stats:
        usuario_recurrente = max(user_stats, key=user_stats.get)
        print(f"Usuario mas recurrente: {usuario_recurrente} ({user_stats[usuario_recurrente]} interacciones)")
        
    # Hora donde haya mas interacción con el público
    if hour_stats:
        hora_interaccion = max(hour_stats, key=hour_stats.get)
        print(f"Hora con mas interaccion: {hora_interaccion}:00 ({hour_stats[hora_interaccion]} interacciones)")

if __name__ == '__main__':
    run_reducer()
