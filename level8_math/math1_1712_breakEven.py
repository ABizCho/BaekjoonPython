fc,vc,price = map(int, input().split())

if price > vc : print((fc//(price-vc))+1)
else : print(-1)

# def breakEven(f,v,n) :
#   return v*n + f
    

# i = 1
# while 1 :
  
#   if breakEven(fc,vc,i) < price*i :
#     break
#   else :
#     i += 1

# print(i)
