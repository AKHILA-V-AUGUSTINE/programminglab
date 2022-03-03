def finalstr(a, b):
  firsts = b[:1] + a[1:]
  seconds = a[:1] + b[1:]

  return firsts + ' ' + seconds
print(finalstr('cute', 'girl'))
