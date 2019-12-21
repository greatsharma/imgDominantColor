import cv2
from utils import getColorPalette
from flask import Flask, request, jsonify
from exceptions import URLException, CV2Exception

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():

    response = {
        'status': {
            'code': None,
            'msg': ""
        }
    }

    if 'src' not in request.args:
        response['status']['code'] = 404
        response['status']['msg'] = "Specify source image"
    else:
        src = request.args['src']
        try:
            dominant_color, palette = getColorPalette(src)
            response['status']['code'] = 200
            response['status']['msg'] = "OK"
            response['dominantColor'] = str('hsv' + str(dominant_color))
            response['palette'] = [str('hsv' + str(ele)) for ele in palette]
        except URLException:
            response['status']['code'] = 404
            response['status']['msg'] = "Image not found"
        except CV2Exception:
            response['status']['code'] = 500
            response['status']['msg'] = "Internal server error"

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
