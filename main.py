import tkinter as tk
from PIL import ImageTk, Image
import os
# var = input("Give a bag number: ")
# var = int(var)


class DDS:
    def __init__(self):

        def resource_path(relative_path):
            """ Get absolute path to resource, works for dev and for PyInstaller """
            try:
                # PyInstaller creates a temp folder and stores path in _MEIPASS
                base_path = sys._MEIPASS
            except Exception:
                base_path = os.path.abspath(".")

            return os.path.join(base_path, relative_path)

        self.array = ""
        self.input = ""
        self.output = ""


        self.lines2 = ""
        self.window = tk.Tk()
        self.window.geometry("561x668")
        #self.window.geometry("599x796")
        self.window.title("DDS Bag Calculator")
        self.window.config(bg="lightgrey")

        self.window.attributes('-topmost', True)

        # self.window.attributes('-fullscreen', True)
        self.window.resizable(True, True)

        # Our Frame
        self.content = tk.Frame(self.window, borderwidth=5, relief='ridge')

        self.window.grid_rowconfigure(0, weight=1)
        """self.window.grid_rowconfigure(1, weight=0)
        self.window.grid_rowconfigure(2, weight=0)
        self.window.grid_rowconfigure(3, weight=0)
        self.window.grid_rowconfigure(4, weight=0)
        self.window.grid_rowconfigure(5, weight=0)"""

        self.window.grid_columnconfigure(0, weight=1)
        """self.window.grid_columnconfigure(1, weight=0)
        self.window.grid_columnconfigure(2, weight=0)
        self.window.grid_columnconfigure(3, weight=0)
        self.window.grid_columnconfigure(4, weight=0)
        self.window.grid_columnconfigure(5, weight=0)"""


        self.content.grid(column=0, row=0, columnspan=5, rowspan=5, sticky=(tk.N + tk.S + tk.E + tk.W))

        self.iconPath = resource_path('images/bg.png')
        self.tmpimg = Image.open(self.iconPath)
        self.size = self.tmpimg.size
        print(self.size)

        self.icon = ImageTk.PhotoImage(self.tmpimg)

        self.canvas = tk.Canvas(self.content, height=796, width=599)
        #self.canvas.create_image(300, 275, image=self.icon, anchor = 'center')
        self.canvas.create_image(235, 400, image=self.icon, anchor='center')

        def event(event):
            print(event.height)
            #print(self)
            """screen_width = event.width
            screen_height = event.height
            self.canvas.config(height=screen_height, width=screen_width)
            self.tmpimg.resize((screen_width, screen_height), Image.LANCZOS)
            self.tmpimg.save(self.iconPath)
            self.icon = ImageTk.PhotoImage(self.tmpimg)
            self.canvas.create_image(235, 400, image=self.icon, anchor='center')

            #self.canvas.create_image(235,400, image=self.icon, anchor='center')
            for x in range(5):
                self.content.columnconfigure(x, weight=1)
                self.content.columnconfigure(x, weight=1)"""

            #self.window.grid()
            #self.window.geometry("{}x{}".format)

            print("Configure")

        self.window.bind('<Configure>', event, add=self.window)




        self.canvas.grid(column=0, row=0, columnspan=4, rowspan=5, sticky=(tk.N + tk.S + tk.E + tk.W), padx=5, pady=5)
        # Our scrollbar
        v = tk.Scrollbar(self.window, orient='vertical')
        v2 = tk.Scrollbar(self.window, orient='vertical')
        v.grid(column=5, row=1, rowspan=2)
        v2.grid(column=0, row=1, rowspan=2, sticky=(tk.NW + tk.SW))
        # Self t is output
        self.t = tk.Text(master=self.canvas,
                         bg='black',
                         fg='white',
                         height=25,
                         width=25,
                         state='disabled',
                         font=('Segoe UI Black', 10),
                         yscrollcommand=v.set)
        self.t.grid(column=2, row=1, rowspan=1, columnspan=1, sticky=(tk.E), padx=15, pady=15)
        self.entry = tk.Text(master=self.canvas,
                             width=25,
                             height=25,
                             fg='black',
                             bg='white',
                             font=('Segoe UI Black', 10),
                             yscrollcommand=v2.set)

        self.help = ''
        self.refresh = ''
        self.info = ''
        self.exi = ''

        v.config(command=self.t.yview)
        v2.config(command=self.entry.yview)
        self.entry.grid(column=0, row=1, columnspan=1, rowspan=1, sticky=(tk.W), padx=15, pady=15)
        #self.icon_size.pack(side=tk.LEFT)

        """def resize(event):

            pixelX = self.window.winfo_width() - yscrollbar.winfo_width()
            pixelY = self.window.winfo_height()
            LB["width"] = int(round(pixelX / h[1]))
            LB["height"] = int(round(pixelY / h[0]))"""


    def main(self):

        array = ""

        def process():
            # If text widget has data, delete and start fresh
            try:
                self.t.delete("1.0", tk.END)
            except:
                print("No text or failed to delete contents.")

            var = 0
            var2 = ""
            line = "Current Order List:\n"
            Kilo = int(1000)
            Half_K = int(500)
            Hundred = int(100)
            Fifty = int(50)
            Twenty = int(20)
            Ten = int(10)
            Five = int(5)
            Three = int(3)
            Two = int(2)
            One = int(1)
            Bag = 0
            bool = True

            file2 = open('finished.txt', 'w+')
            file2.writelines(line)
            # Use text file to input your orders, or test it out yourself!

            try:
                file1 = open('numbers.txt', 'r+')
            except:
                file1 = open('numbers.txt', 'w+')
                file1.close()
                file1 = open('numbers.txt', 'r')

            Lines = file1.readlines()
            lines2 = ""

            # Switch print to writing to file
            def write(var):
                file2 = open('finished.txt', 'a')
                file2.writelines(var)
                file2.close()

            # Cycle through text file
            for i in Lines:
                lines2 += i
                try:
                    var = int(i)
                    bool = False
                except:
                    var2 = str(i)
                    var = 0
                    line += "--------------------\n{}".format(var2)
                    bool = True

                if bool == True:
                    pass
                else:
                    # Cycle through all current bag sizes
                    if Kilo > var > Half_K or var == Kilo:
                        Bag = var - Kilo
                        if Bag == 0:
                            line += "[{}]: Use a {} gram bag\n".format(var, Kilo)
                        else:
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Kilo, Bag)
                    elif Half_K > var > Hundred or var == Half_K:
                        Bag = var - Half_K
                        if Bag == 0:
                            line += "[{}]: Use a {} gram bag\n".format(var, Half_K)
                        else:
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Half_K, Bag)
                    elif Hundred > var > Fifty or var == Hundred:
                        Bag = var - Hundred
                        if Bag == 0:
                            line += "[{}]: Use a {} gram bag\n".format(var, Hundred)
                        else:
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Hundred, Bag)

                    elif Fifty > var > Twenty or var == Fifty:
                        Bag = var - Fifty
                        if Bag == 0:
                            line += "[{}]: Use a {} gram bag\n".format(var, Fifty)
                        else:
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Fifty, Bag)
                    elif Twenty > var > Ten or var == Twenty:
                        Bag = var - Twenty
                        if Bag == 0:
                            line += "[{}]: Use a {} gram bag\n".format(var, Twenty)
                        else:
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Twenty, Bag)
                    elif Ten > var > Five or var == Ten:
                        Bag = var - Ten
                        if Bag == 0:
                            line += "[{}]: Use a {} gram bag\n".format(var, Ten)
                        else:
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Ten, Bag)
                    elif Five >= var > Three:
                        Bag = var - Five
                        if Bag == 0:
                            line += "[{}]: Use a {} gram bag\n".format(var, Five)
                        else:
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Five, Bag)
                    else:
                        if var == 3:
                            line += "[{}]: Use a 3 gram bag\n".format(var)
                        elif var == 2:
                            line += "[{}]: Use a 2 gram bag\n".format(var)
                        else:
                            if var == 1:
                                line += "[{}]: Use a 1 gram bag\n".format(var)
                            else:
                                pass
            file1.close()
            # print("Finished. Check 'finished.txt'")

            write(line)
            self.lines2 = lines2
            self.array = array
            file2.close()
            return line

        def handle_click2():
            print("2nd button clicked")
            """print(self.window.grid_slaves())
            print(self.content.grid_info())

            print(self.help)
            print(self.refresh)
            print(self.info)
            print(self.exi)
            print(self.entry.grid_info())
            print(self.t.grid_info())"""

            entry = self.entry
            data = entry.get('1.0', tk.END)
            file1 = open('numbers.txt', 'w')
            file1.writelines(data)
            file1.close()
            var = process()
            self.t.config(state='normal')
            #Get width and height for current window
            """
            wid = self.window.winfo_width()
            hei = self.window.winfo_height()
            screen_width = self.window.winfo_screenwidth()
            screen_height = self.window.winfo_screenheight()
            print("Width: {}\nHeight: {}".format(wid, hei))"""

            try:
                self.t.delete('1.0', tk.END)
                self.t.insert("1.0", var)
            except:
                print("Unable to config label")

            self.t.grid(column=2, row=1, rowspan=2, columnspan=3, sticky=(tk.E))
            self.t.config(state='disabled')

        def on_exit():
            print("Exiting...")
            window = self.window
            window.destroy()

        line = process()
        array = ""
        array = line
        label = tk.Label(
            master=self.canvas,
            text="Welcome to DDS Bag Calculator.\nUse the template and put \n"
                 "in your order numbers corresponding\n"
                 " to each category and hit refresh on the far right!")

        output = tk.Label(master=self.canvas,
                          text="Fill in your order on the left and hit\n"
                               " the refresh button. Below shows how\n"
                               " to get each order")

        refresh = tk.Button(
            master=self.canvas,
            text="Refresh Data",
            width=15,
            height=5,
            bg="blue",
            fg="red",
            command=handle_click2
        )

        exit = tk.Button(
            master=self.canvas,
            text="Exit",
            width=15,
            height=5,
            bg='black',
            fg='red',
            command=on_exit
        )

        var = tk.StringVar()
        #If checkbox is clicked, make window transparent
        def com():
            #print("This has been checked.")
            check = var.get()

            if int(check) == 0:
                self.window.attributes('-alpha', 0.5)
            else:
                self.window.attributes('-alpha', 1.0)
            #print(self)

        trans = tk.Checkbutton(master=self.content,
                               width=7,
                               height=5,
                               text="Check here ",
                               command=com,
                               variable=var,
                               onvalue='1',
                               offvalue='0')


        template = 'Amp/Fet\n13\nGanja/Grass\n19\nEctasy/Candy\n23\nMeth\n41\nCoke\n11\nHero\n9\n4'
        self.entry.insert(tk.END, template)

        label.grid(column=0, row=0, sticky=tk.NW, padx=15, pady=15)
        refresh.grid(column=0, row=4, pady=5, padx=5, sticky=tk.W)
        exit.grid(column=2, row=4, pady=5, padx=5, sticky=tk.SE)
        output.grid(column=2, row=0, sticky=tk.NE, padx=15, pady=15)
        trans.grid(column=2, row=4, padx=2, pady=2, sticky=tk.SW)

        self.help = label.grid_info()
        self.refresh = refresh.grid_info()
        self.info = output.grid_info()
        self.exi = exit.grid_info()

        self.window.mainloop()


loop = DDS()
loop.main()
