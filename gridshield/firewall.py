import socket
import threading
import random
from flask import Flask

app = Flask(__name__)

HOST = "0.0.0.0"
PORT = 502

PLC_NODES = ["plc1","plc2","plc3"]

logs = []

protocols = ["modbus","iec","dnp3"]


def detect_anomaly(value):
    return value > 700


def validate(value):
    return value <= 500


def forward(grid,value):

    node = PLC_NODES[grid-1]

    try:

        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect((node,502))
        sock.send(str(value).encode())
        sock.close()

    except Exception as e:

        print("PLC error:",e)


def firewall_server():

    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind((HOST,PORT))
    server.listen()

    print("GridShield firewall listening on port 502")

    while True:

        conn,addr = server.accept()

        data = conn.recv(1024).decode()

        try:

            protocol,grid,value = data.split(",")

            grid = int(grid)
            value = int(value)

            msg = f"{protocol} grid {grid} value {value}"

            if detect_anomaly(value):

                log = f"⚠ ANOMALY → {msg}"

            elif not validate(value):

                log = f"❌ BLOCKED → {msg}"

            else:

                log = f"✅ EXECUTED → {msg}"

                forward(grid,value)

            logs.append(log)

        except:

            logs.append("Invalid packet")

        conn.close()


@app.route("/")
def dashboard():

    html = """
    <html>

    <head>
    <title>GridShield Smart Grid Security</title>

    <style>

    body{
        font-family: Arial;
        background:#0f172a;
        color:white;
        margin:0;
        padding:0;
    }

    .header{
        padding:20px;
        background:#020617;
        border-bottom:1px solid #1e293b;
    }

    h1{
        margin:0;
        color:#38bdf8;
    }

    .container{
        padding:30px;
    }

    .card{
        background:#1e293b;
        padding:20px;
        border-radius:8px;
        margin-bottom:20px;
    }

    .btn{
        background:#38bdf8;
        color:black;
        border:none;
        padding:12px 25px;
        font-size:16px;
        border-radius:6px;
        cursor:pointer;
    }

    .btn:hover{
        background:#0ea5e9;
    }

    .logs{
        background:#020617;
        padding:20px;
        border-radius:8px;
    }

    .executed{
        color:#22c55e;
    }

    .blocked{
        color:#ef4444;
    }

    .anomaly{
        color:#facc15;
    }

    .protocol{
        color:#38bdf8;
    }

    </style>
    </head>

    <body>

    <div class="header">
        <h1>GridShield Smart Grid Firewall</h1>
    </div>

    <div class="container">

    <div class="card">

        <h2>System Status</h2>

        Firewall Status : <b style='color:#22c55e'>ACTIVE</b><br><br>

        Protocol Monitoring :
        <span class="protocol">MODBUS</span> |
        <span class="protocol">IEC61850</span> |
        <span class="protocol">DNP3</span>

        <br><br>

        <button class="btn" onclick="run()">Run 5 Packet Simulation</button>

    </div>

    <div class="card logs">

    <h2>Security Logs</h2>

    """

    for log in logs[::-1]:

        if "EXECUTED" in log:
            html += f"<p class='executed'>{log}</p>"

        elif "BLOCKED" in log:
            html += f"<p class='blocked'>{log}</p>"

        elif "ANOMALY" in log:
            html += f"<p class='anomaly'>{log}</p>"

        else:
            html += f"<p>{log}</p>"


    html += """

    </div>

    </div>

    <script>

    function run(){
        fetch('/simulate').then(()=>location.reload())
    }

    </script>

    </body>

    </html>
    """

    return html


@app.route("/simulate")
def simulate():

    for i in range(5):

        protocol = random.choice(protocols)
        grid = random.randint(1,3)

        if random.random() < 0.8:
            value = random.randint(150,350)
        else:
            value = random.randint(600,900)

        msg = f"{protocol},{grid},{value}"

        try:

            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.connect(("localhost",502))
            sock.send(msg.encode())
            sock.close()

        except:
            pass

    return "done"


if __name__ == "__main__":

    t = threading.Thread(target=firewall_server)
    t.daemon = True
    t.start()

    app.run(host="0.0.0.0",port=5000)