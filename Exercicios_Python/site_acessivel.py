import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')

except urllib.error.URLError:
    print(f'\033[0;30mO site pudim não está disponivel no momento.\033[m')

else:
    print(f'\033[0;32mConsegui acessar o site pudim com sucesso!\033[m')