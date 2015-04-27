# this collects the pallets at the end

class PalletSink:

    def __init__(self):
        self.pallets = []
        self.in_pallet = None
        self.input = None
        self.pallets_collected = 0

    # called by the simulator to clear the state so it can start over
    def reset(self):
        self.__init__()

    # called by the simulator to connect the input
    def connect_input(self, conv):
        self.input = conv

    # called by the input when there's a pallet that's available
    # puts the pallet in in_pallet for next cycle
    def incoming_pallet(self, pallet):
        self.in_pallet = pallet

    # called by the simulator once per time step
    #   lenth of time is the input
    def tick(self, time):
        # if incoming pallet
        if self.in_pallet != None:
            # chaneg its status
            self.in_pallet.status = 'done'
            # set the time it finished
            self.in_pallet.end = time
            self.pallets.append(self.in_pallet)
            self.in_pallet = None
            self.input.remove_pallet()
            self.pallets_collected = self.pallets_collected + 1
