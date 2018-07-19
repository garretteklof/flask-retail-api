from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from models.store import StoreModel

_store_parser = reqparse.RequestParser()
_store_parser.add_argument('name',
                           type=str,
                           required=True,
                           help="This field cannot be left blank!"
                           )


class Store(Resource):
    @jwt_required
    def get(self, _id):
        store = StoreModel.find_by_id(_id)
        if store:
            return store.json()
        return {'message': 'Store not found'}, 404

    @jwt_required
    def delete(self, _id):
        store = StoreModel.find_by_id(_id)
        if store:
            store.delete_from_db()

        return {'message': 'Store deleted'}


class StoreList(Resource):

    def get(self):
        return {'stores':  [x.json() for x in StoreModel.find_all()]}

    @jwt_required
    def post(self):
        data = _store_parser.parse_args()
        store_name = data['name'].lower()
        if StoreModel.find_by_name(store_name):
            return {f'message': "A store with name '{name}' already exists."}, 400
        store = StoreModel(store_name)
        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred creating the store."}, 500

        return store.json(), 201
