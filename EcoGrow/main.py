from flask import Flask
from space_identification import space_identification_bp  
from Disease_Prediction import disease_identification_bp

app = Flask(__name__)

app.register_blueprint(space_identification_bp, url_prefix='/space_identification')
app.register_blueprint(disease_identification_bp, url_prefix = '/disease_identification')


if __name__ == '__main__':
    app.run(debug=True)



