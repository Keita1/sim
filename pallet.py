# this is a pallet object

class Pallet:

    def __init__(self, pal_num, pal_len):
        self.pal_num = pal_num
        # plen in inches, not used here
        self.pal_len = pal_len
        # these are the times it starts and ends
        self.start = 0
        self.end = 0
        # this is a status object where stuff can get written as needed
        self.status = "new"


    # currently nothing gets called other than reset
    def reset(self):
        self.__init__()
