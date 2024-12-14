# Simulating UI elements
class Button:
    def __init__(self, name):
        self.name = name
        self.onClick = None

    def click(self):
        if self.onClick:
            self.onClick()

# UserInterface class with buttons
class UserInterface:
    def __init__(self):
        self.lockButton = Button("Lock")
        self.playButton = Button("Play")
        self.nextButton = Button("Next")
        self.prevButton = Button("Previous")

# Context Class (AudioPlayer)
class AudioPlayer:
    def __init__(self):
        self.state = ReadyState(self)  # Initial state is ReadyState
        self.UI = UserInterface()

        # UI button handlers
        self.UI.lockButton.onClick = self.clickLock
        self.UI.playButton.onClick = self.clickPlay
        self.UI.nextButton.onClick = self.clickNext
        self.UI.prevButton.onClick = self.clickPrevious

    def changeState(self, state):
        self.state = state

    def clickLock(self):
        self.state.clickLock()

    def clickPlay(self):
        self.state.clickPlay()

    def clickNext(self):
        self.state.clickNext()

    def clickPrevious(self):
        self.state.clickPrevious()

    # Playback methods (to be implemented)
    def startPlayback(self):
        print("Playback started")

    def stopPlayback(self):
        print("Playback stopped")

    def nextSong(self):
        print("Next song")

    def previousSong(self):
        print("Previous song")

    def fastForward(self, time):
        print(f"Fast forwarded by {time} seconds")

    def rewind(self, time):
        print(f"Rewinded by {time} seconds")

# Base State class
class State:
    def __init__(self, player):
        self.player = player

    def clickLock(self): pass
    def clickPlay(self): pass
    def clickNext(self): pass
    def clickPrevious(self): pass

# Concrete State classes
class LockedState(State):
    def clickLock(self):
        if self.player.state == "Playing":
            self.player.changeState(PlayingState(self.player))
        else:
            self.player.changeState(ReadyState(self.player))

    def clickPlay(self): pass
    def clickNext(self): pass
    def clickPrevious(self): pass

class ReadyState(State):
    def clickLock(self):
        self.player.changeState(LockedState(self.player))

    def clickPlay(self):
        self.player.startPlayback()
        self.player.changeState(PlayingState(self.player))

    def clickNext(self):
        self.player.nextSong()

    def clickPrevious(self):
        self.player.previousSong()

class PlayingState(State):
    def clickLock(self):
        self.player.changeState(LockedState(self.player))

    def clickPlay(self):
        self.player.stopPlayback()
        self.player.changeState(ReadyState(self.player))

    def clickNext(self):
        # You can define double-click logic here (just a placeholder)
        self.player.nextSong()

    def clickPrevious(self):
        # You can define double-click logic here (just a placeholder)
        self.player.previousSong()

# Example usage
audioPlayer = AudioPlayer()

# Simulating UI button clicks
audioPlayer.UI.playButton.click()  # Starts playback
audioPlayer.UI.nextButton.click()  # Goes to the next song
audioPlayer.UI.prevButton.click()  # Goes to the previous song
audioPlayer.UI.lockButton.click()  # Locks the player
audioPlayer.UI.playButton.click()  # Starts playback again
