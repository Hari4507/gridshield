import socket
import random
import time

protocols = ["modbus", "iec", "dnp3"]

HOST = "gridshield"
PORT = 502


def send_packets():

    print("\nSending 5 SCADA commands...\n")

    for i in range(5):

        protocol = random.choice(protocols)
        grid = random.randint(1,3)

        if random.random() < 0.8:
            value = random.randint(150,350)
        else:
            value = random.randint(600,900)

        msg = f"{protocol},{grid},{value}"

        try:

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            sock.send(msg.encode())

            print("Sent:", msg)

            sock.close()

        except Exception as e:

            print("Error:", e)

        time.sleep(1)


while True:

    print("\nSCADA CONTROL PANEL")
    print("1 → Run 5 command simulation")
    print("2 → Quit")

    choice = input("Select option: ")

    if choice == "1":

        send_packets()

    elif choice == "2":

        print("Stopping SCADA simulator")
        break

    else:

        print("Invalid option")