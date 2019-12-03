from extension import app, db, admin
from routes.routes import *
from models.modul import *
from flask_admin.contrib.sqla import ModelView


admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Comment, db.session))


if __name__=='__main__':
    app.run()
