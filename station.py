# this is a generic station object
# it gets a call once per second
# It returns a two-item list:

class Station:

    def __init__(self, sta_num, sta_loc, sta_type, cycle_time):
        self.sta_type = sta_type
        self.sta_num = sta_num
        self.sta_loc = sta_loc
        self.cycle_time = cycle_time
        # time a pallet has been here
        self.pallet_time_done = 0
        self.pallet = None
        self.pallets = 0
        self.pallet_old_status = ""

    def reset(self):
        self.pallet = None
        self.pallets = 0
        self.pallet_time_done = 0

    def new_pallet(self, pallet, time):
        # make sure you don't already have a pallet
        if self.pallet != None:
            error("Already have a pallet: station " + str(snum))
        else:
            self.pallet=pallet
            self.pallet_old_status = self.pallet.status
            self.pallet.status = "in station " + str(self.sta_num)
            self.pallet_time_done = time + self.cycle_time

    # called by the conveyor once per time step
    def tick(self, time):
        # if pallet is done, change its status
        if (self.pallet != None) & (time > self.pallet_time_done):
            self.pallets = self.pallets + 1
            # resent the pallets status to what it was before
            self.pallet.status = self.pallet_old_status
            self.pallet = None
