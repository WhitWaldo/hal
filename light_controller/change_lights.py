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
        "modedown": "\x28\x00\x55",
        "color": "\x20{0}\x55"
        }

colors = {
        "violet": "\x00",
        "blue": "\x10",
        "lightblue": "\x20",
        "aqua": "\x30",
        "mint": "\x40",
        "lightgreen": "\x50",
        "green": "\x60",
        "lime": "\x70",
        "yellow": "\x80",
        "yelloworange": "\x90",
        "orange": "\xA0",
        "red": "\xB0",
        "pink": "\xC0",
        "fusia": "\xD0",
        "lilac": "\xE0",
        "lavendar": "\xF0"
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
    return "Lights " + command

def change_color(color):
    if color == "white":
        for i in range(0,19):
            send(hex_commands.get("modedown"))
    else:
        hex_command = hex_commands.get("color")
        if color in colors:
            hex_color = colors.get(color)
        elif color.isdigit():
            hex_color = chr(int(color))
        else:
            return "Invalid color"
        send(hex_command.format(str(hex_color)))
    return "Light color " + color

def send(hex_command):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(hex_command, (wifi_bridge_ip, wifi_bridge_port))
    return "Success"
