
# Python class to drag tkinter widgets and windows v1.1 by erick esau martinez
# martinezesau90@yahoo.com
# www.erickesau.wordpress.com
# https://github.com/Erickesau
# https://www.paypal.com/paypalme/erickesau0

class Drag:
    """
Use: Drag(widget to drag)\n
You can drag widgets, windows, and Toplevel windows.
Drag(widget name)
Drag(window name)
you can create an objet and later call stop
or start method to stop or start dragging.
objet = Drag(widget name)
now you can stop dragging with objet.stop()
or start dragging with objet.start()\n


Example code:\n
from tkinter import Button, Tk
from tkdrag import Drag
root = Tk()
bt = Button(text="drag me", bg="yellow")
bt.pack()
Drag(bt)
root.geometry("400x400+50+50")
root.mainloop()\n
"""
    def __init__(self, widget, *args):
        """
widget :
    is the tkinter widget or window to make draggable\n
args :
    sticky aditional widgets or windows to move
    togueter with the draggable widget\n
    Example: Drag(button, somelabel, somewindow)\n
"""
        self.widget = widget
        self.method_in_use = False
        self.add = args
        # we dont know if the programm will use the same bind secuences in the same button
        # we dont want our class bind to be overwrited so
        # process after idle so the lines of user bind are set already,
        # then add this class bind so the user bind will not replace this class bind.
        def fun():
            if self.method_in_use:
                return
            self.bindID = self.widget.bind("<Button-1>", self.__click, add=True)
            self.bindID2 = self.widget.bind("<B1-Motion>", self.__drag, add=True)
        self.widget.after_idle(fun)

        self.lastclickx = 0
        self.lastclicky = 0

    def __click(self, event):
        self.lastclickx = event.x
        self.lastclicky = event.y

    def __drag(self, event):
        try:
            # try if is a widget will use this code to move widgets
            self.widget.place(
                x=event.x - self.lastclickx + self.widget.winfo_x(),
                y=event.y - self.lastclicky + self.widget.winfo_y())

            # if there is more widgets or windows added to drag togueter will use next code to precess then
            if self.add:
                for w in self.add:
                    try:
                        w.place(
                            x=event.x - self.lastclickx + w.winfo_x(),
                            y=event.y - self.lastclicky + w.winfo_y())
                    except:
                        try:
                            w.geometry(
                                "+" + str(event.x - self.lastclickx + w.winfo_x()) +
                                "+" + str(event.y - self.lastclicky + w.winfo_y()))
                        except:
                            pass
        except:
            # if is a window will use this code to move the window
            self.widget.geometry(
                "+" + str(event.x - self.lastclickx + self.widget.winfo_x()) +
                "+" + str(event.y - self.lastclicky + self.widget.winfo_y()))

            # if there is more windows or widgets added to drag togueter process then
            if self.add:
                for w in self.add:
                    try:
                        w.geometry(
                            "+" + str(event.x - self.lastclickx + w.winfo_x()) +
                            "+" + str(event.y - self.lastclicky + w.winfo_y()))
                    except:
                        try:
                            w.place(
                                x=event.x - self.lastclickx + w.winfo_x(),
                                y=event.y - self.lastclicky + w.winfo_y())
                        except:
                            pass
    def stop(self):
        """
Use this method to stop dragging
"""
        self.method_in_use = True
        try:
            self.widget.unbind("<Button-1>", self.bindID)
            self.widget.unbind("<B1-Motion>", self.bindID2)
        except:
            pass
    def start(self):
        """
use this method to start draginng
"""
        self.method_in_use = True
        self.bindID = self.widget.bind("<Button-1>", self.__click, add=True)
        self.bindID2 = self.widget.bind("<B1-Motion>", self.__drag, add=True)


    # ____________________________________	End








if __name__ == "__main__":
    # lets make a small programm to try	
    from tkinter import *
    from tkdrag import Drag
    root = Tk()
    
    label = Label(width=30, height=10, bg="#225588", borderwidth=10, relief="ridge")
    label.grid()
    # let configure dragging to the label, you can do to the main window or Toplevel window too.
    # dragging bind will be configured few milisecons after the mainloop run to avoid to be replaced.

    dl = Drag(label)
    #Drag(root)

    # we can call the stop or start method to enable or disable dragging
    button = Button(text="stop drag label",command=dl.stop, bg="#ff99dd")
    button.grid()
    button2 = Button(text="start drag label",command=dl.start, bg="#ff99dd")
    button2.grid()

    # configure drag is easy
    Drag(button)
    Drag(button2)

    root.geometry("400x400+50+50")
    root.mainloop()


