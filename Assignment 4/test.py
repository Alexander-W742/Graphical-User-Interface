import tkinter as tk

class FoodViewer:
    def __init__(self, root):
        print("Constructor entered")
        self.root = root

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodViewer(root)
    root.mainloop()