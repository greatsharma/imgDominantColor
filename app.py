import cv2
from utils import getColorPalette
from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    if 'src' not in request.args:
        return jsonify({'code': 404, 'error': "no source image found"})

    src = request.args['src']
    dominant_color, palette = getColorPalette(src)

    response = {
        'dominantColor': str('hsv' + str(dominant_color)),
        'palette': [str('hsv' + str(ele)) for ele in palette]
    }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
