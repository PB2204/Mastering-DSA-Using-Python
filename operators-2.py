# Bitwise Operators
print("Bitwise Operators")

a = 10
b = 8

print(bin(a), bin(b))

# a = 10 = 1010
# b = 8  = 1000

# a&b =    1000 = 8
# a|b =    1010 = 10
# a^b =    0010 = 2

print(a&b , bin(a&b)) # 8
print(a|b , bin(a|b)) # 10
print(a^b , bin(a^b)) # 2

# Membership Operators
print("Membership Operators")

c = "Hello, world!"

print('h' in c)
print('h' not in c)
print('H' in c)
print('H' not in c)

# Identity Operators
print("Identity Operators")

d = 30
e = 40
f = 30

print(d is e)
print(d is not e)
print(d is f)
print(d is not f)

# Shift Operators
print("Shift Operators")

# Left Shift Operator ::  <<
g = 10 # bin(g) = 1010
h = g << 2
print(h, bin(h)) # 40 = 101000

# Right Shift Operator :: >>
i = 10 # bin(i) = 1010
j = i >> 2
print(j, bin(j)) # 2 = 10


# Arithmetic -Assignment Operators

k = 25
l = 10
k += l
print(k)
k -= l
print(k)
k *= l
print(k)
k /= l
print(k)
k %= l
print(k)
k //= l
print(k)

m = 7
n = 2
m **= n
print(m)
m **= n
print(m)