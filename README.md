# Assembly Sim

This code implements a straightforward assembly line.  Items move along the line on free-moving pallets, i.e. pallets can move at their pace independent of those around them.

## Usage

The *Sim* class maintains and runs the simulation.  It processes the configuraiton of the simulation, builds the appropriate components, and runs the simulation.  

When a Sim object is created you can pass in the configuration as either a dict or a string.  If a dict it will be passed directly to load().  If a string it will be treated as the name for a YAML file, which will be loaded into a dict then passed to load().

Main operations:

* *load(config)* - loads a dict that describes a valid configuration (see below).  The *config* can also be passed in when the *Sim* object is created.
* *reset()* - resets the simulation by calling reset() on all components.
* *tick(n=1, display=True)* - runs the simulation for *n* ticks. Stops if all pallets reach the end of the line prior to *n* ticks. If *display=True* then print out the state at the end of the ticks.
* *display()* - prints out a simple display of the state of the simulation.  

The simulator runs using fixed-length time periods called *ticks*.  Ticks are defined as the time it will take a pallet to go one pallet length on the conveyor.  

### Example (pass in a dict)

```
$ python
import sim
import sample
s = sim.Sim(sample.config)
s.tick()  # runs one tick
s.tick(5) # runs 5 ticks
s.reset() # resets simulation
```

### Example (pass in a dict)

```
$ python
import sim
s = sim.Sim("sample.yaml")
s.tick()  # runs one tick
s.tick(5) # runs 5 ticks
s.reset() # resets simulation
```

## Components

The following are the main components of the system:

- *conveyor*

- *source*

- *sink*

- *station*

- *pallet*

## Configuration

The configuration is a python *dict* that contains the information to define the simulation.  The top-level items are:

- *pal_len*:  length of a pallet in inches (int)
- *num_pallets*: number of pallets in the simulation (int)
- *conveyors*:  an array of conveyor definitions (array)

Conveyor configurations have the following items:

- *conv_name'*:  name of the conveyor (string).  Currently not used for anything.
- *conv_len*:  length of the conveyor in feet (int)
- *conv_spd*:  conveyor speed in feet/minute (int)
- *stations*:  an array of station definitions (array)

Station configurations have the following items:

- *sta_num*:  station number (int)
- *sta_pos*:  station position on the conveyor in feet (int)
- *sta_cycle_time*:  number of seconds to process a pallet (int)
- *sta_type*::  type of station (not currently used (int)

The files *sample.py* and *sample.yaml* contain a valid configuration.

Note that only one conveyor can currently be specified.

## Current Limitations and Todos

1.  Currently only supports one conveyor

2. Currently the stations take a pallet, operate on it for a fixed amount of time, and pass it out.  Todo:  build out a set of more complex

3. The configuration and simulation currently expect one conveyor with a set of stations on it.  Todo:  generalize number of conveyors.

4. Currently ticks are an integer number of seconds.  A warning is given if a configuration yields a non-integer result.
