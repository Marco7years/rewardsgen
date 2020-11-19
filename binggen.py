import webbrowser
import time
import os

url = 'https://www.bing.com/search?q=reddit'

webbrowser.register('edge', None, webbrowser.GenericBrowser(os.environ['ProgramFiles(x86)'] + r'\Microsoft\Edge\Application\msedge_proxy.exe'), preferred=True)
webbrowser.open_new(url)

with open('binggenlist.txt', 'r') as fh:
    for line in fh:
        webbrowser.open(url+'+'+line)
        time.sleep(2)
