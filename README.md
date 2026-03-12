# GridShield
### Protecting Smart Grids from Malicious Control Commands

GridShield is a prototype cybersecurity firewall designed to protect **modern power grid infrastructure** from malicious or unsafe control commands.

Power grids rely on Industrial Control Systems (ICS) and SCADA networks that communicate using protocols like **Modbus, IEC 61850, and DNP3**. These protocols were originally designed decades ago when networks were isolated and trusted. As these systems became connected to modern networks, they became vulnerable to cyber attacks.

GridShield demonstrates how **protocol-aware inspection and command validation** can prevent unsafe commands before they reach critical infrastructure.

---

# Project Motivation

Traditional network firewalls inspect only **IP addresses, ports, and packet structure**. They do not understand the **actual meaning of commands being sent to grid equipment**.

For example, a command that increases voltage beyond safe limits may still look valid at the network level and pass through a normal firewall.

GridShield solves this by performing **semantic inspection of industrial control commands** before they are executed.

Instead of simply checking the network layer, GridShield checks whether the command **makes sense for the physical grid system**.

---

# What GridShield Does

GridShield acts as a **security layer between SCADA systems and field devices**.

It performs:

• Protocol-aware command inspection  
• Rule-based safety validation  
• Anomaly detection  
• Command forwarding to PLC devices  
• Real-time monitoring through a web dashboard  

This allows operators to detect malicious activity before it affects the grid.

---

# System Architecture
SCADA Simulator
↓
GridShield Firewall
↓
Command Validation + Anomaly Detection
↓
PLC Devices (Grid Nodes)

GridShield sits **between the control center and grid equipment**, inspecting every command before it is executed.

---

# Core Features

## Protocol Monitoring

The system simulates communication used in industrial energy infrastructure:

- Modbus
- IEC 61850
- DNP3

These protocols are widely used in **SCADA systems and smart grid automation**.

---

## Command Validation

Commands are validated against safety constraints.

Example rule:

Grid control values must remain within safe operational limits
If the command violates the rule it is **blocked immediately**.

Example:
BLOCKED → iec grid 3 value 780
---

## Anomaly Detection

Some commands may not directly violate rules but still appear suspicious.

These commands are flagged as anomalies.

Example:

ANOMALY → dnp3 grid 2 value 850
This helps detect **False Data Injection (FDI) attacks** or unusual behavior in the grid.

---

## Real-Time Dashboard

GridShield includes a simple monitoring dashboard that shows:

• firewall status  
• monitored protocols  
• executed commands  
• blocked attacks  
• anomaly alerts  

The dashboard helps operators quickly understand what is happening in the grid network.

---

# Example Output
EXECUTED → modbus grid 1 value 220
BLOCKED → iec grid 3 value 780
ANOMALY → dnp3 grid 2 value 850
Color coding helps distinguish events:

• Green → valid command executed  
• Red → malicious command blocked  
• Yellow → anomaly detected  

---

# Technology Stack

## Backend

Python  
Used for firewall logic and command processing.

Flask  
Used to create the web dashboard.

Socket Programming  
Handles communication between SCADA, firewall, and PLC devices.

---

## Infrastructure

Docker  
Each component runs inside its own container.

Docker Compose  
Orchestrates the complete system architecture.

---

## Industrial Communication Concepts

The project simulates industrial communication protocols used in energy systems:

• Modbus  
• IEC 61850  
• DNP3  

These protocols are commonly used in **power plants, substations, and SCADA networks**.

---

# Project Structure

docker-compose.yml

gridshield/
firewall.py
Dockerfile

scada/
scada_generator.py
Dockerfile

plc/
plc_server.py
Dockerfile
