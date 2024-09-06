from Input import Input
import math

class Client_Move():
    def __init__(self, Device):
        self.Device = Device
        self.cli_coord = []
        self.cli_RSSI = ''
        self.cli_range = []

    def establish_cli_coords(self):
        for Dict in self.Device:
            if Dict['Type'] == 'CLIENT':
                cli_coord_x = int(Dict['Coord_x'])
                cli_coord_y = int(Dict['Coord_y'])
                self.cli_coord.append(cli_coord_x)
                self.cli_coord.append(cli_coord_y)
                return self.cli_coord

    def cli_rssi(self, Device):
        for Dict in Device:
            if Dict['Type'] == 'CLIENT':
                self.cli_RSSI = int(Dict['Minimal_RSSI'])
                return self.cli_RSSI

    def cli_calculate_range(self):
        cli_x_range = []
        cli_y_range = []
        for Dict in self.Device:
            if Dict['Type'] == 'CLIENT':
                cli_range_x_right = int(Dict['Coord_x']) + int(Dict['Minimal_RSSI'])
                cli_x_range.append(cli_range_x_right)
                cli_range_x_left = int(Dict['Coord_x']) - int(Dict['Minimal_RSSI'])
                if cli_range_x_left < 0:
                    cli_range_x_left = 0
                cli_x_range.append(cli_range_x_left)
                self.cli_range.append(cli_x_range)

                cli_range_y_right = int(Dict['Coord_y']) + int(Dict['Minimal_RSSI'])
                cli_y_range.append(cli_range_y_right)
                cli_range_y_left = int(Dict['Coord_y']) - int(Dict['Minimal_RSSI'])
                if cli_range_y_left < 0:
                    cli_range_y_left = 0
                cli_y_range.append(cli_range_y_left)
                self.cli_range.append(cli_y_range)

        return self.cli_range


class AC(Input):
    def __init__(self, Device):
        super().__init__(Device)
        self.ac_log = []
        self.pref_channel = [1, 6, 11]

    def identify_channel(self):
        for dict in self.Device:
            if dict['Type'] == 'AP':
                for channel in self.pref_channel:
                    if int(dict['Channel']) != channel:
                        old_value = int(dict['Channel'])
                        old_value -= 1
                        dict['Channel'] = old_value
                        identify_statement = f'AC REQUIRES {dict["APName"]} TO CHANGE CHANNEL TO {dict["Channel"]}'
                        self.ac_log.append(identify_statement)

                return identify_statement

class AP_Move():
    #GOAL: The class should return a list of dictionaries containing one or more APs that can be accessed by the Output
    #class but cannot be updated because AP coordinates and range should remain the same?

    #Meaning I should instead initialize a dictionary that holds the permanent locations of different AP's, and this
    #list of dictionaries can be accessed by the AP name.
    #OR: I can create multiple instances that aren't instantiated yet, then updated those instances throughout each method
    #and save those instances to the dictionaries.

    def __init__(self, Device):
        self.Device = Device
        self.aps = []
        self.ap_coord = []
        self.ap_total_range = []

    def establish_ap_coords(self):
        for Dict in self.Device:
            if Dict['Type'] == 'AP':
                ap_coord_x = int(Dict['Coord_x'])
                ap_coord_y = int(Dict['Coord_y'])
                self.ap_coord.append(ap_coord_x)
                self.ap_coord.append(ap_coord_y)
                return self.ap_coord

    def ap_rssi(self):
        for dict in self.Device:
            if dict['Type'] == 'AP':
                if dict['Minimal RSSI'] != '':
                    ap_rssi = dict['Minimal RSSI']
                    return ap_rssi

    def ap_range(self):
        for dict in self.Device:
            if dict['Type'] == 'AP':
                ap_x_range = []
                ap_y_range = []

                ap_range_x_right = int(dict['Coord_x']) + int(dict['Minimal RSSI'])
                ap_x_range.append(ap_range_x_right)
                ap_range_x_left = int(dict['Coord_x']) - int(dict['Minimal RSSI'])
                if ap_range_x_left > 0:
                    ap_range_x_left = 0
                ap_x_range.append(ap_range_x_left)
                self.ap_total_range.append(ap_x_range)

                ap_range_y_right = int(dict['Coord_y']) + int(dict['Minimal RSSI'])
                ap_y_range.append(ap_range_y_right)
                ap_range_y_left = int(dict['Coord_y']) - int(dict['Minimal RSSI'])
                if ap_range_y_left > 0:
                    ap_range_y_left = 0
                ap_y_range.append(ap_range_y_left)
                self.ap_total_range.append(ap_y_range)

                return self.ap_total_range

class Final_Coord:

    def __init__(self, Device):
        self.device = Device
        self.final_coord = []

    def establish_final_coord(self):
        for dict in self.Device:
            if dict['Type'] == 'MOVE':
                final_coord_x = int(dict['Coord_x'])
                final_coord_y = int(dict['Coord_y'])
                self.final_coord.append(final_coord_x)
                self.final_coord.append(final_coord_y)
                return self.final_coord

class Output(Client_Move, AP_Move):
    #Should contain:
        #Client: When Client has connected, disconnected, signal strength, and roaming status.
        #AP: Number of APs, AP Location, AP signal strength, and whether AP is connected to it or not.

    def __init__(self, Device, step_n, cli_coord, cli_RSSI, cli_range, ap_coord, ap_RSSI, ap_total_range):
        #NOTE: For some reason, the program is not able to detect arguments. Will have to revise on multiple inheritance
        super().__init__(cli_coord, cli_RSSI, cli_range, ap_coord, ap_RSSI, ap_total_range)
        self.Device = Device
        self.step_n = step_n

    def __iter__(self):
        return self

"""
        Might consider using an iter/next methods to deal with client location. __iter__ iterates and adds/subtracts
        by 1 up until it equals the final location.
        __next__ should check the connection status before moving on to the next coordinate. Should store the range of
        the device and the AP to make sure that they are in each other's range. If not, then __next__ should send a
        message
"""

"""
    def __next__(self):
        while self.cli_coord != self.final_coord:
            if self.cli_coord[0] > self.final_coord[0]:
                self.cli_coord[0] -= 1
            if self.cli_coord[1] > self.final_coord[1]:
                self.cli_coord[1] -= 1
            if self.cli_coord[0] < self.final_coord[0]:
                self.cli_coord[0] += 1
            if self.cli_coord[1] < self.final_coord[1]:
                self.cli_coord[1] += 1
        if self.cli_coord[0] == self.final_coord[0]:
            if self.cli_coord_tup[1] == self.final_coord_tup[1]:
                return f'Client has arrived at {self.cli_coord[0], self.cli_coord[1]}'
"""
