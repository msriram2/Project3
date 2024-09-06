import unittest
from Input import Input
from Output import Client_Move, AC, AP_Move, Final_Coord
from pathlib import Path

#Testcase for input works!


class TestOpenFile(unittest.TestCase):
    def setUp(self):
        path = Path(r"C:\Users\Owner\OneDrive\Desktop\ICS 33 Summer\Projects\Project3\P3TestFile.txt")
        self.input = Input(path)

    def test_assign_dicts(self):
        Lines = [['AP','AP1','0','0','6','20', '2.4/5','WiFi6','true','true','true','50','10','75'],
                 ['CLIENT','Client1','10','10','WiFi6','2.4/5','true','true','true','73'],
                 ['MOVE', 'Client1', '10', '9']]
        Result = [{'Type': 'AP', 'APName': 'AP1', 'Coord_x': '0', 'Coord_y': '0', 'Channel': '6', 'Power': '20',
                   'Frequency': '2.4/5', 'Standard': 'WiFi6', 'Supports_11k': 'true', 'Supports_11v': 'true',
                   'Supports_11r': 'true', 'Coverage Radius': '50', 'Device Limit': '10', 'Minimal RSSI': '75'},
                  {'Type':'CLIENT', 'Client Name': 'Client1', 'Coord_x': '10', 'Coord_y':'10', 'Standard':'WiFi6',
                   'Speed':'2.4/5', 'Supports_11k':'true', 'Supports_11v':'true', 'Supports_11r':'true',
                   'Minimal_RSSI':'73'},
                  {'Type': 'MOVE', 'Client Name': 'Client1', 'Coord_x': '10', 'Coord_y': '9'}]
        assign_dicts = self.input.assign_dicts(Lines)
        self.assertEqual(assign_dicts, Result)

#OUTPUT MODULE


class TestClientVarAssign(unittest.TestCase):
    
    def setUp(self):
        Device = [{'Type': 'AP', 'APName': 'AP1', 'Coord_x': '0', 'Coord_y': '0', 'Channel': '6', 'Power': '20',
                   'Frequency': '2.4/5', 'Standard': 'WiFi6', 'Supports_11k': 'true', 'Supports_11v': 'true',
                   'Supports_11r': 'true', 'Coverage Radius': '50', 'Device Limit': '10'},
                  {'Type': 'CLIENT', 'Client Name': 'Client1', 'Coord_x': '10', 'Coord_y': '10', 'Standard': 'WiFi6',
                   'Speed': '2.4/5', 'Supports_11k': 'true', 'Supports_11v': 'true', 'Supports_11r': 'true',
                   'Minimal_RSSI': '73'},
                  {'Type': 'MOVE', 'Client Name': 'Client1', 'Coord_x': '10', 'Coord_y': '9'}]
        self.cli_move = Client_Move(Device)

    def test_establish_cli_coords(self):
        establish_cli_coords = self.cli_move.establish_cli_coords()
        self.assertEqual(establish_cli_coords, [10, 10])


    def test_cli_rssi(self):
        Device = [{'Type': 'AP', 'APName': 'AP1', 'Coord_x': '0', 'Coord_y': '0', 'Channel': '6', 'Power': '20',
                   'Frequency': '2.4/5', 'Standard': 'WiFi6', 'Supports_11k': 'true', 'Supports_11v': 'true',
                   'Supports_11r': 'true', 'Coverage Radius': '50', 'Device Limit': '10'},
                  {'Type': 'CLIENT', 'Client Name': 'Client1', 'Coord_x': '10', 'Coord_y': '10', 'Standard': 'WiFi6',
                   'Speed': '2.4/5', 'Supports_11k': 'true', 'Supports_11v': 'true', 'Supports_11r': 'true',
                   'Minimal_RSSI': '73'},
                  {'Type': 'MOVE', 'Client Name': 'Client1', 'Coord_x': '10', 'Coord_y': '9'}]
        cli_rssi = self.cli_move.cli_rssi(Device)
        self.assertEqual(cli_rssi, 73)
    

    def test_cli_calc_range(self):
        cli_range = self.cli_move.cli_calculate_range()
        self.assertEqual(cli_range, [[83,0], [83,0]])

class TestACOverlapDetection(unittest.TestCase):
    def setUp(self):
        Device = [{'Type': 'AP', 'APName': 'AP1', 'Coord_x': '0', 'Coord_y': '0', 'Channel': '6', 'Power': '20',
                   'Frequency': '2.4/5', 'Standard': 'WiFi6', 'Supports_11k': 'true', 'Supports_11v': 'true',
                   'Supports_11r': 'true', 'Coverage Radius': '50', 'Device Limit': '10'}]
        self.ac = AC(Device)

    def test_identify_channel(self):
        channel_test = self.ac.identify_channel()
        self.assertEqual(channel_test, 'AC REQUIRES AP1 TO CHANGE CHANNEL TO 5')



class TestAPVarAssign(unittest.TestCase):

    def setUp(self):
        Device = [{'Type': 'AP', 'APName': 'AP1', 'Coord_x': '0', 'Coord_y': '0', 'Channel': '6', 'Power': '20',
                   'Frequency': '2.4/5', 'Standard': 'WiFi6', 'Supports_11k': 'true', 'Supports_11v': 'true',
                   'Supports_11r': 'true', 'Coverage Radius': '50', 'Device Limit': '10', 'Minimal RSSI': '75'},
                  {'Type': 'CLIENT', 'Client Name': 'Client1', 'Coord_x': '10', 'Coord_y': '10', 'Standard': 'WiFi6',
                   'Speed': '2.4/5', 'Supports_11k': 'true', 'Supports_11v': 'true', 'Supports_11r': 'true',
                   'Minimal_RSSI': '73'},
                  {'Type': 'MOVE', 'Client Name': 'Client1', 'Coord_x': '10', 'Coord_y': '9'}]
        self.ap_move = AP_Move(Device)

    def test_establish_ap_coords(self):
        establish_ap_coords = self.ap_move.establish_ap_coords()
        self.assertEqual(establish_ap_coords, [0, 0])

    def test_ap_rssi(self):
        ap_rssi = self.ap_move.ap_rssi()
        self.assertEqual(ap_rssi, '75')

    def test_ap_calc_range(self):
        ap_range = self.ap_move.ap_range()
        self.assertEqual(ap_range, [[75, -75], [75, -75]])

class TestFinalCoord(unittest.TestCase):

    def setUp(self):
        Device = [{'Type': 'AP', 'APName': 'AP1', 'Coord_x': '0', 'Coord_y': '0', 'Channel': '6', 'Power': '20',
                   'Frequency': '2.4/5', 'Standard': 'WiFi6', 'Supports_11k': 'true', 'Supports_11v': 'true',
                   'Supports_11r': 'true', 'Coverage Radius': '50', 'Device Limit': '10', 'Minimal RSSI': '75'},
                  {'Type': 'CLIENT', 'Client Name': 'Client1', 'Coord_x': '10', 'Coord_y': '10', 'Standard': 'WiFi6',
                   'Speed': '2.4/5', 'Supports_11k': 'true', 'Supports_11v': 'true', 'Supports_11r': 'true',
                   'Minimal_RSSI': '73'},
                  {'Type': 'MOVE', 'Client Name': 'Client1', 'Coord_x': '10', 'Coord_y': '9'}]
        self.final_coord = Final_Coord(Device)

    def test_final_coord(self):
        establish_final_coord = self.final_coord.establish_final_coord()
        self.assertEqual(establish_final_coord, [10, 9])

class TestUpdateCoords(unittest.TestCase):
    def setUp(self):
        Device = [{'Type': 'AP', 'APName': 'AP1', 'Coord_x': '0', 'Coord_y': '0', 'Channel': '6', 'Power': '20',
                   'Frequency': '2.4/5', 'Standard': 'WiFi6', 'Supports_11k': 'true', 'Supports_11v': 'true',
                   'Supports_11r': 'true', 'Coverage Radius': '50', 'Device Limit': '10', 'Minimal RSSI': '75'},
                  {'Type': 'CLIENT', 'Client Name': 'Client1', 'Coord_x': '10', 'Coord_y': '10', 'Standard': 'WiFi6',
                   'Speed': '2.4/5', 'Supports_11k': 'true', 'Supports_11v': 'true', 'Supports_11r': 'true',
                   'Minimal_RSSI': '73'},
                  {'Type': 'MOVE', 'Client Name': 'Client1', 'Coord_x': '10', 'Coord_y': '9'}]
        self.final_coord = Final_Coord(Device)






