import random
import tkinter as tk
from tkinter import messagebox
import sys

window = tk.Tk()
window.title("Rock_paper_scissor")
window.geometry('400x250')
menu = tk.Menu(window)
window.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label = 'File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)
helpmenu = tk.Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')

#Showing message
# def clicked():
#
#     messagebox.showinfo('Message title', 'Message content')
#
# btn = tk.Button(window, text = 'Click', command = clicked)
#
# btn.grid(column=0,row=0)
# window.mainloop()
# e1 = tk.Entry(window)
# e1.grid(row=0, column=1)
#
# # tk.Label(window, text = "Last Name").grid(row = 1)
#

# button.pack()
# window.mainloop()

choices = ["Rock","Paper","Scissors"]
choice_in = tk.StringVar()


def get_choice():
    cpu_score, player_score = 0, 0
    computer = random.choice(choices)
    choice = choice_in.get()
    print("Your Choice: %s"%choice)
    print("Computer's choice: %s"%computer)
    player = choice

    if player not in choices:
        messagebox.showerror('error', 'Invalid choice!\n Enter any choice among these("Rock","Paper","Scissors")')

        # msg = tk.Label(window, textvariable='Invalid choice!')
        # msg.pack()
        '''
        msg = tk.Message(window, text='Invalid choice!')
        msg.config(bg='red')
        msg.pack()
        '''

        print("Invalid choice!")
        # sys.exit()
    else:
        if player == computer:
            messagebox.showinfo('Tie', 'Tie!Computer  and You have the same choice "%s"'% computer)
            print("Tie!!")

        elif player == "Rock":
            if computer == "Paper":
                print("You lose!")
                messagebox.showinfo('Fail', 'Oops! Your computer chose "%s"\n You lose' % computer)
                cpu_score+=1
            else:
                print("You win!!")
                messagebox.showinfo('Success', 'Congrats! Your computer chose "%s"\n You win' % computer)
                player_score += 1
        elif player == "Scissors":
            if computer == "Rock":
                print("You lose!!")
                messagebox.showinfo('Fail', 'Oops! Your computer chose "%s"\n You lose'%computer)
                cpu_score += 1
            else:
                print("You win!!")
                messagebox.showinfo('Success', 'Congrats! Your computer chose "%s"\n You win'%computer)
                player_score += 1

        elif player == "Paper":
            if computer == "Scissors":
                print("You lose!!")
                messagebox.showinfo('Fail', 'Oops! Your computer chose "%s"\n You lose' % computer)
                cpu_score+=1
            else:
                print("You win!!")
                messagebox.showinfo('Success', 'Congrats! Your computer chose "%s"\n You win' % computer)
                player_score+=1
    print(f"Player score : {player_score} and Computer score:{cpu_score}")



    choice_in.set("")

label_1 = tk.Label(window, text = "Enter choice").pack() #grid(column=0, row=0)

player = tk.Entry(window, textvariable = choice_in, width=10).pack() #grid(column=0, row=1)

b = tk.Button(window, text="Play", width=10, command=get_choice).pack() #grid(column=0, row=2)

messagebox.showinfo('Game', 'Hi! Try your luck for Rock,Paper,Scissors')

window.mainloop()






