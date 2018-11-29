import itchat
import wave
from pyaudio import PyAudio,paInt16
import configparser


# 登录
# itchat.login();

def readConfig(filePath):
    config = configparser.ConfigParser()
    config.read(filePath)

    currIndex = config.get('conf','index')
    nextIndex = str(int(currIndex) + 1)

    config.set('conf','index',nextIndex)
    config.write(open(filePath,'w'))
    return currIndex

#录音参数
framerate = 8000
NUM_SAMPLES = 2000
channels = 1
sampwidth = 2
TIME = 2

#配置文件参数
filePath = 'test.ini'

# 保存录音文件
def save_wave_file(fileName,data):
    '''保存录音文件'''
    wf = wave.open(fileName,'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(sampwidth)
    wf.setframerate(framerate)
    wf.writeframes(b"".join(data))
    wf.close()

def my_record():
    pa = PyAudio()
    stream = pa.open(format = paInt16,channels = 1,
                     rate = framerate,input = True,
                     frames_per_buffer = NUM_SAMPLES)
    my_buf = []
    count = 0
    while count < TIME * 20: #空值录音时间
        string_audio_data = stream.read(NUM_SAMPLES)
        my_buf.append(string_audio_data)
        count += 1
        print('.')
    fileName = readConfig(filePath) + '.wav'
    save_wave_file(fileName,my_buf)
    stream.close()

chunk = 2014
def play(filePath):
    wf = wave.open(filePath,'rb')
    p = PyAudio()
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),channels = wf.getnchannels(),rate = wf.getframerate(),output = True)

    while True:
        data = wf.readframes(chunk)
        if data == "" : break
        stream.write(data)

    stream.close()
    p.terminate()

if __name__ == '__main__':
    my_record()


