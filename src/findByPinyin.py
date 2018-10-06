# -*- coding: utf-8 -*-

import glob
from pypinyin import pinyin, Style

mao = 'mao'
mao1 = ['māo', 'máo', 'mǎo', 'mào']
mao2 = ['ma1o', 'ma2o', 'ma3o', 'ma4o']

excludes = ['◎卷.', '毛熙震', '毛文锡', '毛明素']


def readFile(fname):
    with open(fname) as f:
        content = f.readlines()
    return content

if __name__ == "__main__":
    count = 0
    # files = ["../corpus/诗经.txt"]
    files = glob.glob("../corpus/*.txt")
    for file in files:
        for line in readFile(file):
            line = line.strip()

            pinyinList = pinyin(line, style=Style.TONE2)

            if [mao2[1]] in pinyinList:
                should_exluce = False
                for exclude in excludes:
                    if (line.find(exclude) != -1):
                        should_exluce = True
                        break
                if should_exluce:
                    continue

                count = count + 1
                indices = [i for i, x in enumerate(pinyinList) if x == [mao2[1]]]
                newLine = ''
                for idx, val in enumerate(line):
                    if idx in indices:
                        newLine += '\033[1m ' + '[' + val + ']' + '\033[0m'
                    else:
                        newLine += val
                newLine = newLine.strip()
                print(str(count) + ". " + newLine)

