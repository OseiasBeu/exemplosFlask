from flask import jsonify, render_template
def configure(app):

    @app.route('/')
    def index():
        return "FUNCIONA FDP!"

    @app.route('/api')
    def api():
        return jsonify(data={"name":"Oseias"})

    @app.route('/langs')
    def langs():
        linguagens = ['Python','JS','C#','Shell']
        return render_template(
                'index.html',
                title="Melhores Linguagens",
                linguagens=linguagens
        )
