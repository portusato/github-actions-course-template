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
