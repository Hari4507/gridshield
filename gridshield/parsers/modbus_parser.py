def parse_modbus(data):

    try:
        parts = data.split(",")

        protocol = "modbus"
        grid = int(parts[1])
        value = int(parts[2])

        return protocol, grid, value

    except:
        return None