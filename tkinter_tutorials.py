# Tutorial
# TheNewBoston - Python GUI with Tkinter Playlist
# Platform - YouTube
# Date 05/02/20


from tkinter import *

# root == Window; mainloop() == stay open;
root = Tk()
root.mainloop()



# Tutorial 1 - Basics of Tkinter

# root = Tk()
# root.mainloop()

##############################################################

# Tutorial 2 - Buttons / Pack LEFT

# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)
#
# button1 = Button(topFrame, text="Don't press this button", fg="red")
# button2 = Button(topFrame, text="Do press THIS button never", fg="green")
# button3 = Button(topFrame, text="Yes, stay away from this button", fg="blue")
# button4 = Button(bottomFrame, text="okay, click away from here", fg="purple")
#
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack()

##############################################################

# Tutorial 3 // Labels / FILL

# one = Label(root, text="One", bg="teal", fg="black")
# one.pack()
# two = Label(root, text="Two", bg="blue", fg="orange")
# two.pack(fill=X)
# three = Label(root, text="Three", bg="blue", fg="white")
# three.pack(side=LEFT, fill=Y)

##############################################################

# # Tutorial 4 & 5 // Grid layout
#
# label_1 = Label(root, text="Name")
# label_2 = Label(root, text="Password")
# entry_1 = Entry(root)
# entry_2 = Entry(root)
#
#
# # Grid Layout
# label_1.grid(row=0, sticky=E)
# label_2.grid(row=1, sticky=E)
# entry_1.grid(row=0, column=1)
# entry_2.grid(row=1, column=1)
#
# c = Checkbutton(root, text="Keep me logged in")
# c.grid(columnspan=2)

##############################################################

# # Tutorial 6 - Button Events
#
# def printName(event):
#     print("Chello my name is Crush")
# button_1 = Button(root, text="Display Name")
# button_1.bind("<Button-1>", printName)
# button_1.grid(row=1)
#

##############################################################

# # Tutorial 7 - Mouse click events using Frames
#
# def leftClick(event):
#     print("Left")
#
# def middleClick(event):
#     print("Middle")
#
# def rightClick(event):
#     print("Right")
#
# frame = Frame(root, width=600, height=450)
# frame.bind("<Button-1>", leftClick)
# frame.bind("<Button-2>", middleClick)
# frame.bind("<Button-3>", rightClick)
# frame.pack()

##############################################################

# Tutorial 8 - Classes with tkinter

# class AustinsButtons:
#
#     def __init__(self, master):
#         frame = Frame(master, width=600, height=250)
#         frame.pack()
#
#         self.printButton = Button(frame, text="Print message", command=self.printMessage)
#         self.printButton.grid(row=0)
#
#         self.quitButton = Button(frame, text="Quit", command=frame.quit)
#         self.quitButton.grid(row=1)
#
#     def printMessage(self):
#         print("Wow, this actually worked...")
#
#
# root = Tk()
# a = AustinsButtons(root)
# root.mainloop()

##############################################################

# # Tutorial 9 - Dropdown menu
#
# def doNothing():
#     print("ok, I won't...")
#
# root = Tk()
#
# menu = Menu(root)
# root.config(menu=menu)
#
# subMenu = Menu(menu)
# menu.add_cascade(label="File", menu=subMenu)
# subMenu.add_command(label="New Project...", command=doNothing)
# subMenu.add_separator()
# subMenu.add_command(label="Open", command=doNothing)
#
# subMenu2 = Menu(menu)
# menu.add_cascade(label="Edit", menu=subMenu2)
#
#
# root.mainloop()

##############################################################

# Tutorial 10 - Toolbar

#
# toolbar = Frame(root, bg="blue", width=600, height=60)
#
# insertButt = Button(toolbar, text="Insert Image", command=doNothing)
# insertButt.pack(side=LEFT, padx=2, pady=2)
#
# printButt = Button(toolbar, text="Print", command=doNothing)
# printButt.pack(side=LEFT, padx=2, pady=2)
#
# toolbar.pack(fill=X)
# root.mainloop()

##############################################################

# Tutorial 11 - Status Bar (Bottom) (W/ no Updating Text)

# import tkinter.messagebox

# status = Label(root, text="Praparing to do nothing...", bd="1", relief=SUNKEN, anchor=W)
# status.pack(side=BOTTOM, fill=X)

# Tutorial 12 - Messagebox - Alert Dialog
# root = Tk() #Start ow window
#
# tkinter.messagebox.showinfo('Window Title', 'Monkey can live up to 300 years.')
#
# answer = tkinter.messagebox.askquestion('Question 1', 'Do you like silly faces')
#
# if answer == 'yes':
#     print(";)")
#

# root.mainloop() # When Break -> End of Window

##############################################################

# Tutorial 12 - Messagebox [DELETED]

##############################################################

# Tutorial 13 - Canvas Shapes

# root = Tk() #Start ow window
#
# canvas = Canvas(root, width=200, height=100)
# canvas.pack()
#
# blackLine = canvas.create_line(0, 0, 200, 50)
# redLine = canvas.create_line(0, 100, 200, 50, fill="red")
# greenBox = canvas.create_rectangle(25,25,130,60, fill="green")
#
# # Delete graphics
# canvas.delete(redLine)
# canvas.delete(ALL)
#
# root.mainloop() # When Break -> End of Window

##############################################################

# # Tutorial 14 - Images and Icons
# root = Tk() #Start ow window
#
# photo = PhotoImage(file="filename.png")
# # Photo needs to be set in label in order to display
# label = Label(root, image=photo)
# label.pack()
#
# root.mainloop() # When Break -> End of Window

##############################################################
