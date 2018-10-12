Software Architecture
=====================

Client (Subscriber Unit)
------------------------

**Main Components:**

* Hardware Abstraction Layer
    The Hardware Abstraction Layer, or HAL, provides a decoupling layer between the behavior and exposed interface of the hardware and device drivers and the rest of the application. While HALs are normally important for purposes of providing future-proofing against new platforms and requirements, this HAL will be used to ease the debugging situation. By abstracting over the actual hardware, much of the development effort can be carried out on normal GNU/Linux desktops or virtual machines.

    The basic structure will be define a set of interfaces that describe an abstract version of the hardware (from the software's point of view). The interfaces will describe high-level subsystems like the status LED, button events, and volume control. There will be two implementations of the interfaces: the dummy implementation for initial development and the actual hardware layer (implemented later).
* Client Core
    This component will encapsulate the actual logic of the application. There will be at least the following submodules:
    * Configuration
        The configuration submodule holds the configuration written to the unit at provision time or from over-the-air configuration.
    * Backend Interface
        This component encapsulate discovery and communication with the backend. The implementation will likely be similar to the HAL with a mock and real version.
    * Calling
        The Calling submodule handles sending and receiving audio when enabled (which depends on PTT and mute settings).
* User Interface
    The UI should be a rather thin layer that sends and receives events to the Client Core. The business logic is abstracted to ease adding new features and make the code more testable.

Backend (Call Routing and Management Console)
---------------------------------------------