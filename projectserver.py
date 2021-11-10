from flask import Flask
from pymongo import MongoClient

# Database
my_client = MongoClient("mongodb://localhost:27017/")
my_database = my_client["WebAppDatabase"]
# this collection contains user accounts, and profile pictures names.
user_accounts = my_database["UserAccounts"]

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello 312"


if __name__ == '__main__':
    app.run(debug=True)
