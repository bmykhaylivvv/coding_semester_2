import collections

lst = ['tv', 'tv', 'chair', 'desk', 'desk', 'desk']

a = collections.Counter(lst)
for item in a.items():
    print(item)