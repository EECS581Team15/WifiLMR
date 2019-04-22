################################################################################
#
# python3-pymumble
#
################################################################################

PYTHON3_PYMUMBLE_VERSION = v1.1

PYTHON3_PYMUMBLE_SITE = https://github.com/azlux/pymumble/archive
PYTHON3_PYMUMBLE_SETUP_TYPE = distutils
PYTHON3_PYMUMBLE_SOURCE = $(PYTHON3_PYMUMBLE_VERSION).tar.gz
PYTHON3_PYMUMBLE_DEPENDENCIES = python3-opuslib python-protobuf python3

$(eval $(python-package))