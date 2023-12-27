"""
podpac module
"""

import sys
import subprocess

# Always prefer setuptools over distutils
from setuptools import find_packages, setup
from setuptools.command.develop import develop

# get version
sys.path.insert(0, "podpacdatalib")
import version

__version__ = version.version()

install_requires = [
    "podpac[datatype,aws,stac,intake]",
]

extras_require = {
    "dev": [],
}

# set long description to readme
with open("README.MD") as f:
    long_description = f.read()

all_reqs = []
for key, val in extras_require.items():
    if "key" == "dev":
        continue
    all_reqs += val
extras_require["all"] = all_reqs
extras_require["devall"] = all_reqs + extras_require["dev"]

# install pre-commit hooks after setup in develop mode
class PostDevelopCommand(develop):
    def run(self):
        try:
            subprocess.check_call(["pre-commit", "install"])
        except subprocess.CalledProcessError as e:
            print("Failed to install pre-commit hook")

        develop.run(self)

setup(
    # ext_modules=None,
    name="podpacdatalib",
    version=__version__,
    description="Pipeline for Observational Data Processing, Analysis, and Collaboration: Encapsulation of public data sets.",
    author="Creare",
    url="https://podpac.org",
    license="APACHE 2.0",
    classifiers=[
        # How mature is this project? Common values are
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: GIS",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: Apache Software License",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python",
    ],
    packages=find_packages(),
    install_requires=install_requires,
    extras_require=extras_require,
    cmdclass={"develop": PostDevelopCommand},
    long_description=long_description,
    long_description_content_type="text/markdown"
    # entry_points = {
    #     'console_scripts' : []
    # }
)
