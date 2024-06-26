from main import login
from werkzeug.security import generate_password_hash, check_password_hash
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from main import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    categories: so.WriteOnlyMapped['Category'] = so.relationship(back_populates='user')

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Category(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    category_name: so.Mapped[str] = so.mapped_column(sa.String(20))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)
    user: so.Mapped[User] = so.relationship(back_populates='categories')
    links: so.WriteOnlyMapped['Link'] = so.relationship(back_populates='category')

    def __repr__(self):
        return '<Category {}>'.format(self.category_name)

class Link(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    link: so.Mapped[str] = so.mapped_column(sa.String(256))
    category_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Category.id), index=True)
    category: so.Mapped['Category'] = so.relationship('Category', back_populates='links')

    def __repr__(self):
        return '<Link {}>'.format(self.link) 
    
@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))