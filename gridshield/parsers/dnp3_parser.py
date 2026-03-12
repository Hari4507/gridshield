def parse_dnp3(data):

    try:

        parts = data.split(",")

        protocol = "dnp3"
        grid = int(parts[1])
        value = int(parts[2])

        return protocol, grid, value

    except:
        return None