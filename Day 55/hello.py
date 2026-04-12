from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return (
        "<h1 style='text-align: center'> Hello, world!</h1>"
        "<p>This is a paragraph</p>"
        "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExc3U3Yzh5cW1rajJua3BlaTRudDkxbmR2aXE3aWV2NTRzaHFkcDI3YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/901mxGLGQN2PyCQpoc/giphy.gif' width=200>"
    )


@app.route("/bye")
def say_bye():
    return "Bye"


@app.route("/hello/<name>/<int:number>")
def say_hello(name, number):
    return f"Hello {name} {number}"


if __name__ == "__main__":
    app.run(debug=True)
