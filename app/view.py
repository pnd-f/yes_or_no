from flask import Flask


def include_views(app: Flask) -> None:

    @app.route('/', methods=['GET'])
    def index():
        return 'hello'
