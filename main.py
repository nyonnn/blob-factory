import pygame 
import os
from settings import * 
from sys import exit
from game import Game 
from menu import Menu 

# Set the screen parameters

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Factory Blob")

# Load music

folder_path = "music"
audio_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
current_track = 0
pygame.mixer.music.load("music/1.mp3")
pygame.mixer.music.play()

# Calculate ingame time

clock = pygame.time.Clock()

game = Game()
menu = Menu()

# Main loop

while True:
    clock.tick(FPS)
    if not pygame.mixer.music.get_busy():
        # Restart the audio file if its ended
        current_track = (current_track + 1) % len(audio_files)
        track_path = os.path.join(folder_path, audio_files[current_track])
        pygame.mixer.music.load(track_path)
        pygame.mixer.music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                menu.gameOn = False 

    screen.fill('black')
    if menu.gameOn:
        game.run()
    else:
        menu.run()
    pygame.display.update()