

import urllib3

afilnet_class="country"
afilnet_method="getcountries"
afilnet_user="user"
afilnet_password="password"

# Create an URL request
sUrl = "https://www.afilnet.com/api/http/?class="+afilnet_class+"&method="+afilnet_method+"&user="+afilnet_user+"&password="+afilnet_password
	
result = urllib3.urlopen(sUrl).read()


