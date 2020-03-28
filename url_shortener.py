class url_shortner:
    url2id = {}
    id = 1
    
    def shorten_url(self,original_url):
        if original_url in self.url2id:
            id = self.url2id[original_url]
            shorten = self.encoded(id)
        else:
            self.url2id[original_url] = self.id
            shorten = self.encoded(self.id)
            self.id +=1
        return 'tinyurl.com/' + str(shorten)
    
    def encoded(self,id):
        characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        length = len(characters)
        temp = []
        while (id > 0):
            val = id % length
            temp.append(characters[val])
            id = id // length
            
        return ''.join(temp[::-1])

            
shortner = url_shortner()
print(shortner.shorten_url("Google.com"))
print(shortner.shorten_url("Amazon.com"))
print(shortner.shorten_url("http://home.iitk.ac.in/~chouhan/"))
print(shortner.shorten_url("https://www.facebook.com/profile.php?id=100008925755091"))
print(shortner.shorten_url("https://github.com/pcgotan"))
print(shortner.shorten_url("Google.com"))
print(shortner.shorten_url("http://home.iitk.ac.in/~chouhan/"))
