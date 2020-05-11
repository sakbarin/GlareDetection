# Glare Detection

## Instructions

### Create a conda environment:
conda create --name GlareDetection <br>
conda activate GlareDetection

### Install libraries:
- pip (pip install --upgrade pip)
- timezonefinder (pip install timezonefinder)
- astropy (pip install astropy)
- flask (conda install flask)
- flask_restful (pip install flask_restful)
- python-dateutil (pip install python-dateutil)

### Start the server
Run the following command to start the server:<br>
python runserver.py <br>
The server will start on the address http://127.0.0.1:5000 [if port 5000 is not occupied]<br><br>

### Call REST API
Open a terminal in Linux and type the following command:<br>

curl -H "Content-Type: application/json" -X POST -d '{"lat": 49.2699648, "long": -123.1290368, "epoch": 1588704959.321, "orientation": -10.2}' http://127.0.0.1:5000/detect_glare
