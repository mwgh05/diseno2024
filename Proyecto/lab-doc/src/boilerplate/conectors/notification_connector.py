class NotificationConnector:
    def __init__(self, azure_notification_bus):
        self.azure_notification_bus = azure_notification_bus  # Azure Notification Bus Client

    def send_notification_to_service(self, user_id, message):
        """
        Descripción: Envía una notificación instantánea a través del Azure Notification Bus.
        """
        # Lógica para construir la notificación
        notification_payload = {
            "user_id": user_id,
            "message": message
        }
        
        # Se envía la notificación al servicio remoto (Azure Notification Bus)
        self.azure_notification_bus.send_message(notification_payload)

    def schedule_notification_to_service(self, user_id, message, datetime):
        """
        Descripción: Programa una notificación para una hora y fecha específicas a través de Azure Notification Bus.
        """
        # Lógica para construir la notificación programada
        notification_payload = {
            "user_id": user_id,
            "message": message,
            "datetime": datetime
        }

        # Programar la notificación en Azure Notification Bus
        self.azure_notification_bus.schedule_message(notification_payload, datetime)
