from main import create_app

# Call the Application Factory function to construct a Flask application instance
# using the standard configuration defined in /instance/flask.cfg

if __name__ == '__main__':
    app = create_app('prod.cfg')
    app.run()
