class File:
    def __init__(self, filename):
        self.filename = filename

    def write(self, content):
        print(f"Writing to {self.filename}: {content}")


# Bazowa klasa publikującego
class EventManager:
    def __init__(self):
        # Tablica asocjacyjna typów zdarzeń i słuchaczy
        self.listeners = {}

    def subscribe(self, eventType, listener):
        if eventType not in self.listeners:
            self.listeners[eventType] = []
        self.listeners[eventType].append(listener)

    def unsubscribe(self, eventType, listener):
        if eventType in self.listeners:
            self.listeners[eventType].remove(listener)

    def notify(self, eventType, data):
        if eventType in self.listeners:
            for listener in self.listeners[eventType]:
                listener.update(data)


# Konkretny publikujący
class Editor:
    def __init__(self):
        self.events = EventManager()
        self.file = None

    # Metody logiki biznesowej mogą powiadamiać subskrybentów o zmianach.
    def openFile(self, path):
        self.file = File(path)
        self.events.notify("open", self.file.filename)

    def saveFile(self):
        if self.file:
            self.file.write("File saved.")
            self.events.notify("save", self.file.filename)


# Interfejs subskrybenta
class EventListener:
    def update(self, filename):
        pass


# Konkretni subskrybenci
class LoggingListener(EventListener):
    def __init__(self, log_filename, message):
        self.log = File(log_filename)
        self.message = message

    def update(self, filename):
        content = self.message.replace('%s', filename)
        self.log.write(content)


class EmailAlertsListener(EventListener):
    def __init__(self, email, message):
        self.email = email
        self.message = message

    def update(self, filename):
        email_content = self.message.replace('%s', filename)
        # Assuming a simple system email simulation
        print(f"Sending email to {self.email}: {email_content}")


# Aplikacja konfigurowania publikujących i subskrybentów
class Application:
    def config(self):
        editor = Editor()

        logger = LoggingListener(
            "/path/to/log.txt",
            "Someone has opened the file: %s"
        )
        editor.events.subscribe("open", logger)

        emailAlerts = EmailAlertsListener(
            "admin@example.com",
            "Someone has changed the file: %s"
        )
        editor.events.subscribe("save", emailAlerts)

        # Example of triggering events
        editor.openFile("file1.txt")
        editor.saveFile()


# Użycie
app = Application()
app.config()
