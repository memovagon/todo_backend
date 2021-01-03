from flask import Flask, jsonify, make_response, request
from flask_cors import CORS
import json

todo_list = ["Limpiar casa de mascotas", "Trabajar ocho horas", "Comer en horarios correctos"]

def get_app():
    app = Flask(__name__)
    CORS(app)
    print("Hello World")

    @app.route("/api/todo", methods=['GET'])
    def todo_get():
        print('info: get request')
        response = make_response({'status': 'success', 'todos': todo_list}, 200)
        response.headers.add('Content-Type', 'application/json')

        return response

    @app.route("/api/todo", methods=['DELETE'])
    def todo_delete():
        args = request.args
        note = args['note']
        print("info: delete requested")
        todo_list.remove(note)

        response = make_response({'status': 'success'}, 200)
        response.headers.add('Content-Type', 'application/json')
        return response

    @app.route("/api/todo", methods=['POST'])
    def todo_add():
        args = request.args
        note = args['note']
        print("info: add request")
        todo_list.append(note)

        response = make_response({'status': 'success'}, 200)
        response.headers.add('Content-Type', 'application/json')
        return response


    

    return app

if __name__ == '__main__':
    app = get_app()
    app.run('0.0.0.0')