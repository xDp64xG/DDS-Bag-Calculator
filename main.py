import tkinter as tk
from PIL import ImageTk, Image

# var = input("Give a bag number: ")
# var = int(var)


class DDS:
    def __init__(self):
        self.array = ""
        self.lines2 = ""
        self.window = tk.Tk()
        self.window.geometry("599x796")
        self.window.title("DDS Bag Calculator")
        self.window.config(bg="lightgrey")

        #bgdir = "images/bg.jpg"
        #tmpimg = Image.open(bgdir)
        #tmpimg.resize((100, 100),Image.ANTIALIAS)

        #bg = ImageTk.PhotoImage(tmpimg)
        #bg.resize(width=100, height=100)
        #print("BG: {}".format(bg))
        #hmmm
        self.window.attributes('-topmost', True)

        # self.window.attributes('-fullscreen', True)
        self.window.resizable(True, True)

        # Our Frame
        self.content = tk.Frame(self.window, borderwidth=5, relief='ridge')

        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=0)
        self.window.grid_rowconfigure(2, weight=0)
        self.window.grid_rowconfigure(3, weight=0)
        self.window.grid_rowconfigure(4, weight=0)
        self.window.grid_rowconfigure(5, weight=0)

        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_columnconfigure(1, weight=0)
        self.window.grid_columnconfigure(2, weight=0)
        self.window.grid_columnconfigure(3, weight=0)
        self.window.grid_columnconfigure(4, weight=0)
        self.window.grid_columnconfigure(5, weight=0)


        self.content.grid(column=0, row=0, columnspan=4, rowspan=5, sticky=(tk.N + tk.S + tk.E + tk.W))

        self.iconPath = 'images/bg.png'
        self.tmpimg = Image.open(self.iconPath)
        self.size = self.tmpimg.size
        print(self.size)

        #self.tmpimg.resize((self.size[0] * 100), (self.size[1] * 100))
        #self.tmpimg.resize(700, 800)
        self.icon = ImageTk.PhotoImage(self.tmpimg)
        #print(self.icon.size)
        #self.icon_size = tk.Label(self.content)
        #self.icon_size.image = self.icon  # <== this is were we anchor the img object
        #self.icon_size.configure(image=self.icon)
        #self.icon_size.grid()
        self.canvas = tk.Canvas(self.content, height=796, width=599)
        #self.canvas.create_image(300, 275, image=self.icon, anchor = 'center')
        self.canvas.create_image(235, 400, image=self.icon, anchor='center')



        self.canvas.grid(column=0, row=0, columnspan=4, rowspan=5, sticky=(tk.N + tk.S + tk.E + tk.W), padx=5, pady=5)
        """self.bg_canv = tk.Canvas(
                                 width=500,
                                 height=500)
        #self.bg_canv.grid()
        
        self.bg_lbl = tk.Label(master=self.window, image=bg,
                               width=100, height=100)
        self.bg_lbl.grid()
        
        self.bg_lbl.config(image=bg)
        
        self.bg_canv.create_image(20,20, anchor=tk.N, image=bg)"""
        #self.bg_label.grid(column=0, row=0, columnspan=4, rowspan=4, sticky=(tk.N + tk.S + tk.E + tk.W))
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
                         yscrollcommand=v.set)
        self.t.grid(column=2, row=1, rowspan=1, columnspan=1, sticky=(tk.E), padx=15, pady=15)
        self.entry = tk.Text(master=self.canvas,
                             width=25,
                             height=25,
                             fg='black',
                             bg='white',
                             font=('Times New Roman', 11),
                             yscrollcommand=v2.set)

        self.help = ''
        self.refresh = ''
        self.info = ''
        self.exi = ''

        v.config(command=self.t.yview)
        v2.config(command=self.entry.yview)
        self.entry.grid(column=0, row=1, columnspan=1, rowspan=1, sticky=(tk.W), padx=15, pady=15)
        #self.icon_size.pack(side=tk.LEFT)

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
            print(self.window.grid_slaves())
            print(self.content.grid_info())

            print(self.help)
            print(self.refresh)
            print(self.info)
            print(self.exi)
            print(self.entry.grid_info())
            print(self.t.grid_info())

            entry = self.entry
            data = entry.get('1.0', tk.END)
            file1 = open('numbers.txt', 'w')
            file1.writelines(data)
            file1.close()
            var = process()
            self.t.config(state='normal')
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

        template = 'Amp/Fet\n13\nGanja/Grass\n19\nEctasy/Candy\n23\nMeth\n41\nCoke\n11\nHero\n9\n4'
        self.entry.insert(tk.END, template)

        label.grid(column=0, row=0, sticky=tk.NW, padx=15, pady=15)
        refresh.grid(column=0, row=4, pady=5, padx=5, sticky=tk.W)
        exit.grid(column=2, row=4, pady=5, padx=5, sticky=tk.SE)
        output.grid(column=2, row=0, sticky=tk.NE, padx=15, pady=15)

        self.help = label.grid_info()
        self.refresh = refresh.grid_info()
        self.info = output.grid_info()
        self.exi = exit.grid_info()

        self.window.mainloop()


loop = DDS()
loop.main()
