################################################################################
#
# radioapp
#
################################################################################

RADIOAPP_VERSION = 0.1

# Invokes setuptools so that radioapp gets rebuilt
define RADIOAPP_BUILD_SRC
	cd $(BR2_EXTERNAL_WiFiLMR_PATH)/../../radioapp && python3 setup.py sdist
endef

# Hack to create the download directory since there is no real download
define RADIOAPP_MAKE_DL_DIR
	mkdir -pv $(BR2_DL_DIR)/radioapp/
endef

# Remove the .stamp_extracted to force buildroot to use the current version of radioapp
define RADIOAPP_REMOVE_EXTRACT_STAMP
	rm -vf $(BASE_DIR)/build/radioapp-$(RADIOAPP_VERSION)/.stamp_extracted
endef

RADIOAPP_PRE_EXTRACT_HOOKS += RADIOAPP_BUILD_SRC
RADIOAPP_SITE = file://$(BR2_DL_DIR)/../../../radioapp/dist
RADIOAPP_SOURCE = radioapp-$(RADIOAPP_VERSION).tar.gz
RADIOAPP_SETUP_TYPE = setuptools

$(eval $(python-package))