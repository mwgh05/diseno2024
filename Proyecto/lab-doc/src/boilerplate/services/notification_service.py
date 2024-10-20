from conectors import notification_connector
from services import event_listener

class NotificationService:
    def __init__(self, notification_connector, event_listener):
        self.notification_connector = notification_connector
        self.event_listener = event_listener 
      
        self.event_listener.subscribe('alert_event', self.process_alert_event)

    def process_alert_event(self, alert_event):
        """
        Descripción: Procesa un evento de alerta y envía una notificación al usuario.
        """
        user_id = alert_event['user_id']
        message = alert_event['message']
        self.notification_connector.send_notification_to_user(user_id, message)

    def send_notification(self, user_id, message):
        """
        Envía una notificación al usuario.
        """
        self.notification_connector.send_notification_to_user(user_id, message)
