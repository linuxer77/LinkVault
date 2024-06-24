from main import app, db
import sqlalchemy.orm as so
import sqlalchemy as sa
from main.models import User, Category, Link

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Category': Category, 'Link': Link}
