Feature Listing
===============

Software - Radio Application
----------------------------

**Required**

* VOIP
    * Logical groupings of connected clients
        * Channels (base grouping)
        * Zones (groups of channels)
    * Bandwidth efficient, low-latency codec for voice transfer (CELT, Opus, etc.)
    * PTT-triggered transmit
* [User Interface](../basics/UIParadigm.md)
    * Main status screen
        * Status icons
            * WiFi signal strength
            * RX/TX status
            * Battery life
        * Text display lines
            * Channel name
            * Easy to read font
    * Menu system
        * Usability
            * Easily navigated by a D-pad
            * Easy to read - high contrast
            * Intuitive - requires minimal instruction for non-technical users
        * Items
            * Extended WiFi status
            * Backend connection status
            * Extended battery information
            * Zone Select
            * Channel Select
            * Power Off
            * Factory Reset
* [Provisioning mode](../features/ProvisioningMode.md)


**Optional**



Software - Management Console/Backend
-----------------------------

* Inventory Control
    * List of all units
    * Unit status
        * Uptime
        * Battery status
        * Connection status
* Subscriber unit configuration
    * All parameters except for initial WiFi setup
    * Templates to start from
    * Push configuration updates to units
* Call Routing
    * Audio distribution within channels

Hardware
--------

* Screen
    * Resolution: 160x128
    * Type: Color TFT LCD
* Logic board
    * Raspberry Pi Zero W
    * Processor: ARM 1176JZF-S @ 1 GHz
    * RAM: 512 MB DDR2
    * Wifi: BCM43143
    * Storage: MMC card
* Audio
    * Speaker: 90 dB output
    * I2S DAC
    * I2S digital microphone
* Input Devices
    * 4-way + select digital joystick
    * Combined power and volume knob (non-continuous)
    * Rotary channel knob (continuous)
    * PTT button on left side