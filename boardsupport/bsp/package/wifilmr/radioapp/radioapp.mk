################################################################################
#
# radioapp
#
################################################################################

RADIOAPP_VERSION = 0.1

# Invokes setuptools so that radioapp gets rebuilt


# Make the init script executable
define RADIOAPP_MAKE_INIT_SCRIPT_EXEC
	chmod +x $(BASE_DIR)/target/etc/init.d/S91radioapp.sh
endef

RADIOAPP_PRE_DOWNLOAD_HOOKS += RADIOAPP_BUILD_SRC
RADIOAPP_POST_INSTALL_TARGET_HOOKS += RADIOAPP_MAKE_INIT_SCRIPT_EXEC
RADIOAPP_SITE = $(BR2_DL_DIR)/../../../radioapp
RADIOAPP_SITE_METHOD = local
RADIOAPP_SOURCE = radioapp-$(RADIOAPP_VERSION).tar.gz
RADIOAPP_SETUP_TYPE = setuptools
RADIOAPP_DEPENDENCIES = python-alsaaudio python3-pymumble

$(eval $(python-package))