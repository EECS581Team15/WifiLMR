import setuptools
import os

setuptools.setup(
    name="radioapp",
    author="EECS 581 Team 15",
    version="0.1",
    url="https://github.com/EECS581Team15/WifiLMR/",
    packages=setuptools.find_packages(),
    data_files=[
        ("{}/target/etc/init.d/S90radioapp.sh"
         .format(os.environ["BASE_DIR"]),
            ["radioapp/misc/init_script.sh"])
    ]
)
