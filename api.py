from app.utils.db import *
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from app.routes.details import *

if __name__ == "__main__":
    app.run(port=3000, debug=True)


# pip install flask
# pip install flask_sqlalchemy
# pip install flask_json_schema
# pip install pytz
