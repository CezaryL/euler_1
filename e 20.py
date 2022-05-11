# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!


x= int(input())
fact=1

for i in range(1, x+1):
    fact = fact * i
print(fact)
y=0
z=str(fact)
for i in range (len(z)):
    y=y+int(z[i])
print(y)