from app.init import create_app
from app.routes import bp

app = create_app()
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True)
