import io

stream = io.StringIO('abc')
stream.write('d')

print(stream.getvalue())