from irc import *
import os
import random
import time
import re
import math


server = "irc.root-me.org"       #settings
channel = "#root-me_challenge"
nickname = "mathsbot"

square = ""
multiple = ""
ans = ""
n = 1

irc = IRC()
irc.connect(server, channel, nickname)




while 1:
    text = irc.get_text()
    print text

    time.sleep(2)
    if n == 1:
        irc.send("Candy", "!ep1")
        n = 0

    if "PRIVMSG mathsbot :" in text:
        regex = re.compile('mathsbot :(\d{3}) \/ (\d{4})')
        rx = regex.search(text)

        square = int(rx.group(1))
        multiple = int(rx.group(2))

        ans = math.sqrt(square) * multiple
        ans = round(ans,2)
        ans = "!ep1 -rep " + str(ans)
        #print  ans
        #time.sleep(2)
        irc.send("Candy", ans)
        #time.sleep(3)
