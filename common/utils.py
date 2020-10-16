#!/user/bin/python
# _*_ coding:utf-8 _*_
import hashlib


from settings import TOKEN

__author__ = "super.gyk"


# 验证签名 第一步创建列表 第二步进行排序 第三步拼接成字符串 第四步 验签
def validate_wx_public(form, token=TOKEN):
    timestamp = form.timestamp.data
    nonce = form.nonce.data
    echostr = form.echostr.data
    signature = form.signature.data

    array = [str(timestamp), nonce, token]
    array.sort()
    arr_to_str = ''.join(array)
    result = hashlib.sha1(arr_to_str.encode('utf8')).hexdigest()

    return result == signature, echostr

