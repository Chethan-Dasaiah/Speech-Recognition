import os

from flask import Flask, request, Response ,jsonify, render_template
from flask_cors import CORS, cross_origin

import speechToText
from imp_file.utils import decodeSound

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

'''@app.route("/", methods=['GET'])
@cross_origin()
def home():
    return render_template('index2.html')'''


@app.route("/convertRecord", methods=['POST'])
@cross_origin()
def predictRoute_convertRecord():
    file_name = request.json['file_name']
    result = speechToText.recorded_audio_speech2Text(file_name)
    file = open("output_result/result.txt","w+")
    file.writelines(result)
    file.close()
    return Response("Converted text : " + result)


@app.route("/convertlive", methods=['GET'])
@cross_origin()
def predictRoute_convertlive():
    result = speechToText.live_audio_speech2Text()
    # Write results to a txt file
    file = open("output_result/result.txt","w+")
    file.writelines(result)
    # file.writelines(L)
    file.close()
    return Response("Converted text : " + result)
    #return jsonify({"Result" : str(result)})


#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=port)
    app.run(host='0.0.0.0', port=5000, debug=True)
    #predictRoute_convertlive()