import random
import json
from datetime import datetime
import os
import utils
import responses
import settings
import commands
import webbrowser

def __init__():
    with open("vars.json", "r") as openFile:
        json_obj = json.load(openFile)
        print(json_obj)
        settings.USER_NAME = json_obj["user_name"]
        settings.AI_NAME = json_obj["ai_name"]
    print(settings.USER_NAME)

def welcome(command):
    if commands.dailyGreetings[0] in command:
        utils.speak(responses.dailyGreetings[0] + responses.beingHelpful[random.randint(0, 4)])
    if commands.dailyGreetings[1] in command:
        utils.speak (responses.dailyGreetings[1] + responses.beingHelpful[random.randint(0, 4)])
    if commands.dailyGreetings[2] in command:
        utils.speak (responses.dailyGreetings[2] + responses.beingHelpful[random.randint(0, 4)])
    if commands.dailyGreetings[3] in command:
        utils.speak (responses.dailyGreetings[3] + responses.beingHelpful[random.randint(0, 4)])

def smallTalk(command):
    for c in commands.howAreYouQuestions:
        if c in command:
            utils.speak(responses.howAreYouResponses[random.randint(0, 2)])
    if 'thank you' in command:
        utils.speak(responses.thankYouResponse[random.randint(0,4)])
    if 'bye' in command:
        utils.speak(responses.goodbyeResponse[random.randint(0,6)])
        on = False

def tabManager(command):
    if commands.tabCommands[0] in command:
        utils.speak("Sure, opening your work tabs.")
        for x in settings.WORK_TABS:
            webbrowser.open(x)
    if commands.tabCommands[1] in command:
        utils.speak("Sure, opening your coding tabs.")
        for x in settings.CODING_TABS:
            webbrowser.open(x)
    if commands.tabCommands[2] in command:
        utils.speak("Sure, opening your movie tabs.")
        for x in settings.MOVIE_TABS:
            webbrowser.open(x)
    if commands.tabCommands[3] in command:
        utils.speak("Sure, opening your news tabs.")
        for x in settings.NEWS_TABS:
            webbrowser.open(x)

def webSearch(command):
    if 'search' in command:
        searchTerm = ""
        if 'search for' in command:
            searchTerm = command.split("search for")[-1]
        else:
            searchTerm = command.split("search")[-1]
        utils.speak(responses.generalPositiveRequestRetorts[random.randint(0, len(responses.generalPositiveRequestRetorts) - 1)])
        webbrowser.open("https://duckduckgo.com/" + searchTerm)
    if 'web' in command:
        webbrowser.open("https://duckduckgo.com/")

def randomTasks(command):
    if 'time' in command:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        utils.speak("The Current Time is " + current_time)  
    if 'random number' in command:
        randInt = random.randint(0, 10) 
        utils.speak("A random number between 0 and 10 is " + str(randInt))

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
    __init__()
    on = True
    initCommand = utils.takeCommand()
    if settings.AI_NAME in initCommand:
        utils.speak(responses.basicGreetings[random.randint(0,2)] + settings.USER_NAME + "How can I help you?")
        on = True

    while on:
        command = utils.takeCommand()
        #Conversational
        welcome(command)
        smallTalk(command)

        #Tasks
        tabManager(command)
        webSearch(command)
        randomTasks(command)

main()