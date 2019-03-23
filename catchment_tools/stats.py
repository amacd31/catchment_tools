import pandas as pd

def get_catchment_average(ds, grid, measurand):
    """
        Get catchment average.

        :param ds: XArray dataset containing the gridded data to extract average from.
        :type ds: xarray.Dataset
        :param grid: Catchment grid cells to extract from the data set and average together.
        :type grid: numpy.ndarray or pandas.DataFrame containing rows of lon, lat.
        :param measurand: Name of xarray variable to extract.
        :type measaurand: str

        :return: xarray of floats
    """
    rain_tot = 0
    for row in grid:
        lon, lat = row
        rain_tot += ds.sel(
            lat=lat,
            lon=lon,
            method='nearest'
        )[measurand].values

    catchment_avg = rain_tot / len(grid)

    return pd.Series(catchment_avg, ds.time)
