import subprocess

dict_hardware = {'video': [], 'audio': []}

# 문자열 명령어 실행


def subprocess_open(command):
    with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as popen:
        (stdoutdata, stderrdata) = popen.communicate()
    return stdoutdata, stderrdata


stdoutdata, stderrdata = subprocess_open('ffmpeg -list_devices true -f dshow -i dummy -hide_banner')

stderrdata = stderrdata.decode('utf-8')

out_list = stderrdata.split('\r\n')

temp_video = []
temp_audio = []
for i in out_list:
    if i.find('Video') >= 0:
        temp_video.append(i.split('"')[1])
    if i.find('Audio') >= 0:
        temp_audio.append(i.split('"')[1])

dict_hardware['video'] = temp_video
dict_hardware['audio'] = temp_audio

print(dict_hardware)
