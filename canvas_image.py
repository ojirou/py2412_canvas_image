import tkinter as tk
from PIL import ImageTk
class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.title("Image Display")
        self.master.geometry("361x339")
        self.canvas = tk.Canvas(self.master)
        self.canvas.pack(expand = True, fill = tk.BOTH)
        self.photo_image = ImageTk.PhotoImage(file = "ojirou.png")
        self.update()
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        self.canvas.create_image(
                canvas_width / 2,
                canvas_height / 2,    
                image=self.photo_image 
                )
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()