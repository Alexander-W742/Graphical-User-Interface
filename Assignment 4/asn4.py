import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class FoodViewer:
    def __init__(self, root):

        self.root = root
        self.root.title("Food Viewer")
        self.root.geometry("400x300")

        # Frames
        self.img_frame = tk.Frame(self.root)
        self.img_frame.pack()

        self.rbdBtn_frame = tk.Frame(self.root)
        self.rbdBtn_frame.pack()

        # Load Images
        try:
            print("Loading images...")

            self.img1 = Image.open("chicken.jpg").resize((400, 300))
            self.imgOne = ImageTk.PhotoImage(self.img1)

            self.img2 = Image.open("pie.jpg").resize((400, 300))
            self.imgTwo = ImageTk.PhotoImage(self.img2)

            self.img3 = Image.open("pizza.jpg").resize((350, 300))
            self.imgThree = ImageTk.PhotoImage(self.img3)

            self.img4 = Image.open("steak.jpg").resize((300, 300))
            self.imgFour = ImageTk.PhotoImage(self.img4)

            print("Images loaded successfully!")

        except Exception as e:
            print("IMAGE ERROR:", e)

        # Label
        self.lbl = tk.Label(self.img_frame, image = self.imgOne)
        self.lbl.pack()

        # IntVar (init to 1)
        self.var = tk.IntVar()
        self.var.set(1)

        # Radiobuttons
        self.radio_a = tk.Radiobutton(
            self.rbdBtn_frame,
            text = "Chicken",
            variable = self.var,
            value = 1,
            command = self.on_radio_select
        )
        self.radio_a.pack(side = "left", padx = 10)

        self.radio_b = tk.Radiobutton(
            self.rbdBtn_frame,
            text = "Pie",
            variable = self.var,
            value = 2,
            command = self.on_radio_select
        )
        self.radio_b.pack(side = "left", padx = 10)

        self.radio_c = tk.Radiobutton(
            self.rbdBtn_frame,
            text = "Pizza",
            variable = self.var,
            value = 3,
            command = self.on_radio_select
        )
        self.radio_c.pack(side = "left", padx = 10)

        self.radio_d = tk.Radiobutton(
            self.rbdBtn_frame,
            text = "Steak",
            variable = self.var,
            value = 4,
            command = self.on_radio_select
        )
        self.radio_d.pack(side = "left", padx = 10)

    def on_radio_select(self):
        selection = self.var.get()
        images = {
            1: self.imgOne,
            2: self.imgTwo,
            3: self.imgThree,
            4: self.imgFour
        }
        self.lbl.config(image = images[selection])

# run program
if __name__ == "__main__":
    root = tk.Tk()
    app = FoodViewer(root)
    root.mainloop()