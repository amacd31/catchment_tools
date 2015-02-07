Catchment cutter
===============

Simple library for calculating catchment grid cells that fall within a catchment boundary.

Dependencies
------------

Requires Python 2.6 or greater (mostly tested with Python 3.3 on Linux), numpy, gdal, shapely, and fiona.

Usage
-----

.. code:: python

    from catchment_cutter import get_grid_cells

    grid_file = 'grid_file.asc' # ASCII grid file of cells
    boundary = 'catchment_boundary.json' # GeoJSON catchment boundary
    # Get the grid cells (lat/long) from grid_file that fall within the catchment boundary
    cells = np.asarray(get_grid_cells(boundary, grid_file))

