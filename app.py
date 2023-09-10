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
    window = tk.Tk()
    window.title("Luna Voice Assistant")
    window.minsize(width=800, height=400)

    titleLabel = tk.Label(text="Hi, I'm luna!", font=("Arial", 20, "bold"))
    titleLabel.pack()
    descriptionLabel = tk.Label(text="I'm a programmable voice assistant for managing your computer.", font=("Arial", 15, ""))
    descriptionLabel.pack()

    startButton = tk.Button(text="Activate Luna", command=start_assistant)
    startButton.pack()

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