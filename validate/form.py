#!/user/bin/python
# _*_ coding:utf-8 _*_
from wtforms import Form, IntegerField, StringField
from wtforms.validators import DataRequired

__author__ = "super.gyk"


# 使用wtforms 验证form
class WxPublicForm(Form):
    timestamp = IntegerField(validators=[DataRequired(message="timestamp不能为空！")])
    nonce = StringField(validators=[DataRequired(message="nonce不能为空！")])
    signature = StringField(validators=[DataRequired(message="signature不能为空！")])
    echostr = StringField(validators=[DataRequired(message="echostr不能为空！")])
