import math
import os
import sys
import face_recognition
import numpy as np
import cv2 as cv2
from tkinter import *  # Import the required Libraries
import keyboard
import pylab as p

print('press "p" to start, and then wait until you see names in "[]"')
while True:  # making a loop# used try so that if user pressed other than the given key error will not be shown
    if keyboard.is_pressed('p'):
        import \
            time  # this is for making an action delayed by time in seconds, the import of it

        print('lease wait approximately 5 seconds...loading')
        from pynput.mouse import Button, \
            Controller as MouseController  # this imports the automation for mouse

        mouse = MouseController()  # same as keyboard define but for the mouse
        time.sleep(.5)  # the actual action of delaying time by 2 seconds
        mouse.position = (2000, 1100)  # makes the mouse go to these coordinates
        mouse.press(
            Button.left)  # make the mouse click,/ adding ,2 will make it click twice/ intuitive
        mouse.release(Button.left)
        mouse.position = (1850, 950)
        time.sleep(.25)
        mouse.press(
            Button.left)
        mouse.release(Button.left)
        time.sleep(.25)
        mouse.press(
            Button.left)
        mouse.release(Button.left)
        mouse.position = (1215, 1060)
        mouse.press(
            Button.left)
        mouse.release(Button.left)
        mouse.position = (1355, 1060)
        time.sleep(2.3)
        mouse.press(
            Button.left)
        mouse.release(Button.left)


        def face_confidence(face_distance, face_match_threshold=0.6):
            arange = (1.0 - face_match_threshold)
            linear_val = (1.0 - face_distance) / (arange * 2.0)
            if face_distance > face_match_threshold:
                return str(round(linear_val * 100, 2)) + '%'
            else:
                value = (linear_val + ((1.0 - linear_val) * math.pow((linear_val - .05) * 2, 0.2))) * 100
                return str(round(value, 2)) + '%'


        class facerecognition:
            face_locations = []
            face_encodings = []
            face_names = []
            known_face_encodings = []
            known_face_names = []
            process_current_frame = True

            def __init__(self):
                self.encode_faces()

            def encode_faces(self):
                for image in os.listdir('faces'):
                    face_image = face_recognition.load_image_file(f'faces/{image}')
                    face_encoding = face_recognition.face_encodings(face_image)[0]

                    self.known_face_encodings.append(face_encoding)
                    self.known_face_names.append(image)
                print(self.known_face_names)

            def run_recognition(self):
                video_capture = cv2.VideoCapture(0)
                print('display face to camera, if guest says "unknown", and you are in the system press enter and '
                      'display face again. (sorry, im buggy)')

                if not video_capture.isOpened():
                    sys.exit('video source not found')
                while True:
                    ret, frame = video_capture.read()
                    if self.process_current_frame:
                        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
                        rgb_small_frame = small_frame[:, :, ::-1]

                        self.face_locations = face_recognition.face_locations(rgb_small_frame)
                        self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                        self.face_names = []
                        for face_encoding in self.face_encodings:
                            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                            name = 'unknown'
                            confidence = 'unknown'

                            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                            best_match_index = np.argmin(face_distances)
                            if matches[best_match_index]:
                                name = self.known_face_names[best_match_index]
                                confidence = face_confidence(face_distances[best_match_index])
                            self.face_names.append(f'{name} ({confidence})')
                            if name == 'austin.jpg':
                                request = (input(
                                    "Hello creator, what would you like me to do?"))  # dialogue for user, WORK ON
                                # THIS LATER

                                if request == 'note':  # if what the user requests is this text
                                    import subprocess  # import this for opening programs on comp
                                    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')  # hopefully self-explanatory
                                elif request == 'help':

                                    from tkinter import ttk

                                    win = Tk()  # Create an instance of Tkinter frame
                                    win.geometry("450x120")  # set geometry
                                    from pynput.mouse import Button, \
                                        Controller as MouseControllers  # this imports the automation for mouse
                                    import time
                                    mousee = MouseControllers()
                                    mousee.position = (1355, 1060)
                                    time.sleep(3.5)
                                    mousee.press(
                                        Button.left)
                                    mousee.release(Button.left)
                                    mousee.position = (1355, 1010)
                                    time.sleep(.5)
                                    mousee.press(
                                        Button.left)
                                    mousee.release(Button.left)

                                    def open_popup():
                                        top = Toplevel(win)
                                        top.geometry("500x300")
                                        top.title("help interface")
                                        Label(top,
                                              text='Hello, welcome to my inteface. \n COMMANDS:\n"calc" will open the '
                                                   'calculator\n "raid" will'
                                                   'open plarium for raid \n "grass" just try it \n "rick" my '
                                                   'favorite so far'
                                                   '\n "note" to open'
                                                   'notepad \n NEW try "voice" to open voice commands, consisting of everything in the help folder through voice except their full names.I.E "calculator" \n voice will also be implimenting website opening, such as "facebook.com"', background="black", foreground="white",
                                              font='times_new_roman').place(x=150, y=100)

                                    Label(win,
                                          text='If you need help, press "help" below. \nOtherwise, close this window.',
                                          background="yellow", foreground="red",
                                          font='Helvetica 14 bold').pack(pady=20)
                                    ttk.Button(win, text='HELP',
                                               command=open_popup).pack()  # Create a button in the main Window to
                                    # open the
                                    # popup
                                    win.mainloop()

                                elif request == 'calc':
                                    import subprocess

                                    subprocess.Popen('C:\\Windows\\System32\\calc.exe')
                                    from playsound import playsound

                                    playsound('C:\\Users\\16829\\Desktop\\core.wav')
                                elif request == 'raid':

                                    import subprocess
                                    subprocess.Popen(r'C:\\Users\16829\AppData\Local\PlariumPlay\PlariumPlay.exe')

                                elif request == 'grass':
                                    import time
                                    import webbrowser

                                    webbrowser.open('https://www.youtube.com/watch?v=rtCXYZfRvhI')
                                    from pynput.keyboard import Key, Controller  # this imports the automation for keys

                                    keyboard = Controller()
                                    time.sleep(2)
                                    keyboard.press(' ')
                                elif request == 'voice':
                                    import speech_recognition as sr
                                    import webbrowser as web

                                    if __name__ == "__main__":
                                        path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                                        r = sr.Recognizer()
                                        with sr.Microphone() as source:
                                            r.adjust_for_ambient_noise(source)
                                            print('what would you like?')
                                            audio = r.listen(source)
                                            print("Thinking...")
                                            dest = r.recognize_google(audio)
                                        try:
                                            if dest == "facebook.com":
                                                dest = r.recognize_google(audio)
                                                print("you said:" + dest)
                                                web.register('firefox', None, web.BackgroundBrowser(path))
                                                web.get('firefox').open_new_tab(dest)
                                            if dest == 'notepad':  # if what the user requests is this text
                                                import subprocess  # import this for opening programs on comp
                                                subprocess.Popen(
                                                    'C:\\Windows\\System32\\notepad.exe')  # hopefully self-explanatory
                                            elif dest == 'help':

                                                from tkinter import ttk

                                                win = Tk()  # Create an instance of Tkinter frame
                                                win.geometry("450x120")  # set geometry
                                                from pynput.mouse import Button, \
                                                    Controller as MouseControllers  # this imports the automation for mouse
                                                import time
                                                mouseee = MouseControllers()
                                                mouseee.position = (1355, 1060)
                                                time.sleep(3.5)
                                                mouseee.press(
                                                    Button.left)
                                                mouseee.release(Button.left)
                                                mouseee.position = (1355, 1010)
                                                time.sleep(.5)
                                                mouseee.press(
                                                    Button.left)
                                                mouseee.release(Button.left)

                                                def open_popup():
                                                    top = Toplevel(win)
                                                    top.geometry("500x300")
                                                    top.title("help interface")
                                                    Label(top,
                                                          text='Hello, welcome to my inteface. \n COMMANDS:\n"calc" will open the '
                                                               'calculator\n "raid" will'
                                                               'open plarium for raid \n "grass" just try it \n "rick" my '
                                                               'favorite so far'
                                                               '\n "note" to open'
                                                               'notepad \n NEW type voice to enable voice commands, except for voice try the full name og help indexes I.E "notepad" or "calculator", \n i am also enabling web search like "facebook.com"', background="black", foreground="white",
                                                          font='times_new_roman').place(x=150, y=100)

                                                Label(win,
                                                      text='If you need help, press "help" below. \nOtherwise, close this window.',
                                                      background="yellow", foreground="red",
                                                      font='Helvetica 14 bold').pack(pady=20)
                                                ttk.Button(win, text='HELP',
                                                           command=open_popup).pack()  # Create a button in the main Window to
                                                # open the
                                                # popup
                                                win.mainloop()

                                            elif dest == 'calculator':
                                                import subprocess

                                                subprocess.Popen('C:\\Windows\\System32\\calc.exe')
                                                from playsound import playsound

                                                playsound('C:\\Users\\16829\\Desktop\\core.wav')
                                            elif dest == 'raid':

                                                import subprocess
                                                subprocess.Popen(
                                                    r'C:\\Users\16829\AppData\Local\PlariumPlay\PlariumPlay.exe')

                                            elif dest == 'grass':
                                                import time
                                                import webbrowser

                                                webbrowser.open('https://www.youtube.com/watch?v=rtCXYZfRvhI')
                                                from pynput.keyboard import Key, \
                                                    Controller  # this imports the automation for keys

                                                keyboard = Controller()
                                                time.sleep(2)
                                                keyboard.press(' ')
                                            elif dest == 'search':
                                                msg = input('what would you like to search? (google)')
                                                from pynput.mouse import Button, \
                                                    Controller as MouseControllers  # this imports the automation for mouse
                                                import time
                                                import pyperclip as p
                                                import time
                                                p.copy(msg)
                                                import webbrowser
                                                import keyboard
                                                webbrowser.open('https://google.com')
                                                mousers = MouseControllers()
                                                mousers.position = (940, 480)
                                                time.sleep(1.5)
                                                mousers.press(Button.left)
                                                mousers.release(Button.left)
                                                keyboard.press('ctrl+v')
                                                keyboard.release('ctrl+v')
                                                keyboard.press('enter')
                                                keyboard.release('enter')

                                            elif dest == 'rick':  # the rickest rick ;)
                                                import webbrowser  # defined above
                                                import \
                                                    time  # this is for making an action delayed by time in seconds, the import
                                                # of it
                                                from pynput.keyboard import Key, \
                                                    Controller as KeyboardController  # import automation for the keys "as"
                                                # allows two instances of "controller" without conflict by giving it a nickname
                                                from pynput.mouse import Button, \
                                                    Controller as MouseController  # this imports the automation for mouse

                                                webbrowser.open('https://www.youtube.com')
                                                keyboard = KeyboardController()  # define the keyboard as the keyboard input,
                                                # so it can
                                                # be used
                                                mouse = MouseController()  # same as keyboard define but for the mouse
                                                time.sleep(3)  # the actual action of delaying time by 2 seconds
                                                mouse.position = (835, 100)  # makes the mouse go to these coordinates
                                                mouse.press(
                                                    Button.left)  # make the mouse click,/ adding ,2 will make it click twice/
                                                # intuitive
                                                mouse.release(Button.left)
                                                time.sleep(2)
                                                keyboard.press('R')
                                                time.sleep(.09)
                                                keyboard.press('i')
                                                time.sleep(.09)
                                                keyboard.press('c')
                                                time.sleep(.09)
                                                keyboard.press('k')
                                                time.sleep(.09)
                                                keyboard.press(' ')
                                                time.sleep(.09)
                                                keyboard.press('R')
                                                time.sleep(.09)
                                                keyboard.press('o')
                                                time.sleep(.09)
                                                keyboard.press('l')
                                                time.sleep(.09)
                                                keyboard.press('l')
                                                time.sleep(.09)
                                                keyboard.press(
                                                    Key.enter)  # key. is required before any key you want it to press
                                                keyboard.release(
                                                    Key.enter)  # you need to release the key, so it does not press forever same
                                                # as mouse
                                                time.sleep(2)
                                                mouse.position = (650, 250)
                                                mouse.press(Button.left)
                                                mouse.release(Button.left)

                                        except Exception as e:
                                            print("error:" + str(e))

                                elif request == 'search':
                                    msg = input('what would you like to search? (google)')
                                    from pynput.mouse import Button, \
                                        Controller as MouseControllers  # this imports the automation for mouse
                                    import time
                                    import pyperclip as p
                                    import time
                                    p.copy(msg)
                                    import webbrowser
                                    import keyboard
                                    webbrowser.open('https://google.com')
                                    mousers = MouseControllers()
                                    mousers.position = (940, 480)
                                    time.sleep(1.5)
                                    mousers.press(Button.left)
                                    mousers.release(Button.left)
                                    keyboard.press('ctrl+v')
                                    keyboard.release('ctrl+v')
                                    keyboard.press('enter')
                                    keyboard.release('enter')

                                elif request == 'rick':  # the rickest rick ;)
                                    import webbrowser  # defined above
                                    import \
                                        time  # this is for making an action delayed by time in seconds, the import
                                    # of it
                                    from pynput.keyboard import Key, \
                                        Controller as KeyboardController  # import automation for the keys "as"
                                    # allows two instances of "controller" without conflict by giving it a nickname
                                    from pynput.mouse import Button, \
                                        Controller as MouseController  # this imports the automation for mouse

                                    webbrowser.open('https://www.youtube.com')
                                    keyboard = KeyboardController()  # define the keyboard as the keyboard input,
                                    # so it can
                                    # be used
                                    mouse = MouseController()  # same as keyboard define but for the mouse
                                    time.sleep(3)  # the actual action of delaying time by 2 seconds
                                    mouse.position = (835, 100)  # makes the mouse go to these coordinates
                                    mouse.press(
                                        Button.left)  # make the mouse click,/ adding ,2 will make it click twice/
                                    # intuitive
                                    mouse.release(Button.left)
                                    time.sleep(2)
                                    keyboard.press('R')
                                    time.sleep(.09)
                                    keyboard.press('i')
                                    time.sleep(.09)
                                    keyboard.press('c')
                                    time.sleep(.09)
                                    keyboard.press('k')
                                    time.sleep(.09)
                                    keyboard.press(' ')
                                    time.sleep(.09)
                                    keyboard.press('R')
                                    time.sleep(.09)
                                    keyboard.press('o')
                                    time.sleep(.09)
                                    keyboard.press('l')
                                    time.sleep(.09)
                                    keyboard.press('l')
                                    time.sleep(.09)
                                    keyboard.press(Key.enter)  # key. is required before any key you want it to press
                                    keyboard.release(
                                        Key.enter)  # you need to release the key, so it does not press forever same
                                    # as mouse
                                    time.sleep(2)
                                    mouse.position = (650, 250)
                                    mouse.press(Button.left)
                                    mouse.release(Button.left)
                            else:
                                request = (input(
                                    'hello,' + name + 'type help for an index. \n otherwise, make a request:'))

                                if request == 'note':  # if what the user requests is this text
                                    import subprocess  # import this for opening programs on comp
                                    subprocess.Popen('C:\\Windows\\System32\\notepad.exe')  # hopefully self-explanatory
                                elif request == 'voice':
                                    import speech_recognition as sr
                                    import webbrowser as web

                                    if __name__ == "__main__":
                                        path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
                                        r = sr.Recognizer()
                                        with sr.Microphone() as source:
                                            r.adjust_for_ambient_noise(source)
                                            print('what would you like?')
                                            audio = r.listen(source)
                                            print("Thinking...")
                                            dest = r.recognize_google(audio)
                                        try:
                                            if dest == "facebook.com":
                                                dest = r.recognize_google(audio)
                                                print("you said:" + dest)
                                                web.register('firefox', None, web.BackgroundBrowser(path))
                                                web.get('firefox').open_new_tab(dest)
                                            if dest == 'notepad':  # if what the user requests is this text
                                                import subprocess  # import this for opening programs on comp
                                                subprocess.Popen(
                                                    'C:\\Windows\\System32\\notepad.exe')  # hopefully self-explanatory
                                            elif dest == 'help':

                                                from tkinter import ttk

                                                win = Tk()  # Create an instance of Tkinter frame
                                                win.geometry("450x120")  # set geometry
                                                from pynput.mouse import Button, \
                                                    Controller as MouseControllers  # this imports the automation for mouse
                                                import time
                                                mouseee = MouseControllers()
                                                mouseee.position = (1355, 1060)
                                                time.sleep(3.5)
                                                mouseee.press(
                                                    Button.left)
                                                mouseee.release(Button.left)
                                                mouseee.position = (1355, 1010)
                                                time.sleep(.5)
                                                mouseee.press(
                                                    Button.left)
                                                mouseee.release(Button.left)

                                                def open_popup():
                                                    top = Toplevel(win)
                                                    top.geometry("500x300")
                                                    top.title("help interface")
                                                    Label(top,
                                                          text='Hello, welcome to my inteface. \n COMMANDS:\n"calc" will open the '
                                                               'calculator\n "raid" will'
                                                               'open plarium for raid \n "grass" just try it \n "rick" my '
                                                               'favorite so far'
                                                               '\n "note" to open  \n NEW try "voice" to open voice commands, consisting of everything in the help folder through voice except their full names.I.E "calculator" \n voice will also be implimenting website opening, such as "facebook.com"'
                                                               'notepad', background="black", foreground="white",
                                                          font='times_new_roman').place(x=150, y=100)

                                                Label(win,
                                                      text='If you need help, press "help" below. \nOtherwise, close this window.',
                                                      background="yellow", foreground="red",
                                                      font='Helvetica 14 bold').pack(pady=20)
                                                ttk.Button(win, text='HELP',
                                                           command=open_popup).pack()  # Create a button in the main Window to
                                                # open the
                                                # popup
                                                win.mainloop()

                                            elif dest == 'calculator':
                                                import subprocess

                                                subprocess.Popen('C:\\Windows\\System32\\calc.exe')
                                                from playsound import playsound

                                                playsound('C:\\Users\\16829\\Desktop\\core.wav')
                                            elif dest == 'raid':

                                                import subprocess
                                                subprocess.Popen(
                                                    r'C:\\Users\16829\AppData\Local\PlariumPlay\PlariumPlay.exe')

                                            elif dest == 'grass':
                                                import time
                                                import webbrowser

                                                webbrowser.open('https://www.youtube.com/watch?v=rtCXYZfRvhI')
                                                from pynput.keyboard import Key, \
                                                    Controller  # this imports the automation for keys

                                                keyboard = Controller()
                                                time.sleep(2)
                                                keyboard.press(' ')
                                            elif dest == 'search':
                                                msg = input('what would you like to search? (google)')
                                                from pynput.mouse import Button, \
                                                    Controller as MouseControllers  # this imports the automation for mouse
                                                import time
                                                import pyperclip as p
                                                import time
                                                p.copy(msg)
                                                import webbrowser
                                                import keyboard
                                                webbrowser.open('https://google.com')
                                                mousers = MouseControllers()
                                                mousers.position = (940, 480)
                                                time.sleep(1.5)
                                                mousers.press(Button.left)
                                                mousers.release(Button.left)
                                                keyboard.press('ctrl+v')
                                                keyboard.release('ctrl+v')
                                                keyboard.press('enter')
                                                keyboard.release('enter')

                                            elif dest == 'rick':  # the rickest rick ;)
                                                import webbrowser  # defined above
                                                import \
                                                    time  # this is for making an action delayed by time in seconds, the import
                                                # of it
                                                from pynput.keyboard import Key, \
                                                    Controller as KeyboardController  # import automation for the keys "as"
                                                # allows two instances of "controller" without conflict by giving it a nickname
                                                from pynput.mouse import Button, \
                                                    Controller as MouseController  # this imports the automation for mouse

                                                webbrowser.open('https://www.youtube.com')
                                                keyboard = KeyboardController()  # define the keyboard as the keyboard input,
                                                # so it can
                                                # be used
                                                mouse = MouseController()  # same as keyboard define but for the mouse
                                                time.sleep(3)  # the actual action of delaying time by 2 seconds
                                                mouse.position = (835, 100)  # makes the mouse go to these coordinates
                                                mouse.press(
                                                    Button.left)  # make the mouse click,/ adding ,2 will make it click twice/
                                                # intuitive
                                                mouse.release(Button.left)
                                                time.sleep(2)
                                                keyboard.press('R')
                                                time.sleep(.09)
                                                keyboard.press('i')
                                                time.sleep(.09)
                                                keyboard.press('c')
                                                time.sleep(.09)
                                                keyboard.press('k')
                                                time.sleep(.09)
                                                keyboard.press(' ')
                                                time.sleep(.09)
                                                keyboard.press('R')
                                                time.sleep(.09)
                                                keyboard.press('o')
                                                time.sleep(.09)
                                                keyboard.press('l')
                                                time.sleep(.09)
                                                keyboard.press('l')
                                                time.sleep(.09)
                                                keyboard.press(
                                                    Key.enter)  # key. is required before any key you want it to press
                                                keyboard.release(
                                                    Key.enter)  # you need to release the key, so it does not press forever same
                                                # as mouse
                                                time.sleep(2)
                                                mouse.position = (650, 250)
                                                mouse.press(Button.left)
                                                mouse.release(Button.left)

                                        except Exception as e:
                                            print("error:" + str(e))
                                elif request == 'help':

                                    from tkinter import ttk

                                    win = Tk()  # Create an instance of Tkinter frame
                                    win.geometry("450x120")  # set geometry
                                    from pynput.mouse import Button, \
                                        Controller as MouseControllers  # this imports the automation for mouse
                                    import time
                                    mouseee = MouseControllers()
                                    mouseee.position = (1355, 1060)
                                    time.sleep(3.5)
                                    mouseee.press(
                                        Button.left)
                                    mouseee.release(Button.left)
                                    mouseee.position = (1355, 1010)
                                    time.sleep(.5)
                                    mouseee.press(
                                        Button.left)
                                    mouseee.release(Button.left)

                                    def open_popup():
                                        top = Toplevel(win)
                                        top.geometry("500x300")
                                        top.title("help interface")
                                        Label(top,
                                              text='Hello, welcome to my inteface. \n COMMANDS:\n"calc" will open the '
                                                   'calculator\n "raid" will'
                                                   'open plarium for raid \n "grass" just try it \n "rick" my '
                                                   'favorite so far'
                                                   '\n "note" to open'
                                                   'notepad \n NEW try "voice" to open voice commands, consisting of everything in the help folder through voice except their full names.I.E "calculator" \n voice will also be implimenting website opening, such as "facebook.com"p', background="black", foreground="white",
                                              font='times_new_roman').place(x=150, y=100)

                                    Label(win,
                                          text='If you need help, press "help" below. \nOtherwise, close this window.',
                                          background="yellow", foreground="red",
                                          font='Helvetica 14 bold').pack(pady=20)
                                    ttk.Button(win, text='HELP',
                                               command=open_popup).pack()  # Create a button in the main Window to
                                    # open the
                                    # popup
                                    win.mainloop()

                                elif request == 'calc':
                                    import subprocess

                                    subprocess.Popen('C:\\Windows\\System32\\calc.exe')
                                    from playsound import playsound

                                    playsound('C:\\Users\\16829\\Desktop\\core.wav')
                                elif request == 'raid':

                                    import subprocess
                                    subprocess.Popen(r'C:\\Users\16829\AppData\Local\PlariumPlay\PlariumPlay.exe')

                                elif request == 'grass':
                                    import time
                                    import webbrowser

                                    webbrowser.open('https://www.youtube.com/watch?v=rtCXYZfRvhI')
                                    from pynput.keyboard import Key, Controller  # this imports the automation for keys

                                    keyboard = Controller()
                                    time.sleep(2)
                                    keyboard.press(' ')
                                elif request == 'search':
                                    msg = input('what would you like to search? (google)')
                                    from pynput.mouse import Button, \
                                        Controller as MouseControllers  # this imports the automation for mouse
                                    import time
                                    import pyperclip as p
                                    import time
                                    p.copy(msg)
                                    import webbrowser
                                    import keyboard
                                    webbrowser.open('https://google.com')
                                    mousers = MouseControllers()
                                    mousers.position = (940, 480)
                                    time.sleep(1.5)
                                    mousers.press(Button.left)
                                    mousers.release(Button.left)
                                    keyboard.press('ctrl+v')
                                    keyboard.release('ctrl+v')
                                    keyboard.press('enter')
                                    keyboard.release('enter')

                                elif request == 'rick':  # the rickest rick ;)
                                    import webbrowser  # defined above
                                    import \
                                        time  # this is for making an action delayed by time in seconds, the import
                                    # of it
                                    from pynput.keyboard import Key, \
                                        Controller as KeyboardController  # import automation for the keys "as"
                                    # allows two instances of "controller" without conflict by giving it a nickname
                                    from pynput.mouse import Button, \
                                        Controller as MouseController  # this imports the automation for mouse

                                    webbrowser.open('https://www.youtube.com')
                                    keyboard = KeyboardController()  # define the keyboard as the keyboard input,
                                    # so it can
                                    # be used
                                    mouse = MouseController()  # same as keyboard define but for the mouse
                                    time.sleep(3)  # the actual action of delaying time by 2 seconds
                                    mouse.position = (835, 100)  # makes the mouse go to these coordinates
                                    mouse.press(
                                        Button.left)  # make the mouse click,/ adding ,2 will make it click twice/
                                    # intuitive
                                    mouse.release(Button.left)
                                    time.sleep(2)
                                    keyboard.press('R')
                                    time.sleep(.09)
                                    keyboard.press('i')
                                    time.sleep(.09)
                                    keyboard.press('c')
                                    time.sleep(.09)
                                    keyboard.press('k')
                                    time.sleep(.09)
                                    keyboard.press(' ')
                                    time.sleep(.09)
                                    keyboard.press('R')
                                    time.sleep(.09)
                                    keyboard.press('o')
                                    time.sleep(.09)
                                    keyboard.press('l')
                                    time.sleep(.09)
                                    keyboard.press('l')
                                    time.sleep(.09)
                                    keyboard.press(Key.enter)  # key. is required before any key you want it to press
                                    keyboard.release(
                                        Key.enter)  # you need to release the key, so it does not press forever same
                                    # as mouse
                                    time.sleep(2)
                                    mouse.position = (650, 250)
                                    mouse.press(Button.left)
                                    mouse.release(Button.left)
                    self.process_current_frame = not self.process_current_frame

                    for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                        top *= 4
                        right *= 4
                        left *= 4
                        bottom *= 4

                        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
                        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), -1)
                        cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255),
                                    1)

                    cv2.imshow('face_recognition', frame)
                    if cv2.waitKey(1) == ord('q'):
                        break
                video_capture.release()
                cv2.destroyAllWindows()


        if __name__ == '__main__':
            fr = facerecognition()
            fr.run_recognition()
