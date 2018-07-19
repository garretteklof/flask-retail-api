# flask-retail-api
A contrived 'virtual mall' REST API built with Flask.

## Getting Started

This API was created in Python 3.7. For a local copy, clone the repo and from the command line: 

`pip install -r requirements.txt && python api.py`

(However, you must add your own config.json file in the config folder, or override both \_APP_SECRET\_ and \_JWT_SECRET_KEY\_).

### Features

This is a fully-functional 'virtual mall' REST API with the ability to login / logout shoppers (users), as well as create, update, delete items, and create and delete stores (with jwt authentication).

The database is SQLite and will be created (data.db) with first request.

There is no UI, just endpoints. I recommend trying it out with an ADE, such as [Postman](https://www.getpostman.com/).

### Endpoints

#### Users

`POST /signup` create a user _(email & password required)_

`POST /login` login user with credentials

`POST /logout` logout user

`GET /users/<id>` get a user

`DELETE /users/<id>` delete a user

`POST /refresh` refresh jwt access_token _(expiration handler)_

#### Items _(authentication required)_

`GET /items` get all items _(limited access for those not logged in)_

`POST /items` create an item _(name, price, store_id required)_

`GET /items/<id>` get specific item

`DELETE /items/<id>` delete specific item

`PATCH /items/<id>` update specific item _(price only)_

#### Stores _(authentication required)_

`GET /stores` get all stores and corresponding items

`POST /stores` create a store _(name required)_

`GET /stores/<id>` get specific store

`DELETE /stores/<id>` delete specific store
