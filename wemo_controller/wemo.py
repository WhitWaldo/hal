from ouimeaux.environment import Environment

env = Environment()
DISCOVER_DELAY = .5
def start_and_discover(env, switch_name):
    try:
        env.start()
        env.discover(seconds=DISCOVER_DELAY)
        switch_list = env.list_switches()
        if switch_name in switch_list:
           switch = env.get_switch(switch_name)
           return switch 
        else:
            return False
    except:
        print "An exception was raised trying to find the switch."
        return False

def on(switch_name, discover_delay = None):
    if discover_delay is None:
        return on(switch_name, DISCOVER_DELAY)
    else:
        switch = start_and_discover(env, switch_name)
        if switch is not False: 
            switch.on()
            return str(switch.get_state()) 
        else:
            return "No Switches Found With Name: " + switch_name;

def off(switch_name, discover_delay = None):
    if discover_delay is None:
        return off(switch_name, DISCOVER_DELAY)
    else:
        switch = start_and_discover(env, switch_name)
        if switch is not False: 
            switch.off()
            return str(switch.get_state()) 
        else:
            return "No Switches Found With Name: " + switch_name;

def get_state(switch_name, discover_delay = None):
    if discover_delay is None:
        return get_state(switch_name, DISCOVER_DELAY)
    else:
        switch = start_and_discover(env, switch_name)
        if switch is not False: 
            return str(switch.get_state()) 
        else:
            return "No Switches Found With Name: " + switch_name;
