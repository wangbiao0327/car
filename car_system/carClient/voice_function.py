#！user/bin/env python3.7
# coding:utf-8
# author:wanghongzhang
# email:458620786@qq.com
# time: 2018/11/20


# """ 你的 APPID AK SK """
# APP_ID = '14658832'
# API_KEY = 'sf3u476szZ4cOLUfYEEGGTiE'
# SECRET_KEY = 'ZuG7qwNnh1OQWbRZUxv3vKwK8oOvb8Sw'
#



import urllib.request
import urllib
import json
import base64
import mp3play
import time
import pygame

class BaiduRest:
    def __init__(self, cu_id, api_key, api_secert):
     # token认证的url
        self.token_url = "https://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s"
             # 语音合成的resturl
        self.getvoice_url = "http://tsn.baidu.com/text2audio?tex=%s&lan=zh&cuid=%s&ctp=1&tok=%s"
             # 语音识别的resturl
        self.upvoice_url = 'http://vop.baidu.com/server_api'

        self.cu_id = cu_id
        self.getToken(api_key, api_secert)
        return

    def getToken(self, api_key, api_secert):
        # 1.获取token
        token_url = self.token_url % (api_key,api_secert)
        r_str = urllib.request.urlopen(token_url).read()
        token_data = json.loads(r_str)
        self.token_str = token_data['access_token']


    def getVoice(self, text, filename):
        # 2. 向Rest接口提交数据
        get_url = self.getvoice_url % (urllib.parse.quote(text), self.cu_id, self.token_str)
        #
        voice_data = urllib.request.urlopen(get_url).read()
        # # 3.处理返回数据
        voice_fp = open(filename,'w+b')
        voice_fp.write(voice_data)
        voice_fp.close()
        # f = 'D:\PycharmProjects\car_system2.0\car_plate_voice.mp3'
        # pygame.mixer.init()
        # track = pygame.mixer.music.load(f)
        # pygame.mixer.music.play()
        # time.sleep(3)
        # pygame.mixer.music.stop()
        # voice_fp.close()



    def getText(self, filename):
        # 2. 向Rest接口提交数据
        data = {}
        # 语音的一些参数
        data['format'] = 'wav'
        data['rate'] = 8000
        data['channel'] = 1
        data['cuid'] = self.cu_id
        data['token'] = self.token_str

        wav_fp = open(filename,'rb')
        voice_data = wav_fp.read()
        data['len'] = len(voice_data)
        data['speech'] = base64.b64encode(voice_data).decode('utf-8')
        post_data = json.dumps(data)
        r_data = urllib.request.urlopen(self.upvoice_url,data=bytes(post_data,encoding="utf-8")).read()
    # 3.处理返回数据
        print(json.loads(r_data))
        return json.loads(r_data)['result']


if __name__ == "__main__":

    api_key = "sf3u476szZ4cOLUfYEEGGTiE"
    api_secert = "ZuG7qwNnh1OQWbRZUxv3vKwK8oOvb8Sw"
    # 初始化
    bdr = BaiduRest("14658832", api_key, api_secert)
    # 将字符串语音合成并保存为out.mp3

    bdr.getVoice('14658832', "car_plate_voice.mp3")
    # 识别test.wav语音内容并显示
    print(bdr.getText("car_plate_voice.mp3"))








