import tkinter as TK
from tkinter import ttk as TTK
import keyboard as KB
import time
import random

class App:
    def __init__(self):
        pass

class Gui:
    def __init__(self, app: App, fonts: [str], width: int, height: int):
        self.app = app
        self.sizeW = width
        self.sizeH = height

        self.mistakes = 2
        self.avagareSpeed = 0

        self.fonts = fonts

        self.keyArray = ["+ěščřžýáíéqwertyuiopasdfghjklzxcvbnm,."]
        self.client = TK.Tk()
        self.client.title("Zav script")
        self.client.geometry(f"{self.sizeW}x{self.sizeH}")
        self.client.resizable(False, False)
        self.client.configure(background="#fff")
        self.main_style = TTK.Style()
        self.main_style.configure("MainFrame", background="#fff")
        self.main_style.configure('MainFrame.TFrame', background='#fff')

        self.main_frame = TTK.Frame(self.client, style="MainFrame.TFrame", padding=10)
        self.main_frame.grid()

        self.label = TTK.Label(self.main_frame, text="Napis sem text", font=self.fonts[1], wraplength=200, anchor="w", justify="left")
        self.label.grid()

        self.inputField = TK.Text(self.main_frame, height=20, width=40, bg="#e5e5e5")
        self.inputField.grid()

        self.label = TTK.Label(self.main_frame, text="Napis prumernou rychlost psani textu v KPS(key per minutes)", font=self.fonts[1], wraplength=200, anchor="w", justify="left")
        self.label.grid()

        self.mistakesInput = TK.Entry(self.main_frame)
        self.mistakesInput.grid()


        self.label = TTK.Label(self.main_frame, text="Napis kolik chces mit chyb", font=self.fonts[1], wraplength=200, anchor="w", justify="left")
        self.label.grid()

        self.mistakesInput = TK.Entry(self.main_frame)
        self.mistakesInput.grid()

        self.button = TTK.Button(self.main_frame, text="Zacit",command = lambda: self.writeTextInTextArea(self.inputField.get("1.0", "end-1c")))
        self.button.grid()

    def Run(self):
        self.client.mainloop()
    def getSelfMistakes(self):
        mistakes = self.mistakesInput.get()
        try:
            mistakes = int(mistakes)
            if type(mistakes) == int:
                self.mistakes = mistakes
            elif mistakes <= 0:
                self.mistakes = 0
        except:
            print("Please write integer number in input field")


    def writeTextInTextArea(self, text):
        time.sleep(2)

        self.getSelfMistakes()
        if self.mistakes <= 0:
            pass
        else:
            for i in range(self.mistakes):
                randomTask = random.randint(1,3)
                randomLetter = random.randint(0,len(text)-1)
                randomLetter2 = random.randint(0,len(text)-1)
                if randomTask == 1:
                    text = text[:randomLetter] + text[randomLetter2] + text[randomLetter + 1:]
                elif randomTask == 2:
                    randomLetter3 = random.randint(0,len(text)-1)
                    text = text[:randomLetter] + text[randomLetter2] + text[randomLetter3] + text[randomLetter + 1:]
                elif randomTask == 3:
                    text = text[:randomLetter] + text[randomLetter + 1:]
        # self.avagareSpeed
        for index, letter in enumerate(text):
            cof = random.randint(1, 4)

            lNumber = 100 * cof
            rNumber = 100 * cof * 1.5
            time.sleep(random.randint(lNumber,rNumber)/1000) 
            KB.write(letter)

app = App()
client = Gui(app, [('Helvetica bold', 14),('Helvetica light', 10), ('Helvetica regular', 12), ('Helvetica bold', 18)], 400, 500)
client.Run()
# Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
# Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy
# Lorem Ipsum i#t simply dummy text of the print nng andntypesetting industry. Lorem Ipsum has been the industry's standarb dummy
