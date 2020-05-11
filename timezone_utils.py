from timezonefinder import TimezoneFinder

class TimeZoneUtils():
    def __init__(self):
        self.tz_finder = TimezoneFinder()

    # get the time zone using lat and long
    def get_time_zone(self, lat, long):
        return self.tz_finder.timezone_at(lat=lat, lng=long)
