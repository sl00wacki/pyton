# "Abstrakcja" - Klasa kontrolująca
class RemoteControl:
    def __init__(self, device):
        # Odniesienie do obiektu implementacji.
        self.device = device

    def toggle_power(self):
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()

    def volume_down(self):
        self.device.set_volume(self.device.get_volume() - 10)

    def volume_up(self):
        self.device.set_volume(self.device.get_volume() + 10)

    def channel_down(self):
        self.device.set_channel(self.device.get_channel() - 1)

    def channel_up(self):
        self.device.set_channel(self.device.get_channel() + 1)


# Rozszerzona Abstrakcja - Dodaje nowe funkcje do bazowej abstrakcji.
class AdvancedRemoteControl(RemoteControl):
    def mute(self):
        self.device.set_volume(0)


# "Implementacja" - Interfejs implementacyjny
class Device:
    def is_enabled(self):
        raise NotImplementedError()

    def enable(self):
        raise NotImplementedError()

    def disable(self):
        raise NotImplementedError()

    def get_volume(self):
        raise NotImplementedError()

    def set_volume(self, percent):
        raise NotImplementedError()

    def get_channel(self):
        raise NotImplementedError()

    def set_channel(self, channel):
        raise NotImplementedError()


# Konkretna Implementacja 1: Telewizor
class Tv(Device):
    def __init__(self):
        self._enabled = False
        self._volume = 50
        self._channel = 1

    def is_enabled(self):
        return self._enabled

    def enable(self):
        print("TV: Włączone")
        self._enabled = True

    def disable(self):
        print("TV: Wyłączone")
        self._enabled = False

    def get_volume(self):
        return self._volume

    def set_volume(self, percent):
        self._volume = max(0, min(100, percent))
        print(f"TV: Głośność ustawiona na {self._volume}")

    def get_channel(self):
        return self._channel

    def set_channel(self, channel):
        self._channel = max(1, channel)
        print(f"TV: Kanał ustawiony na {self._channel}")


# Konkretna Implementacja 2: Radio
class Radio(Device):
    def __init__(self):
        self._enabled = False
        self._volume = 30
        self._channel = 1

    def is_enabled(self):
        return self._enabled

    def enable(self):
        print("Radio: Włączone")
        self._enabled = True

    def disable(self):
        print("Radio: Wyłączone")
        self._enabled = False

    def get_volume(self):
        return self._volume

    def set_volume(self, percent):
        self._volume = max(0, min(100, percent))
        print(f"Radio: Głośność ustawiona na {self._volume}")

    def get_channel(self):
        return self._channel

    def set_channel(self, channel):
        self._channel = max(1, channel)
        print(f"Radio: Kanał ustawiony na {self._channel}")


# Kod klienta
if __name__ == "__main__":
    # Przykład użycia pilota z telewizorem
    tv = Tv()
    remote = RemoteControl(tv)
    remote.toggle_power()
    remote.volume_up()
    remote.channel_up()

    # Przykład użycia zaawansowanego pilota z radiem
    radio = Radio()
    advanced_remote = AdvancedRemoteControl(radio)
    advanced_remote.toggle_power()
    advanced_remote.volume_down()
    advanced_remote.mute()
