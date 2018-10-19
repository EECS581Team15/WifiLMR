Provisioning Mode
=================

Introduction
------------
Most LMRs use a PC application to configure subscriber units. To avoid having to build a separate application and having to design a working USB interface, we should implement a WiFi hotspot + web panel mode. This will be similar to the provisioning mode found in WiFi-enabled printers. This allows the "bootstrapping" of new units into a state in which the normal configuration procedures can be used.

Workflow
--------

*Note: This assumes the unit is in an unprovisioned state upon boot.*

1. Start Provisioning Mode
    1. Generate a semi-random unit name
    2. Start a WiFi network with the unit name
    3. Start the Provisioning Web UI
2. User connects to UI
    1. Present instructions on the screen on how to connect to the UI
    2. User connects to the Provisioning Web UI
3. User selects WiFi network
    1. User selects a network on the Web UI and provides security credentials
    2. Unit stops the Web UI and attempts to connect to given network
    3. If connection succeeds, continue, otherwise restart the Web UI and provisioning hot spot
4. Backend discovery and detection
    1. Unit discovers backends and presents them as a list on the display
    2. User selects a discovered backend from the list

Requirements
------------

* WiFi hotspot
    * WPA2 security (WPS or display password on screen)
    * DHCP for automatic addressing (needs to be started only for provisioning mode)
    * DNS entry for "provision"
* Instruction screen understandable by non-technical users
* Provisioning Web UI
    * Same visual theme as backend interface
    * Displays list of available networks
        * Network name
        * Signal strength
        * Security
    * Button to trigger rescan
    * Temporary unit name displayed
* Backend discovery
    * mDNS + DNS-SD (a.k.a. Bonjour)
    * List names of available backends
    * Ability to cancel and go back to WiFi connection stage