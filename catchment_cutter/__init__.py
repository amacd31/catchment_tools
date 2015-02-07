from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .catchment_cutter import get_grid_cells
