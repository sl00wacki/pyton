# Interfejs zdalnej usługi
class ThirdPartyYouTubeLib:
    def list_videos(self):
        raise NotImplementedError

    def get_video_info(self, id):
        raise NotImplementedError

    def download_video(self, id):
        raise NotImplementedError


# Konkretna implementacja łącza do usługi
class ThirdPartyYouTubeClass(ThirdPartyYouTubeLib):
    def list_videos(self):
        # Wyślij żądanie do API YouTube
        print("Requesting list of videos from YouTube...")
        return ["Video1", "Video2", "Video3"]

    def get_video_info(self, id):
        # Pobierz metadane filmu
        print(f"Fetching info for video {id}...")
        return f"Info for video {id}"

    def download_video(self, id):
        # Pobierz plik wideo z YouTube
        print(f"Downloading video {id}...")


# Klasa Proxy implementująca pamięć podręczną
class CachedYouTubeClass(ThirdPartyYouTubeLib):
    def __init__(self, service: ThirdPartyYouTubeLib):
        self.service = service
        self.list_cache = None
        self.video_cache = {}
        self.need_reset = False

    def list_videos(self):
        if self.list_cache is None or self.need_reset:
            print("Fetching video list from service...")
            self.list_cache = self.service.list_videos()
        return self.list_cache

    def get_video_info(self, id):
        if id not in self.video_cache or self.need_reset:
            print(f"Fetching video info for {id} from service...")
            self.video_cache[id] = self.service.get_video_info(id)
        return self.video_cache[id]

    def download_video(self, id):
        if self.need_reset:
            print(f"Resetting cache for {id}...")
        print(f"Downloading video {id} via proxy...")
        self.service.download_video(id)


# Klasa zarządzająca interfejsem użytkownika
class YouTubeManager:
    def __init__(self, service: ThirdPartyYouTubeLib):
        self.service = service

    def render_video_page(self, id):
        info = self.service.get_video_info(id)
        print(f"Rendering video page with info: {info}")

    def render_list_panel(self):
        list_of_videos = self.service.list_videos()
        print(f"Rendering video list: {list_of_videos}")

    def react_on_user_input(self):
        # Użytkownik wprowadza dane
        self.render_video_page("Video1")
        self.render_list_panel()


# Aplikacja konfigurująca pośredników
class Application:
    def init(self):
        # Tworzymy obiekt usługi YouTube
        aYouTubeService = ThirdPartyYouTubeClass()

        # Tworzymy obiekt proxy, który używa pamięci podręcznej
        aYouTubeProxy = CachedYouTubeClass(aYouTubeService)

        # Tworzymy managera, który korzysta z pośrednika
        manager = YouTubeManager(aYouTubeProxy)

        # Symulacja działania aplikacji
        manager.react_on_user_input()


# Uruchomienie aplikacji
if __name__ == "__main__":
    app = Application()
    app.init()
