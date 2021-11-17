from flask import render_template, jsonify


def init_error_views(app):
    @app.errorhandler(403)
    def page_not_found(e):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('errors/500.html'), 500

    # Return validation errors as JSON
    @app.errorhandler(422)
    @app.errorhandler(400)
    def handle_error(err):
        headers = err.data.get("headers", None)
        messages = err.data.get("messages", ["Invalid request."]).get('json')
        print(err.data.get("messages"))
        print(messages.items())
        msg = ''

        for i in messages.items():
            msg = str(i[0]) + str(i[1][0])
            break

        if headers:
            return jsonify({"success": False, "msg": msg})
        else:
            return jsonify({"success": False, "msg": msg})
