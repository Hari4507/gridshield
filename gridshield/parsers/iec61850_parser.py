def parse_iec61850(data):

    try:

        parts = data.split(",")

        protocol = "iec61850"
        grid = int(parts[1])
        value = int(parts[2])

        return protocol, grid, value

    except:
        return None