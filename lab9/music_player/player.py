import pygame
import os


class MusicPlayer:
    def __init__(self, music_folder):
        self.music_folder = music_folder
        self.playlist = []
        self.current = 0
        self.playing = False

        self.load_music()

    def load_music(self):
        for file in os.listdir(self.music_folder):
            if file.endswith(".wav") or file.endswith(".mp3"):
                self.playlist.append(os.path.join(self.music_folder, file))

    def play(self):
        if not self.playlist:
            return
        pygame.mixer.music.load(self.playlist[self.current])
        pygame.mixer.music.play()
        self.playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False

    def next(self):
        self.current = (self.current + 1) % len(self.playlist)
        self.play()

    def prev(self):
        self.current = (self.current - 1) % len(self.playlist)
        self.play()

    def get_name(self):
        if not self.playlist:
            return "No music"
        return os.path.basename(self.playlist[self.current])

    def get_time(self):
        t = pygame.mixer.music.get_pos() // 1000
        if t < 0:
            t = 0
        return t