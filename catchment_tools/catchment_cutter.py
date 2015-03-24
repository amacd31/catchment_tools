import fiona
import numpy as np
from osgeo import gdal
from shapely.geometry import shape
from shapely.wkt import loads as load_wkt

def get_grid_cells(boundary_file, grid_file, area_percent_match = 0.3):
    """
        Return the grid cells from a grid file that fall within the boundary of the boundary file.

        :param boundary_file: The path to file defining the boundary of the catchment. i.e. a geojson file.
        :type boundary_file: string
        :param grid_file: Path to ASCII grid file to find coordinates within the boundary.
        :type grid_file: string
        :param area_match_percent: Ratio of how much of the grid cell needs to be overlapped by the boundary for inclusion. Defaults to 0.3 (30%).
        :type area_match_percent: float

        :returns: Array of lat/longs.
    """

    grid = gdal.Open(grid_file, gdal.GA_ReadOnly)

    lon_min, lon_step, lon_s, lat_min, lat_s, lat_step = grid.GetGeoTransform()

    lon_half_step = lon_step / 2.0
    lat_half_step = lat_step / 2.0

    lon_min = lon_min + lon_half_step
    lat_min = lat_min + lat_half_step
    ncols = grid.RasterXSize
    nrows = grid.RasterYSize

    lons = np.array([lon_min + lon_step * i for i in range(ncols)])
    lats = np.array([lat_min + lat_step * i for i in range(nrows)])

    grid_cells = []

    with fiona.open(boundary_file, 'r') as boundary:
        catchment_geom = shape(boundary[0]['geometry'])

        lon_min = catchment_geom.bounds[0] - lon_step
        lon_max = catchment_geom.bounds[2] + lon_step
        lat_min = catchment_geom.bounds[1] + lat_step
        lat_max = catchment_geom.bounds[3] - lat_step

        lons = lons[lons>=lon_min]
        lons = lons[lons<=lon_max]
        lats = lats[lats>=lat_min]
        lats = lats[lats<=lat_max]

        for lon in lons:
            for lat in lats:
                pt = load_wkt('POLYGON((%f %f, %f %f, %f %f, %f %f, %f %f))' % (
                        lon - lon_half_step, lat - lat_half_step,
                        lon - lon_half_step, lat + lat_half_step,
                        lon + lon_half_step, lat + lat_half_step,
                        lon + lon_half_step, lat - lat_half_step,
                        lon - lon_half_step, lat - lat_half_step,
                    )
                )

                intersection = catchment_geom.intersection(pt)

                # Include cell if more than area_percent_match is inside the catchment geometry
                if intersection.area > area_percent_match * pt.area:
                    grid_cells.append((lon, lat))

    return grid_cells

