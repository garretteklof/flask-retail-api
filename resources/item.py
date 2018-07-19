from time import gmtime, strftime
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from models.item import ItemModel


class Item(Resource):

    @jwt_required
    def get(self, _id):
        item = ItemModel.find_by_id(_id)
        if item:
            return item.json()

        return {'message': 'Item not found'}, 404

    @jwt_required
    def patch(self, _id):
        item = ItemModel.find_by_id(_id)
        _item_parser = reqparse.RequestParser()
        _item_parser.add_argument('price',
                                  type=float,
                                  required=True,
                                  help="This field cannot be left blank!"
                                  )
        data = _item_parser.parse_args()

        if not item:
            return {'message': f"Can't patch that which doesn't already exist! Please create a new item."}, 400

        item.price = data['price']
        item.updated_at = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        try:
            item.save_to_db()
        except:
            return {"message": "An internal error occurred updating the item."}, 500

        return item.json(), 200

    @jwt_required
    def delete(self, _id):
        item = ItemModel.find_by_id(_id)
        if item:
            try:
                item.delete_from_db()
            except:
                return {"message": "An internal error occurred deleting the item."}, 500
            return {'message': 'Item deleted!'}
        return {'message': 'Item not found.'}, 404


class ItemList(Resource):

    def get(self):
        items = [item.json() for item in ItemModel.find_all()]
        return {'items': items}, 200

    @jwt_required
    def post(self):
        _item_parser = reqparse.RequestParser()

        _item_parser.add_argument('name',
                                  type=str,
                                  required=True,
                                  help="This field cannot be left blank!"
                                  )
        _item_parser.add_argument('price',
                                  type=float,
                                  required=True,
                                  help="This field cannot be left blank!"
                                  )
        data = _item_parser.parse_args()

        if ItemModel.find_by_name(data['name']):
            return {'message': f"An item with name '{data['name']}' already exists."}, 400

        data['created_at'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        item = ItemModel(**data)

        try:
            item.save_to_db()
        except:
            return {"message": "An internal error occurred creating the item."}, 500
        return item.json(), 201
