import io

stream = io.StringIO('abc')
stream.seek(0, io.SEEK_END)
stream.write('d')

print(stream.getvalue())