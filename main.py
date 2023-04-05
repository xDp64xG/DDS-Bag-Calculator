import tkinter as tk

#var = input("Give a bag number: ")
#var = int(var)


class DDS:
    def __init__(self):
        self.array = ""
        self.lines2 = ""
        self.window = tk.Tk()
        self.entry = tk.Text()
        self.numbersR = open('numbers.txt', 'r')
        self.numbersW = open('numbers.txt', 'w')
        self.finishedW = open('finished.txt', 'w')

    def main(self):

        array = ""

        def process():

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

            #file2 = open('finished.txt', 'w')

            #self.finishedW.writelines(line)
            file2 = open('finished.txt', 'w')
            file2.writelines(line)
            #Use text file to input your orders, or test it out yourself!
            file1 = open('numbers.txt')

            #file1 = self.numbersR

            #Lines = file1.readlines()
            Lines = file1.readlines()
            #print("Lines: {}".format(Lines))
            lines2 = ""
            #print(Lines)
            #Cycle through text file

            #Switch print to writing to file
            def write(var):
                file2 = open('finished.txt', 'a')
                file2.writelines(var)
                file2.close()


            for i in Lines:
                #print('i: {}'.format(i))
                lines2 += i
                #print(i)
                try:

                    var = int(i)
                    bool = False
                except:
                    var2 = str(i)
                    var = 0
                    #print("--------------------\n{}".format(var2))
                    line += "--------------------\n{}".format(var2)
                    #write(line)
                    bool = True

                if bool == True:
                    pass
                else:
                    #Cycle through all current bag sizes
                    if var < Kilo and var > Half_K or var == Kilo:
                        Bag = var - Kilo
                        if Bag == 0:
                            #print("[{}]: Use a {} gram bag\n".format(var, Kilo))
                            line += "[{}]: Use a {} gram bag\n".format(var, Kilo)
                            #write(line)
                        else:
                            #print("[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Kilo, Bag))
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Kilo, Bag)
                            #write(line)

                    elif var < Half_K and var > Hundred or var == Half_K:
                        Bag = var - Half_K
                        if Bag == 0:
                            #print("[{}]: Use a {} gram bag\n".format(var, Half_K))
                            line += "[{}]: Use a {} gram bag\n".format(var, Half_K)
                            #write(line)
                        else:
                            #print("[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Half_K, Bag))
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Half_K, Bag)
                            #write(line)

                    elif var < Hundred and var > Fifty or var == Hundred:
                        Bag = var - Hundred
                        if Bag == 0:
                            #print("[{}]: Use a {} gram bag\n".format(var, Hundred))
                            line += "[{}]: Use a {} gram bag\n".format(var, Hundred)
                            #write(line)
                        else:
                            #print("[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Hundred, Bag))
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Hundred, Bag)
                            #write(line)

                    elif var < Fifty and var > Twenty or var == Fifty:
                        Bag = var - Fifty
                        if Bag == 0:
                            #print("[{}]: Use a {} gram bag\n".format(var, Fifty))
                            line += "[{}]: Use a {} gram bag\n".format(var, Fifty)
                            #write(line)
                        else:
                            #print("[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Fifty, Bag))
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Fifty, Bag)
                            #write(line)

                    elif var < Twenty and var > Ten or var == Twenty:
                        Bag = var - Twenty
                        if Bag == 0:
                            #print("[{}]: Use a {} gram bag\n".format(var, Twenty))
                            line += "[{}]: Use a {} gram bag\n".format(var, Twenty)
                            #write(line)
                        else:
                            #print("[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Twenty, Bag))
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Twenty, Bag)
                            #write(line)

                    elif var < Ten and var > Five or var == Ten:
                        Bag = var - Ten
                        if Bag == 0:
                            #print("[{}]: Use a {} gram bag\n".format(var, Ten))
                            line += "[{}]: Use a {} gram bag\n".format(var, Ten)
                            #write(line)
                        else:
                            #print("[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Ten, Bag))
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Ten, Bag)
                            #write(line)

                    elif var <= Five and var > Three:
                        Bag = var - Five
                        if Bag == 0:
                            #print("[{}]: Use a {} gram bag\n".format(var, Five))
                            line += "[{}]: Use a {} gram bag\n".format(var, Five)
                            #write(line)
                        else:
                            #print("[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Five, Bag))
                            line += "[{}]: Use a {} gram bag\nThen put up {}\n".format(var, Five, Bag)
                            #write(line)

                    else:
                        if var == 3:
                            #print("[{}]: Use a 3 gram bag\n".format(var))
                            line += "[{}]: Use a 3 gram bag\n".format(var)
                            #write(line)

                        elif var == 2:
                            #print("[{}]: Use a 2 gram bag\n".format(var))
                            line += "[{}]: Use a 2 gram bag\n".format(var)
                            #write(line)

                        else:
                            if var == 1:
                                #print("[{}]: Use a 1 gram bag\n".format(var))
                                line += "[{}]: Use a 1 gram bag\n".format(var)
                                #write(line)
                            else:
                                pass
            file1.close()
            print("Finished. Check 'finished.txt'")
            #print(line)

            write(line)
            self.lines2 = lines2
            self.array = array
            file2.close()
            return line

        def handle_click2():
            print("2nd button clicked")

            window = self.window
            entry = self.entry
            data = entry.get('1.0', tk.END)

            #print(data)

            #self.numbersW.writelines(data)
            file1 = open('numbers.txt', 'w')
            file1.writelines(data)
            file1.close()
            var = process()
            #print("Var: {}".format(var))
            label = tk.Label(text=var)


            #array = self.array
            #print(array)
            #label = tk.Label(text=array)
            label.pack()
        def on_exit():
            print("Exiting...")
            window = self.window
            window.destroy()
            file1 = self.numbersW
            file2 = self.finishedW
            file1.close()
            file2.close()

        line = process()


        array = ""
        array = line



        #window = tk.Tk()
        window = self.window
        label = tk.Label(
            text="Welcome to [].\nClick on the buttons below to get started.")


        button2 = tk.Button(
            text="Refresh Data",
            width=25,
            height=5,
            bg="blue",
            fg="red",
            command=handle_click2
        )

        button3 = tk.Button(
            text="Exit",
            width=25,
            height=5,
            bg='black',
            fg='red',
            command=on_exit
        )
        entry = self.entry
        template = 'Amp/Fet\n13\nGanja/Grass\n19\nEctasy/Candy\n23\nMeth\n41\nCoke\n11\nHero\n9\n4'
        #entry = tk.Text()
        entry.insert(tk.END, template)

        label.pack()
        entry.pack()

        button2.pack()
        button3.pack()
        #label = tk.Label(text=array)
        #label.pack()

        window.mainloop()


loop = DDS()
loop.main()



#foundation
#g