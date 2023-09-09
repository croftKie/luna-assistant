import utils
import random

class Assistant:
    def __init__(self, user_name, assistant_name, responses, commands):
        self.user_name = user_name
        self.assistant_name = assistant_name
        self.responses = responses
        self.known_commands = commands
        self.active = False

    def get_active_status(self):
        return self.active
    
    def start(self, command):

        if self.assistant_name in command:
            utils.speak(f"{self.responses['greetings_basic'][random.randint(0,2)]} {self.user_name} How can I help you?")
            self.active = True

    def welcome(self, command):
        if self.known_commands["daily_greetings"][0] in command:
            utils.speak(self.responses["greetings_daily"][0] + self.responses["reponses_helpful"][random.randint(0, 4)])
        if self.known_commands["daily_greetings"][1] in command:
            utils.speak(self.responses["greetings_daily"][1] + self.responses["reponses_helpful"][random.randint(0, 4)])
        if self.known_commands["daily_greetings"][2] in command:
            utils.speak(self.responses["greetings_daily"][2] + self.responses["reponses_helpful"][random.randint(0, 4)])
        if self.known_commands["daily_greetings"][3] in command:
            utils.speak(self.responses["greetings_daily"][3] + self.responses["reponses_helpful"][random.randint(0, 4)])


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