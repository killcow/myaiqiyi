from flask import jsonify, render_template

from aiyiqi_app import app


@app.route('/')
def route_map():
    """
    主视图，返回所有视图网址
    """
    rules_iterator = app.url_map.iter_rules()
    return jsonify(
        {rule.endpoint: rule.rule for rule in rules_iterator if rule.endpoint not in ('route_map', 'static')})



def register_blueprint():
    from resources.movies import movie_bp
    app.register_blueprint(movie_bp)


register_blueprint()
