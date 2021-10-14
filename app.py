import os
import uuid

from flask import Flask, send_from_directory
from utils import generate_random_objs_file, check_folder_exists
from flask import request, jsonify

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'media')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/generate_file')
def generate_file():
    try:
        check_folder_exists(UPLOAD_FOLDER)
        file_name = "file{}.txt".format(str(uuid.uuid4()).split('-')[0])
        file = os.path.join(UPLOAD_FOLDER, file_name)
        count = generate_random_objs_file(file)

        context = {
            'status': 200,
            'data': {
                'file_name': file_name,
                'alphabetical_count': count,
                'integer_count': count,
                'alphabetical_string': count,
                'real_number': count

            }
        }
        return jsonify(context)
    except Exception as e:
        error = {
            'error': e.args[0]
        }
    return jsonify(error)


@app.route('/download_file/')
def download_file():
    try:
        file_name = request.args.get('file_name', '')
        return send_from_directory(app.config['UPLOAD_FOLDER'], file_name)
    except Exception as e:
        error = {
            'error': e.args[0]
        }
    return jsonify(error)


if __name__ == '__main__':
    app.run()
