Adding Software Dependencies
============================

radioapp
--------

### Python Dependencies

Python dependencies should be added to the requirements.txt file in the radioapp folder. The package version should be specified to prevent surprises in the future. For now, Buildroot doesn't know how to process this file, so the dependencies have be synchronized with the utils/scanpypi script in Buildroot. Specify "-o bsp/packages" to place the generated package definitions in the external Buildroot tree. Don't forget to select the package in the Buildroot configuration and synchronize that configuration with wifilmr_defconfig.

### Other Dependencies

Other dependencies, like wpa_supplicant, must be specified using Buildroot. Don't forget to synchronize the new configuration with wifilmr_defconfig.

radiomanager
------------

This project should only have Python dependencies for the most part. These are specified in the requirements.txt file in the radiomanager directory. Any system dependencies, such as Avahi, should be specified in the INSTALLING.md file in radiomanager.
