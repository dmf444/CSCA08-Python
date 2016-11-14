class LightSwitch():
    """A class that simulates a light switch allowing for toggling it on and
    off."""

    def __init__(self, setting):
        if(setting == "on"):
            self._setting = True
        else:
            self._setting = False

    def turn_on(self):
        self._setting = True

    def turn_off(self):
        self._setting = False

    def flip(self):
        if(self._setting):
            self.turn_off()
        else:
            self.turn_on()

    def __str__(self):
        if(self._setting):
            response = "I am on"
        else:
            response = "I am off"
        return response


class SwitchBoard():
    """Class to represent a switchboard and allow for turning on/off lights
    connected to the switch."""
