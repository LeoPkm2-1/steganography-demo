def greeting(name):
    print("hello hehe, ",name)
    
def say2(name):
    greeting(name)
    
def count(numb):
    res=0
    say2(numb)
    for i in range(0,numb+1):
        res+=i
    return res