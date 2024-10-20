from conectors import ai_connector
from services import event_publisher

class AIService:
    def __init__(self, ai_connector):
        self.ai_connector = ai_connector
        self.event_publisher = event_publisher

    def analyze_step_video(self, video_stream, experiment_id):
        """
        Descripción: Analiza el video de un paso de experimento en tiempo real y genera un evento de análisis.
        """
        event = {
            'video_stream': video_stream,
            'experiment_id': experiment_id,
            'event_type': 'analyze_video'
        }

        alert_event = self.ai_connector.process_video_stream(video_stream, experiment_id)

        if alert_event:  # Si hay alguna alerta en el análisis
            self.publish_alert_event(alert_event)
      
        self.process_ai_event(event)

    def publish_alert_event(self, alert_event):
        """
        Descripción: Publica un evento de alerta que será escuchado por el servicio de notificaciones.
        """
        event_data = {
            'user_id': alert_event['user_id'],
            'message': alert_event['message'],
            'event_type': 'alert_detected'
        }
        self.event_publisher.publish('alert_event', event_data)
    
    def train_model(self, training_data):
        """
        Descripción: Entrena el modelo de IA con datos y genera un evento de entrenamiento.
        """
        event = {
            'training_data': training_data,
            'event_type': 'train_model'
        }
        self.process_ai_event(event)

    def generate_ai_report(self, analysis_results):
        """
        Genera un reporte basado en los resultados del análisis de IA y genera un evento de reporte.
        """
        event = {
            'analysis_results': analysis_results,
            'event_type': 'generate_report'
        }
        self.process_ai_event(event)

    def process_ai_event(self, ai_event):
        """
        Procesa eventos relacionados con IA como análisis de video, detección de anomalías y entrenamiento de modelos.
        """
        pass
