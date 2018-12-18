#！user/bin/env python3.7
# coding:utf-8
# author:wanghongzhang
# email:458620786@qq.com
# time: 2018/11/21

# coding=utf-8

import sys
import json

IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
else:
    import urllib2
    from urllib import quote_plus
    from urllib2 import urlopen
    from urllib2 import Request
    from urllib2 import URLError
    from urllib import urlencode

API_KEY = 'sf3u476szZ4cOLUfYEEGGTiE'
SECRET_KEY = 'ZuG7qwNnh1OQWbRZUxv3vKwK8oOvb8Sw'

TEXT = "欢迎使用百度语音合成"

# 发音人选择, 0为普通女声，1为普通男生，3为情感合成-度逍遥，4为情感合成-度丫丫，默认为普通女声
PER = 0
# 语速，取值0-15，默认为5中语速
SPD = 5
# 音调，取值0-15，默认为5中语调
PIT = 5
# 音量，取值0-9，默认为5中音量
VOL = 5
# 下载的文件格式, 3：mp3(default) 4： pcm-16k 5： pcm-8k 6. wav
AUE = 3

FORMATS = {3: "mp3", 4: "pcm", 5: "pcm", 6: "wav"}
FORMAT = FORMATS[AUE]

CUID = "123456PYTHON"

TTS_URL = 'http://tsn.baidu.com/text2audio'


class DemoError(Exception):
    pass


    """  TOKEN start """

TOKEN_URL = 'http://openapi.baidu.com/oauth/2.0/token'
SCOPE = 'audio_tts_post'  # 有此scope表示有tts能力，没有请在网页里勾选


def fetch_token():
    # print("fetch token begin")
    params = {'grant_type': 'client_credentials',
              'client_id': API_KEY,
              'client_secret': SECRET_KEY}
    post_data = urlencode(params)
    if (IS_PY3):
        post_data = post_data.encode('utf-8')
    req = Request(TOKEN_URL, post_data)
    try:
        f = urlopen(req, timeout=5)
        car_plate_voice_str = f.read()
    except URLError as err:
        # print('token http response http code : ' + str(err.code))
        car_plate_voice_str = err.read()
    if (IS_PY3):
        car_plate_voice_str = car_plate_voice_str.decode()

    # print(car_plate_voice_str)
    car_plate_voice = json.loads(car_plate_voice_str)
    # print(car_plate_voice)
    if ('access_token' in car_plate_voice.keys() and 'scope' in car_plate_voice.keys()):
        if not SCOPE in car_plate_voice['scope'].split(' '):
            raise DemoError('scope is not correct')
        # print('SUCCESS WITH TOKEN: %s ; EXPIRES IN SECONDS: %s' % (car_plate_voice['access_token'], car_plate_voice['expires_in']))
        return car_plate_voice['access_token']
    else:
        raise DemoError('MAYBE API_KEY or SECRET_KEY not correct: access_token or scope not found in token response')


"""  TOKEN end """
#
# if __name__ == '__main__':
#     token = fetch_token()
#     tex = quote_plus(TEXT)  # 此处TEXT需要两次urlencode
#     print(tex)
#     params = {'tok': token, 'tex': tex, 'per': PER, 'spd': SPD, 'pit': PIT, 'vol': VOL, 'aue': AUE, 'cuid': CUID,
#               'lan': 'zh', 'ctp': 1}  # lan ctp 固定参数
#
#     data = urlencode(params)
#     print('test on Web Browser' + TTS_URL + '?' + data)
#     #
#     req = Request(TTS_URL, data.encode('utf-8'))
#
#     has_error = False
#     try:
#         f = urlopen(req)
#         car_plate_voice_str = f.read()
#
#         has_error = ('Content-Type' not in f.headers.keys() or f.headers['Content-Type'].find('audio/') < 0)
#     except  URLError as err:
#         print('asr http response http code : ' + str(err.code))
#         car_plate_voice_str = err.read()
#         has_error = True
#
#     save_file = "error.txt" if has_error else 'car_plate_voice.' + FORMAT
#     with open(save_file, 'wb') as of:
#         of.write(car_plate_voice_str)












    #
    # if has_error:
    #     if (IS_PY3):
    #         car_plate_voice_str = str(car_plate_voice_str, 'utf-8')
    #     print("tts api  error:" + car_plate_voice_str)
    #
    # print("car_plate_voice saved as :" + save_file)
