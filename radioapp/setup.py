import setuptools
import os

setuptools.setup(
    name="radioapp",
    author="EECS 581 Team 15",
    version="0.1",
    install_requires=open("requirements.txt").read(),
    dependency_links=[
        "git+https://github.com/azlux/pymumble.git",
    ],
    url="https://github.com/EECS581Team15/WifiLMR/",
    packages=setuptools.find_packages(),
    package_data={
        "": [
            "*.wav",
        ],
    },
    data_files=[
        ("{}/target/etc/init.d/"
         .format(os.environ["BASE_DIR"]),
            ["radioapp/misc/S91radioapp.sh"])
    ]
)
