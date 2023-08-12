import tkinter as tk
from PIL import ImageTk, Image
import os
import sys


"""
MIT License

Copyright (c) 2023 Paul Brow
"""
# pyinstaller --onefile --icon=images/icon.ico --add-data "images;images" --add-data "LICENSE.txt;." main.py



class BagCalculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("561x668")
        self.window.title("Bag Calculator")
        self.window.config(bg="lightgrey")
        if getattr(sys, 'frozen', False):
            # If the script is run as a standalone executable (frozen)
            base_path = sys._MEIPASS
        else:
            # If the script is run as a regular Python script
            base_path = os.path.abspath(".")

        self.image_path = os.path.join(base_path, "images/bg.png")

        self.initialize_ui()

    def initialize_ui(self):
        self.canvas = tk.Canvas(self.window)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Configure>', self.update_ui_layout)  # Bind event to canvas

        self.load_background_image()

        self.t = tk.Text(master=self.canvas, bg='black', fg='white', height=25, width=25, state='disabled',
                         font=('Segoe UI Black', 10))
        self.t.grid(column=3, row=1, sticky=tk.NE, padx=15, pady=15)

        self.entry = tk.Text(master=self.canvas, width=25, height=25, fg='black', bg='white',
                             font=('Segoe UI Black', 10))
        self.entry.grid(column=0, row=1, sticky=tk.NW, padx=15, pady=15)

        # Create the vertical scrollbars for the text widgets
        v_scrollbar1 = tk.Scrollbar(master=self.canvas, orient='vertical', command=self.entry.yview)
        v_scrollbar2 = tk.Scrollbar(master=self.canvas, orient='vertical', command=self.t.yview)

        self.checkbox_var = tk.IntVar(value=0)
        self.checkbox = tk.Checkbutton(master=self.canvas, text="Transparent", variable=self.checkbox_var,
                                       command=self.toggle_transparency)
        self.checkbox.grid(column=1, row=1, columnspan=2, sticky=tk.N, pady=5)
        self.entry.config(yscrollcommand=v_scrollbar1.set)
        self.t.config(yscrollcommand=v_scrollbar2.set)
        self.initialize_buttons()

    def toggle_transparency(self):
        if self.checkbox_var.get():
            self.window.attributes("-alpha", 0.2)  # Set window transparency to 20%
        else:
            self.window.attributes("-alpha", 1.0)  # Reset window transparency to 100%

    def update_ui_layout(self, event):
        self.update_background_image()

        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # Update the positions of the text boxes
        self.entry.grid(column=0, row=1, sticky=(tk.W, tk.N), padx=15, pady=15)
        self.t.grid(column=2, row=1, sticky=(tk.E, tk.N), padx=15, pady=15)

        # Update the positions of the buttons
        self.refresh_button.grid(column=0, row=4, sticky=(tk.W, tk.S), padx=5, pady=5)
        self.exit_button.grid(column=2, row=4, sticky=(tk.E, tk.S), padx=5, pady=5)

    def load_background_image(self):
        self.background_image = Image.open(self.image_path)
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        self.background_label = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_photo)
        self.update_background_image()

    def update_background_image(self):
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        img_width, img_height = self.background_image.size
        canvas_aspect_ratio = canvas_width / canvas_height
        img_aspect_ratio = img_width / img_height

        if canvas_aspect_ratio > img_aspect_ratio:
            new_width = canvas_width
            new_height = int(new_width / img_aspect_ratio)
        else:
            new_height = canvas_height
            new_width = int(new_height * img_aspect_ratio)

        resized_img = self.background_image.resize((new_width, new_height))
        self.background_photo = ImageTk.PhotoImage(resized_img)

        self.canvas.itemconfig(self.background_label, image=self.background_photo)
        self.canvas.config(width=new_width, height=new_height)

    def initialize_buttons(self):
        self.refresh_button = tk.Button(
            master=self.canvas,
            text="Refresh Data",
            width=15,
            height=5,
            bg="blue",
            fg="red",
            command=self.handle_refresh
        )
        self.refresh_button.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

        self.exit_button = tk.Button(
            master=self.canvas,
            text="Exit",
            width=15,
            height=5,
            bg='black',
            fg='red',
            command=self.on_exit
        )
        self.exit_button.grid(column=3, row=2, sticky=tk.E, padx=5, pady=5)

    def handle_refresh(self):
        data = self.entry.get('1.0', tk.END)
        self.process_data(data)

    def process_data(self, data):
        input_text = self.entry.get('1.0', tk.END)

        output_text = "Current Order List:\n"
        lines = input_text.split("\n")

        bag_sizes = [
            (1, "one"), (2, "two"), (3, "three"), (5, "five"), (10, "ten"),
            (20, "twenty"), (50, "fifty"), (100, "hundred"), (500, "half_k"), (1000, "kilo")
        ]

        for line in lines:
            line = line.strip()
            if line:  # Skip empty lines
                try:
                    var = int(line)
                    output_text += f"--------------------\n{var}\n"
                except ValueError:
                    output_text += f"--------------------\n{line}\n"
                    continue  # Skip the rest of the processing for non-integer lines

                bag = var
                bag_amount = 0  # Initialize the bag amount for the line
                if bag == next((size for size, _ in bag_sizes if size == bag), None):
                    output_text += f"[{var}]: Use a [{var}] gram bag\n"
                else:
                    next_bag_size = next((size for size, _ in bag_sizes if size > bag), None)
                    if next_bag_size:
                        output_text += f"[{var}]: Use a {next_bag_size} gram bag\n"
                        bag_amount = next_bag_size - bag
                        output_text += f"Then put up {bag_amount}\n"
                    else:
                        output_text += "Not enough bag sizes available\n"

        self.t.config(state='normal')
        self.t.delete('1.0', tk.END)
        self.t.insert("1.0", output_text)
        self.t.config(state='disabled')

    def on_exit(self):
        self.window.destroy()

    def run(self):
        #self.load_background_image()
        self.window.mainloop()

if __name__ == "__main__":
    calculator = BagCalculator()
    calculator.run()
