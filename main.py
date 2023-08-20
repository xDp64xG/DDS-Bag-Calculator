import tkinter as tk
from tkinter import font
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import sys
import json

"""
MIT License

Copyright (c) 2023 Paul Brow
"""
# pyinstaller --onefile --icon=images/icon.ico --add-data "images;images" --add-data "LICENSE.txt;." main.py

class BagCalculator:
    def __init__(self):
        self.options = {}
        self.filename = ""
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
        self.DEFAULT_OPTIONS = {
            "Transparency": 0.2,
            "Font": "Segoe UI Black",
            "Template": "gimme orders...",
            "FontSize": 10,
            "Bg": self.image_path
        }
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
        # Create a new checkbox for 'Stay on Top'
        self.stay_on_top_var = tk.IntVar(value=0)
        self.stay_on_top_checkbox = tk.Checkbutton(
            master=self.canvas,
            text="Stay on Top",
            variable=self.stay_on_top_var,
            command=self.toggle_stay_on_top
        )
        self.stay_on_top_checkbox.grid(column=2, row=3, sticky=tk.S, pady=5)

        self.checkbox.grid(column=0, row=3, sticky=tk.E, pady=5)
        self.entry.config(yscrollcommand=v_scrollbar1.set)
        self.t.config(yscrollcommand=v_scrollbar2.set)
        self.initialize_buttons()

    def toggle_stay_on_top(self):
        if self.stay_on_top_var.get():
            self.window.attributes("-topmost", 1)  # Make the window stay on top
        else:
            self.window.attributes("-topmost", 0)  # Allow the window to be moved behind other windows


    def toggle_transparency(self):
        if self.checkbox_var.get():
            transparency = self.options.get("Transparency", .2)
            self.window.attributes("-alpha", transparency)  # Set window transparency to 20%
        else:
            self.window.attributes("-alpha", 1.0)  # Reset window transparency to 100%

    def update_ui_layout(self, event):
        new_width = self.canvas.winfo_width()
        new_height = self.canvas.winfo_height()

        # Resize background image
        resized_img = self.background_image.resize((new_width, new_height), Image.ANTIALIAS)
        self.background_image_tk = ImageTk.PhotoImage(resized_img)
        self.canvas.create_image(0, 0, image=self.background_image_tk, anchor='nw')

        # Update text box and entry positions
        self.canvas.grid_rowconfigure(1, weight=1)
        self.canvas.grid_columnconfigure(1, weight=1)
        self.t.grid(row=1, column=2, sticky=tk.NE, padx=15, pady=15)
        self.entry.grid(row=1, column=0, sticky=tk.NW, padx=15, pady=15)

    def load_background_image(self):

        #Add custom background path...maybe to image folder?
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
        self.exit_button.grid(column=2, row=2, sticky=tk.E, padx=5, pady=5)

        self.setting = tk.Button(
            master=self.canvas,
            text="Settings",
            width=15,
            height=5,
            bg="grey",
            fg="black",
            command=self.settings_
        )
        self.setting.grid(column=1, row=2, sticky=tk.S, padx=5, pady=5)

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
                    output_text += f"--------------------\n\n"
                except ValueError:
                    output_text += f"--------------------\n{line}\n"
                    continue  # Skip the rest of the processing for non-integer lines

                bag = var
                bag_amount = 0  # Initialize the bag amount for the line
                if bag == next((size for size, _ in bag_sizes if size == bag), None):
                    output_text += f"[{var} grams]: Use a [{var}] gram bag\n"
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

    def settings_(self):
        new_window = tk.Toplevel(self.window)
        new_window.title("Settings")

        # Add a scrollbar to select transparency
        transparency_label = tk.Label(new_window, text="Transparency:")
        transparency_label.pack()
        transparency_scrollbar = tk.Scale(new_window, from_=0.2, to=1.0, resolution=0.2, orient="horizontal")
        transparency_scrollbar.set(self.options.get("Transparency"))
        transparency_scrollbar.pack()

        # Add font options dropdown
        font_label = tk.Label(new_window, text="Font:")
        font_label.pack()
        fonts = ("Arial", "Times New Roman", "Segoe UI", "Calibri", "Verdana")
        font_var = tk.StringVar(value=self.options.get("Font"))
        #font_var.set(fonts[0])

        font_dropdown = tk.OptionMenu(new_window, font_var, *fonts)
        font_dropdown.pack()

        # Add font size options for input and output text widgets
        font_size_label = tk.Label(new_window, text="Font Size:")
        font_size_label.pack()
        ####
        font_size_var = tk.IntVar(value=self.options.get("FontSize"))
        font_size_entry = tk.Entry(new_window, textvariable=font_size_var)
        font_size_entry.pack()

        # Add a button to apply font size changes

        save_text_label = tk.Label(new_window, text="Save Text:")
        save_text_label.pack()
        save_textbox = tk.Text(new_window, width=30, height=5)
        save_textbox.insert(tk.END, "{}".format(self.options.get("Template")))
        save_textbox.pack()
        #If button pressed, select img
        def get_file():
            filename = filedialog.askopenfilename(
            parent=new_window,
            title="Browse File"
        )
            self.filename = filename

        bg_file = tk.Button(new_window, text="Choose your own background image", command=get_file)
        bg_file.pack()

        # Add a button to save options
        def save_options():
            options = {
                "Transparency": transparency_scrollbar.get(),
                "Font": font_var.get(),
                "FontSize": font_size_var.get(),
                "Template": save_textbox.get("1.0", tk.END).strip(),
                "Bg": self.filename
            }
            with open("options.json", "w") as json_file:
                json.dump(options, json_file, indent=4)
                self.apply_options(options)
                self.options = options

        save_button = tk.Button(new_window, text="Save Options", command=save_options)
        save_button.pack()

        def default_():
            self.options = self.DEFAULT_OPTIONS
            self.apply_options(self.options)
        reset_button = tk.Button(new_window, text='Reset to default', command=default_)
        reset_button.pack()

        #Make a default button

    def apply_options(self, options):

        if "FontSize" in options:
            font_size = options["FontSize"]
            #Just use 1, font_update = [], self.[].config(font=font_update
            input_font = font.Font(family=options["Font"], size=font_size)
            output_font = font.Font(family=options["Font"], size=font_size)
            self.entry.config(font=input_font)
            self.t.config(font=output_font)

        if "Template" in options:
            template_text = options["Template"]
            self.entry.delete("1.0", tk.END)
            self.entry.insert("1.0", template_text)
        if "Bg" in options:
            self.image_path = options["Bg"]
            self.load_background_image()
        for key, value in self.DEFAULT_OPTIONS.items():
            if key not in options:
                options[key] = value

    def load_options(self):
        try:
            with open("options.json", "r") as json_file:
                self.options = json.load(json_file)
        except FileNotFoundError:
            self.options = self.DEFAULT_OPTIONS
        except json.JSONDecodeError:
            self.options = self.DEFAULT_OPTIONS

        self.apply_options(self.options)

        if self.options != self.DEFAULT_OPTIONS:
            with open("options.json", "w") as json_file:
                json.dump(self.options, json_file, indent=4)


    def run(self):
        #self.load_background_image()
        self.load_options()
        self.window.mainloop()

if __name__ == "__main__":
    calculator = BagCalculator()
    calculator.run()
