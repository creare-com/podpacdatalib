"""
Podpac Datalib Module

Public API
See https://podpac.org/developer/contributing.html#public-api
for more information about import conventions

Attributes
----------
version_info : OrderedDict
    Dict with keys MAJOR, MINOR, HOTFIX depicting version
"""
import sys
# version handling
from podpacdatalib import version

__version__ = version.version()
version_info = version.VERSION_INFO

from podpacdatalib.cosmos_stations import COSMOSStations
from podpacdatalib.drought_monitor import DroughtCategory, DroughtMonitorCategory
from podpacdatalib.egi import EGI
from podpacdatalib.gfs import GFS, GFSLatest
from podpacdatalib.modis_pds import MODIS
from podpacdatalib.satutils import Landsat8, Sentinel2
from podpacdatalib.smap_egi import SMAP
from podpacdatalib.terraintiles import TerrainTiles
from podpacdatalib.weathercitizen import WeatherCitizen
from podpacdatalib.soilscape import SoilSCAPE20min
from podpacdatalib import soilgrids

# intake requires python >= 3.6
__all__ = [
    "COSMOSStations",
    "DroughtCategory", "DroughtMonitorCategory",
    "EGI",
    "GFS", "GFSLatest",
    "MODIS",
    "Landsat8", "Sentinel2",
    "SMAP",
    "TerrainTiles",
    "WeatherCitizen",
    "SoilSCAPE20min",
    "soilgrids",
]
if sys.version >= "3.6":
    from podpacdatalib.intake_catalog import IntakeCatalog
    __all__.append("IntakeCatalog")
