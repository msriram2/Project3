from Input import Input

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

class Update_Coords(Client_Move, AP_Move):
    def __init__(self, Device, cli_coord, final_coord, cli_RSSI, cli_range, ap_coord, ap_RSSI, ap_total_range):
        super().__init__(cli_coord, final_coord, cli_RSSI, cli_range, ap_coord, ap_RSSI, ap_total_range)
        self.Device = Device

    def __iter__(self):
        return self


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
            if self.cli_coord[1] == self.final_coord[1]:
                return f'Client has arrived at {self.cli_coord[0], self.cli_coord[1]}'
