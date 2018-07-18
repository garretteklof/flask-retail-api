from config.config import _APP_SECRET_

from flask import Flask
from flask_restful import Api

from item import Item, ItemList

app = Flask(__name__)
app.config.update(
    SECRET_KEY=_APP_SECRET_
)
api = Api(app)

api.add_resource(Item, '/items/<int:_id>')
api.add_resource(ItemList, '/items')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
