import math
def convert(n):
    global count 
    count = 0 
    back(n)
    print(count)



def back(n):
    if n<10:
        count = count +1
        return ;

    elif n>=20:
        x1 = math.floor(n/10**(math.ceil(math.log(n,10))-2))
        print(x1)
        # print(n)
        # print(x1)
        if x1>25:

            back(n//10)
            
        else:
            
            back(n//10)
            back(n//100)
        
    return count

        
if __name__ =="__main__":
    convert(11258)
