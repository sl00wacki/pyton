from abc import ABC, abstractmethod


# Interfejs kolekcji (SocialNetwork)
class SocialNetwork(ABC):
    @abstractmethod
    def create_friends_iterator(self, profile_id):
        pass

    @abstractmethod
    def create_coworkers_iterator(self, profile_id):
        pass


# Klasa reprezentująca profil użytkownika
class Profile:
    def __init__(self, profile_id, name, email):
        self.profile_id = profile_id
        self.name = name
        self.email = email

    def get_id(self):
        return self.profile_id

    def get_email(self):
        return self.email

    def __str__(self):
        return f"{self.name} ({self.email})"


# Facebook - konkretna kolekcja implementująca interfejs SocialNetwork
class Facebook(SocialNetwork):
    def __init__(self):
        # Zasymulowana graf społecznościowy z danymi
        self.profiles = [
            Profile("1", "Alice", "alice@example.com"),
            Profile("2", "Bob", "bob@example.com"),
            Profile("3", "Charlie", "charlie@example.com"),
            Profile("4", "David", "david@example.com")
        ]

    def create_friends_iterator(self, profile_id):
        return FacebookIterator(self, profile_id, "friends")

    def create_coworkers_iterator(self, profile_id):
        return FacebookIterator(self, profile_id, "coworkers")

    # Symulacja zapytania do grafu społecznościowego (np. bazy danych)
    def social_graph_request(self, profile_id, rel_type):
        if rel_type == "friends":
            return [profile for profile in self.profiles if profile.get_id() != profile_id]
        elif rel_type == "coworkers":
            return [profile for profile in self.profiles if profile.get_id() != profile_id]
        return []


# Interfejs iteratora
class ProfileIterator(ABC):
    @abstractmethod
    def get_next(self):
        pass

    @abstractmethod
    def has_more(self):
        pass


# Konkretna implementacja iteratora dla Facebooka
class FacebookIterator(ProfileIterator):
    def __init__(self, facebook, profile_id, rel_type):
        self.facebook = facebook
        self.profile_id = profile_id
        self.rel_type = rel_type
        self.current_position = 0
        self.cache = None

    def lazy_init(self):
        if self.cache is None:
            # Pobieramy dane z grafu społecznościowego
            self.cache = self.facebook.social_graph_request(self.profile_id, self.rel_type)

    def get_next(self):
        if self.has_more():
            result = self.cache[self.current_position]
            self.current_position += 1
            return result
        return None

    def has_more(self):
        self.lazy_init()
        return self.current_position < len(self.cache)

    def __str__(self):
        return f"Iterator for {self.rel_type} of profile {self.profile_id}"


# Klasa aplikacji konfiguruje kolekcję i przekazuje iterator do klienta
class Application:
    def __init__(self):
        self.network = None
        self.spammer = SocialSpammer()

    def config(self, platform):
        if platform == "Facebook":
            self.network = Facebook()
        elif platform == "LinkedIn":
            pass  # Tu można dodać klasę LinkedIn w przyszłości

    def send_spam_to_friends(self, profile):
        iterator = self.network.create_friends_iterator(profile.get_id())
        self.spammer.send(iterator, "Very important message")

    def send_spam_to_coworkers(self, profile):
        iterator = self.network.create_coworkers_iterator(profile.get_id())
        self.spammer.send(iterator, "Very important message")


# Klasa do wysyłania wiadomości do profili
class SocialSpammer:
    def send(self, iterator, message):
        while iterator.has_more():
            profile = iterator.get_next()
            print(f"Sending message to {profile}: {message}")


# Testowanie aplikacji
app = Application()
app.config("Facebook")

profile = Profile("1", "Alice", "alice@example.com")

# Wysyłanie wiadomości do znajomych
app.send_spam_to_friends(profile)

# Wysyłanie wiadomości do współpracowników
app.send_spam_to_coworkers(profile)
