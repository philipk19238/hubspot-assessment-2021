from dataclasses import dataclass


@dataclass
class Event:
    url: str
    visitorId: str
    timestamp: int


class Session:

    def __init__(self, start_time):
        self.start_time = start_time
        self.recent_time = start_time
        self.pages = []


class VisitorSessions:

    def __init__(self):
        self.sessions = []

    def add_event(self, event):
        session = self.get_session(event.timestamp)
        session.pages.append(event.url)
        session.recent_time = event.timestamp

    def to_dictionary(self):
        res = []
        for session in self.sessions:
            res.append({
                'duration': session.recent_time - session.start_time,
                'pages': session.pages,
                'startTime': session.start_time
            })
        return res

    def get_session(self, timestamp):
        if not self.sessions:
            self.sessions.append(Session(start_time=timestamp))
        else:
            most_recent = self.sessions[-1]
            time_elapsed_minutes = self.get_time_elapsed(
                timestamp, most_recent.recent_time)
            if time_elapsed_minutes > 10:
                self.sessions.append(Session(start_time=timestamp))
        return self.sessions[-1]

    def get_time_elapsed(self, timestamp, recent_time):
        time_elapsed_seconds = (timestamp - recent_time)/1000
        time_elapsed_minutes = time_elapsed_seconds / 60
        return time_elapsed_minutes


class VisitorHolder:

    def __init__(self):
        self.holder = {}

    def add_event(self, event):
        visitor_id = event.visitorId
        if visitor_id not in self.holder:
            self.holder[visitor_id] = VisitorSessions()
        self.holder[visitor_id].add_event(event)

    def items(self):
        return self.holder.items()
