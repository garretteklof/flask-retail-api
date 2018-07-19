from config.config import _APP_SECRET_, _JWT_SECRET_KEY_

from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.user import User, UserSignUp, UserLogin, UserLogout, TokenRefresh
from resources.store import Store, StoreList
from resources.item import Item, ItemList
from blacklist import BLACKLIST

app = Flask(__name__)
app.config.update(
    SECRET_KEY=_APP_SECRET_,
    SQLALCHEMY_DATABASE_URI='sqlite:///data.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    JWT_SECRET_KEY=_JWT_SECRET_KEY_,
    PROPAGATE_EXCEPTIONS=True,
    JWT_BLACKLIST_ENABLED=True,
    JWT_BLACKLIST_TOKEN_CHECKS=['access', 'refresh']
)
api = Api(app)
jwt = JWTManager(app)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST


api.add_resource(UserSignUp, '/signup')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(TokenRefresh, '/refresh')
api.add_resource(User, '/users/<int:_id>')
api.add_resource(StoreList, '/stores')
api.add_resource(Store, '/stores/<int:_id>')
api.add_resource(ItemList, '/items')
api.add_resource(Item, '/items/<int:_id>')


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
