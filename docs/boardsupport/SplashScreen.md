Boot Splash Screen
==================

Introduction
------------

The screen drivers and splash screen are loaded in an init script called
`S02Screen`. This is in the `rootfs_overlay` directory.

Adding a New Splash Screen
--------------------------

The splash screen is read from /boot/splash.bmp. This is part of
`rootfs_overlay`. The image should be 160x128 pixels. This **must** be an older
format BMP (BMP3 or earlier) or `fbv` won't be able to read it.