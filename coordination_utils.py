import astropy.coordinates as coord
import astropy.units as u
from astropy.time import Time
from astropy.utils import iers

AZIMUTHAL_DIFF_BOUNDARY = 30
SUN_ALTITUDE_BOUNDARY = 45

class CoordinationUtils():

    def __init__(self, date_utils, lat, long, epoch, orientation):
        iers.Conf.iers_auto_url.set('ftp://cddis.gsfc.nasa.gov/pub/products/iers/finals2000A.all')

        self.data_utils = date_utils

        self.pic_location = coord.EarthLocation(lat=lat * u.deg, lon=long * u.deg)
        self.pic_datetime = Time(date_utils.get_utc_datetime(epoch))

        self.azimuth = 0
        self.altitude = 0
        self.orientation = orientation

        self.sun = coord.get_sun(self.pic_datetime)

    def __compute_azimuth_and_altitude(self):
        alt_and_az = coord.AltAz(location=self.pic_location, obstime=self.pic_datetime)
        self.altitude = self.sun.transform_to(alt_and_az).alt.degree
        self.azimuth = self.sun.transform_to(alt_and_az).az.degree

    def detect_glare(self):
        self.__compute_azimuth_and_altitude()

        temp_orientation = (self.orientation + 360) % 360

        phi = abs(self.azimuth - temp_orientation) % 360
        if (phi > 180):
            azimuth_distance = 360 - phi
        else:
            azimuth_distance = phi

        if (azimuth_distance <= AZIMUTHAL_DIFF_BOUNDARY and self.altitude <= SUN_ALTITUDE_BOUNDARY):
            return True

        return False

    '''
    def print_glare_data(self):
        print('              azimuth:', azimuth)
        print('          orientation:', orientation)
        print('             altitude:', altitude)
        print('azimuth - orientation:', azimuth_distance)
        print('             altitude:', altitude)

    def print_picture_data(self):
        print('Picture location:', self.pic_location)
        print('    Picture time:', self.pic_datetime)
        print('             Sun:', self.sun)
    '''
