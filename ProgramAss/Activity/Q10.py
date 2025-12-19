class NegativeNumberError(Exception):
 def __init__(self,n):
 self.n=n
 def __str__(self):
 return f"the given list has negative number {self.n}"
n=input().split()
n=[int(i) for i in n]
def neg_num(n):
 for i in n:
 if i<0:
 raise NegativeNumberError(i)
try:
 neg_num(n)
except NegativeNumberError as e:
 print("Error :\n ",e)
