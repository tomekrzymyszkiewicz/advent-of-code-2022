print(max(sum(int(value) for value in values.splitlines()) for values in open('input.txt','r').read().split('\n'*2)))
