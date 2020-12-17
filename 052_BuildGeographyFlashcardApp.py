import tkinter as tk
from PIL import ImageTk, Image
from random import randint

from PIL import ImageTk,Image

root = tk.Tk()
root.title("Flashcards!")
root.iconbitmap(r'D:\SONY\Nauka\Python\12.Other\002.Codemy_Tkinter\codemy_tkinter_prj/codemy.ico')
root.geometry("500x500")

def states():
    """Create State Flascard Function"""
    hide_all_frames()
    state_frame.pack(fill="both", expand=1)
    myLabel = tk.Label(state_frame, text="States").pack()

    # Create la list of states names
    our_states = ['california', 'florida', 'illinois','kentucky','nebraska','nevada','newyork','oregon','texas','vermont']

    # Generate random number
    rando = randint(0, len(our_states)-1)
    state = "states_images/" + our_states[rando] + ".png"

    #Create our State Images
    global state_image
    state_image = ImageTk.PhotoImage(Image.open(state))
    show_state = tk.Label(state_frame, image=state_image)
    show_state.pack(pady=15)

    #Create button to randomize
    myButton = tk.Button(state_frame, text="Shuffle new state", command=states)
    myButton.pack()

def state_capitals():
    """Create State Capitals Flascard Function"""
    hide_all_frames()
    state_capitals_frame.pack(fill="both", expand=1)
    myLabel = tk.Label(state_capitals_frame, text="Capitals").pack()

def hide_all_frames():
    """Hide all frames"""
    for widget in state_frame.winfo_children():
        widget.destroy()

    for widget in state_capitals_frame.winfo_children():
        widget.destroy()

    state_frame.pack_forget()
    state_capitals_frame.pack_forget()



# Create our menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)

# Create Geography menu items
states_menu = tk.Menu(my_menu)
my_menu.add_cascade(label="Geography", menu=states_menu)
states_menu.add_command(label="States", command=states)
states_menu.add_command(label="States Capitals", command=state_capitals)
states_menu.add_separator()
states_menu.add_command(label="Exit", command=root.quit)

# Create our Frames
state_frame = tk.Frame(root, width=500, height=500)
state_capitals_frame = tk.Frame(root, width=500, height=500)


root.mainloop()