# Documentation: http://www.limitlessled.com/dev/
import socket

wifi_bridge_ip = "192.168.1.157"
wifi_bridge_port = 50000

hex_commands = {
        "on": "\x35\x00\x55",
        "off": "\x39\x00\x55",
        "brighten": "\x3C\x00\x55",
        "dim": "\x34\x00\x55",
        "warmer": "\x3E\x00\x55",
        "cooler": "\x3F\x00\x55",
        "full": "\xB5\x00\x55",
        "night": "\xB9\x00\x55",
        "color": "\x20{0}\x55"
        }

def change_function(command):
    hex_command = hex_commands.get(command)
    if hex_command is not None:
        send(hex_command)
    else:
        if command == "maxbright":
            for i in range(0,9):
                send(hex_commands.get("brighten"))
        elif command == "maxdim":
            for i in range(0,9):
                send(hex_commands.get("dim"))
    return "Success"

def send(hex_command):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(hex_command, (wifi_bridge_ip, wifi_bridge_port))
    return "Success"
