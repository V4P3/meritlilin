a=format(1, '03b')
b=format(1, '03b')
c='10'
cmd=c+a+b
print(cmd)
print(hex(int(cmd,2))[2:])
