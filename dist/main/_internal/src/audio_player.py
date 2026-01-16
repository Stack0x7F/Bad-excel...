import pygame
import os

class AudioPlayer:
    def __init__(self, asset_path):
        if not pygame.mixer.get_init():
            pygame.mixer.init(frequency=44100, size=-16, channels=2)
        
        self.enabled = False
        possible_files = [asset_path.replace(".mp4", ".mp3"), asset_path]

        for file in possible_files:
            if os.path.exists(file):
                try:
                    pygame.mixer.music.load(file)
                    pygame.mixer.music.set_volume(0.2)
                    self.enabled = True
                    break
                except:
                    continue

    def play(self):
        if self.enabled:
            pygame.mixer.music.play()

    def get_pos_ms(self):
        if self.enabled and pygame.mixer.music.get_busy():
            return pygame.mixer.music.get_pos()
        return -1

    def stop(self):
        if self.enabled:
            pygame.mixer.music.stop()
