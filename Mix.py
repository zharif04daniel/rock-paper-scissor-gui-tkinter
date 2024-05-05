from tkinter import *
from functools import partial
import random

root = Tk()
root.configure(bg="black")
root.geometry('+0+0')
root.iconbitmap("Game.ico")
root.title("Rock-Paper-Scissor")
root.resizable(width=False,height=False)


"""def printDetails(usernameEntry):
    usernameText = usernameEntry.get()
    print(usernameText + "has entered")
    return


#Label
usernameLabel = Label(root, text="Enter your name")

#Entry for user input
usernameEntry = Entry(root)

#Define callable function w printDetails function and usernameEntry argument
printDetailsCallable = partial(printDetails, usernameEntry)

#Submit Button
submitButton = Button(root, text="Submit", command=printDetailsCallable)

# Place label, entry and button in grid
usernameLabel.grid(row=0, column=0)
usernameEntry.grid(row=0, column=1)
submitButton.grid(row=1, column=1)
"""

#Image RPS
rock = PhotoImage(file="Rock_1.png")
paper = PhotoImage(file="Paper_1.png")
scissors = PhotoImage(file="Scissor_1.png")

decisionPhoto = PhotoImage(file="Decision_Final.png")

#Button
rockbutton = " "
paperbutton = " "
scissorsbutton = " "
nextbutton = " "

#Create the result button :
resultButton = Button(root,image=decisionPhoto)

click = True

#Result images :
winPhoto = PhotoImage(file="G_WIN.png")
losePhoto = PhotoImage(file="G_LOST.png")
tiePhoto = PhotoImage(file="G_DRAW.png")


def play():
    global rockbutton,paperbutton,scissorsbutton

    #set image and commands for buttons
    rockbutton = Button(root,image = rock, command=lambda:userPick("Rock"))
    paperbutton = Button(root,image = paper, command=lambda:userPick("paper"))
    scissorsbutton = Button(root,image = scissors, command=lambda:userPick("scissors"))
    nextbutton= Button(root, text="Next")

    #Place button on the window
    rockbutton.grid(row=0,column=0)
    paperbutton.grid(row=0,column=1)
    scissorsbutton.grid(row=0,column=2)
    resultButton.grid(row=3,column=1)
    nextbutton.grid(row=4, column=1)

    #Add space :
    root.grid_rowconfigure(1, minsize=50) 

def computerPick():
    choice = random.choice(["rock","paper","scissors"])
    return choice

def userPick(yourChoice):
    global click

    compPick = computerPick()

    if click==True:

        if yourChoice == "rock":

            if compPick == "rock":
                    rockbutton.configure(image=rock)
                    paperbutton.grid_forget()
                    scissorsbutton.grid_forget()
                    resultButton.configure(image=tiePhoto)
                
            elif compPick == "paper":
                    rockbutton.grid_forget()
                    paperbutton.configure(image=paper)
                    scissorsbutton.grid_forget()
                    resultButton.configure(image=losePhoto)
                  

            elif compPick == "scissors":
                    rockbutton.grid_forget()
                    paperbutton.grid_forget()
                    scissorsbutton.configure(image=scissors)
                    resultButton.configure(image=winPhoto)
                   

        elif yourChoice == 'paper':
              
            if compPick == 'rock':
                    rockbutton.configure(image=rock)
                    paperbutton.grid_forget()
                    scissorsbutton.grid_forget()
                    resultButton.configure(image=winPhoto)

            elif compPick == 'paper':
                    rockbutton.grid_forget()
                    paperbutton.configure(image=paper)
                    scissorsbutton.grid_forget()
                    resultButton.configure(image=tiePhoto)

            elif compPick == 'scissors':
                    rockbutton.grid_forget()
                    paperbutton.grid_forget()
                    scissorsbutton.grid_forget(image=scissors)
                    resultButton.configure(image=losePhoto)

        elif yourChoice == 'scissors':
            if compPick == ' rock':
                    rockbutton.configure(image=rock)
                    paperbutton.grid_forget()
                    scissorsbutton.grid_forget()
                    resultButton.configure(image=losePhoto)

            elif compPick == 'paper':
                    rockbutton.grid_forget()
                    paperbutton.configure(image=paper)
                    scissorsbutton.grid_forget()
                    resultButton.configure(image=winPhoto)    


            elif compPick == 'scissors':
                    rockbutton.grid_forget()
                    paperbutton.grid_forget()
                    scissorsbutton.grid_forget(image=scissors)
                    resultButton.configure(image=tiePhoto)

        if yourChoice=='rock' or yourChoice=='paper' or yourChoice=='scissors':
          
                rockbutton.grid(row=0,column=0)
                paperbutton.grid(row=0,column=1)
                scissorsbutton.grid(row=0,column=2)
                resultButton.grid(row=3,column=1)
                nextbutton.grid(row=4, column=1)

                rockbutton.configure(image=rock)
                paperbutton.configure(image=paper)
                scissors.configure(image=scissors)
                click = True

          
play()

root.mainloop()