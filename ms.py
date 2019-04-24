from flask import *
import PyLineNotify

#あなたのトークンを入力してください
TOKEN = 'YOURTOKEN'

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def Send():
    if request.method == "GET":
        return """
            メッセージを入力してください。
            <form action="/" method="POST">
            <input name="ms"></input>
            </form>"""
    else:
        PyLineNotify.send_message(token=TOKEN, message=str(request.form["ms"]))
        return """'{}'と送信しました。メッセージを入力してください。
            <form action="/" method="POST">

            <input name="ms"></input>
            </form>""".format(str(request.form["ms"]))
if __name__ == "__main__":
    app.run(debug=True)