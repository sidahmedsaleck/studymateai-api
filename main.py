from app.api import create_app




def run_app():
    app = create_app("dev")
    app.run()


if __name__ == "__main__":
    run_app()