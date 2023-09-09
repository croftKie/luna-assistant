from datetime import datetime
import os
import webbrowser
import utils
import settings
import json
from assistant_manager import Assistant
from response_library import responses
from command_library import commands

# def __init__():
#     with open("vars.json", "r") as openFile:
#         json_obj = json.load(openFile)
#         print(json_obj)
#         settings.USER_NAME = json_obj["user_name"]
#         settings.AI_NAME = json_obj["ai_name"]
#     print(settings.USER_NAME)

# YouTube Search
    # Other web search types
        # search stack overflow
        # search images
        # Netflix search
        
# Security mode

# save a note

# set an alarm

# reminder system


def main():
    # __init__()

    luna = Assistant(settings.USER_NAME, settings.AI_NAME, responses, commands)

    initCommand = utils.takeCommand()
    luna.start(initCommand)

    while luna.get_active_status():
        command = utils.takeCommand()
        #Conversational
        luna.welcome(command)
        # luna.smallTalk(command)

        # #Tasks
        # luna.tabManager(command)
        # luna.webSearch(command)
        # luna.randomTasks(command)

main()