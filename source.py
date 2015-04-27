# this is a source of pallets

import pallet

class PalletSource:

    def __init__(self, num_pallets, pal_len):
        self.name = "pallet source"
        self.num_pallets = num_pallets
        self.pal_len = pal_len
        self.pallets = []
        for i in range(0, num_pallets):
            self.pallets.append(pallet.Pallet(i, pal_len))
        # start with pallet 0
        self.curr_pallet = 0

    # called by the simulator to clear the state so it can start over
    def reset(self):
        # just call init again
        self.__init__(self.num_pallets, self.pal_len)

    # called by the simulator to connect the output
    def connect_output(self, conv):
        self.output = conv

    # called by the output when it takes the pallet
    # removes the next pallet to go
    def remove_pallet(self):
        self.pallets[self.curr_pallet] = None
        self.curr_pallet = self.curr_pallet + 1

    # called by the simulator once per time step
    #   current time is the input
    def tick(self, time):
        # if station in last slot and moving, then tell send it to your output
        # may call this multiple times, but not a big deal
        if self.curr_pallet < self.num_pallets:
            # set the start time in case it gets taken
            self.pallets[self.curr_pallet].start = time
            self.output.incoming_pallet(self.pallets[self.curr_pallet])
