import tempfile
file_name = tempfile.mktemp()
print(file_name)

with open(file_name, 'w') as fp:
    fp.write("hello world\n")

with open (file_name) as fp:
    buf = fp.read()
    print('Read from file:' + buf)
