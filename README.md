# WifiLMR
A land mobile radio-like product for unlicensed campus-wide use.

Getting Started
---------------

1. Install VS Code
2. Install .NET Core SDK
3. Clone repository and install the extensions that VS Code recommends for this repository


### Radio Firmware

1. Sync git submodules (`git submodule init && git submodule update`)
2. Enter the `boardsupport/buildroot directory`
3. Execute `make BR2_EXTERNAL=../bsp wifilmr_defconfig`
4. Execute `make`
5. Go get coffee.
6. Write `boardsupport/buildroot/output/images/sdcard.img` to a MicroSD card.

Building
--------

VS Code is configured to build the application automatically by pressing Ctrl-Shift-B or F5 (for debuggging).