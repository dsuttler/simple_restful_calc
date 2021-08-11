from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

"""
This code is purposefully verbose and redundant.
As my first Flask application and my first time playing 
around with building a restful API.
"""


def check_posted_data(posted_data, operation):
    if operation == "add" or operation == "subtract" or operation == "multiply":
        if "x" not in posted_data or "y" not in posted_data:
            return 301  # missing param
        else:
            return 200
    elif operation == "divide":
        if 'x' not in posted_data or 'y' not in posted_data:
            return 301  # missing param
        elif posted_data['y'] == 0:
            return 302  # divide by 0
        else:
            return 200


class Add(Resource):
    def post(self):
        # resource add was requested using POST

        # Step 1: Get posted data
        posted_data = request.get_json()

        # verify the validity of the inputs
        status_code = check_posted_data(posted_data, "add")

        if status_code != 200:
            ret_json = {
                "Message": "An error occurred",
                "Status Code": status_code
            }
            return jsonify(ret_json)

        # If we get 200 then add correctly
        x = int(posted_data["x"])
        y = int(posted_data["y"])
        ret = x + y
        ret_map = {
            "Message": ret,
            "Status Code": status_code
        }

        return jsonify(ret_map)


class Subtract(Resource):
    def post(self):
        # resource subtract was requested using POST

        # Step 1: Get posted data
        posted_data = request.get_json()

        # verify the validity
        status_code = check_posted_data(posted_data, "subtract")

        if status_code != 200:
            ret_json = {
                "Message": "An error occurred",
                "Status Code": status_code
            }
            return jsonify(ret_json)

        # If we get 200 then subtract correctly
        x = int(posted_data["x"])
        y = int(posted_data["y"])
        ret = x - y
        ret_map = {
            "Message": ret,
            "Status Code": status_code
        }

        return jsonify(ret_map)


class Multiply(Resource):
    def post(self):
        # resource multiply was requested using POST

        # Step 1: Get posted data
        posted_data = request.get_json()

        # Verify the validity
        status_code = check_posted_data(posted_data, "multiply")

        if status_code != 200:
            ret_json = {
                "Message": "An error occurred",
                "Status Code": status_code
            }
            return jsonify(ret_json)

        # If we get 200 then multiply correctly
        x = int(posted_data["x"])
        y = int(posted_data["y"])
        ret = x * y
        ret_map = {
            "Message": ret,
            "Status Code": status_code
        }

        return jsonify(ret_map)


class Divide(Resource):
    def post(self):
        # resource divide was requested using POST

        # Step 1: Get posted data
        posted_data = request.get_json()

        # Verify the validity
        status_code = check_posted_data(posted_data, "divide")

        if status_code != 200:
            ret_json = {
                "Message": "An error occurred",
                "Status Code": status_code
            }
            return jsonify(ret_json)

        # If we get 200 then divide correctly
        x = int(posted_data["x"])
        y = int(posted_data["y"])
        ret = (x * 1.0) / y  # make sure we return a float
        ret_map = {
            "Message": ret,
            "Status Code": status_code
        }

        return jsonify(ret_map)


# Add the resources to the app
api.add_resource(Add, "/add")
api.add_resource(Subtract, "/subtract")
api.add_resource(Multiply, "/multiply")
api.add_resource(Divide, "/divide")


# Base
@app.route('/')
def hello_world():
    return "Hello World"


# main
if __name__ == "__main__":
    app.run(debug=True)

"""
Resource Method Chart - Simple Calculator App 
Objective: Build a Restful API that supports + - * /
Methods: GET POST(Create) PUT(update) DELETE
Resources(What you're offering): + - * /

Resource | Method | Path      | Used For   | Param | status code
-------------------------------------------------------------------------
    +    |  POST  | /add      | addition   | x + y | 200 ok
                                              int  | 301 Missing Argument
-------------------------------------------------------------------------
    -    |  POST  | /subtract |subtraction | x - y | 200 ok
                                              int  | 301 Missing Argument
-------------------------------------------------------------------------
    /    | POST   | /divide   | division   | x / y | 200 ok
                                           |  int  | 301 Missing Argument
                                                   | 302 Y is 0 - Invalid
-------------------------------------------------------------------------
    *    |  POST  | /multiply |multiply    | x * y | 200 ok
                                              int  | 301 Missing Argument

"""
