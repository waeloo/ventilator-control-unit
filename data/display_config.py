import json

test_config = "settings.json"
currentSettings = None


def readConfig(configFile):
    with open(configFile) as f:
        return json.load(f)


def writeConfig(configFile, brightness, lang, mode, alarm, trigger):
    newSettings = {"brightness" : brightness,
                    
                    "silence_time" : alarm,
                    "trigger"   : trigger }  
    
    with open(configFile, 'w') as f:
        json.dump(newSettings, f)