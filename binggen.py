import webbrowser
import time
import os

url = 'https://www.bing.com/search?q=reddit'

webbrowser.register('edge', None, webbrowser.GenericBrowser(os.environ['ProgramFiles(x86)'] + r'\Microsoft\Edge\Application\msedge.exe'), preferred=True)
webbrowser.open_new(url)

fh = open('binggenlist.txt', 'r')
for line in fh:

    webbrowser.open(url+'+'+line)
    time.sleep(2)

fh.close()