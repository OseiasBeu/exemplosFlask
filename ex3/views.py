from flask import jsonify
def configure(app):

    @app.route('/')
    def index():
        return "FUNCIONA FDP!"

    @app.route('/api')
    def api():
        return jsonify(data={"name":"Oseias"})
