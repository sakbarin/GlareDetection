from flask import Flask, request
from flask_restful import Resource, Api

from date_utils import DateUtils
from timezone_utils import TimeZoneUtils
from coordination_utils import CoordinationUtils

app = Flask(__name__, template_folder="templates")
api = Api(app)

def to_float(input, var_name):
    try:
        return float(input)
    except:
        raise TypeError(str.format("TypeError: %s with value %s can't be converted to float." % (var_name, input)))


# class used for the REST API
class GlareDetection(Resource):

    # method
    def post(self):
        try:
            # get input data as json and read required fields
            some_json = request.get_json()

            lat = to_float(some_json['lat'], 'lat')
            long = to_float(some_json['long'], 'long')
            epoch = to_float(some_json['epoch'], 'epoch')
            orientation = to_float(some_json['orientation'], 'orientation')

            if (lat < 0 or lat > 90):
                raise ValueError("ValueError: lat out of range = [0 to 90]")
            elif (long < -180 or long > 180):
                raise ValueError("ValueError: long out of range = [-180 to 180")
            elif (orientation < -180 or orientation > 180):
                raise ValueError("ValueError: orientation out of range = [-180 to 180]")
            elif (epoch < 0):
                raise ValueError("ValueError: epoch out of range = [epoch > 0]")
            else:
                # create objects
                tz_utils = TimeZoneUtils()
                date_utils = DateUtils(tz_utils)
                coord_utils = CoordinationUtils(date_utils, lat, long, epoch, orientation)

                # compute glare and return results
                return ({'glare': coord_utils.detect_glare()})
        except Exception as e:
            print(e)
            return ({'Error': str(e)})

api.add_resource(GlareDetection, '/detect_glare')

if __name__ == '__main__':
    app.run(debug=True)
