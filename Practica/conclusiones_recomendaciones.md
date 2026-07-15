# Conclusiones y Recomendaciones

## Conclusiones
1. **Balanceador de Carga Funcional**: Se implementó de manera exitosa un servidor NGINX como balanceador de carga que distribuye el tráfico HTTP de forma eficiente entre dos servidores Flask (`server1` y `server2`), asegurando alta disponibilidad de la información proveniente de la base de datos MySQL.
2. **Pipelines Distribuidos con MapReduce**: La arquitectura simulada (preparador, mappers en paralelo y reducer) logró procesar adecuadamente la data de texto plano. Este flujo MapReduce se demostró robusto, permitiendo abstraer la complejidad del cálculo de métricas en pasos atómicos de procesamiento.
3. **Métricas Obtenidas y Ratio de Interacción**: 
   - El modelo analítico extrajo de manera correcta el comportamiento dentro de la red social estudiantil, identificando con precisión a los usuarios más frecuentes y las franjas horarias con más tráfico.
   - La métrica de Ratio de Interacción calculada, definida como `((likes + comments + shares) / views)`, resultó ser un excelente indicador para discernir la calidad de los videos más allá del consumo pasivo, resaltando el contenido verdaderamente viral.
4. **Almacenamiento Persistente en Docker**: El uso de volúmenes compartidos de Docker (`mr_data`) fue fundamental para establecer la comunicación por archivos entre las etapas (de preparador a mapper, y de mappers a reducer) en un entorno de microservicios efímeros.

## Recomendaciones
1. **Monitoreo de la Base de Datos**: Para escenarios con más alto tráfico, se recomienda la implementación de réplicas de lectura (Read Replicas) en MySQL, imitando una arquitectura Primary/Secondary para evitar cuellos de botella en el acceso de los servidores Flask.
2. **Estrategia de Publicación Basada en Datos**: Basándonos en la "Hora con más interacción" detectada por el MapReduce, la empresa PowerESFOT debería enfocar la publicación de sus futuros contenidos y anuncios importantes en esa franja horaria para maximizar el retorno de inversión y la viralidad del contenido.
3. **Tolerancia a Fallos en MapReduce**: Aunque el pipeline procesa chunks de manera correcta, sería beneficioso en el futuro usar un framework como Hadoop o Apache Spark para escalar de una simulación MapReduce local a un cluster verdaderamente distribuido que gestione la tolerancia a fallos automáticamente.
4. **Caché en el Balanceador**: Implementar una política de caché en NGINX para el endpoint `/datos` podría acelerar la respuesta ante consultas masivas, dado que la información de análisis no cambia en tiempo real segundo a segundo.
