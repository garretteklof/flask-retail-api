from flask_restful import Resource


class Item(Resource):

    def get(self, _id):
        return {'id': _id}, 200

    def put(self, _id):
        pass

    def delete(self, _id):
        pass


class ItemList(Resource):

    def get(self):
        pass

    def post(self):
        pass
