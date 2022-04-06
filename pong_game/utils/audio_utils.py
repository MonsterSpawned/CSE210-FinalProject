from playsound import playsound

class AudioUtils():
    
    # Play a sound file
    def play_sound(self, path: str):
        playsound(sound=path)