from applications import create_app
from flask_migrate import Migrate
from applications.extensions import db
from applications.common.utils.init_databases import init_db

app = create_app()

migrate = Migrate(app, db)


@app.cli.command()
def init():
    init_db()


if __name__ == '__main__':
    app.run()
