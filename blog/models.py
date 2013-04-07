from google.appengine.ext import db


class Post(db.Model):
    title = db.StringProperty(required=True)
    body = db.TextProperty(required=True)
    created_at = db.DateTimeProperty(auto_now_add=True)
    updated_at = db.DateTimeProperty(auto_now_add=True)
    is_edited = db.BooleanProperty(default=False)
    active = db.BooleanProperty(default=True)

    def __unicode__(self):
        return self.title
