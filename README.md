# url_shortener

* Used python dictionary to store each new url and assign it a new unique id++   
* Applied base64 encoding and compress base10 to base64


#### Time Complexity:
* **O(n * log_62(id))** : adding n ids to dictionary takes **O(n)** and encoding takes **O(log_64(id))**   
#### Space Complexity:
* **O(n)** : We have n ids  
