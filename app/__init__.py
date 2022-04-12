
# Import flask and template operators
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os

# Define the WSGI application object

app = Flask(__name__)
# Configurations
app.config.from_json('./config/local/config.json')
print(app.config.values())

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
api = Api(app)

from .controller.supplier import Supplier
from .controller.spending import Spending
from .controller.spending_type import SpendingType

api.add_resource(Supplier, '/supplier')
api.add_resource(Spending, '/spending')
api.add_resource(SpendingType, '/spending-type')



