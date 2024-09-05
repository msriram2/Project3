from Input import Input
import math

#Input module works! Everything is opened, and a list of dictionaries is returned!
class Client_Move():
    # Keep a list of actions for each move the client makes
    def __init__(self, Device):
        self.Device = Device
        self.cli_coord = []
        self.cli_RSSI = ''
        self.cli_range = []

    def __setattr__(self, name, value):
        if name == 'Device':
            if isinstance(name, list):
                for Dict in name:
                    if Dict['Type'] == 'CLIENT':
                        value = Dict
            else:
                raise ValueError("Instance must be a list")
        super().__setattr__(name, value)

    def establish_cli_coords(self):
        for Dict in self.Device:
            if Dict['Type'] == 'CLIENT':
                cli_coord_x = int(self.Device['Coord_X'])
                cli_coord_y = int(self.Device['Coord_y'])
                self.cli_coord.append(cli_coord_x)
                self.cli_coord.append(cli_coord_y)
                return self.cli_coord

    #Test Works!
    def cli_rssi(self, Device):
        for Dict in Device:
            if Dict['Type'] == 'CLIENT':
                self.cli_RSSI = int(Dict['Minimal_RSSI'])
                return self.cli_RSSI

    #Test Works!
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

    def identify_channel(self):
        pref_channel = [1, 6, 11]
        for dict in self.Device:
            if dict['Type'] == 'AP':
                for channel in pref_channel:
                    if int(dict['Channel']) != channel:
                        old_value = int(dict['Channel'])
                        old_value -= 1
                        dict['Channel'] = old_value
                        identify_statement = f'AC REQUIRES {dict["APName"]} TO CHANGE CHANNEL TO {dict["Channel"]}'
                        self.ac_log.append(identify_statement)
                        return identify_statement

"""
class AP_Move(Input):
    #GOAL: The class should return a list of dictionaries containing one or more APs that can be accessed by the Output
    #class but cannot be updated because AP coordinates and range should remain the same?

    #Meaning I should instead initialize a dictionary that holds the permanent locations of different AP's, and this
    #list of dictionaries can be accessed by the AP name.
    #OR: I can create multiple instances that aren't instantiated yet, then updated those instances throughout each method
    #and save those instances to the dictionaries.

    def __init__(self, Device):
        super().__init__(Device)
        self.aps = [] #List containing dictionaries of APs
        self.ap_coord = []
        self.ap_total_range = []

    def __setattr__(self, name, value):
        if name == 'Device':
            if isinstance(name, list):
                for Dict in name:
                    if Dict['Type'] == 'AP':
                        value = Dict
            else:
                raise ValueError("Instance must be a list")
        super().__setattr__(name, value)

    def establish_ap_coords(self):
        for Dict in self.Device:
            if Dict['Type'] == 'AP':
                ap_coord_x = int(self.Device['Coord_X'])
                ap_coord_y = int(self.Device['Coord_y'])
                self.ap_coord.append(ap_coord_x)
                self.ap_coord.append(ap_coord_y)
                return self.ap_coord

    
    def ap_rssi(self):
        #What is power? Will have to better understand RSSI to calculate.
        if self.Device['Minimal_RSSI'] != '':
            ap_rssi = self.Device['Minimal_RSSI']
        else:
            #Run calculation here
            ap_rssi = #power - 20 * math.log(
        return ap_rssi
    

    def ap_range(self):
        for dict in self.Device:
            if dict['Type'] == 'AP':
                ap_x_range = []
                ap_y_range = []

                ap_range_x_right = int(self.Device['Coord_x']) + int(self.Device['Minimal_RSSI'])
                ap_x_range.append(ap_range_x_right)
                ap_range_x_left = int(self.Device['Coord_x']) - int(self.Device['Minimal_RSSI'])
                if ap_range_x_left > 0:
                    ap_range_x_left = 0
                ap_x_range.append(ap_range_x_left)
                self.ap_total_range.append(ap_x_range)

                ap_range_y_right = int(self.Device['Coord_y']) + int(self.Device['Minimal_RSSI'])
                ap_y_range.append(ap_range_y_right)
                ap_range_y_left = int(self.Device['Coord_y']) - int(self.Device['Minimal_RSSI'])
                if ap_range_y_left > 0:
                    ap_range_y_left = 0
                ap_y_range.append(ap_range_y_left)
                self.ap_total_range.append(ap_y_range)

                return self.ap_total_range

    def total_aps(self):


"""
"""

class Output(Client_Move, AP_Move):
    #Should contain:
        #Client: When Client has connected, disconnected, signal strength, and roaming status.
        #AP: Number of APs, AP Location, AP signal strength, and whether AP is connected to it or not.

    def __init__(self, step_n, cli_coord, cli_RSSI, cli_range, ap_coord, ap_RSSI, ap_range):
        #NOTE: For some reason, the program is not able to detect arguments. Will have to revise on multiple inheritance
        super().__init__(cli_coord, cli_RSSI, cli_range, ap_coord, ap_RSSI, ap_range)
        self.step_n = step_n

    def __iter__(self):
        #Derive from parent class and establish initial location of client.
        #Derve from parent class and establish initial location of final location (move)
        #GOAL: If client location == final location, the iteration stops.
        """
"""
        Might consider using an iter/next methods to deal with client location. __iter__ iterates and adds/subtracts
        by 1 up until it equals the final location.
        __next__ should check the connection status before moving on to the next coordinate. Should store the range of
        the device and the AP to make sure that they are in each other's range. If not, then __next__ should send a
        message
        
        return self
"""

"""
    def __next__(self):
        How does disconnect happen?: Signal strength is determined by RSSI. We know that the client
        starts at a specific coordinate. The goal is for the client to move to the coordinates in 'Move'.
        Therefore, while the client coord is trying to match Move coords, it will either move closer to, farther
        from, leave, or enter the vicinity of an AP signal.

        Think about it this way. Coordinates only represent position, however, RSSI represents the coverage.
        For example, if the coordinates of Client is (10, 10), then the coordinates the width of the signal
        strength all around is max (10, 85), (85, 10). If the AP coordinate is at (0,0), then the width will be
        (0, 75) (75, 0).

        RSSI will change over time based on Client's distance from AP.
        
        if self.cli_coord_tup[0] == self.final_coord_tup[0]:
            if self.cli_coord_tup[1] == self.final_coord_tup[1]:
                return f'Client has arrived at {self.cli_coord_tup[0], self.cli_coord_tup[0]}'
        else:
            while self.cli_coord_tup != self.final_coord_tup:
                if self.cli_coord_tup[0] > self.final_coord_tup[0]:
                    self.cli_coord_tup[0] -= 1
                if self.cli_coord_tup[1] > self.final_coord_tup[1]:
                    self.cli_coord_tup[1] -= 1
                if self.cli_coord_tup[0] < self.final_coord_tup[0]:
                    self.cli_coord_tup[0] += 1
                if self.cli_coord_tup[1] < self.final_coord_tup[1]:
                    self.cli_coord_tup[1] += 1

    def established_locations(self):
        for dict in self.Device:
            if dict['Type'] == 'AP':
                ap_loc_x = dict['Coord_x']
                ap_loc_y = dict['Coord_y']
            if dict['Type'] == 'CLIENT':
                cli_loc_x = dict['Coord_x']
                cli_loc_y = dict['Coord_y']
            if dict['Type'] == 'MOVE':
                final_loc_x = dict['Coord_x']
                final_loc_y = dict['Coord_y']
        #Question, how would I be able to return this? Should I instead use a generator function that identifies
        #keys with coordinates and yields assigned coordinates?
"""


