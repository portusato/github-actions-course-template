import tempfile
file_name = tempfile.mktemp()
print(file_name)

with open(file_name, 'w') as fp:
    fp.write("hello world\n")

print('Which file do you want to read? ')
user_file_name = input()
with open (user_file_name) as fp:
    buf = fp.read()
    print('Read from file:' + buf)

def user_picture1(request):
    """A view that is vulnerable to malicious file access."""
    filename = request.GET.get('p')
    # BAD: This could read any file on the file system
    data = open(filename, 'rb').read()
    return HttpResponse(data)

from Crypto.Cipher import DES, AES

cipher = DES.new(SECRET_KEY)

def send_encrypted(channel, message):
    channel.send(cipher.encrypt(message)) # BAD: weak encryption


cipher = AES.new(SECRET_KEY)

def send_encrypted(channel, message):
    channel.send(cipher.encrypt(message)) # GOOD: strong encryption
