################################################################################
#
# python3-opuslib
#
################################################################################

PYTHON3_OPUSLIB_VERSION = 2.0.0

PYTHON3_OPUSLIB_SITE = https://pypi.python.org/packages/source/o/opuslib
PYTHON3_OPUSLIB_SETUP_TYPE = setuptools
PYTHON3_OPUSLIB_SOURCE = opuslib-$(PYTHON3_OPUSLIB_VERSION).tar.gz
PYTHON3_OPUSLIB_DEPENDENCIES = opus
PYTHON3_OPUSLIB_DEPENDENCIES = python3

$(eval $(python-package))