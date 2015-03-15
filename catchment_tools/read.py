from numpy import ma
from osgeo import gdal
from shapely.geometry import shape

def lat_long_to_idx(gt, lon, lat):
    """
        Take a geotransform and calculate the array indexes for the given lat,long.

        :param gt: GDAL geotransform (e.g. gdal.Open(x).GetGeoTransform()).
        :type gt: GDAL Geotransform tuple.
        :param lon: Longitude.
        :type lon: float
        :param lat: Latitude.
        :type lat: float
    """
    return (int((lat - gt[3]) / gt[5]),
            int((lon - gt[0]) / gt[1]))

def get_masked_image(ascii):
    """
        Get numpy masked array of raster grid.

        :param ascii: Path to input raster file.
        :type ascii: string

        :returns: tuple(numpy.ma, tuple(geotransform))
    """
    grid = gdal.Open(ascii, gdal.GA_ReadOnly)
    gt = grid.GetGeoTransform()

    band = grid.GetRasterBand(1)
    nodata = band.GetNoDataValue()
    image = band.ReadAsArray(0, 0, band.XSize, band.YSize)
    masked_image = ma.masked_values(image, nodata, copy=False)
    masked_image.fill_value = nodata

    return masked_image, gt

def get_values_for_catchments(ascii, catchments):
    """
        Read the values for all points inside each of the supplied catchments.


        :param ascii: Path to input raster file.
        :type ascii: string
        :param catchments: Dictionary of catchments and their grid points.
        :type catchments: dict
    """
    mi, gt = get_masked_image(ascii)

    results = {}
    for catchment, points in catchments.iteritems():
        # TODO: Properly handle small/null catchments.
        if len(points) <= 2:
            continue
        catchment_values = []
        for point in points:
            x, y = lat_long_to_idx(gt, point[0], point[1])
            catchment_values.append(mi[x][y])

        results[catchment] = catchment_values

    return results
