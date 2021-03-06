# -*- coding:utf-8  -*-

# 导入 flask
from flask import Flask
from flask import render_template
from flask import jsonify

# 创建 flask 应用
app = Flask(__name__,
    static_folder="",
    template_folder=""
)

# 全局设置
HOST, PORT = "localhost", "5000"
# HOST, PORT = "0.0.0.0", "5000"

@app.route('/')
def index():
    # return "Hello world"
    return render_template("index.html")

@app.route("/api/getButtonName")
def getButtonName():
    return jsonify({"name": "FLASK BUTTON"})


if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True)
