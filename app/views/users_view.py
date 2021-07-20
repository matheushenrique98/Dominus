from http import HTTPStatus
from flask import Blueprint, Response, jsonify, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models.users_model import UsersModel
from app.settings.database import db
from app.services.users_service import UsersService



class Users(Resource):
    @jwt_required()
    def post(self):
        current_user_id = get_jwt_identity()
        request_data = request.get_json()
        response = UsersService(current_user_id).post(request_data)
        return response


    def get(self, user_id=None):
        current_user_id = get_jwt_identity()
        users_service = UsersService(current_user_id)
        if user_id is None:
            return users_service.get_all()
        return users_service.get_one(user_id)
          

    def delete(self, user_id: int):
        current_user_id = get_jwt_identity()
        return UsersService(current_user_id).delete(user_id)

       

    def patch(self, user_id: int):
        current_user_id = get_jwt_identity()
        return UsersService(current_user_id).patch(user_id)





