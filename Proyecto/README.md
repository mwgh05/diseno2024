# Lab.Doc

Se pretende realizar un sistema de software que facilite la tarea de la documentación de procesos de laboratorio, brindado la posibilidad de seleccionar distintos procesos estandarizados y que generen una descripción detalla del proceso automáticamente, además de poder añadir los diferentes materiales utilizados durante el proceso y la posibilidad de añadir más procedimientos con sus propios materiales a las practicas de laboratorio a documentar. Con esta información introducida por el usuario, se generará un archivo en el formato de preferencia, agilizando los procesos de descripción y escritura de los procedimientos realizados. 

A su vez, se pretende incluir un sistema de monitoreo de practica para los dispositivos con cámara que utilicen la aplicación, donde el sistema se capaz de reconocer el tipo de practica y procedimiento a realizar y identifique malas practicas de laboratorio, como pruebas con tiempos desmedidos o contaminación de material en la prueba. Al captar estos errores, ser capaz de enviar una alerta a el practicante para que verifique la advertencia y evitar fallos en los procedimientos que puedan llevar a resultados alterados.

**Requerimientos:**

    Prioridad 1:

    - Registro de laboratorio.
    - Asociar usuarios.
    - Registro de procedimiento.
    - CRUD inventario.
    - Procesos de pago.
    - Administrar subscripciones.
    - Bitácora de procedimiento.
    - Edición de bitácora.
    - Mantenimiento de subscripciones y usuarios.
    - Mantenimiento de laboratorio.
    - Registro de pagos.

    Prioridad 2:

    - Registro de resultados.
    - Autenticación y autorización de usuarios. 
    - Histograma de actividad.
    - Visualizar estadísticas.
    - Entreno de IA.
    - Resolución de dudas.
    - Calibración del procedimiento.
    - Especificación de datos del procedimiento.

    Prioridad 3:

    - Formato de exportación.
    - Análisis de resultados.
    - Alertas de monitoreo.
    - Dashboard estadístico.

## Diagrama de Arquitectura

![Diagrama de Arquitectura](images/Diagrama_Proyecto.png)

## Problem Statement y Storyboard

Crear un registro preciso y confiable.

![Storyboard](images/Storyboard.png)

## Requerimientos No Funcionales


**Compliance**

What legal and regulatory requirements must the system comply with?

- Debe cumplir con las normativas de protección de datos personales ya que contiene información como el correo electrónico y métodos de pago (en caso de que se realice la función). También debe seguir las regulaciones específicas del sector de laboratorios e investigar que tanto varían entre cada país en el que va a estar disponible la aplicación.

Are there industry-specific standards that need to be followed?

- El sistema debe seguir estándares de calidad y seguridad específicos de la industria de laboratorios. Además se debe tomar en cuenta las buenas prácticas de laboratorio.

**Extensibility**

How should the system be designed to accommodate future enhancements?

- Se va a utilizar el modelo MVC y el principio de atomic design. El atomic design permite agregar funcionalidades nuevas que se adaptan a el producto grande ya existente, mientras que MVC permite manejar por separado la interfaz, los servicios y los datos, facilitando modificaciones en cada capa.

Are there specific areas where extensibility is critical?

- En el área de monitoreo se debe poder integrar con nuevos dispositivos de laboratorio y agregar nuevos procedimientos y materiales.

**Localization**

What are the requirements for supporting multiple languages and regions?

- El sistema debe poder soportar varios idiomas por medio de internacionalización y localización. Se deberá traducir la interfaz de usuario, mensajes de error, alertas, documentación, etc. Además, debe poder manejar diferentes horarios y monedas.

How should the system handle different date, time, and currency formats?

- El sistema deberá utilizar bibliotecas de internacionalización que permitan configurar formatos de fecha, hora y moneda según la región del usuario. Deberá convertir y mostrar datos en el formato adecuado según la región del usuario.

**Documentation**

What documentation is required for users, administrators, and developers?

- Usuarios: Manual de usuario detallado que explique cómo utilizar el sistema.
- Administradores: Documentación sobre la configuración y mantenimiento del sistema.
- Desarrolladores: Documentación sobre la arquitectura del sistema, APIs y otra información para el desarrollo.

How should the documentation be maintained and updated?

- La documentación se mantendrá en GitHub y se actualizará regularmente. Cada modificación se documentará, cuando sea necesario, y se subirá al repositorio que estará disponible para usuarios y desarrolladores.