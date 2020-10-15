# Fórmula (A/B) = (x/C) ; x = (A * C) / B ;
# Reformula (A/B) = (C/x) ; x = (A/B) * C ;

a = 2
b = 2
c = 2

x = (a * c) / b

hypothesis_one = a / b

hypothesis_two = x / c

print(hypothesis_one)

print(hypothesis_two)

if hypothesis_one == hypothesis_two:
    print('Your hypothesis is right')
else:
    print('Your hypothesis is wrong')

d = 2
e = 2
f = 2

y = (d / e) * f

hypothesis_three = d / e
 
hypothesis_four = f / y

print(hypothesis_three)

print(hypothesis_four)

if hypothesis_three == hypothesis_four:
    print('Your hypothesis is right')
else:
    print('Your hypothesis is wrong')
