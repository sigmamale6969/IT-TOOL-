from hashlib import shal
import hmac

text = b ("This is a plain text")
print ('Text :', key)

key = b'purvi'
print ('Key:', key)

hashed = hmac.new(key, text, shal)

print ('Hahed Value : ', hashed.digest())