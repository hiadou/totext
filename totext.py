from pydub import AudioSegment
from aip import AipSpeech
import time
import os

APP_ID = 'xxxxx'
API_KEY = 'xxxxxxxx'
SECRET_KEY = 'xxxxxxxxx'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

def listen(save_name1):
    with open(save_name1, 'rb') as f:
        audio_data = f.read()

    result = client.asr(audio_data, 'wav', 16000, {
        'dev_pid': 1737,
    })

    result_text = result["result"][0]

    return result_text


soundy = AudioSegment.from_file('233.mp3')
soundytime=soundy.duration_seconds
a = int(soundytime)
b = 55
st = 0
sp = 55000
print("英语听力转文本，缺点没有标点符号")
print("学习英语，不可能的，这辈子都不存在")
print("原始音频长度："+str(a)+"秒\n稍后分析出的内容会储存到 ytxt.txt 中")
song = AudioSegment.from_mp3('233.mp3').set_frame_rate(16000).set_channels(1).set_sample_width(2)
starttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
ytxt = open('ytxt.txt','a')
ytxt.write('开始时间:'+starttime+"\n")
ytxt.close()
while a>b:
  word = song[st:sp]
  save_name = (str(st/1000)+"-"+str(sp/1000)+".wav")
  word.export(save_name, format="wav")
  print("正在分析文件"+str(st/1000)+"秒到"+str(sp/1000)+"秒的音频")
  btxt = listen(save_name)
  ytxt = open('ytxt.txt','a')
  ytxt.write(str(st/1000)+"秒到"+str(sp/1000)+"秒的内容：\n"+btxt+"\n")
  ytxt.close()
  os.remove(save_name)
  st = sp-5000
  sp = st+55000
  a = a-b+5

sp = st+(a*1000)
word = song[st:sp]
save_name = (str(st/1000)+"-"+str(sp/1000)+".wav")
word.export(save_name, format="wav")
starttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("正在分析文件"+str(st/1000)+"秒到"+str(sp/1000)+"秒的音频")
btxt = listen(save_name)
ytxt = open('ytxt.txt','a')
enttime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
ytxt.write(str(st/1000)+"秒到"+str(sp/1000)+"秒的内容：\n"+btxt+"\n结束时间"+enttime+"\n------分割线------\n\n")
ytxt.close()
os.remove(save_name)
