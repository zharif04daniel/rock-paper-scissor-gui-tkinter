#Import tkinter(GUI), random(random comp pick)
from tkinter import *
import random
import simpleaudio as sa

root = Tk()
root.configure(bg="000000")
root.geometry('+0+0')
root.iconbitmap("Game.ico")
root.title("Rock-Paper-Scissor")
root.resizable(width=False,height=False)

#To play sound files
start = sa.WaveObject.from_wave_file("Start.wav")
WIn = sa.WaveObject.from_wave_file("Win.wav")
Lose = sa.WaveObject.from_wave_file("Lose.wav")
Drsw = sa.WaveObject.from_wave_file("Draw.wav")

start.play()

#Hand images
rockHandPhoto - PhotoImage(file="Rock_1.png")
paperHandPhoto - PhotoImage(file="paper_1.png")
scissorHandPhoto - PhotoImage(file="scissor_1.png")

#Graphical images
rockPhoto = PhotoImage(file="Rock_P.png")
paperPhoto = PhotoImage(file="Paper_P.png")
scissorPhoto = PhotoImage(file="Scissor_P.png")

#Desicion image
decisionPhoto = PhotoImage(file="Decision_Final.png")

#Result images
winPhoto = PhotoImage(file="G_WIN.png")
losePhoto = PhotoImage(file="G_LOST.png")
drawPhoto = PhotoImage(file="G_DRAW.png")

#Button widget

#Initialize the button variables
rockHandButton = " "
paperHandButton = " "
scissorHandButton = " "

#Create result button
resultButton = Button(root,image=decisionPhoto)

click = True

#Main program play() funtion
def play():
    global rockHandButton,paperHandButton,scissorHandButton

    #set images and commands for buttons
    rockHandButton = Button(root,image = rockHandPhoto, command=lambda:youPick("Rock"))
    paperHandButton = Button(root,image = paperHandPhoto, command=lambda:youPick("paper"))
    scissorHandButton = Button(root,image = scissorHandPhoto, command=lambda:youPick("Scissor"))

    #Place button on the window
    rockHandButton.grid(row=0,column=0)
    paperHandButton.grid(row=0,column=0)
    scissorHandButton.gro(row=0,column=0)

    #add space
    root.grid_rowconfigure(1, minsize=50)

    #place resultButton on the window
    reslutButton.grid(row=0,column=0,columnspan=5)

#Computer turn
def computerPick():
    choice = random.choice(["Rock","Paper","Scissor"])
    return choice

#Player pick
def youPick(yourChoice):
    global click

    compPick = computerPick()

    if click==True

if compPick == "Rock":
                paperHandButton.configure(image=rockPhoto)
                resultButton.configure(image=tiePhoto)
                scissorHandButton.grid.forget()
                Draw.play()
                click = False

            elif compPick == "Paper":
                paperHandButton.configure(image=paperPhoto)
                scissorHandButton.grid.forget
                resultButton.configure(image=losePhoto)
                Lose.play()
                click = False

            elif compPick == "Scissor":
                paperHandButton.configure(image=scissorPhoto)
                scissorHandButton.grid.forget()
                resultButton.configure(image=winPhoto)
                Win.play()
                click = False

#user select paper
                elif yourChoice == "Paper":
            rockHandButton.configure(image=paperPhoto)
            
            if compPick == "Rock":
                paperHandButton.configure(image=rockPhoto)
                resultButton.configure(image=losePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False
        
            elif compPick == "Paper":
                paperHandButton.configure(image=paperPhoto)
                resultButton.configure(image=tiePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Draw.play()
                click = False
            
            elif compPick == "Scissor":
                paperHandButton.configure(image=scissorPhoto)
                resultButton.configure(image=losePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False
                
            elif compPick =="Lizard":
                paperHandButton.configure(image=lizardPhoto)
                resultButton.configure(image=losePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False
                
            else :
                paperHandButton.configure(image=spockPhoto)
                resultButton.configure(image=winPhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Win.play()
                click = False

#user select scissor
 elif yourChoice=="Scissor":
            rockHandButton.configure(image=scissorPhoto)
            if compPick == "Rock":
                paperHandButton.configure(image=rockPhoto)
                resultButton.configure(image=losePhoto)
                scissorHandButton.grid_forget()
                lizardHandButton.grid_forget()
                spockHandButton.grid_forget()
                Lose.play()
                click = False
            
            elif compPick == "Paper":
                paperHandButton.configure(image=paperPhoto)
                resultButton.configure(image=winPhoto)
                scissorHandButton.grid_forget()
                Win.play()
                click = False
            
            elif compPick=="Scissor":
                paperHandButton.configure(image=scissorPhoto)
                resultButton.configure(image=tiePhoto)
                scissorHandButton.grid_forget()
                Draw.play()
                click = False

#play again
else:
        #To reset the game
        if yourChoice=="Rock" or yourChoice=="Paper" or yourChoice=="Scisssor":
            rockHandButton.configure(image=rockHandPhoto)
            paperHandButton.configure(image=paperHandPhoto)
            scissorHandButton.configure(image=scissorHandPhoto)

            #Get back the delete button
            scissorHandButton.grid(row=0,column=2)

            click = True

            #play sound file
            start.play()

#calling the play function
play()

#enter the main loop
root.mainloop()
