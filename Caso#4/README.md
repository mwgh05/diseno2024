# Caso 4

## Resultados de Monitoreo

|               | CPU | Memoria |
| ------------- | -----: | :--------: |
| Mongo DB      | 0.83% | 136.8MB |
| Redis         | 0.31% | 19.55MB |
| Backend API   | 0.34% | 72.38MB |

|                         | Tiempo promedio de respuesta |
| ----------------------- | ---------------------------- | 
| /get_registros          | 11932 milliseconds |
| /get_registros_poolsize | 13262 milliseconds |
| /get_registros_cache    | 9924 milliseconds |

## Conclusiones

**Consumo de Recursos** 

- MongoDB: El consumo de CPU de MongoDB es moderado (0.83%), con un uso de memoria de 136.8 MB. Esto indica que la base de datos gestiona adecuadamente los 60,000 registros y las consultas, aunque su uso de CPU es el mayor entre los componentes, dado que es la encargada de realizar las consultas sin cache.
- Redis: Redis tiene un bajo consumo de CPU (0.31%) y memoria (19.55 MB). Esto refleja su eficiencia como sistema de cache en comparación con la base de datos, ya que su función es almacenar y devolver datos rápidamente, lo que lo hace mucho más ligero.
- Backend API: El consumo de CPU (0.34%) y memoria (72.38 MB) por parte de la API es relativamente bajo. Esto sugiere que el servidor Flask está manejando bien las solicitudes, aunque hay un incremento en el uso de recursos cuando se gestionan varias conexiones de base de datos y cache.

**Tiempo de Respuesta**

- /get_registros: El tiempo promedio de respuesta de 11,932 ms es el más alto entre los endpoints. Esto se debe a que las consultas se realizan directamente sobre la base de datos MongoDB. La latencia refleja el esfuerzo necesario para obtener el 35% de los registros.
- /get_registros_poolsize: El tiempo de respuesta aumenta a 13,262 ms. Aunque el pool de conexiones debería reducir la latencia, la implementación de un pool de tamaño fijo podría estar generando alguna sobrecarga o latencia adicional debido a la espera en la asignación de conexiones. Se podría probar ajustando el tamaño del pool.
- /get_registros_cache: El tiempo de respuesta baja a 9,924 ms, demostrando que el uso de Redis mejora el rendimiento al evitar la necesidad de realizar consultas a la base de datos en cada solicitud. Los cache hits ayudan a reducir el tiempo de acceso a los datos almacenados en memoria.

**Impacto del Pool de Conexiones y Cache**

- Pool de Conexiones: La introducción de un pool de conexiones de tamaño fijo no mejora el rendimiento según los resultados obtenidos. El incremento en el tiempo de respuesta podría deberse a la configuración del pool, como su tamaño o la manera en que se distribuyen las conexiones entre solicitudes. Ajustes en el número de conexiones disponibles podrían mejorar el rendimiento.
- Cache Redis: Redis muestra un impacto positivo, ya que reduce el tiempo de respuesta respecto al endpoint sin cache ni pool. Este resultado destaca la importancia de la cache en sistemas que requieren consultas frecuentes sobre datos que no cambian con frecuencia.