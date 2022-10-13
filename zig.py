from pocketsphinx import LiveSpeech

def checkCommands(phrase:str):
    if "computer set lights" in phrase or "computer lights" in phrase:
        try:
            return ("lights", int(phrase[-3:]))
        except:
            if phrase[-3:] == "off": # Check other cases
                return ("lights", 0)
            elif phrase[-2:] == "on":
                return ("lights", 100)
            else:
                raise(Exception(phrase[-3:]+ "is not a valid int or string"))
                

for phrase in LiveSpeech():
    print(phrase)
    if 'computer' in phrase.lower():
        checkCommands(phrase.lower()) # process commands later