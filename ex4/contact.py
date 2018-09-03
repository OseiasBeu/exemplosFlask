from flask import Blueprint, render_template, request, abort

bp = Blueprint('contact',__name__, url_prefix='/contact')

@bp.route('/', methods=['GET','POST'])
def contact():
    if request.method == 'GET':
        return render_template('contact.html')
    #processar dados
    print(request.form)
    name = request.form.get('name')
    message = request.form.get('message')


    #validar
    if not name or not message:
        abort(400, 'Mensagem inválida!')



    return "Your Mensage has been sent successfully!"

def configure(app):
    app.register_blueprint(bp)
