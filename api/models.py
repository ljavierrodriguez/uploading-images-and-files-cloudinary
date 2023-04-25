from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Galeria(db.Model):
    __tablename__ = 'galleries'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    public_id = db.Column(db.String(100), nullable=False)
    type_upload = db.Column(db.String(100), default="images")

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "image": self.image,
            "public_id": self.public_id,
            "type_upload": self.type_upload
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()