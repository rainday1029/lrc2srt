
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

if __name__ == __main__:

    lrc_Path = ''
    str_Path = './output'

    for i in tqdm(os.listdir(lrc_Path)):
        
        str_endswith = os.path.join(str_Path, i)
        p2 = str_endswith[:-4] + '.str'
        
        conv(os.path.join(lrc_Path, i), p2)
