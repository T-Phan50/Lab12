from television import *


class TestTelevsion:
    def test_init(self):
        self.tv = Television()
        self.__init__()
        assert self.tv.__str__() == f'Power = False, Channel = 0, Volume = 0.'

    def test_power(self):
        self.tv = Television()
        self.__init__()
        self.tv.power()
        assert self.tv.__str__() == f'Power = True, Channel = 0, Volume = 0.'
        self.tv.power()
        assert self.tv.__str__() == f'Power = False, Channel = 0, Volume = 0.'

    def test_mute(self):
        self.tv = Television()
        self.tv2 = Television()
        self.tv3 = Television()
        self.tv4 = Television()
        self.__init__()

        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert self.tv.__str__() == f'Power = True, Channel = 0, Volume = 0.'  # tv is on, volume increased and muted

        self.tv2.power()
        self.tv2.mute()
        self.tv2.mute()
        assert self.tv.__str__() == f'Power = True, Channel = 0, Volume = 0.'  # tv is on and unmuted

        self.tv3.mute()
        assert self.tv3.__str__() == f'Power = False, Channel = 0, Volume = 0.'  # tv is off and muted

        self.tv4.power()
        self.tv4.mute()
        self.tv4.mute()
        assert self.tv.__str__() == f'Power = True, Channel = 0, Volume = 0.'  # tv is off and unmuted

    def test_channel_up(self):
        self.tv = Television()
        self.__init__()
        self.tv.channel_up()
        assert self.tv.__str__() == f'Power = False, Channel = 0, Volume = 0.'  # tv is off and channel up

        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == f'Power = True, Channel = 1, Volume = 0.'  # tv is on and channel up

        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == f'Power = True, Channel = 0, Volume = 0.'  # tv is on and channel up

    def test_channel_down(self):
        self.tv = Television()
        self.__init__()
        self.tv.channel_down()
        assert self.tv.__str__() == f'Power = False, Channel = 0, Volume = 0.'  # tv is off and channel down

        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == f'Power = True, Channel = 3, Volume = 0.'  # tv is on and channel down

    def test_volume_up(self):
        self.tv = Television()
        self.__init__()

        self.tv.volume_up()
        assert self.tv.__str__() == f'Power = False, Channel = 0, Volume = 0.'  # tv is off and volume up

        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == f'Power = True, Channel = 0, Volume = 1.'  # tv is on and volume up

        self.tv.mute()
        self.tv.volume_up()
        assert self.tv.__str__() == f'Power = True, Channel = 0, Volume = 2.'  # tv is on, muted and then volume up

        self.tv.volume_up()
        assert self.tv.__str__() == f'Power = True, Channel = 0, Volume = 2.'  # tv is on, and then volume up past max

    def test_volume_down(self):
        self.tv = Television()
        self.__init__()

        self.tv.volume_down()
        assert self.tv.__str__() == f'Power = False, Channel = 0, Volume = 0.'  # tv is off and volume down

        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__() == f'Power = True, Channel = 0, Volume = 1.'  # tv is on and volume down when at max

        self.tv.mute()
        self.tv.volume_down()
        assert self.tv.__str__() == f'Power = True, Channel = 0, Volume = 0.'  # tv is on, muted and volume down

        self.tv.volume_down()
        assert self.tv.__str__() == f'Power = True, Channel = 0, Volume = 0.'  # tv is on and volume down past min
