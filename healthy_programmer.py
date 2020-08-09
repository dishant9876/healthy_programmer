from pygame import mixer
from datetime import datetime
from time import time

def music_on(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a == stopper:
            mixer.music.stop()
            break


def logging_data(msg):
    with open("healthy_programmer_data.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    water = time()
    eyes = time()
    exercise= time()
    water_seconds = 10
    eyes_seconds = 20
    exercise_seconds =30
    while True:
        if time()-water>water_seconds:
            print("Water drinking time. Enter 'drank' to stop the alarm")
            music_on("water.mp3","drank")
            water=time()
            logging_data("Drank water at")

        if time() - eyes > eyes_seconds:
            print("Eyes exercise time. Enter 'done' to stop the alarm")
            music_on("eyes.mp3","done")
            eyes=time()
            logging_data("Eyes relaxed at")

        if time() - exercise > exercise_seconds:
            print("Physical exercise time. Enter 'done' to stop the alarm")
            music_on("physical.mp3","done")
            water=time()
            logging_data("Physical exercise done at")
