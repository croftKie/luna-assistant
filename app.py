from datetime import datetime
import os
import webbrowser
import utils
import settings
import json
from assistant_manager import Assistant
from response_library import responses
from command_library import commands
import tkinter as tk







def start_assistant():
    luna = Assistant(settings.USER_NAME, settings.AI_NAME, responses, commands)
    initCommand = utils.takeCommand()
    luna.start(initCommand)

    while luna.get_active_status():
        command = utils.takeCommand()
        #Conversational
        luna.welcome(command)
        luna.smallTalk(command)

        # #Tasks
        luna.tabManager(command)
        luna.webSearch(command)
        luna.randomTasks(command)


def main():
    TEXT_COL = "#DAFFFB"
    BG_COL = '#001C30'
    window = tk.Tk()
    window.title("Luna Voice Assistant")
    window.config(padx=200, pady=100, bg=BG_COL)


    label = tk.Label(text="Luna Voice Assistant", font=("Courier", 50, "bold"), bg=BG_COL, fg=TEXT_COL)
    label.grid(column=1, row=0)


    canvas = tk.Canvas(width=400, height=400, bg=BG_COL, highlightthickness=0)
    photo = tk.PhotoImage(file="./assets/moon.png")
    canvas.create_image(200, 200, image=photo)
    canvas.grid(column=1, row=1)

    startButton = tk.Button(text="Activate Luna", command=start_assistant)
    startButton.grid(column=0, row=2)

    def close_window(): 
        window.destroy()

    endButton = tk.Button(text="Close Down", command=close_window)
    endButton.grid(column=2, row=2)

    responseLabel = tk.Label(text=settings.CURRENT_RESPONSE, font=("Courier", 30, "bold"), bg=BG_COL, fg=TEXT_COL)
    responseLabel.grid(column=1, row=3)

    window.mainloop()


main()




# YouTube Search
    # Other web search types
        # search stack overflow
        # search images
        # Netflix search
        
# Security mode

# save a note

# set an alarm

# reminder system