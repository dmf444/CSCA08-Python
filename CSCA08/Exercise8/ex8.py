class LightSwitch():
    """A class that simulates a light switch allowing for toggling it on and
    off."""

    def __init__(self, setting):
        '''(LightSwitch, str) -> LightSwitch
        Creates a new light switch.
        REQ: setting must be 'on' or 'off'
        '''
        if(setting == "on"):
            self._setting = True
        else:
            self._setting = False

    def turn_on(self):
        ''' (LightSwitch) -> NoneType
        Toggles the light on.
        '''
        self._setting = True

    def turn_off(self):
        """ (LightSwitch) -> NoneType
        Toggles the light off.
        """
        self._setting = False

    def flip(self):
        """ (LightSwitch) -> NoneType
        Toggles the light from its current state.
        """
        if(self.get_state()):
            self.turn_off()
        else:
            self.turn_on()

    def get_state(self):
        """(LightSwitch) -> Boolean
        Returns the current state of the given light.
        >>> switch1 = LightSwitch("on")
        >>> print(switch1.get_state())
        True
        >>> switch2 = LightSwitch("off")
        >>> print(switch2.get_state())
        False
        """
        return self._setting

    def __str__(self):
        """ (self) -> String
        Returns a string representation of the light switches' current state.
        """
        if(self.get_state()):
            response = "I am on"
        else:
            response = "I am off"
        return response


class SwitchBoard():
    """Class to represent a switchboard and allow for turning on/off lights
    connected to the switch."""

    def __init__(self, num_switches):
        """(SwitchBoard, int) -> SwitchBoard
        Creates a new switchboard with the given num_switches defaulted to off.
        """
        self._switches = []
        for count in range(num_switches):
            self._switches.append(LightSwitch("off"))

    def get_switches(self):
        """(SwitchBoard) -> list of switches
        Returns the internal representation of the list of switches
        """
        return self._switches

    def __str__(self):
        """(SwitchBoard) -> str
        Returns a string of all the switches that are on, numerically index.
        REQ: SwitchBoard must contain some lights
        """
        response = "The following switches are on: "
        # Loop through all switches, if on, add to list
        for count in range(len(self.get_switches())):
            switch = self.get_switches()[count]
            if(switch.get_state()):
                response += str(count) + " "
        return response

    def which_switch(self):
        """(SwitchBoard) -> List of ints
        Returns a list of all lights that are on.
        REQ: LightSwitch must not be empty
        """
        # Empty list to add vailid lights to
        response = []
        # Loop through the lights, if on, add to list
        for count in range(len(self.get_switches())):
            switch = self.get_switches()[count]
            if(switch.get_state()):
                response.append(count)
        return response

    def flip(self, to_flip):
        """(SwitchBoard, int) -> NoneType
        Toggles a light, defined by to_flip from its current state.
        REQ: to_flip must be in the set of lights
        >>> board = SwitchBoard(5)
        >>> board.flip(2)
        >>> print(board)
        The following switches are on: 2
        """
        # Make sure given value is in array
        if(to_flip < len(self.get_switches()) and to_flip >= 0):
            # Get the switch and toggle it
            switch = self.get_switches()[to_flip]
            switch.flip()

    def flip_every(self, int_to_flip):
        """(SwitchBoard, int) -> NoneType
        Toggles every switch in a given multiple of int_to_flip.
        REQ: int_to_flip < len(SwitchBoard.get_switches)
        REQ: int_to_flip > 0
        >>> board = SwitchBoard(10)
        >>> board.flip_every(2)
        >>> print(board)
        The following switches are on: 0 2 4 6 8
        """
        # Make sure int to flip is greater than 0
        if(int_to_flip > 0):
            # Loop through all valid switches
            for count in range(0, len(self.get_switches()), int_to_flip):
                # Toggle said switch
                self.flip(count)

    def reset(self):
        """(SwitchBoard) -> NoneType
        Set all switches in a given board to off.
        REQ: SwitchBoard must not be null
        >>> board = SwitchBoard(5)
        >>> board.flip(1)
        >>> board.reset()
        >>> print(board)
        The following switches are on:
        """
        for switch in self.get_switches():
            switch.turn_off()

# board = SwitchBoard(1023)
# for count in range(1023):
#    board.flip_every(count)
# print(board)
# print(board.which_switch())
