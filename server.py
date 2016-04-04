from flask import Flask, make_response, render_template


app = Flask(__name__)


@app.route("/")
def index():
    return """
    <a href="/launch.jnlp">Open Web Start</a>
    """


@app.route("/launch.jnlp")
def launch_jnlp():
    VERSION = '1.0'

    print render_template('launch.jnlp', version=VERSION)

    resp = make_response(
        render_template('launch.jnlp', version=VERSION),
        200)
    resp.headers['Content-Type'] = 'application/x-java-jnlp-file'
    resp.headers['X-java-jnlp-version-id'] = VERSION

    return resp


@app.route("/bin/webStartOnJython-signed.jar")
def signed_jar():
    # Silly, can be done via flask.url_for('static', ...)
    with open('bin/webStartOnJython-signed.jar') as f:
        return f.read()


if __name__ == "__main__":
    app.run()
