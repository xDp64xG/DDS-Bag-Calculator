import tkinter as tk


# var = input("Give a bag number: ")
# var = int(var)


class DDS:
    def __init__(self):
        self.array = ""
        self.lines2 = ""
        self.window = tk.Tk()

        v = tk.Scrollbar(self.window, orient='vertical')
        v.pack(side=tk.RIGHT, fill='y')
        self.frame_a = tk.Frame(master=self.window, width=75, height=75)
        self.frame_b = tk.Frame(master=self.window, width=50, height=50, bg='black')
        self.frame_c = tk.Frame(master=self.window, width=100, height=100, bg='red')

        self.label = tk.Label(master=self.frame_b,
                              height=75,
                              width=75,
                              bg="black",
                              fg="white",
                              font=("Times New Roman", 15),
                              )
        self.t = tk.Text(self.label, yscrollcommand=v.set)
        self.t.pack(expand=True, fill=tk.BOTH)
        self.t.config(width=50,
                      height=50,
                      bg='black',
                      fg='white',
                      font=("Times New Roman", 15))
        #v.config(command=self.label.yview)

        self.entry = tk.Text(master=self.frame_a,
                             width=50,
                             height=50,
                             fg='black',
                             bg='white')
        v.config(command=self.t.yview)
        # self.numbersR = open('numbers.txt', 'r')
        # self.numbersW = open('numbers.txt', 'w')
        # self.finishedW = open('finished.txt', 'w')

    def main(self):

        array = ""

        def process():
            #If text widget has data, delete and start fresh
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

            # Cycle through text file

            # Switch print to writing to file
            def write(var):
                file2 = open('finished.txt', 'a')
                file2.writelines(var)
                file2.close()

            for i in Lines:
                # print('i: {}'.format(i))
                lines2 += i
                # print(i)
                try:

                    var = int(i)
                    bool = False
                except:
                    var2 = str(i)
                    var = 0
                    # print("--------------------\n{}".format(var2))
                    line += "--------------------\n{}".format(var2)
                    # write(line)
                    bool = True

                if bool == True:
                    pass
                else:
                    # Cycle through all current bag sizes
                    if var < Kilo and var > Half_K or var == Kilo:
                        Bag = var - Kilo
                        if Bag == 0:
                            # print("[{}]: Use a {} gram bag\n".format(var, Kilo))
                            line += "[{}]: Use a {} gram bag\n".format(var, Kilo)
                            # write(line)
                        else:
                            # print("[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Kilo, Bag))
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Kilo, Bag)
                            # write(line)

                    elif var < Half_K and var > Hundred or var == Half_K:
                        Bag = var - Half_K
                        if Bag == 0:
                            # print("[{}]: Use a {} gram bag\n".format(var, Half_K))
                            line += "[{}]: Use a {} gram bag\n".format(var, Half_K)
                            # write(line)
                        else:
                            # print("[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Half_K, Bag))
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Half_K, Bag)
                            # write(line)

                    elif var < Hundred and var > Fifty or var == Hundred:
                        Bag = var - Hundred
                        if Bag == 0:
                            # print("[{}]: Use a {} gram bag\n".format(var, Hundred))
                            line += "[{}]: Use a {} gram bag\n".format(var, Hundred)
                            # write(line)
                        else:
                            # print("[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Hundred, Bag))
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Hundred, Bag)
                            # write(line)

                    elif var < Fifty and var > Twenty or var == Fifty:
                        Bag = var - Fifty
                        if Bag == 0:
                            # print("[{}]: Use a {} gram bag\n".format(var, Fifty))
                            line += "[{}]: Use a {} gram bag\n".format(var, Fifty)
                            # write(line)
                        else:
                            # print("[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Fifty, Bag))
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Fifty, Bag)
                            # write(line)

                    elif var < Twenty and var > Ten or var == Twenty:
                        Bag = var - Twenty
                        if Bag == 0:
                            # print("[{}]: Use a {} gram bag\n".format(var, Twenty))
                            line += "[{}]: Use a {} gram bag\n".format(var, Twenty)
                            # write(line)
                        else:
                            # print("[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Twenty, Bag))
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Twenty, Bag)
                            # write(line)

                    elif var < Ten and var > Five or var == Ten:
                        Bag = var - Ten
                        if Bag == 0:
                            # print("[{}]: Use a {} gram bag\n".format(var, Ten))
                            line += "[{}]: Use a {} gram bag\n".format(var, Ten)
                            # write(line)
                        else:
                            # print("[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Ten, Bag))
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Ten, Bag)
                            # write(line)

                    elif var <= Five and var > Three:
                        Bag = var - Five
                        if Bag == 0:
                            # print("[{}]: Use a {} gram bag\n".format(var, Five))
                            line += "[{}]: Use a {} gram bag\n".format(var, Five)
                            # write(line)
                        else:
                            # print("[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Five, Bag))
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Five, Bag)
                            # write(line)

                    else:
                        if var == 3:
                            # print("[{}]: Use a 3 gram bag\n".format(var))
                            line += "[{}]: Use a 3 gram bag\n".format(var)
                            # write(line)

                        elif var == 2:
                            # print("[{}]: Use a 2 gram bag\n".format(var))
                            line += "[{}]: Use a 2 gram bag\n".format(var)
                            # write(line)

                        else:
                            if var == 1:
                                # print("[{}]: Use a 1 gram bag\n".format(var))
                                line += "[{}]: Use a 1 gram bag\n".format(var)
                                # write(line)
                            else:
                                pass
            file1.close()
            print("Finished. Check 'finished.txt'")
            # print(line)

            write(line)
            self.lines2 = lines2
            self.array = array
            file2.close()
            return line

        def handle_click2():
            print("2nd button clicked")
            entry = self.entry
            data = entry.get('1.0', tk.END)
            file1 = open('numbers.txt', 'w')
            file1.writelines(data)
            file1.close()
            var = process()
            try:
                #self.label.config(text=var)
                self.t.insert("1.0", var)
                #self.t.config(text=var)
                #self.t.pack(master=self.frame_b)
            except:
                print("Unable to config label")

            self.label.pack()

        def on_exit():
            print("Exiting...")
            window = self.window
            window.destroy()

        line = process()
        array = ""
        array = line

        window = self.window
        label = tk.Label(
            master=self.frame_a,
            text="Welcome to DDS Bag Calculator.\nUse the template and put \n"
                 "in your order numbers corresponding\n"
                 " to each category and hit refresh on the far right!")

        button2 = tk.Button(
            master=self.frame_c,
            text="Refresh Data",
            width=15,
            height=5,
            bg="blue",
            fg="red",
            command=handle_click2
        )

        button3 = tk.Button(
            master=self.frame_c,
            text="Exit",
            width=15,
            height=5,
            bg='black',
            fg='red',
            command=on_exit
        )
        entry = self.entry
        template = 'Amp/Fet\n13\nGanja/Grass\n19\nEctasy/Candy\n23\nMeth\n41\nCoke\n11\nHero\n9\n4'
        # entry = tk.Text()
        entry.insert(tk.END, template)

        label.pack()
        entry.pack()

        button2.pack()
        button3.pack()
        # label = tk.Label(text=array)
        # label.pack()
        self.frame_a.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.frame_b.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.frame_c.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        window.mainloop()

loop = DDS()
loop.main()

# foundation
