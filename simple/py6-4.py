class Fib(object):

    def __init__(self, num):
        self.num=num

    def __len__(self):
        return self.num
        
    def __str__(self):
        if self.num == 1:
            return [0];
        elif self.num ==2:
            return [0,1]
        else:
            x=0
            y=1
            n=2
            lst=[0,1]
            while n<self.num:
                n+=1
                x,y=y,x+y
                lst.append(y)
            return lst

f = Fib(10)
print (f)
print (len(f))
