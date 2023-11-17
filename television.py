class Television:
    min_volume = 0
    max_volume = 2
    min_channel = 0
    max_channel = 3

    def __init__(self) -> None:
        '''__init__ defines that variables status muted are False and that the volume and channel variables should be
        their minimum value of 0.

            Args: self

            Returns: None
        '''
        self.__status = False
        self.__muted = False
        self.__volume = self.min_volume
        self.__channel = self.min_channel

    def power(self) -> None:
        '''function checks status of Television class object and turns changes it to opposite

            Args: self

            Returns: None
        '''
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self) -> None:
        '''function checks if status of Television class object is on and will toggle the muted variable
            Args: self

            Returns: None
        '''
        if self.__status == True:
            self.__muted = True

    def channel_up(self) -> None:
        '''function checks if status of Television class object is on and add one to channel. If the channel variable
            goes higher than the max_channel variable, the channel will go back to min_channel
            Args: self

            Returns: None
        '''
        if self.__status == True:
            self.__channel += 1
            if self.__channel >= self.max_channel:
                self.__channel = self.min_channel

    def channel_down(self) -> None:
        '''function checks if status of Television class object is on and subtract one to channel.
            If the channel variable goes lower than the min_channel variable, the channel will go back to max_channel

            Args: self

            Returns: None
        '''
        if self.__status == True:
            self.__channel -= 1
            if self.__channel <= self.min_channel:
                self.__channel = self.max_channel

    def volume_up(self) -> None:
        '''function checks if status of Television class object is on and add one to volume. This will only happen
            if volume is in the defined range. It also will check if the
            volume was previously muted. If it was, then the mute will be toggled to false and continue.

            Args: self

            Returns: None
        '''
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            if 0 <= self.__volume < 2:
                self.__volume += 1

    def volume_down(self) -> None:
        '''function checks if status of Television class object is on and subtracts one to volume. This will only happen
            if volume is in the defined range
            It also will check if the volume was previously muted. If it was, then the mute will be toggled to false
            and continue.

            Args: self

            Returns: None
            '''
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
            if 0 < self.__volume <= 2:
                self.__volume -= 1

    def __str__(self) -> str:
        '''Checks if muted variable was set to true, if so, then it will print that volume = 0
            if muted was set to false, then the volume = volume variable

            Args: self

            Returns: None
        '''
        if self.__muted == True:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = 0.'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}.'

