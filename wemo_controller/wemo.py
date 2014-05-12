from ouimeaux.environment import Environment

env = Environment()
DISCOVER_DELAY = .5

def on(switch_name, discover_delay = None):
    if discover_delay is None:
        return on(switch_name, DISCOVER_DELAY)
    else: 
        env.start() 
        env.discover(seconds=discover_delay)
        if switch_name in env.list_switches():
            switch = env.get_switch(switch_name)
            switch.on()
            return str(switch.get_state()) 
        else:
            return "No Switches Found With Name: " + switch_name;

def off(switch_name, discover_delay = None):
    if discover_delay is None:
        return off(switch_name, DISCOVER_DELAY)
    else:
        env.start() 
        env.discover(seconds=discover_delay)
        if switch_name in env.list_switches():
            switch = env.get_switch(switch_name)
            switch.off()
            return str(switch.get_state()) 
        else:
            return "No Switches Found With Name: " + switch_name;

def get_state(switch_name, discover_delay = None):
    if discover_delay is None:
        return get_state(switch_name, DISCOVER_DELAY)
    else:
        env.start() 
        env.discover(seconds=discover_delay)
        if switch_name in env.list_switches():
            switch = env.get_switch(switch_name)
            switch.get_state()
            return str(switch.get_state()) 
        else:
            return "No Switches Found With Name: " + switch_name;
