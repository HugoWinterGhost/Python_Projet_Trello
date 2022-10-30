from Entity import Event


class GreenImpactEventController:
    def __init__(self, events: dict):
        self.green_impact_events = events
        self.events = self.format_events()

    def print_all_event(self):
        """
        Print all event

        Returns:
            None
        """
        for event in self.events:
            print(event.title)

    def format_events(self):
        """
        Format events

        Returns:
            None
        """
        events = []
        for event in self.green_impact_events:
            events.append(Event(event))
        return events

