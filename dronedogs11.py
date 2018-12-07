# This program uses a GUI to get total cost of hotdogs
from tkinter import *
import tkinter
import tkinter.messagebox
#checkbuttons page 626
#radiobuttons page 622

class TestTotal:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()
        self.main_window.title("Drone Dogs Order Form")
        # Create Canvas
        self.canvas = tkinter.Canvas(self.main_window, width=600, height=200)
        
        #image logo
        photo = PhotoImage(file='C:\\Users\\bagwe\\Desktop\\python\\DroneDogs3.png')
        self.canvas.create_image(10,10, image=photo, anchor=NW )
        # Create the frames.
        self.title_frame = tkinter.Frame(self.main_window)
        self.fname_frame = tkinter.Frame(self.main_window)
        self.lname_frame = tkinter.Frame(self.main_window)
        self.email_frame = tkinter.Frame(self.main_window)
        self.condiments_frame = tkinter.Frame(self.main_window)
        self.location_frame = tkinter.Frame(self.main_window)
        self.delivery_frame = tkinter.Frame(self.main_window)
        self.pork_frame = tkinter.Frame(self.main_window)
        self.turkey_frame = tkinter.Frame(self.main_window)
        self.beef_frame = tkinter.Frame(self.main_window)
        self.total_frame = tkinter.Frame(self.main_window)
        self.subtotal_frame = tkinter.Frame(self.main_window)
        self.tax_frame = tkinter.Frame(self.main_window)
        self.totalprice_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)
        #title order form
        self.title_label = tkinter.Label(self.title_frame,
                    text='Order Form', width=20, font=("bold", 20)) 
        #name of client
        self.fname_label = tkinter.Label(self.fname_frame,
                    text='Enter first name:')
        self.fname_entry = tkinter.Entry(self.fname_frame,
                                          width=20)
        self.lname_label = tkinter.Label(self.lname_frame,
                    text='Enter last name:')
        self.lname_entry = tkinter.Entry(self.lname_frame,
                                          width=20)
        #Email
        self.email_label = tkinter.Label(self.email_frame,
                    text='Enter email:')
        self.email_entry = tkinter.Entry(self.email_frame,
                                          width=30)
        #Pack the title frame's widgets
        self.title_label.pack(side='left')
        # Pack the name frame's widgets.
        self.fname_label.pack(side='left')
        self.fname_entry.pack(side='left')
        self.lname_label.pack(side='left')
        self.lname_entry.pack(side='left')
        #email
        self.email_label.pack(side='left')
        self.email_entry.pack(side='left')
        
        #Condiments
         # Create ten IntVar objects to use with
        # the Checkbuttons.
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        self.cb_var8 = tkinter.IntVar()
        self.cb_var9 = tkinter.IntVar()
        self.cb_var10 = tkinter.IntVar()
        self.cb_var11 = tkinter.IntVar()
        # Set the intVar objects to 0.
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        self.cb_var8.set(0)
        self.cb_var9.set(0)
        self.cb_var10.set(0)
        self.cb_var11.set(0)
        
        # Create the Checkbutton widgets in the top_frame.
        self.cb2 = tkinter.Checkbutton(self.condiments_frame,
                                       text='onions',
                                       variable=self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.condiments_frame,
                                       text='tomatoes',
                                       variable=self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.condiments_frame,
                                       text='pickles',
                                       variable=self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.condiments_frame,
                                       text='peppers',
                                       variable=self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.condiments_frame,
                                       text='chili',
                                       variable=self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.condiments_frame,
                                       text='cheese',
                                       variable=self.cb_var7)
        self.cb8 = tkinter.Checkbutton(self.condiments_frame,
                                       text='relish',
                                       variable=self.cb_var8)
        self.cb9 = tkinter.Checkbutton(self.condiments_frame,
                                       text='ketchup',
                                       variable=self.cb_var9)
        self.cb10 = tkinter.Checkbutton(self.condiments_frame,
                                       text='mustard',
                                       variable=self.cb_var10)
        self.cb11 = tkinter.Checkbutton(self.condiments_frame,
                                       text='sauerkraut',
                                       variable=self.cb_var11)
        #Know your location? Check button
        self.cb_var1 = tkinter.IntVar()
        # Set the intVar objects to 0.
        self.cb_var1.set(0)
        # Create the Checkbutton widgets in the location_frame.
        self.cb1 = tkinter.Checkbutton(self.location_frame,
                                       text='Know your location?',
                                       variable=self.cb_var1)
        # Create an IntVar object to use with
        # the Radiobuttons.
        self.radio_var = tkinter.IntVar()
        
        # Set the intVar object to 1.
        self.radio_var.set(1)

        self.rb1 = tkinter.Radiobutton(self.delivery_frame,
                                       text='Pickup',
                                       variable=self.radio_var,
                                       value=1)
        self.rb2 = tkinter.Radiobutton(self.delivery_frame,
                                       text='Delivery',
                                       variable=self.radio_var,
                                       value=2)

        # Create and pack the widgets for pork dogs.
        self.pork_label = tkinter.Label(self.pork_frame,
                                         text='Enter how many pork dogs:')
        self.pork_entry = tkinter.Entry(self.pork_frame,
                                         width=10)
        self.pork_label.pack(side='left')
        self.pork_entry.pack(side='left')

        # Create and pack the widgets for turkey dogs.
        self.turkey_label = tkinter.Label(self.turkey_frame,
                                         text='Enter how many turkey dogs:')
        self.turkey_entry = tkinter.Entry(self.turkey_frame,
                                         width=10)
        self.turkey_label.pack(side='left')
        self.turkey_entry.pack(side='left')
        
        # Create and pack the widgets for beef dogs.
        self.beef_label = tkinter.Label(self.beef_frame,
                                         text='Enter how many beef dogs:')
        self.beef_entry = tkinter.Entry(self.beef_frame,
                                         width=10)
        self.beef_label.pack(side='left')
        self.beef_entry.pack(side='left')

        # Create and pack the widgets for the total price.
        self.result_label = tkinter.Label(self.total_frame,
                                          text='Total Hot Dogs:')
        self.total = tkinter.StringVar() # To update total_label
        self.total_label = tkinter.Label(self.total_frame,
                                       textvariable=self.total)
        self.result_label.pack(side='left')
        self.total_label.pack(side='left')
        
        self.result_label = tkinter.Label(self.subtotal_frame,
                                          text='Subtotal:')
        self.subtotal = tkinter.StringVar() # To update subtotal_label
        self.subtotal_label = tkinter.Label(self.subtotal_frame,
                                       textvariable=self.subtotal)
        self.result_label.pack(side='left')
        self.subtotal_label.pack(side='left')

        self.result_label = tkinter.Label(self.tax_frame,
                                          text='Tax:')
        self.tax = tkinter.StringVar() # To update tax_label
        self.tax_label = tkinter.Label(self.tax_frame,
                                       textvariable=self.tax)
        self.result_label.pack(side='left')
        self.tax_label.pack(side='left')
        
        self.result_label = tkinter.Label(self.totalprice_frame,
                                          text='TotalPrice:')
        self.totalprice = tkinter.StringVar() # To update totalprice_label
        self.totalprice_label = tkinter.Label(self.totalprice_frame,
                                       textvariable=self.totalprice)
        self.result_label.pack(side='left')
        self.totalprice_label.pack(side='left')
        
       
        self.result_label.pack(side='left')
        self.totalprice_label.pack(side='left')
        # Pack the Checkbuttons for condiments.
        self.cb2.pack(side='left')
        self.cb3.pack(side='left')
        self.cb4.pack(side='left')
        self.cb5.pack(side='left')
        self.cb6.pack(side='left')
        self.cb7.pack(side='left')
        self.cb8.pack(side='left')
        self.cb9.pack(side='left')
        self.cb10.pack(side='left')
        self.cb11.pack(side='left')
        
        
        # Pack the Checkbutton for location.
        self.cb1.pack(side='left')
        # Pack the Radiobuttons.
        self.rb1.pack(side='left')
        self.rb2.pack(side='left')
        
        # Create and pack the button widgets.
        self.calc_button = tkinter.Button(self.button_frame,
                                          text='Total',
                                          command=self.calc_total)
        self.submit_button = tkinter.Button(self.button_frame,
                                          text='Submit',
                                          command=self.submit)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.submit_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        self.value=tkinter.IntVar()
        
        # Pack the frames.
        self.canvas.pack()
        self.title_frame.pack()
        self.fname_frame.pack()
        self.lname_frame.pack()
        self.email_frame.pack()
        self.condiments_frame.pack()
        self.location_frame.pack()
        self.delivery_frame.pack()
        self.pork_frame.pack()
        self.turkey_frame.pack()
        self.beef_frame.pack()
        self.total_frame.pack()
        self.subtotal_frame.pack()
        self.tax_frame.pack()
        self.totalprice_frame.pack()
        self.button_frame.pack()
        # Start the main loop.
        tkinter.mainloop()

    # The calc_total method is the callback function for
    # the calc_button widget.

    def calc_total(self):
        tax_rate = 0.07
        tax = 1
        hotdogprice = 1.99
        totalprice = 0
        total = 0
        subtotal = 0
        # Get the three hotdog types and store them
        # in variables.
        pork = int(self.pork_entry.get())
        turkey = int(self.turkey_entry.get())
        beef = int(self.beef_entry.get())
        
       
        # Calculate the totalprice.
        total = pork + turkey + beef                
        subtotal = total*hotdogprice
        tax = subtotal*tax_rate
        totalprice = subtotal+tax
        
        # Update the total_label widget by storing
        # the value of self.total in the StringVar
        # object referenced by total.
        self.total.set(self.total)
        self.subtotal.set(self.subtotal)
        self.tax.set(self.tax)
        self.totalprice.set(self.totalprice)
    def showImg(self):
        load=Image.open('DroneDogs2.png')
        render=ImageTk.PhotoImage(load)
        img=Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        
    def submit(self):
        tkinter.messagebox.showinfo('Receipt',
                                    'Thanks for your order.')
# Create an instance of the TestTotal class.
test_total = TestTotal()


        
