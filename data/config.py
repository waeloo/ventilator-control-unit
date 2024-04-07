import json

import os
class ConfigSettings:
    global ON_PI

    def __init__(self, config_location):
        self.__config_location = config_location
        self.dictionary = {}
        self.load()

    def save(self):
        with open(self.__config_location, 'w') as json_file:
            json.dump(self.dictionary, json_file)

    def load(self):
        try:
            with open(self.__config_location) as f:
                self.dictionary = json.load(f)
        except:
            self.load_default()

    def load_default(self):
        with open('data/hardware_settings_default.json') as f:
            self.dictionary = json.load(f)

    @staticmethod
    def change_brightness(value):
        if ON_PI:
            try:
                with open('/sys/class/backlight/rpi_backlight/brightness', 'w') as f:
                    print(value)
                    f.write(str(value))
            except FileNotFoundError:
                try:
                    with open('/sys/class/backlight/4d-hats/brightness', 'w') as f:
                        scaled_value = float(value - 15) / float(200-15)
                        new_value = int(1 + (scaled_value * 30))
                        print(new_value)
                        f.write(str(new_value))
                except:
                    print("This is not a supported screen for brightness changes")
