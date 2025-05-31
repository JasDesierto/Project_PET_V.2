from app import create_app
import sys

sys.path.insert(0, "./app")
app = create_app()
if __name__ == "__main__":

    app.run(debug=True)
