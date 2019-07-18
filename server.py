#!/usr/bin/env python

import configparser
from flask import Flask, request
from flask_restful import Resource, Api
from subprocess import Popen

config = configparser.ConfigParser()
config.read('config.ini')

app = Flask(__name__)
api = Api(app)

class Shutdown(Resource):
    def get(self):
        p = Popen(config['commands']['shutdown'].split())

class Reboot(Resource):
    def get(self):
        p = Popen(config['commands']['reboot'].split())

class Suspend(Resource):
    def get(self):
        p = Popen(config['commands']['suspend'].split())

class Lock(Resource):
    def get(self):
        p = Popen(config['commands']['lock'].split())

api.add_resource(Shutdown, '/shutdown')
api.add_resource(Reboot, '/reboot')
api.add_resource(Suspend, '/suspend')
api.add_resource(Lock, '/lock')

if __name__ == '__main__':
    app.run(port = config['default']['port'])
