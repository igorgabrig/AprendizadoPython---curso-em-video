#Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br/')

except urllib.error.URLError:
    print('O site não esta acessivel')

else:
    print('Tudo OK')
    #print(site.read())