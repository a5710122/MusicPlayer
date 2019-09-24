from appJar import gui
from pygame import mixer  # Load the popular external library
import serial
import time
import glob, os

ser = serial.Serial('COM4', 9600)

list_song = []
realnames = []
index_song = 0

count = 0
play_stop = False

for file in os.listdir("C:/Users/Smith/Desktop/Work_pipe/python_to_arduino/Song/"):
    if file.endswith(".mp3"):
        realnames.append(file)
        list_song.append(os.path.join("C:/Users/Smith/Desktop/Work_pipe/python_to_arduino/Song/", file))
        count = count + 1

# mixer.init(index_song)


def play():
    global play_stop

    print("Play...")

    if (play_stop == False):

        # mixer.music.load(list_song[index_song])
        # mixer.music.play()

        app.setLabel("l2", realnames[index_song])
        play_stop = True

        time.sleep(0.1)
        ser.write(b'P')
        ser.write(b'l')
        ser.write(b'a')
        ser.write(b'y')
        ser.write(b'#')

    elif (play_stop == True):
        print("Stop...")

        # mixer.music.stop()

        time.sleep(0.1)
        ser.write(b'S')
        ser.write(b't')
        ser.write(b'o')
        ser.write(b'p')
        ser.write(b'#')
        play_stop = False


def next():
    global index_song

    print("Next Song...")

    if index_song < len(list_song) - 1:
        index_song += 1
    else:
        index_song = 0;

    # mixer.music.load(list_song[index_song])
    # mixer.music.play()

    app.setLabel("l2", realnames[index_song])

    time.sleep(0.1)
    ser.write(b'N')
    ser.write(b'e')
    ser.write(b'x')
    ser.write(b't')
    ser.write(b'#')

def back():
    global index_song

    print("Previous Song...")

    if index_song > 0 :
        index_song -= 1
    else:
        index_song = len(list_song) - 1

    # mixer.music.load(list_song[index_song])
    # mixer.music.play()

    app.setLabel("l2", realnames[index_song])
    time.sleep(0.1)
    ser.write(b'b')
    ser.write(b'a')
    ser.write(b'c')
    ser.write(b'k')
    ser.write(b'#')

with gui("Music Player", "700x200", bg='orange', font={'size':18}) as app:
    app.label("Welcome to MusicPlayer", bg='blue', fg='orange')
    app.addEmptyLabel("l2")
    app.buttons(["<<", "▷", ">>", "Cancel"], [back, play, next, app.stop])
