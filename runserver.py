from flask import Flask, request
from flask_restful import Resource, Api

from date_utils import DateUtils
from timezone_utils import TimeZoneUtils
from coordination_utils import CoordinationUtils

app = Flask(__name__, template_folder="templates")
api = Api(app)

# class used for the REST API
class GlareDetection(Resource):

    # get method
    def get(self):

        # get input data as json and read required fields
        some_json = request.get_json()
        lat = some_json['lat']
        long = some_json['long']
        epoch = some_json['epoch']
        orientation = some_json['orientation']

        # create objects
        tz_utils = TimeZoneUtils()
        date_utils = DateUtils(tz_utils)
        coord_utils = CoordinationUtils(date_utils, lat, long, epoch, orientation)

        # compute glare and return results
        return ({'glare': coord_utils.detect_glare()})

api.add_resource(GlareDetection, '/')

if __name__ == '__main__':
    app.run(debug=True)
