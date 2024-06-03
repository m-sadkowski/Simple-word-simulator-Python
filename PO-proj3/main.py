import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk
from Punkt import Punkt
from Swiat import Swiat

# Constants
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900
ENTITY_SIZE = 32

class WorldSimulatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Symulator świata")
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")

        self.strzalka = -1
        self.swiat = None

        # Images
        self.symbolZdjecia = {
            'C': self.wczytajObrazy('Assets/czlowiek.jpg'),
            'A': self.wczytajObrazy('Assets/antylopa.jpg'),
            'b': self.wczytajObrazy('Assets/barszcz.jpg'),
            'X': self.wczytajObrazy('Assets/cyberowca.jpg'),
            'g': self.wczytajObrazy('Assets/guarana.jpg'),
            'L': self.wczytajObrazy('Assets/lis.jpg'),
            'm': self.wczytajObrazy('Assets/mlecz.jpg'),
            'O': self.wczytajObrazy('Assets/owca.jpg'),
            't': self.wczytajObrazy('Assets/trawa.jpg'),
            'W': self.wczytajObrazy('Assets/wilk.jpg'),
            'Z': self.wczytajObrazy('Assets/zolw.jpg'),
            'w': self.wczytajObrazy('Assets/jagody.jpg')
        }
        self.ziemiaImg = self.wczytajObrazy('Assets/grass.jpg')

        # Create a frame for the canvas and scrollbars
        self.canvas_frame = tk.Frame(self)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)

        # Create horizontal and vertical scrollbars
        self.h_scrollbar = tk.Scrollbar(self.canvas_frame, orient=tk.HORIZONTAL)
        self.h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        self.v_scrollbar = tk.Scrollbar(self.canvas_frame, orient=tk.VERTICAL)
        self.v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create the canvas
        self.canvas = tk.Canvas(self.canvas_frame, width=SCREEN_WIDTH, height=SCREEN_HEIGHT - 200, bg='black', xscrollcommand=self.h_scrollbar.set, yscrollcommand=self.v_scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.h_scrollbar.config(command=self.canvas.xview)
        self.v_scrollbar.config(command=self.canvas.yview)

        self.frame_komunikaty = tk.Frame(self, width=SCREEN_WIDTH, height=200)
        self.frame_komunikaty.pack(side=tk.BOTTOM, fill=tk.X)
        self.scrollbar = tk.Scrollbar(self.frame_komunikaty)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_komunikaty = tk.Text(self.frame_komunikaty, wrap=tk.WORD, yscrollcommand=self.scrollbar.set, state=tk.DISABLED, font=("Bahnschrift", 12))
        self.text_komunikaty.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.text_komunikaty.yview)

        self.ekranPowitalny()

        self.bind("<KeyPress>", self.wcisniecieKlawisza)
        self.bind("<Button-1>", self.klikniecieMyszki)

    def wczytajObrazy(self, path):
        image = Image.open(path)
        image = image.resize((ENTITY_SIZE, ENTITY_SIZE), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)

    def ekranPowitalny(self):
        self.canvas.delete("all")
        self.rysujPrzyciski(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - ENTITY_SIZE * 4, "Nowa gra", self.nowySwiat)
        self.rysujPrzyciski(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, "Wczytaj gre", self.wczytajSwiat)

    def rysujPrzyciski(self, x, y, text, command):
        button = tk.Button(self, text=text, command=command, bg = 'black', fg = 'white', font=("Bahnschrift", 16))
        self.canvas.create_window(x, y, window=button)

    def nowySwiat(self):
        para = self.wczytajRozmiar()
        self.swiat = Swiat(para.x, para.y)
        self.swiat.generujSwiat()
        self.rysujSwiat()

    def wczytajSwiat(self):
        self.wczytajZapis()

    def rysujSwiat(self):
        self.canvas.delete("all")
        MARGIN = ENTITY_SIZE * 12

        self.text_komunikaty.config(state=tk.NORMAL)
        self.text_komunikaty.delete('1.0', tk.END)
        self.text_komunikaty.insert(tk.END, '\n')
        for komunikat in reversed(self.swiat.komunikaty):
            self.text_komunikaty.insert(tk.END, '\t' + komunikat + '\n')
        self.text_komunikaty.config(state=tk.DISABLED)
        self.text_komunikaty.see(tk.END)

        canvas_width = self.swiat.getSzerokosc() * ENTITY_SIZE + MARGIN * 2
        canvas_height = self.swiat.getWysokosc() * ENTITY_SIZE + MARGIN

        self.canvas.config(scrollregion=(0, 0, canvas_width, canvas_height))

        for i in range(self.swiat.getWysokosc()):
            for j in range(self.swiat.getSzerokosc()):
                organizm = self.swiat.getOrganizm(i, j)
                x = MARGIN + j * ENTITY_SIZE
                y = ENTITY_SIZE + i * ENTITY_SIZE
                if organizm:
                    image = self.symbolZdjecia.get(organizm.getSymbol())
                    if image:
                        self.canvas.create_image(x, y, image=image, anchor='nw')
                else:
                    self.canvas.create_image(x, y, image=self.ziemiaImg, anchor='nw')

        self.przyciskiZapiszWczytaj()

    def wyswietlTekst(self, text, x, y, color="white"):
        self.canvas.create_text(x, y, text=text, fill=color, font=("Helvetica", 16))

    def przyciskiZapiszWczytaj(self):
        self.rysujPrzyciski(ENTITY_SIZE * 6, SCREEN_HEIGHT / 2 - ENTITY_SIZE * 4, "Zapisz",
                            lambda: self.zapiszSwiat(self.swiat))
        self.rysujPrzyciski(ENTITY_SIZE * 6, SCREEN_HEIGHT / 2, "Wczytaj", self.wczytajZapis)

    def zapiszSwiat(self, swiat):
        input_text = simpledialog.askstring("Zapisz stan gry", "Podaj nazwę do zapisania:")
        if input_text:
            swiat.zapiszSwiat(input_text)
            self.rysujSwiat()

    def wczytajZapis(self):
        from Fabryka import wczytaj_swiat
        input_text = simpledialog.askstring("Wczytaj stan gry", "Podaj nazwę zapisu:")
        if input_text:
            swiat = wczytaj_swiat(input_text)
            if swiat:
                self.swiat = swiat
                self.rysujSwiat()

    def wczytajRozmiar(self):
        rozmiar = simpledialog.askstring("Wymiary świata",
                                         "Podaj wysokość i szerokość oddzielone przecinkiem (np. 10, 20):")
        if rozmiar:
            wysokosc, szerokosc = map(int, rozmiar.split(","))
            return Punkt(wysokosc, szerokosc)
        else:
            return None

    def wcisniecieKlawisza(self, event):
        if self.swiat:
            if event.keysym == "Up":
                self.strzalka = 0
            elif event.keysym == "Down":
                self.strzalka = 1
            elif event.keysym == "Left":
                self.strzalka = 2
            elif event.keysym == "Right":
                self.strzalka = 3
            elif event.keysym == "Control_L":
                self.strzalka = 4
            elif event.keysym == "Control_R":
                self.zapiszSwiat(self.swiat)
            elif event.keysym == "Escape":
                self.destroy()

            if self.strzalka != -1:
                self.swiat.wykonajTure(self.strzalka)
                self.rysujSwiat()
                self.strzalka = -1

    def klikniecieMyszki(self, event):
        if self.swiat:
            if ENTITY_SIZE * 2 < event.x < ENTITY_SIZE * 10 and SCREEN_HEIGHT / 2 - ENTITY_SIZE * 4 < event.y < SCREEN_HEIGHT / 2 - ENTITY_SIZE * 2:
                self.zapiszSwiat(self.swiat)
            elif ENTITY_SIZE * 2 < event.x < ENTITY_SIZE * 10 and SCREEN_HEIGHT / 2 < event.y < SCREEN_HEIGHT / 2 + ENTITY_SIZE * 2:
                self.swiat = self.wczytajZapis()


if __name__ == "__main__":
    app = WorldSimulatorApp()
    app.mainloop()
