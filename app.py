from flask import Flask, render_template
from flask_assets import Environment, Bundle


app = Flask(__name__)

assets = Environment(app)
assets.register({
    'css-home': Bundle(
        'css/home.scss',
        filters=('libsass', 'cssmin'),
        depends='css/*.scss',
        output='gen/home.%(version)s.min.css'
    ),
    'js-home': Bundle(
        'javascript/home.js',
        filters='jsmin',
        depends='javascript/*.js',
        output='gen/home.%(version)s.min.js'
    )
})


@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
