43# Implements a straight conveyor section
# Can be extended to do more complex stuff
# Breaks teh conveyor length into N senctions, each plen long
# Cycle time is time to traverse one length at speed.

import math

class Conveyor:

    def __init__(self, conv_spd, conv_len, pal_len, conv_name = "mainline"):
        self.conv_name = conv_name
        # save these away, though don't really use them now
        self.conv_spd = conv_spd
        self.conv_name = conv_name
        # We use these below
        self.conv_len = conv_len
        self.pal_len = pal_len
        # make conveyor length an integer number of pallets by rounding up
        # % operator calculates the remainder
        if conv_len * 12 % pal_len != 0:
            print "Making convenor " + str(conv_num) + " slightly longer to be an integer number of pallets"
        # set the number of pallets the conveyor will hold.
        #  round up and make it an integer
        self.slots = int(math.ceil(conv_len * 12 / pal_len))
        # zero based
        self.pallets = self.slots * [None]
        self.stations = self.slots * [None]
        # this conveyor has one input and output
        self.in_pallet = None

    # called by the simulator to clear the state so it can start over
    def reset(self):
        self.pallets = self.slots * [None]
        self.in_pallet = None
        for station in self.stations:
            if station:
                station.reset()

    # called by the simulator to add a station to a specific slot
    def add_station(self, station):
        slot = station.sta_loc
        # put it in right spot on conveyor, 0 based
        self.stations[slot-1] = station

    # called by the simulator to connect the input
    def connect_input(self, conv):
        self.input = conv

    # called by the simulator to connect the output
    def connect_output(self, conv):
        self.output = conv

    # called by the input when there's a pallet that's available
    # puts the pallet in in_pallet for next cycle
    def incoming_pallet(self, pallet):
        self.in_pallet = pallet

    # called by the output when it takes the pallet
    # removes the pallet from the last slot
    def remove_pallet(self):
        self.pallets[self.slots - 1] = None


    # called by the simulator once per time step
    #   lenth of time is the input
    def tick(self, time):
        # call all of the stations
        for slot in range(0, self.slots):
            if self.stations[slot] != None:
                self.stations[slot].tick(time)
        # moves each pallet one slot if it can
        # start with last slot, move back towards beginning
        for slot in range(self.slots - 1, 0, -1):
            # if the slot is free, see if the pallet in hte
            #     next one can move
            if self.pallets[slot] == None:
                if self.pallets[slot - 1] != None:
                    if self.pallets[slot - 1].status == "moving":
                        self.pallets[slot] = self.pallets[slot - 1]
                        self.pallets[slot - 1] = None
                        # if this has a station, then tell the station the pallet is here
                        if self.stations[slot] != None:
                            self.stations[slot].new_pallet(self.pallets[slot], time)
        # if pallet in last slot and moving, then send it to your output
        # may call this multiple times, but not a big deal
        if self.pallets[self.slots - 1] != None:
            if self.pallets[self.slots - 1].status == 'moving':
                self.output.incoming_pallet(self.pallets[self.slots - 1])
        # Now deal with slot 0
        if (self.pallets[0] == None) & (self.in_pallet != None):
            self.pallets[0] = self.in_pallet
            self.pallets[0].status = 'moving'
            self.in_pallet = None
            self.input.remove_pallet()
