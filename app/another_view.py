from flask import Flask


def include_other_views(app: Flask) -> None:

    @app.route('/about', methods=['GET'])
    def about():
        return 'about'
