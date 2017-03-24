from flask import Blueprint

from discovermovies.core.models import User


forums = Blueprint('forums',__name__)

@forums.route('/forum/get')
def get_forum():
    try:
        pass
    except KeyError:
        pass
     