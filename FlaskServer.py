from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/python")
def python():
    return render_template("python.html")

@app.route("/javascript")
def javascript():
    return render_template("javascript.html")

@app.route("/cpp")
def cpp():
    return render_template("cpp.html")

@app.route("/ruby")
def ruby():
    return render_template("ruby.html")

@app.route("/blender")
def blender():
    return render_template("blender.html")

@app.route("/unreal")
def unreal():
    return render_template("unreal.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0")