class EventListener:
    def __init__(self, event_publisher):
        self.event_publisher = event_publisher

    def subscribe(self, event_type, callback):
        """
        Descripción: Suscribe un servicio a un evento específico.
        """
        self.event_publisher.subscribe(event_type, callback)
