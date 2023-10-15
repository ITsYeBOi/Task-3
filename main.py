from website import create_app
from website.models import db  # 

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(debug=True)
