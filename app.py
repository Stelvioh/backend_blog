#app.py
from flask import Flask
from flask_cors import CORS  # Já importado, apenas destacando.
from domain.user import User
from database import db
from config import Config
import controller.user_controller as controller_user
import controller.post_controller as controller_post

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Aplicando CORS para a aplicação. 
    # Isto permitirá que todas as origens acessem sua API. 
    CORS(app)

    db.init_app(app)
    
    app.register_blueprint(controller_user.UserController.blueprint)
    app.register_blueprint(controller_post.PostController.blueprint)

    with app.app_context():
        db.create_all()    

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
