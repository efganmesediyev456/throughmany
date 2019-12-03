from extension import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    posts = db.relationship("Post", backref="user")

    def __repr__(self):
        return self.name

    @property
    def comments(self):
        q=db.session.query(User.name,Post.post_title, Comment.comment).filter(User.id == Post.user_id).filter(Post.id == Comment.post_id).filter(User.id==self.id).all()
        return q


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    post_title=db.Column(db.String(60), nullable=False)
    post_body=db.Column(db.Text, nullable=False)
    comments = db.relationship("Comment" , backref="post")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))


    def __repr__(self):
        return self.post_title

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment=db.Column(db.Text, nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))

    def __repr__(self):
        return self.comment


