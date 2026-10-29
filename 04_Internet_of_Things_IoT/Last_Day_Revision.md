# ⚡ Last Day Revision — Internet of Things (UGCA-1933)
### BCA Sem 5 | IKGPTU | Ultra-Compact — Bullets Only

---

## 📖 TOP 15 DEFINITIONS (3–4 lines each)

**1. IoT (Internet of Things)**
- Network of physical objects with sensors, software, and internet connectivity
- Devices collect and exchange data without human-to-human or human-to-computer interaction
- Examples: smart thermostat, fitness tracker, smart meter
- Key layers: Perception → Network → Application

**2. WSN (Wireless Sensor Network)**
- Network of distributed autonomous sensor nodes monitoring physical conditions
- Nodes have: sensor + microcontroller + wireless transceiver + power source
- Data relayed hop-by-hop to a gateway/base station
- Used in: agriculture, structural monitoring, military surveillance

**3. RFID (Radio Frequency Identification)**
- Identifies objects using radio waves; tag stores data, reader retrieves it
- Passive RFID: no battery (powered by reader field) — range ~1m
- Active RFID: has battery — range up to ~100m
- Used in: supply chain, retail, access control, animal tracking

**4. SDN (Software Defined Networking)**
- Separates network control plane (brain) from data plane (forwarding)
- Network behavior controlled centrally via software, not hardware configuration
- In IoT: manages traffic for millions of devices dynamically from one controller
- Protocol: OpenFlow between controller and switches

**5. NFV (Network Functions Virtualization)**
- Virtualizes network functions (firewall, load balancer, NAT) on standard servers
- Replaces dedicated hardware appliances with software running on VMs
- In IoT: enables flexible, scalable network services for IoT platforms
- Works alongside SDN; SDN = control, NFV = functionality

**6. NETCONF (Network Configuration Protocol)**
- IETF protocol (RFC 6241) for remote configuration of network devices
- Uses SSH/TLS transport + XML encoding + YANG data models
- Supports atomic transactions (commit/rollback) — unlike SNMP
- Operations: get, get-config, edit-config, commit, lock, unlock, close-session

**7. YANG (Yet Another Next Generation)**
- Data modeling language (RFC 6020) for NETCONF configuration data
- Defines structure, types, and constraints of device configuration
- Key constructs: module, container, leaf, leaf-list, list, typedef, grouping
- Works like a schema — validates configuration before it is applied

**8. Raspberry Pi**
- Single-board computer (credit-card size) by Raspberry Pi Foundation
- Runs Linux (Raspberry Pi OS); has 40-pin GPIO header
- Interfaces: SPI, I2C, UART, USB, HDMI, Wi-Fi, Bluetooth, Ethernet
- Used as: IoT gateway, edge device, prototyping platform

**9. M2M (Machine to Machine)**
- Direct communication between devices without human involvement
- Uses cellular (2G/3G/4G) or wired connections; point-to-point architecture
- Predecessor to IoT — closed, proprietary, vertical systems
- Examples: vending machine stock alerts, remote electricity meter reading

**10. Cloud Computing**
- Delivery of computing services (storage, servers, networking, software) over internet
- Models: IaaS (infrastructure), PaaS (platform), SaaS (software)
- Deployment: Public, Private, Hybrid, Community cloud
- For IoT: provides scalable storage, processing, analytics for device data

**11. Big Data**
- Extremely large datasets that cannot be handled by traditional databases
- 5 V's: Volume (huge), Velocity (fast), Variety (formats), Veracity (accuracy), Value (insight)
- IoT generates Big Data from millions of sensors continuously
- Tools: Hadoop, Apache Spark, Kafka, Cassandra, MongoDB

**12. SPI (Serial Peripheral Interface)**
- 4-wire synchronous full-duplex serial protocol: MOSI, MISO, SCLK, CS/CE
- Master-slave model; multiple slaves via separate CS lines
- Speed: up to MHz range — fastest common IoT interface
- Used for: ADC chips, displays, SD cards, RF modules

**13. I2C (Inter-Integrated Circuit)**
- 2-wire serial protocol: SDA (data) + SCL (clock)
- Supports multiple slaves on same bus via unique 7-bit addresses
- Speed: 100 kbps (standard), 400 kbps (fast), 1 Mbps (fast-plus)
- Used for: temperature sensors, OLED displays, RTC, EEPROM

**14. MQTT (Message Queuing Telemetry Transport)**
- Lightweight publish-subscribe messaging protocol for IoT
- Built on TCP/IP; uses a broker (e.g., Mosquitto) to route messages
- Devices publish to topics; subscribers receive messages on subscribed topics
- Ideal for low-bandwidth, high-latency, unreliable networks (sensors, wearables)

**15. CoAP (Constrained Application Protocol)**
- RESTful protocol designed for resource-constrained IoT devices
- Based on UDP (not TCP) — lightweight, low overhead
- Supports: GET, POST, PUT, DELETE (like HTTP but binary-encoded)
- Used for: battery-powered devices, smart energy, building automation

---

## 🔥 MUST-KNOW TABLE 1: M2M vs IoT (Comes Every Year)

| Feature | M2M | IoT |
|---------|-----|-----|
| **Full Form** | Machine to Machine | Internet of Things |
| **Communication** | Point-to-point (device↔server) | Many-to-many (device↔cloud↔apps↔users) |
| **Connectivity** | Cellular (2G/3G), wired | Wi-Fi, Zigbee, BLE, 6LoWPAN, NB-IoT |
| **Intelligence** | Centralized on server | Distributed (edge + fog + cloud) |
| **Scalability** | Limited (hundreds) | Massive (billions of devices) |
| **Standards** | Proprietary, vendor-specific | Open standards (MQTT, CoAP, HTTP) |
| **Internet** | Not always required | Core requirement |
| **Data Sharing** | Closed, siloed | Open, cross-platform |
| **Human Interaction** | Minimal (machine-only) | High (apps, dashboards, voice) |
| **Ecosystem** | Closed ecosystem | Open, interoperable |
| **Architecture** | Simple, vertical | Complex, layered, horizontal |
| **Applications** | Single-domain (meters, fleet) | Cross-domain (home, health, city) |
| **Protocol** | Proprietary | MQTT, CoAP, HTTP, REST |
| **Example** | Remote meter reading | Smart home energy management |
| **Relationship** | Subset of IoT | Superset, extends M2M |

---

## 🔥 MUST-KNOW TABLE 2: NETCONF vs SNMP

| Feature | SNMP | NETCONF |
|---------|------|---------|
| **Full Form** | Simple Network Management Protocol | Network Configuration Protocol |
| **RFC** | RFC 1157 | RFC 6241 |
| **Transport** | UDP | SSH / TLS (secure) |
| **Data Format** | OID-based, ASN.1 | XML + YANG models |
| **Operations** | GET, SET, TRAP, INFORM | get, edit-config, commit, lock, copy-config |
| **Configuration** | Limited (mostly monitoring) | Full CRUD configuration |
| **Transactions** | No rollback support | Atomic commit + rollback |
| **Security** | Weak (v1/v2: community string) | Strong (SSH encryption + authentication) |
| **Validation** | None | YANG schema validation |
| **Datastores** | Single (running only) | Running, Candidate, Startup |
| **Scalability** | Limited | Designed for large-scale |
| **Error Handling** | Basic | Detailed XML error responses |
| **Suitability for IoT** | Legacy, limited | Modern, preferred for IoT mgmt |
| **Monitoring** | Strong (designed for it) | Possible but not primary focus |

---

## 📋 TOP 3 LONG ANSWER FRAMEWORKS

### Framework 1: IoT Enabling Technologies (10-mark answer structure)

**Para 1 — Introduction (2 lines):** IoT relies on convergence of multiple technologies. Key enabling technologies are:

**Main Body (8 technologies, 2–3 bullets each):**

1. **WSN**
   - Distributed sensor nodes collect physical data
   - Self-organizing, low-power mesh networks
   - Protocol: IEEE 802.15.4, Zigbee

2. **RFID**
   - Tags + readers for automatic object identification
   - Passive (no battery) vs Active (battery-powered)
   - Used in: supply chain, retail, access control

3. **Cloud Computing**
   - IaaS / PaaS / SaaS for IoT backend
   - Provides scalable storage + analytics
   - Examples: AWS IoT, Google Cloud IoT, Azure IoT Hub

4. **Big Data Analytics**
   - Handles IoT's massive data volume
   - Batch (Hadoop) + Real-time (Spark, Kafka)
   - Enables: prediction, anomaly detection, optimization

5. **Communication Protocols**
   - MQTT: publish-subscribe, TCP, low-bandwidth
   - CoAP: REST, UDP, resource-constrained
   - Zigbee/BLE: short-range device networks

6. **Embedded Systems (Raspberry Pi, Arduino)**
   - Edge processing — run logic locally
   - Interface with sensors/actuators via GPIO

7. **Middleware**
   - Bridges devices and applications
   - Handles: device management, protocol translation, data routing

8. **IPv6 / 6LoWPAN**
   - IPv6 provides enough addresses for billions of IoT devices
   - 6LoWPAN: IPv6 over low-power wireless networks

**Conclusion (1 line):** Together these technologies form the foundation of modern IoT ecosystems.

---

### Framework 2: Domain Applications of IoT (10-mark answer structure)

**Para 1 — Introduction:** IoT has transformed multiple real-world domains. Key application areas:

**6 Domains (draw a table or write as sections):**

| Domain | Devices/Sensors Used | Key Applications | Benefit |
|--------|---------------------|-----------------|---------|
| **Smart Home** | Smart thermostat, smart locks, cameras | Automation, security, energy control | Comfort + energy saving |
| **Smart Agriculture** | Soil sensors, drones, weather stations | Precision irrigation, crop monitoring | Higher yield, water saving |
| **Smart Health** | Wearables, ECG, smart beds | Remote monitoring, wearables, asset tracking | Early detection, fewer visits |
| **Smart Cities** | Traffic sensors, smart lights, waste sensors | Traffic mgmt, parking, waste, air quality | Efficiency + sustainability |
| **Smart Energy** | Smart meters, solar inverters | Dynamic pricing, outage detection, grid mgmt | Energy saving |
| **Industrial IoT** | Vibration sensors, RFID, vision cameras | Predictive maintenance, inventory, QC | Reduced downtime |

**Add 2–3 lines elaborating on 2 domains in detail.**

**Conclusion:** IoT enables data-driven management across all critical infrastructure sectors.

---

### Framework 3: NETCONF-YANG Architecture for IoT Management (10-mark answer)

**Para 1 — Why IoT needs management:** Millions of heterogeneous devices → need unified remote configuration + monitoring.

**NETCONF overview (5 bullets):**
- Protocol: RFC 6241; transport: SSH/TLS
- XML-based RPCs: get-config, edit-config, commit, lock
- Three datastores: Running (live), Candidate (being edited), Startup (on boot)
- Atomic transactions: commit succeeds entirely or rolls back
- Secure and validated — overcomes SNMP limitations

**YANG overview (5 bullets):**
- Data modeling language: RFC 6020
- Defines structure/types/constraints for NETCONF config data
- Key constructs: module, container, leaf, list
- Acts as schema — device validates incoming XML against YANG
- Tools: pyang (YANG compiler), yangcli (CLI for NETCONF)

**Draw/describe architecture diagram:**
```
[Manager/NMS] ←—SSH/TLS—→ [NETCONF Server on IoT Device]
     ↕ XML RPCs                      ↕
[YANG Models]             [YANG Model + Config Datastore]
```

**Workflow steps (numbered):**
1. IoT device advertises supported YANG models (capabilities)
2. Manager fetches YANG schemas using `<get-schema>`
3. Manager builds XML config document per YANG model
4. Manager sends `<edit-config>` to candidate datastore
5. YANG validation occurs on device
6. Manager sends `<commit>` → candidate becomes running config
7. On error → `<discard-changes>` for rollback

**Conclusion:** NETCONF+YANG enables standardized, secure, transactional IoT device management at scale.

---

## 🔌 RASPBERRY PI INTERFACES — QUICK REFERENCE

### SPI vs I2C vs UART

| Property | SPI | I2C | UART |
|----------|-----|-----|------|
| **Wires** | 4 (MOSI, MISO, SCLK, CS) | 2 (SDA, SCL) | 2 (TX, RX) |
| **RPi Pins (GPIO)** | MOSI=10, MISO=9, SCLK=11, CE0=8 | SDA=2(Pin3), SCL=3(Pin5) | TX=14(Pin8), RX=15(Pin10) |
| **Speed** | Up to 125 MHz | 100k–1 Mbps | Up to 1 Mbps |
| **Duplex** | Full-duplex | Half-duplex | Full-duplex |
| **Multi-device** | Yes (one CS per slave) | Yes (7-bit address) | No (point-to-point) |
| **Type** | Synchronous | Synchronous | Asynchronous |
| **Wiring complexity** | High (4+ wires) | Low (2 wires) | Low (2 wires) |
| **Typical devices** | ADC, SD card, Display, RF | Sensors, OLED, RTC, EEPROM | GPS, GSM, Bluetooth modules |
| **Example IC** | MCP3008 ADC, nRF24L01 | BME280, DS3231 | HC-05 Bluetooth, NEO-6M GPS |
| **Enable in RPi** | `raspi-config` → SPI | `raspi-config` → I2C | `raspi-config` → Serial |

---

## 🎯 LAST-MINUTE CHEAT BULLETS

**IoT Levels 1–6 (quick memory):**
- Level 1: Single node — senses + analyzes + stores locally (e.g., simple sensor)
- Level 2: Single node — sends data to cloud for storage
- Level 3: Single node — cloud stores + analyzes
- Level 4: Multiple nodes + local controller → cloud
- Level 5: Multiple nodes + coordinator → cloud
- Level 6: Multiple nodes + coordinator + cloud + web portal (full IoT system)

**IoT Design Methodology Steps:**
1. Purpose & requirements spec
2. Process specification
3. Domain model spec
4. Information model spec
5. Service spec
6. IoT level spec
7. Functional view spec
8. Operational view spec
9. Device & component integration
10. Application development

**IoT Security Threats by Layer:**
- **Perception layer:** Node capture, eavesdropping, physical tampering, side-channel attacks
- **Network layer:** DoS/DDoS, MITM, routing attacks, traffic analysis
- **Application layer:** Phishing, malware, unauthorized access, data breach, SQL injection

**Cloud Storage Models for IoT:**
- **Public Cloud:** AWS, Google, Azure — shared resources, pay-per-use
- **Private Cloud:** Organization-owned, more control/security
- **Hybrid Cloud:** Mix of public + private
- **Community Cloud:** Shared by organizations with common interests (govt, hospitals)

**MQTT Key Terms:**
- **Broker:** Central server routing messages (e.g., Mosquitto)
- **Publisher:** Device sending data to a topic
- **Subscriber:** Device/app receiving data from a topic
- **Topic:** Hierarchical string like `home/bedroom/temperature`
- **QoS levels:** 0 (at most once), 1 (at least once), 2 (exactly once)

**CoAP vs MQTT quick diff:**
- CoAP: UDP, RESTful, request-response, 1:1
- MQTT: TCP, pub-sub, broker-based, 1:many

**Raspberry Pi Python GPIO quick code:**
```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # Pin 18 as output
GPIO.output(18, GPIO.HIGH)  # Turn ON
GPIO.output(18, GPIO.LOW)   # Turn OFF
GPIO.cleanup()
```

**NFV vs SDN (one liner each):**
- SDN: Separates CONTROL from FORWARDING (software-defined network behavior)
- NFV: Runs network FUNCTIONS as software on commodity hardware (no dedicated boxes)

---

*Focus: NETCONF+YANG, M2M vs IoT table, Raspberry Pi SPI/I2C, Enabling Technologies, Domain Applications — these 5 topics = ~70% of your exam*
