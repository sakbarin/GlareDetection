from timezonefinder import TimezoneFinder

# this class is created to get time zone where the picture was taken
class TimeZoneUtils():
    def __init__(self):
        self.tz_finder = TimezoneFinder()

    # get the time zone using lat and long
    def get_time_zone(self, lat, long):
        try:
            return self.tz_finder.timezone_at(lat=lat, lng=long)
        except Exception as e:
            raise e
