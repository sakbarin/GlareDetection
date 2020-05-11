import datetime
from dateutil import tz

class DateUtils():
    def __init__(self, tz_utils):
        self.tz_utils = tz_utils
        pass

    # get the UTC datetime
    def get_utc_datetime(self, epoch):
        try:
            return datetime.datetime.utcfromtimestamp(epoch)
        except Exception as e:
            raise e

    # convert UCT to local datetime
    def get_local_datetime(self, epoch, lat, long):
        try:
            utc_datetime = self.get_utc_datetime(epoch)

            timezone_from = tz.gettz('UTC')
            timezone_to = tz.gettz(self.tz_utils.get_time_zone(lat, long))

            utc_datetime = utc_datetime.replace(tzinfo=timezone_from)
            local_datetime = utc_datetime.astimezone(timezone_to)

            local_datetime = local_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')
            return datetime.datetime.strptime(local_datetime, '%Y-%m-%d %H:%M:%S.%f')
        except Exception as e:
            raise e
