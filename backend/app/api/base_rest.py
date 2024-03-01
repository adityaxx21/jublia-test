from flask import  jsonify

class BaseRest():
    def get_response_object(self, code, object = ""):
        """
        Generate a json response given a status code and object type
        """
        response_object = {
            200: {
                "status": "OK", 
                "message": "Action successfully completed", 
                "data": object},
            201: {
                "status": "CREATED", 
                "message": "successfully created", 
                "data": object},
            204: {},
            400: {
                "status": "error", 
                "message": "Invalid Argument", 
                "error": object},
            403: {
                "status": "error",
                "error": object,
                "message": "Action on can't be completed"},
            404: {
                "status": "error", 
                "message": "not found"},
            405: {
                "status": "error", 
                "message": "Method not allowed on that resource", 
                "error": object},
            500: {
                "status": "error", 
                "message": "An error occurred", 
                "error": object},
        }
        return response_object[code], code