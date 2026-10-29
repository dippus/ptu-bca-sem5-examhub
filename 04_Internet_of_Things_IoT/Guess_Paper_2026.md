# 📝 Guess Paper 2026 — Internet of Things (UGCA-1933)
### IKGPTU | BCA Semester 5 | M.Code 90316 | PTU-Style

> **Total Marks: 60 | Time: 3 Hours**
> Section A: Attempt ALL 10 questions (2 marks each = 20 marks)
> Section B: Attempt ANY 4 out of 6 questions (10 marks each = 40 marks)

---

## 📌 SECTION A — Short Answer Questions (10 × 2 = 20 Marks)

---

**Q1. Define IoT. List any four key characteristics of IoT.**

**Answer:**
- **IoT (Internet of Things):** A network of physical objects (things) embedded with sensors, software, and connectivity to collect and exchange data over the internet without human intervention.
- **Key Characteristics:**
  1. **Connectivity** — Things are connected to the internet/network
  2. **Intelligence** — Devices can process data and take decisions
  3. **Sensing** — Collect real-world data via sensors
  4. **Dynamic Nature** — Devices change state (on/off, location)
  5. **Scalability** — Supports billions of connected devices
  6. **Heterogeneity** — Different hardware/software platforms

---

**Q2. What is a Wireless Sensor Network (WSN)? Give its role in IoT.**

**Answer:**
- **WSN:** A network of spatially distributed autonomous sensors that monitor physical/environmental conditions and cooperatively pass data through the network to a main location.
- **Role in IoT:**
  - Provides the sensing layer — collects temperature, humidity, motion, etc.
  - Enables remote monitoring without human presence
  - Forms the "perception layer" of IoT architecture
  - Used in smart agriculture, healthcare, smart cities
- **Components:** Sensor nodes, gateway, base station, user interface

---

**Q3. What are communication protocols in IoT? Name the main ones.**

**Answer:**
- **Communication Protocols:** Rules governing how IoT devices send and receive data.
- **Main IoT Protocols:**
  | Protocol | Full Form | Layer | Use Case |
  |----------|-----------|-------|----------|
  | MQTT | Message Queuing Telemetry Transport | Application | Low-bandwidth M2M |
  | CoAP | Constrained Application Protocol | Application | Resource-constrained devices |
  | HTTP/HTTPS | HyperText Transfer Protocol | Application | Web-based IoT |
  | Zigbee | — | Network | Smart home sensors |
  | Z-Wave | — | Network | Home automation |
  | BLE | Bluetooth Low Energy | Physical | Wearables |
- MQTT uses publish-subscribe model; CoAP uses request-response model

---

**Q4. What is SDN (Software Defined Networking) in IoT?**

**Answer:**
- **SDN:** An approach that separates the network's control plane (decision-making) from the data plane (packet forwarding), making the network programmable via software.
- **SDN in IoT:**
  - Centralized controller manages all IoT network devices
  - Enables dynamic traffic management for millions of devices
  - Reduces complexity of heterogeneous IoT networks
  - Improves security, scalability, and flexibility
  - **Controller** programs switches via OpenFlow protocol
- Benefit: Network behavior can be changed via software without touching hardware

---

**Q5. What is Big Data Analytics in IoT?**

**Answer:**
- **Big Data in IoT:** IoT devices generate massive volumes of data (velocity, variety, volume) that traditional databases cannot handle — this is Big Data.
- **Analytics in IoT:**
  - **Descriptive:** What happened? (sensor logs)
  - **Predictive:** What will happen? (machine failure prediction)
  - **Prescriptive:** What should be done? (automated action)
- **Tools used:** Hadoop, Spark, Kafka, NoSQL databases
- **Why needed:** Extract meaningful patterns from billions of sensor readings to enable smart decisions

---

**Q6. What are network operator requirements in IoT?**

**Answer:**
Network operators need the following to manage IoT deployments:
1. **Device Management** — Register, configure, monitor millions of devices remotely
2. **Scalability** — Handle billions of device connections simultaneously
3. **QoS (Quality of Service)** — Prioritize critical IoT traffic (healthcare, safety)
4. **Security** — Authentication, encryption, access control for all devices
5. **Interoperability** — Support heterogeneous devices and protocols
6. **Remote Monitoring** — Real-time status, fault detection, performance metrics
7. **Low Latency** — Time-sensitive IoT applications (industrial control)
8. **Billing/Accounting** — Track usage per device/application

---

**Q7. What is YANG in IoT? What is its purpose?**

**Answer:**
- **YANG (Yet Another Next Generation):** A data modeling language used to model configuration and state data of network devices/IoT systems.
- **Purpose:**
  - Defines the structure of data exchanged via NETCONF
  - Specifies what parameters a network device supports
  - Enables validation of configuration data before applying
  - Makes configuration self-documenting and machine-readable
- **YANG models define:** Data types, hierarchical structure, constraints, relationships
- Used with **NETCONF protocol** to configure IoT devices uniformly

---

**Q8. What is I2C interface in Raspberry Pi?**

**Answer:**
- **I2C (Inter-Integrated Circuit):** A two-wire serial communication protocol for connecting multiple slave devices to a master.
- **In Raspberry Pi:**
  - Uses only 2 wires: **SDA** (Serial Data) + **SCL** (Serial Clock)
  - Supports multiple slaves on same bus (each has unique address)
  - Speed: 100 kbps (standard) / 400 kbps (fast mode)
  - GPIO Pins: SDA → Pin 3, SCL → Pin 5
- **Use Cases:** Temperature sensors (BME280), OLED displays, RTC modules, accelerometers
- **Advantage:** Fewer wires; **Disadvantage:** Slower than SPI

---

**Q9. What is a Web Server in IoT / Web of Things (WoT)?**

**Answer:**
- **Web Server in IoT:** An IoT device running a lightweight web server (HTTP/HTTPS) that exposes its data and control as web resources accessible via browser or API.
- **Web of Things (WoT):**
  - W3C standard to make IoT devices accessible via standard web protocols
  - Each IoT thing has a **Thing Description (TD)** — a JSON-LD document describing its properties, actions, and events
  - Enables interoperability across different IoT platforms
- **Example:** A Raspberry Pi running a Flask web server that displays sensor data on a webpage and accepts commands via REST API

---

**Q10. Why is Cloud Computing needed for IoT?**

**Answer:**
Cloud is essential for IoT because:
1. **Storage:** IoT generates TB/PB of data — cloud provides unlimited scalable storage
2. **Processing Power:** Edge devices are resource-constrained; cloud provides compute
3. **Accessibility:** Data accessible from anywhere via internet
4. **Analytics:** Cloud platforms (AWS IoT, Google Cloud IoT) offer built-in analytics
5. **Cost:** Pay-per-use model — no upfront hardware investment
6. **Scalability:** Automatically scales as number of IoT devices grows
7. **Integration:** Connects IoT with other services (AI/ML, databases, notifications)
8. **Reliability:** Cloud SLAs ensure high availability for critical IoT applications

---

## 📌 SECTION B — Long Answer Questions (Attempt any 4 × 10 = 40 Marks)

---

### Q1. Explain the Need for IoT and Discuss its Enabling Technologies in Detail. (10 Marks)

**NEED FOR IoT:**
1. **Remote Monitoring** — Monitor assets, health, environment without physical presence
2. **Automation** — Automate repetitive tasks (smart homes, factories)
3. **Efficiency** — Reduce energy, water, resource waste via smart control
4. **Data-Driven Decisions** — Real-time data enables better decisions
5. **Safety & Security** — Smart surveillance, fire detection, emergency response
6. **New Business Models** — Predictive maintenance, product-as-a-service
7. **Quality of Life** — Healthcare monitoring, assisted living for elderly

---

**IoT ENABLING TECHNOLOGIES:**

**1. Wireless Sensor Networks (WSN)**
- Network of tiny sensor nodes collecting environmental data
- Each node: sensor + microcontroller + transceiver + battery
- Applications: precision agriculture, structural health monitoring
- Protocols: Zigbee, IEEE 802.15.4

**2. RFID (Radio Frequency Identification)**
- Identifies objects using radio waves
- Components: RFID tag (passive/active) + RFID reader
- Passive RFID: No battery, powered by reader signal (range: ~1m)
- Active RFID: Has battery (range: ~100m)
- Applications: Supply chain, asset tracking, retail inventory, access control

**3. Cloud Computing**
- Provides storage, computation, and services on-demand over the internet
- Models: IaaS, PaaS, SaaS
- Enables IoT data storage, processing, and remote access at scale
- Examples: AWS IoT, Azure IoT Hub, Google Cloud IoT Core

**4. Big Data Analytics**
- Processes massive IoT data streams to extract insights
- 5 V's: Volume, Velocity, Variety, Veracity, Value
- Tools: Hadoop (batch), Spark (real-time), Kafka (streaming)
- Enables: Predictive maintenance, anomaly detection, pattern recognition

**5. Communication Protocols**
- **MQTT:** Lightweight publish-subscribe; ideal for low-bandwidth devices
- **CoAP:** RESTful protocol for constrained devices; UDP-based
- **Zigbee:** Low-power mesh network for short-range sensor networks
- **6LoWPAN:** IPv6 over Low-Power Wireless Personal Area Networks

**6. Embedded Systems / Microcontrollers**
- Raspberry Pi, Arduino — provide processing power at the edge
- Execute local logic, interface with sensors/actuators

**7. Middleware**
- Software layer bridging IoT devices and applications
- Handles device management, data aggregation, protocol translation

---

### Q2. Describe Domain-Specific IoT Applications with Examples. (10 Marks)

IoT has revolutionized multiple domains. Major domain applications:

---

**1. Smart Home**
- **What:** Automating home appliances, security, and energy via IoT
- **Components:** Smart thermostat, smart locks, smart lights, security cameras
- **Examples:**
  - Google Nest Thermostat — learns user preferences, auto-adjusts temperature
  - Smart door locks — unlock via smartphone
  - Amazon Echo — voice-controlled home automation
- **Benefits:** Energy savings, security, convenience

---

**2. Smart Agriculture**
- **What:** Using IoT sensors to optimize crop production
- **Components:** Soil moisture sensors, weather stations, drones, irrigation controllers
- **Examples:**
  - Soil moisture monitoring → automatic irrigation when dry
  - Drone-based crop health monitoring using NDVI cameras
  - Livestock tracking using GPS tags
- **Benefits:** 30–50% water savings, higher crop yield, reduced manual labor

---

**3. Smart Health / Healthcare IoT**
- **What:** Remote patient monitoring, wearables, hospital asset tracking
- **Components:** Wearable sensors, ECG monitors, glucose meters, smart beds
- **Examples:**
  - Fitbit/Apple Watch — heart rate, SpO2, sleep monitoring
  - Remote ICU — doctors monitor patients from anywhere
  - Smart pill dispensers — remind patients, track compliance
- **Benefits:** Early disease detection, reduced hospital visits, better outcomes

---

**4. Smart Cities**
- **What:** Using IoT to manage urban infrastructure efficiently
- **Components:** Smart streetlights, traffic sensors, waste sensors, air quality monitors
- **Examples:**
  - Smart traffic lights — adjust timing based on real-time traffic
  - Smart parking — guide drivers to empty spots via app
  - Smart waste bins — alert when full for optimized collection
  - Air quality monitoring — trigger alerts for pollution spikes
- **Benefits:** Reduced congestion, energy savings, better governance

---

**5. Smart Energy / Smart Grid**
- **What:** Intelligent electricity generation, distribution, and consumption
- **Components:** Smart meters, solar inverters, demand response systems
- **Examples:**
  - Smart meters — real-time electricity usage; no manual meter reading
  - Dynamic pricing — charge less during off-peak hours automatically
  - Solar + storage management — optimize home solar panel usage
- **Benefits:** Reduced energy waste, outage detection, renewable integration

---

**6. Smart Industry (Industrial IoT — IIoT)**
- **What:** IoT in manufacturing, logistics, supply chain
- **Examples:**
  - Predictive maintenance — vibration sensors detect machine failure before it happens
  - Inventory tracking — RFID in warehouses
  - Quality control — vision sensors detect defects on production line
- **Benefits:** Reduced downtime, cost savings, better quality

---

### Q3. Explain M2M (Machine to Machine) Communication — Applications, Architecture, and Comparison with IoT. (10 Marks)

**M2M DEFINITION:**
- M2M (Machine-to-Machine): Direct communication between devices using wired or wireless networks, without human intervention.
- Predecessor technology to IoT.

---

**M2M ARCHITECTURE:**
```
[Field Device/Machine]
        ↓ (sensors, actuators)
[M2M Device] — local data collection
        ↓ (cellular: 2G/3G/4G, wired)
[M2M Gateway] — protocol translation
        ↓ (internet/WAN)
[M2M Middleware/Server] — data aggregation
        ↓
[Application/User Interface]
```

---

**PURPOSE OF M2M:**
1. Remote monitoring of assets (oil pipelines, electrical grids)
2. Automated meter reading (electricity, water, gas)
3. Fleet management and vehicle tracking
4. Industrial equipment monitoring
5. Vending machine monitoring and restocking alerts
6. Point-of-Sale (PoS) terminal communications

---

**M2M APPLICATIONS:**
| Domain | M2M Application |
|--------|----------------|
| Utilities | Smart meters, remote meter reading |
| Transport | GPS tracking, fleet management |
| Healthcare | Remote patient monitoring |
| Retail | Vending machine management, inventory |
| Industrial | SCADA systems, machine monitoring |
| Agriculture | Irrigation control, environmental monitoring |

---

**M2M vs IoT — Detailed Comparison:**

| Feature | M2M | IoT |
|---------|-----|-----|
| **Communication** | Point-to-point (device to server) | Many-to-many (device, cloud, apps, users) |
| **Connectivity** | Mostly cellular (2G/3G), wired | Wi-Fi, Zigbee, BLE, 6LoWPAN, cellular |
| **Intelligence** | Limited, on server side | Distributed (edge, fog, cloud) |
| **Scalability** | Limited (hundreds of devices) | Massive (billions of devices) |
| **Standards** | Proprietary, vendor-specific | Open standards (MQTT, CoAP, HTTP, REST) |
| **Data Sharing** | Closed/siloed systems | Open data sharing between platforms |
| **Human Interaction** | Minimal | Extensive (apps, dashboards, voice) |
| **Internet Required** | Not necessarily | Core requirement |
| **Ecosystem** | Closed ecosystem | Open, interoperable ecosystem |
| **Example** | Remote electricity meter reading | Smart home energy management system |
| **Architecture** | Simple point-to-point | Complex layered architecture |
| **Application** | Specific, vertical | Broad, cross-domain |

---

**Key Insight:** M2M is a subset of IoT. IoT extends M2M by adding internet connectivity, open standards, big data analytics, and user-facing applications.

---

### Q4. Explain the Need for IoT System Management. Describe SNMP Protocol for IoT Management. (10 Marks)

**NEED FOR IoT SYSTEM MANAGEMENT:**

IoT networks involve millions of heterogeneous devices → management is critical:
1. **Device Lifecycle Management**
   - Register new devices, update firmware, decommission old devices
2. **Fault Management**
   - Detect device failures, network outages; trigger alerts; auto-recovery
3. **Configuration Management**
   - Remotely configure device parameters (thresholds, reporting intervals)
4. **Performance Management**
   - Monitor CPU, memory, battery, bandwidth usage of devices
5. **Security Management**
   - Enforce access control, patch vulnerabilities, manage certificates
6. **Scalability Management**
   - Handle dynamic addition/removal of devices at scale
7. **Interoperability**
   - Manage devices from different vendors using common protocols
8. **Cost Optimization**
   - Identify underperforming devices, optimize resource use

---

**SNMP (Simple Network Management Protocol):**

**Definition:** Standard protocol for monitoring and managing network devices.

**SNMP Components:**
| Component | Role |
|-----------|------|
| **Manager (NMS)** | Central system that monitors/controls devices |
| **Agent** | Software running on managed device; responds to manager |
| **MIB (Management Information Base)** | Database of variables that can be monitored |
| **OID (Object Identifier)** | Unique ID for each managed variable in MIB |

**SNMP Operations:**
1. **GET** — Manager requests value of a variable from agent
2. **GET-NEXT** — Traverse MIB tree
3. **GET-BULK** — Retrieve large amounts of data (SNMPv2)
4. **SET** — Manager changes a variable value on the agent
5. **TRAP** — Agent proactively notifies manager of an event (unsolicited)
6. **INFORM** — Acknowledged version of TRAP

**SNMP Versions:**
- **SNMPv1** — Basic, no security
- **SNMPv2c** — Community strings for authentication
- **SNMPv3** — Encryption + authentication (recommended for IoT)

**SNMP Limitations for IoT:**
- Not designed for resource-constrained devices
- Limited transaction support (no rollback)
- XML/text configuration not supported natively
- Does not handle large-scale IoT device management well

→ **This is why NETCONF + YANG was developed** for modern IoT management.

---

### Q5. Explain NETCONF Protocol and YANG Data Modeling for IoT Device Management. (10 Marks)

**NETCONF (Network Configuration Protocol):**

**Definition:** An IETF standard protocol (RFC 6241) for installing, manipulating, and deleting network device configurations.

**NETCONF Architecture:**
```
[IoT Manager / NMS]
        ↓↑ (SSH / TLS transport)
[NETCONF Client] <——————————> [NETCONF Server (on IoT device)]
        ↓↑ (RPC / XML messages)
   [YANG Data Models]
        ↓
[Device Configuration Datastore]
     (Running | Candidate | Startup)
```

**NETCONF Key Features:**
1. **Transport:** Runs over SSH (secure) or TLS
2. **Encoding:** XML-based messages
3. **Operations (RPCs):**
   | Operation | Description |
   |-----------|-------------|
   | `<get>` | Retrieve running config + state data |
   | `<get-config>` | Retrieve configuration from datastore |
   | `<edit-config>` | Modify device configuration |
   | `<copy-config>` | Copy one datastore to another |
   | `<delete-config>` | Delete a configuration datastore |
   | `<lock>` | Lock datastore to prevent conflicts |
   | `<unlock>` | Release lock |
   | `<commit>` | Apply candidate config to running |
   | `<close-session>` | Terminate NETCONF session |
4. **Datastores:** Running (active), Candidate (being edited), Startup (on reboot)
5. **Transactions:** Supports atomic commit — all or nothing (unlike SNMP)

**Advantages of NETCONF over SNMP:**
| Feature | SNMP | NETCONF |
|---------|------|---------|
| Configuration | Limited | Full CRUD |
| Transaction | No rollback | Atomic commit + rollback |
| Security | Weak (v1/v2) | SSH/TLS (strong) |
| Data format | OID-based | XML + YANG |
| Scalability | Limited | Designed for large-scale |
| Validation | None | YANG-based validation |

---

**YANG (Yet Another Next Generation) Data Modeling:**

**Definition:** A data modeling language (RFC 6020) that defines the structure, syntax, and semantics of configuration data for NETCONF.

**YANG Concepts:**
| Concept | Description |
|---------|-------------|
| `module` | Top-level container for a YANG model |
| `container` | Groups related nodes (like a folder) |
| `leaf` | Single value node (like a variable) |
| `leaf-list` | List of same-type values |
| `list` | Sequence of instances with keys |
| `typedef` | Define custom data types |
| `grouping` | Reusable set of nodes |

**Simple YANG Example:**
```yang
module iot-sensor {
  namespace "http://example.com/iot-sensor";
  prefix sensor;

  container sensors {
    list sensor {
      key "id";
      leaf id { type string; }
      leaf temperature { type decimal64 { fraction-digits 2; } }
      leaf unit { type string; default "Celsius"; }
    }
  }
}
```

**NETCONF-YANG Workflow for IoT:**
1. IoT device loads YANG model describing its configuration capabilities
2. Manager discovers device's YANG models (via `<get-schema>`)
3. Manager sends `<edit-config>` XML message structured per YANG model
4. Device validates XML against YANG model
5. If valid → applies configuration; if error → returns detailed error

**Benefits of NETCONF+YANG for IoT:**
- Standardized device configuration across vendors
- Schema validation prevents misconfiguration
- Automation-friendly (machine-readable models)
- Supports versioning and backward compatibility

---

### Q6. Describe Raspberry Pi Architecture and Explain SPI Interface with Its Applications in IoT. (10 Marks)

**RASPBERRY PI OVERVIEW:**
- A credit-card sized single-board computer developed by Raspberry Pi Foundation (UK)
- Runs Linux OS (Raspbian/Raspberry Pi OS)
- Used as an IoT gateway, edge computing device, and prototyping platform

---

**RASPBERRY PI ARCHITECTURE (Pi 4 Model B):**

```
┌─────────────────────────────────────────────────────┐
│                 Raspberry Pi 4 Model B               │
│                                                      │
│  ┌──────────┐  ┌──────────┐  ┌───────────────────┐  │
│  │ BCM2711  │  │  RAM     │  │ MicroSD Card Slot  │  │
│  │ (ARM     │  │ 2/4/8 GB │  │ (OS Storage)       │  │
│  │ Cortex-  │  │ LPDDR4   │  └───────────────────┘  │
│  │ A72,     │  └──────────┘                          │
│  │ 1.5 GHz) │                                        │
│  └──────────┘                                        │
│                                                      │
│  GPIO (40 pins)  USB 3.0 × 2   USB 2.0 × 2          │
│  HDMI × 2        Ethernet       Wi-Fi / BT           │
│  CSI (Camera)    DSI (Display)  3.5mm Audio          │
└─────────────────────────────────────────────────────┘
```

**Key Specs:**
| Component | Spec |
|-----------|------|
| SoC | Broadcom BCM2711 |
| CPU | Quad-core ARM Cortex-A72 @ 1.5 GHz |
| RAM | 2/4/8 GB LPDDR4 |
| Storage | MicroSD card |
| GPIO | 40 pins (26 usable GPIO) |
| Interfaces | SPI, I2C, UART, USB, HDMI, CSI, DSI |
| Connectivity | Wi-Fi 802.11ac, Bluetooth 5.0, Gigabit Ethernet |
| Power | 5V via USB-C |

---

**GPIO PINS:**
- 40-pin header on Raspberry Pi
- Types: 3.3V, 5V power pins; Ground pins; GPIO (programmable); Special function pins (SPI, I2C, UART)
- GPIO can be INPUT (read sensor) or OUTPUT (control LED/relay)

---

**SPI (Serial Peripheral Interface) IN DETAIL:**

**Definition:** A synchronous, full-duplex serial communication protocol used for short-distance communication between a master and one or more slave devices.

**SPI Pins (4-wire interface):**
| Pin | Name | Direction | Description |
|-----|------|-----------|-------------|
| MOSI | Master Out Slave In | Master→Slave | Data from master to slave |
| MISO | Master In Slave Out | Slave→Master | Data from slave to master |
| SCLK | Serial Clock | Master→Slave | Clock signal from master |
| CE/CS | Chip Enable/Select | Master→Slave | Select which slave is active |

**On Raspberry Pi GPIO:**
- MOSI → GPIO 10 (Pin 19)
- MISO → GPIO 9 (Pin 21)
- SCLK → GPIO 11 (Pin 23)
- CE0 → GPIO 8 (Pin 24) [Slave 1]
- CE1 → GPIO 7 (Pin 26) [Slave 2]

**SPI Working:**
1. Master pulls CE/CS LOW to select a slave
2. Master generates clock on SCLK
3. Data shifted out on MOSI (master→slave) simultaneously with MISO (slave→master)
4. Full-duplex: send and receive simultaneously
5. Master pulls CE HIGH to deselect

**SPI Modes (Clock polarity and phase):**
| Mode | CPOL | CPHA | Clock Idle | Data Capture |
|------|------|------|-----------|--------------|
| 0 | 0 | 0 | LOW | Rising edge |
| 1 | 0 | 1 | LOW | Falling edge |
| 2 | 1 | 0 | HIGH | Falling edge |
| 3 | 1 | 1 | HIGH | Rising edge |

**SPI Speed:** Up to 125 MHz on Raspberry Pi (much faster than I2C)

**IoT Applications of SPI:**
1. **ADC (MCP3008)** — Convert analog sensor signals (LDR, temperature) to digital
2. **SD Card / Flash Memory** — High-speed data logging
3. **Display modules** — TFT LCD screens (ILI9341), OLED displays
4. **RF Modules** — nRF24L01 wireless transceiver for IoT communication
5. **IMU Sensors** — High-speed accelerometer/gyroscope (MPU-9250)
6. **DAC** — Digital-to-analog conversion for audio output

**SPI vs I2C vs UART Comparison:**
| Feature | SPI | I2C | UART |
|---------|-----|-----|------|
| Wires | 4 (MOSI, MISO, SCLK, CS) | 2 (SDA, SCL) | 2 (TX, RX) |
| Speed | Very High (MHz) | Moderate (100k–400kbps) | Moderate (up to 1Mbps) |
| Full Duplex | Yes | No | Yes |
| Multi-slave | Yes (one CS per slave) | Yes (address-based) | No |
| Distance | Short | Short | Longer |
| Complexity | Higher (more wires) | Simple | Simple |
| Use Case | Fast peripherals, ADC, display | Sensors, RTC, EEPROM | GPS, GSM modules |

**Python SPI Code Example (Raspberry Pi):**
```python
import spidev
spi = spidev.SpiDev()
spi.open(0, 0)           # Bus 0, Device 0 (CE0)
spi.max_speed_hz = 1000000  # 1 MHz
response = spi.xfer2([0x01, 0x80, 0x00])  # MCP3008 read
spi.close()
```

---

*End of Guess Paper 2026*
