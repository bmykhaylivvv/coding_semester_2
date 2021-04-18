import datetime

now = datetime.datetime.now()

print(now)
print(repr(now))
print(eval(repr(now)))