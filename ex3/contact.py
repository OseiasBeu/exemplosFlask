from flask import Blueprint

bp = Blueprint('contact',__name__, url_prefix='/contact')

@bp.route('/')
def contact():
    return "Fale Conosco"

def configure(app):
    app.register_blueprint(bp)
