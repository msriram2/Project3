from pathlib import Path

#GOAL: Return a list of dictionaries labeling each element of the line so the output function can work with it
class Input:

    def __init__(self, Path):
        self.Path = Path
        self.Device = []

    #Open file WORKS!
    def open_file(self):
        Lines = []
        with open(self.Path, 'r') as file:
            for line in file:
                Line = line.split()
                Lines.append(Line)
            return Lines

    #Assign Dicts works!
    def assign_dicts(self, Lines):
        for line in Lines:
            if line[0] == 'AP':
                AP_Dict = {}
                AP_Dict['Type'] = line[0]
                AP_Dict['APName'] = line[1]
                AP_Dict['Coord_x'] = line[2]
                AP_Dict['Coord_y'] = line[3]
                AP_Dict['Channel'] = line[4]
                AP_Dict['Power'] = line[5]
                AP_Dict['Frequency'] = line[6]
                AP_Dict['Standard'] = line[7]
                AP_Dict['Supports_11k'] = line[8]
                AP_Dict['Supports_11v'] = line[9]
                AP_Dict['Supports_11r'] = line[10]
                AP_Dict['Coverage Radius'] = line[11]
                AP_Dict['Device Limit'] = line[12]
                AP_Dict['Minimal RSSI'] = line[13]
                self.Device.append(AP_Dict)

            if line[0] == 'CLIENT':
                Client_Dict = {}
                Client_Dict['Type'] = line[0]
                Client_Dict['Client Name'] = line[1]
                Client_Dict['Coord_x'] = line[2]
                Client_Dict['Coord_y'] = line[3]
                Client_Dict['Standard'] = line[4]
                Client_Dict['Speed'] = line[5]
                Client_Dict['Supports_11k'] = line[6]
                Client_Dict['Supports_11v'] = line[7]
                Client_Dict['Supports_11r'] = line[8]
                Client_Dict['Minimal_RSSI'] = line[9]
                self.Device.append(Client_Dict)

            if line[0] == 'MOVE':
                Move_Dict = {}
                Move_Dict['Type'] = line[0]
                Move_Dict['Client Name'] = line[1]
                Move_Dict['Coord_x'] = line[2]
                Move_Dict['Coord_y'] = line[3]
                self.Device.append(Move_Dict)

        return self.Device


#if __name__ == '__main__':


        
