from flask import Flask, render_template
from flask_assets import Environment, Bundle
from flask_caching import Cache



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

cache = Cache(app, config={
    'CACHE_TYPE': 'simple',
    'CACHE_DEFAULT_TIMEOUT': 24*60*60
})



@app.route('/')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
