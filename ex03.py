from urllib.request import urlopen
from urllib.error import HTTPError, URLError

try:
    html = urlopen("http://dlfjaskdflsdjfklds.com")
except HTTPError as e:
    print(e)
except URLError as e:
    print("The server could not be found!")
else:
    print("It Worked!")

