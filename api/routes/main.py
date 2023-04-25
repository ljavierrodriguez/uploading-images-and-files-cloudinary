from flask import Blueprint, request, jsonify
from cloudinary.uploader import upload
from models import Galeria

api = Blueprint('api', __name__)

@api.route('/')
def main():
    return jsonify({ "msg": "API REST WITH FLASK AND CLOUDINARY"})


@api.route('/upload', methods=['POST'])
def upload_image():
    
    #title = request.json.get('title')
    title = request.form['title']
    type_upload = request.form['type_upload']

    if not title:
        return jsonify({ "msg": "El titulo es requerido"}), 400    

    if not 'image' in request.files:
        return jsonify({ "msg": "La imagen es requerida"}), 400    
    
    image = request.files['image']
    public_id = image.filename
    resp = upload(image, resource_type = type_upload, folder="galleries", public_id=public_id)

    if not resp:
        return jsonify({ "msg": "Error al subir imagen"}), 400

    gallery = Galeria()
    gallery.title = title
    gallery.image = resp['secure_url']
    gallery.public_id = public_id

    gallery.save()

    return jsonify(gallery.serialize()), 201

@api.route('/upload/<int:id>', methods=['PUT'])
def update_upload_image(id):
    gallery = Galeria.query.get(id)

    if not gallery:
        return jsonify({ "msg": "Gallery no encontrada."}), 404

    #title = request.json.get('title')
    title = request.form['title']

    if not title:
        return jsonify({ "msg": "El titulo es requerido"}), 400    

    if not 'image' in request.files:
        return jsonify({ "msg": "La imagen es requerida"}), 400    
    
    image = request.files['image']
    resp = upload(image, folder="galleries", public_id=gallery.public_id)

    if not resp:
        return jsonify({ "msg": "Error al subir imagen"}), 400

    gallery.title = title
    gallery.image = resp['secure_url']
    gallery.update()

    return jsonify(gallery.serialize()), 200


@api.route('/uploads', methods=['GET'])
def list_uploads():

    uploads = Galeria.query.all()
    uploads = list(map(lambda item: item.serialize(), uploads))

    return jsonify(uploads), 200
