# Question 7-1
# def test_square_root(x,a):
#     while True:
#         print(x)
#         y=(x+a/x)/2
#         if y==x:
#             break

#         x=y
# print(test_square_root(15,16))

# Question 2
import math as m
# def eval_loop(x):
#     y=eval(x)
#     if x!="done":
#      return y
#     else:
#         return y

# print(eval_loop(x=input("Please enter only string:")))

# Question 3

def factorial(n):
 if n == 0:
      return 1
 else:
      recurse = factorial(n-1)
      result = n * recurse
      return result
def estimate_pi():
     total=0
     k=0
     factor= 2* m.sqrt(2)/ 9801
     while True:
         num= factorial(4*k)*(1103+26390*k)
         div= (factorial(k)**4)*396**(4*k)
         term= factor * num/div
         total+=term
         if abs(term) < 1e-15:
             break
         k+=1
     return 1/total
estimate_pi()
