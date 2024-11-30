
import sys
import os
from tqdm import tqdm



def conv(lrcPath, srtPath):
    with open(lrcPath, encoding='utf8') as lrc:
        with  open(srtPath, "w", encoding='utf8') as srt:
            prevDate = None
            n = 1
            for i in lrc.readlines():
                if ']' not in i:
                    continue
                d, s = i.split(']')
                mm, sec = d[1:].split(':')
                s = s.strip()
                secInt, secCent = sec.split('.')
                srtDate = '00:%s:%s,%s0' % (mm, secInt, secCent)
                if prevDate is not None and prevDate != srtDate and prevStr:
                    print(n, file=srt)
                    print(prevDate, '-->', srtDate, file=srt)
                    print(prevStr, file=srt)
                    print(file=srt)
                    n = n+1
                prevDate = srtDate
                prevStr = s


def walkLrc(p='.'):
    for root, _, files in os.walk(p):
        for f in files:
            if not f.endswith('.lrc'):
                continue
            p = os.path.join(root, f)
            p2 = p[:-4]+'.srt'
            print(p, p2)
            conv(p, p2)


walkLrc(sys.argv[1])

if __name__ == __main__:

    lrc_Path = ''
    str_Path = ''

    for i in tqdm(os.listdir(lrc_Path)):
        
        str_endswith = os.path.join(str_Path, i)
        p2 = str_endswith[:-4] + '.str'
        
        conv(os.path.join(lrc_Path, i), p2)
