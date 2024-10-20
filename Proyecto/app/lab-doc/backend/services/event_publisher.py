class EventPublisher:
    def __init__(self):
        self.subscribers = {}

    def publish(self, event_type, event_data):
        """
        Descripción: Publica un evento a todos los suscriptores.
        """
        if event_type in self.subscribers:
            for callback in self.subscribers[event_type]:
                callback(event_data)

    def subscribe(self, event_type, callback):
        """
        Descripción: Suscribe un callback a un tipo de evento específico.
        """
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)
