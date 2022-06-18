# from main import db, login_manager
# # from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import relationship
# from flask_login import UserMixin
#     # , login_user, LoginManager, login_required, current_user, logout_user
#
# ##CONNECT TO DB
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# # db = SQLAlchemy(app)
#
# class User(UserMixin, db.Model):
#     __tablename__ = "users"
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))
#     name = db.Column(db.String(1000))
#
#     posts = relationship("BlogPost", back_populates="author")
#     comments = relationship("Comment", back_populates="user")
#
#
# class BlogPost(db.Model):
#     __tablename__ = "blog_posts"
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(250), unique=True, nullable=False)
#     subtitle = db.Column(db.String(250), nullable=False)
#     date = db.Column(db.String(250), nullable=False)
#     body = db.Column(db.Text, nullable=False)
#     img_url = db.Column(db.String(250), nullable=False)
#     author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#
#     author = relationship("User", back_populates="posts")
#     comments = relationship("Comment", back_populates="post")
#
# class Comment(db.Model):
#     __tablename__ = "comments"
#     id = db.Column(db.Integer, primary_key=True)
#     comment = db.Column(db.Text, nullable=False)
#
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
#     user = relationship("User", back_populates="comments")
#
#     post_id = db.Column(db.Integer, db.ForeignKey('blog_posts.id'))
#     post = relationship("BlogPost", back_populates="comments")
#
#
#
#
#
# # db.create_all()