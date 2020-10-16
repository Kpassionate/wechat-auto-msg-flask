from flask import Flask, request
from wechatpy import parse_message, create_reply

from common.utils import validate_wx_public
from validate.form import WxPublicForm

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def valid_and_auto():
    global reply
    if request.method == 'GET':
        # 验签
        data = request.args.to_dict()
        form = WxPublicForm(**data)
        if form.validate():
            result = validate_wx_public(form)
            if result[0]:
                return result[1]
            else:
                raise ValueError

    else:
        # 自动回复
        msg = parse_message(request.get_data())
        if msg.type == 'text':
            reply = create_reply('欢迎您！我的主人', message=msg)
            # reply = create_reply('你发送了条文字信息：' + msg.content, message=msg)
        elif msg.type == 'image':
            reply = create_reply('哇您的神仙颜值小管必须给您给打满分哦', message=msg)
            # reply = create_reply('你发送了条图片信息', msg)
        else:
            reply = create_reply('小管不明白，小管只能识别文字和图片哦', message=msg)
    return reply.render()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
