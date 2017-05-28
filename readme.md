## Requirements
1. ffmpeg
1. python3
## Create configfile .config

```
[youtube]
secret = XXX

[twitch]
secret = XXX
server = live-tyo.twitch.tv

[common]
filtertype = vf
filters = split[a][b];
          [a]edgedetect,scale=320:240,split[tl][br];
          [b]format=gray,waveform,scale=320:240,split[tr][bl];
          [tl][tr]hstack[top];
          [bl][br]hstack[bottom];
          [top][bottom]vstack,scale=640:480


```
## Start streaming:
```
python stream.py <twitch|youtube> <source> <ffmpeg input options>
```
## Example
Pipe stream to twitch
```
python stream.py twitch rtsp://mpv.cdn3.bigCDN.com:554/bigCDN/_definst_/mp4:bigbuckbunnyiphone_400.mp4
```

Pipe stream to youtube
```
python stream.py youtube rtsp://mpv.cdn3.bigCDN.com:554/bigCDN/_definst_/mp4:bigbuckbunnyiphone_400.mp4
```

Pipe stream to ffplay
```
python stream.py play rtsp://mpv.cdn3.bigCDN.com:554/bigCDN/_definst_/mp4:bigbuckbunnyiphone_400.mp4
```

Play webcam image for windows
```
python stream.py play 0 "-f vfwcap"
```
