# Avance de clase - Andrés

**Componentes planeados**

Para una representación de los componentes a gran escala se plantaron los siguientes elementos

- Controllers Layer
  
    En este componente podrían ir archivos como LabProcedureController, UserController y NotificationController para manejar las principales solicitudes
  
- Services Layer
  
    En este podría ir LabProcedureService, UserService, NotificationService y AIService para separar cada funcionalidad

- Repositories Layer
  
    Para manejar procedimientos de almacenamiento de datos, donde se podrían implmentar archivos como UserRepository, LabProcedureRepository y MaterialRepository para trabajar las operaciones CRUD por separado
  
- Security Middleware
  
    Manejo de autenticación y autorización de la aplicación, que podría contener AuthMiddleware para trabajar estos procesos

- Third-Party Connectors Layer
  
    Para almacenar concecciones con APIs de terceros, con archivos como AIConnector y NotificationConnector

-Models Layer
  
  Define los modelos de datos, que representan las entidades de la base de datos y su estructura.
    
**Prototipo Propuesto**

Se diseño el siguente diagrama de componentes con la estructura mencionada

![diagrama](ejemplo_diagrama.jpg)


