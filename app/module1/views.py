from . import module1


@module1.route("/")
def hello():
    return "Hello, World!"


@module1.route("/alive")
def alive():
    return "Yes!"
