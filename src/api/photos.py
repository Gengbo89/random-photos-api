from flask import Blueprint, send_file, jsonify
import random
from utils.file_utils import get_all_photos

photos_bp = Blueprint('photos', __name__)

@photos_bp.route('/api/images', methods=['GET'])
def get_random_image():
    photos = get_all_photos('/photos')
    if not photos:
        return jsonify({"error": "No photos found"}), 404
    photo = random.choice(photos)
    return send_file(photo)
