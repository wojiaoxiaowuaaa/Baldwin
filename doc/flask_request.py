from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/platform', methods=['POST'])
def get_platform():
    # 从请求入参的JSON数据中获取platform字段，并去除首尾空格.如果请求的入参中不包含platform字段，则默认返回空字符串.
    platform = request.json.get("platform", "").strip()
    # print(platform)
    # 返回获取到的platform值
    return jsonify({"platform": platform})


if __name__ == '__main__':
    app.run(debug=True)
