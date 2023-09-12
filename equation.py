from SymPy import simbols, solve
a=int(input("a ? "))
b=int(input("b ? "))
c=int(input("c ? "))
d=int(input("d ? "))
x=symbols("x")
eq=a(x**3) + b(x**3) + c(x) + d
sol=solve(eq,x)
print("the solution : ",sol)

# import math 
# from colorama import Fore
# print (Fore.CYAN , " The shape of equation is : a*x^3 + b*x^2 + c*x + d = 0 " )
# print (" Please enter a , b , c and d as inputs to get the results " , Fore.RESET )
# def delta3 ( a , b , c  ) :
#     p = b - ( ( a**2 )/3 )
#     q = (( 2*( a**3 ))/27 ) - ( ( a*b )/3 ) + c
#     delta = ( ( q**2 )/4 ) + ( ( p**3 )/ 27 )
#     print (delta, q, p)
#     if delta > 0 :
#         print ( Fore.BLUE , " The equation has one real root " , Fore.RESET )
#         return delta , q , p
#     elif delta == 0 :
#         print ( Fore.BLUE , " The equation has one real root and one additional real roots " , Fore.RESET )
#         return delta
#     else :
#         print (Fore.BLUE , " The equation has three roots " , Fore.RESET )
#         return delta
# def delta2 ( a , b , c ) :
#     delta = ( b**2 ) - ( 4*a*c )
#     if delta > 0 :
#         print ( Fore.BLUE , " The equation has two real roots " , Fore.RESET )
#         return delta
#     elif delta == 0 :
#         print ( Fore.BLUE , " The equation has one real root " , Fore.RESET )
#         return delta
#     else :
#         print ( Fore.BLUE , " The equation dosen't have any answer " , Fore.RESET )
#         return delta
# a = int ( input (" Please enter a : "))
# b = int ( input (" Please enter b : "))
# c = int ( input (" Please enter c : "))
# d = int ( input (" Please enter d : "))
# if a == 0 and b != 0 :                                                             #second digree
#     print ( Fore.RED , " This is a second degree equation " , Fore.RESET )
#     delta = delta2 ( b , c , d )
#     if delta > 0 :
#         x1 = ( -b + ( math.sqrt ( delta ))) / ( 2 * a )
#         x2 = ( -b - ( math.sqrt ( delta ))) / ( 2 * a )
#         print ( Fore.GREEN , " The answers are : " , x1 , x2 , Fore.RESET )
#     elif delta == 0 :
#         x = -b / ( 2 * a )
#         print ( Fore.GREEN , " The answer is : " , x , Fore.RESET )
#     elif delta < 0 :
#         print ( Fore.GREEN , " The equation doesn't have any answer " , Fore.RESET )
# elif a == 0 and b == 0 and c != 0 :                                                #firs digree
#     print ( Fore.RED , " This is a simple equation " , Fore.RESET )
#     x = - d / c
#     print ( Fore.GREEN , " The answer is : ", x , Fore.RESET )
# elif a == 0 and b == 0 and c == 0 :                                                #not equation
#     print ( Fore.RED , " This is not an equation " , Fore.RESET )
# else :
#     print ( Fore.RED , " This is a third grade equation " , Fore.RESET )
#     if a != 1 :
#         b = b / a
#         c = c / a
#         d = d / a
#     delta , q , p = delta3 ( b , c , d )
#     if delta > 0 :
#         x = ((( -q / 2 ) + math.sqrt( delta ))**( 1/3 )) + ((( -q / 2 ) - math.sqrt( delta ))**( 1/3 )) - ( a / 3 )
#         print ( Fore.GREEN , " The answer is : ", x , Fore.RESET )
#     elif delta == 0 :
#         x1 = ( -2 * (( q / 2 )**( 1 / 3 ))) - ( a / 3 )
#         x2 = (( q / 2 )**( 1 / 3 )) - ( a / 3 )
#         print ( Fore.GREEN , " The first answer is : " , x1 , " and the additional answer is : " , x2 , Fore.RESET )
#     elif delta < 0 :
#         x1 = (( 2 / ( math.sqrt (3) )) * ( math.sqrt ( -p )) * ( math.sin (( 1 / 3 ) * ( math.asin ( (3 * math.sqrt(3) * q )/( 2 * (( math.sqrt(-p))**3)) ))))) - ( a / 3 )
#         x2 = (( -2 / ( math.sqrt (3))) * ( math.sqrt ( -p )) * ( math.sin ((( 1 / 3 ) * ( math.asin (( 3 * q * ( math.sqrt (3))) / ( 2 * (( math.sqrt (-p))**3 ))))) + ( math.pi / 3 )))) - ( a / 3 )
#         x3 = (( 2 / ( math.sqrt (3) )) * ( math.sqrt ( -p )) * ( math.cos ((( 1 / 3 ) * ( math.asin (( 3 * q * ( math.sqrt (3))) / ( 2 * (( math.sqrt (-p))**3 ))))) + ( math.pi / 6 )))) - ( a / 3 )
#         print ( Fore.GREEN , " The answers are : " , x1 , x2 , x3 , Fore.RESET )
# print ( Fore.MAGENTA , " DONE " , Fore.RESET)
