from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('61ezGOYZ6XiAbZzI6AnSdhDTeTAhSg96+6AW4z5Z+8KUk6vz5yzTt3Ko23Umkh3+dFSqBSi6GVDPWBz64wAvaj2KM4gm38BziqeZ9voTM2oOj62zaWVv2jnJfqOFnzbAIdc+TEfEL4CMuxE5H/qn3QdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('990326e1a8911b7b3f3c0d4c1c60f7e1')

@app.route("/")
def hello_world():
    return "hello world!"

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
