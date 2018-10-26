"""
radioapp.core.calling
=====================

The Calling submodule receives and transmits audio from the backend. To control
the scope of this project, the sending and receiving of audio is delegated to an
external piece of software known as “Mumble”. Mumble is a voice chat solution
with a client-server architecture. As such, the Calling submodule is primarily
concerned with the setup and control of a Mumble client.
"""