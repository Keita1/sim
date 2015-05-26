# main file of the simluator

# import the parts
import pallet
import sink
import source
import station
import conveyor
import config as conf

class Sim:

    def __init__(self, config=None):
        self.start = None
        self.conveyor = None
        self.stations = []
        self.source = None
        self.sink = None
        self.time = 0
        self.tick_len = 0
        if type(config) is str:
            self.load(conf.read_yaml(config))
        elif type(config) is dict:
            self.load(config)

    def load(self, config):
        # save the config
        self.config = config
        # create the pallet source and sink
        self.source = source.PalletSource(config['num_pallets'], config['pal_len'])
        self.sink = sink.PalletSink()
        # create the conveyor
        # only one supported right now
        if len(config['conveyors']) > 1:
            error("Only one conveyor supported at this time")
        conv_config = config['conveyors'][0]
        self.conveyor = conveyor.Conveyor(conv_config['conv_spd'], conv_config['conv_len'], config['pal_len'])
        # connect the source, conveyor and sink
        self.source.connect_output(self.conveyor)
        self.conveyor.connect_input(self.source)
        self.sink.connect_input(self.conveyor)
        self.conveyor.connect_output(self.sink)
        # create the stations
        for stn in conv_config['stations']:
            # create it
            new_station = station.Station(stn['sta_num'], stn['sta_pos'],
                stn['sta_type'], stn['sta_cycle_time'])
            # keep a pointer to it, though don't do anything with it now
            self.stations.append(new_station)
            # add it to the conveyor
            self.conveyor.add_station(new_station)
        # set the length of the time tick to time for pallet to go one pallet length
        self.tick_len = config['pal_len'] * 5 / conv_config['conv_spd']
        # create the array of things to call in the right order
        self.top_level_objects = [self.sink, self.conveyor, self.source]
        self.display()
        
    def reset(self):
        self.time= 0
        for obj in self.top_level_objects:
            obj.reset()
        self.display()

    def tick(self, n=1, display=True):
        for i in range(0, n):
            self.time = self.time + self.tick_len
            for obj in self.top_level_objects:
                obj.tick(self.time)
            if self.sink.pallets_collected == self.config['num_pallets']:
                print "Simulation ended"
                break
        if display:
            self.display()


    def display(self):
        slots = self.conveyor.slots
        print "Time = " + str(self.time)
        print "Unstarted pallets = " + str(self.source.num_pallets - self.source.curr_pallet)
        print "Finished pallets = " + str(self.sink.pallets_collected)
        out_string = ""
        for slot in range(0, slots):
            new_char = " "
            if self.conveyor.stations[slot] != None:
                if self.conveyor.stations[slot].pallet == None:
                    new_char = "S"
                else:
                    new_char = "P"
            out_string = out_string + new_char
        print out_string
        out_string = ""
        for slot in range(0, slots):
            new_char = "_"
            if self.conveyor.pallets[slot] != None:
                if self.conveyor.pallets[slot].status == 'moving':
                    new_char = "P"
            out_string = out_string + new_char
        print out_string
