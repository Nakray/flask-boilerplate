from app.main import bp


@bp.route('/')
def main():
    return "Hello!"
