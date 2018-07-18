from time import gmtime, strftime
from flask_restful import Resource, reqparse

from models.item import ItemModel

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


class Item(Resource):

    def get(self, _id):
        item = ItemModel.find_by_id(_id)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404

    def patch(self, _id):
        pass

    def delete(self, _id):
        pass


class ItemList(Resource):

    def get(self):
        pass

    def post(self):

        data = _item_parser.parse_args()

        if ItemModel.find_by_name(data['name']):
            return {'message': f"An item with name '{data['name']}' already exists."}, 400

        data['created_at'] = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        item = ItemModel(**data)

        try:
            item.save_to_db()
        except:
            return {"message": "An internal error occurred inserting the item."}, 500

        return item.json(), 201
