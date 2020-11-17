import webbrowser
import time

url = 'https://www.bing.com/search?q=reddit'

webbrowser.open_new(url)

fh = open('binggenlist.txt')
for line in fh:

    webbrowser.open(url+'+'+line)
    time.sleep(2)

fh.close()
