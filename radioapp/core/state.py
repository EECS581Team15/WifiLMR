"""
radioapp.core.state
===================

The State submodule provides stateful, persistent stores of three types of
information: configuration, user preferences, and persistent UI state.
Configuration is defined in this context as values that can only be set at
provisioning time or by configuring the radio via the Management Console. User
preferences are values such as backlight level that are set via a local menu.
Persistent UI state includes values that are set by the end user or by some
radio action that are not preferences but must survive reboots. The backing
store for this data will provide forward compatibility in the case of schema
changes.
"""