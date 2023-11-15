import pygame
import os

def play_music(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

def main():
    print("Simple Music Player in Python")
    file_path = input("Enter the path of the music file: ")

    if not os.path.isfile(file_path):
        print("File not found. Exiting.")
        return

    play_music(file_path)

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)  # Adjust the playback speed if needed

if __name__ == "__main__":
    main()
