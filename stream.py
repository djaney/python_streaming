
import sys
import subprocess
import configparser

Config = configparser.ConfigParser()
Config.read(".config")
YOUTUBE_SECRET = Config['youtube']['secret']
TWITCH_SECRET = Config['twitch']['secret']
TWITCH_SERVER = Config['twitch']['server']
FILTERS = Config['common']['filters']
FILTER_TYPE = Config['common']['filtertype']

def main():

    if 1 >= len(sys.argv):
        print('No command')
        sys.exit(0)

    if 'play' == sys.argv[1]:
        if 3 <= len(sys.argv):
            play(input(2), input(3, ""))
        else:
            print('play has 2 arguments. '+ str(len(sys.argv)-1) + ' provided')
    elif 'youtube' == sys.argv[1]:
        if 3 <= len(sys.argv):
            youtube(input(2), YOUTUBE_SECRET, input(3, ""), input(4, ""))
        else:
            print('play has 2 arguments. '+ str(len(sys.argv)-1) + ' provided')

    elif 'twitch' == sys.argv[1]:
        if 3 <= len(sys.argv):
            twitch(input(2), TWITCH_SECRET, input(3, ""), input(4, ""))
        else:
            print('play has 2 arguments. '+ str(len(sys.argv)-1) + ' provided')
    else:
        print ("invalid command")

def play(inp, opts):
    cmd = "ffplay -i %s %s %s"% (inp, opts, getFilters() )
    subprocess.call( cmd )

def youtube(inp, secret, opts, outOpts):
    cmd = "ffmpeg -thread_queue_size 512 %s -probesize 8192 -i %s -c:v libx264 -b:v 1M -vf scale=-1:720 -r 25 -c:a aac -ar 44100 -b:a 128k -tune zerolatency -preset ultrafast -flags +global_header -f flv %s %s rtmp://a.rtmp.youtube.com/live2/%s"% (opts, inp, getFilters(),outOpts, secret);
    subprocess.call( cmd )

def twitch(inp, secret, opts, outOpts):
    cmd = "ffmpeg -thread_queue_size 512 %s -probesize 8192 -i %s -c:v libx264 -b:v 1M -vf scale=-1:720 -r 25 -c:a aac -ar 44100 -b:a 128k -tune zerolatency -preset ultrafast -flags +global_header -f flv %s %s rtmp://%s/app/%s"% (opts, inp, getFilters(),outOpts, TWITCH_SERVER, secret);
    subprocess.call( cmd )

def input (idx, default = None):
    try:
        return sys.argv[idx]
    except IndexError:
        return default
def getFilters():
    if 0 < len(FILTERS):
        return  '-'+FILTER_TYPE+' "'+FILTERS+'"'
    else:
        return '';
if '__main__' == __name__:
    main()
