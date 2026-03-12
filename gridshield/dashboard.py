from flask import Flask

app = Flask(__name__)

logs = []

@app.route("/")
def dashboard():

    html="""

    <h1>GridShield Smart Grid Cybersecurity Dashboard</h1>

    <h3>System Status</h3>
    <p>Firewall: ACTIVE</p>
    <p>Protocols monitored: Modbus / IEC61850 / DNP3</p>

    <h3>Recent Events</h3>

    """

    for log in logs[-20:]:
        html += f"<p>{log}</p>"

    html += """

    <h3>Threat Detection</h3>

    <p>✔ False Data Injection Detection</p>
    <p>✔ Command Validation</p>
    <p>✔ Anomaly Detection</p>

    """

    return html


def run_dashboard():

    app.run(host="0.0.0.0",port=5000)