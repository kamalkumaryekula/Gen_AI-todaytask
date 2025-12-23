class operations:
    #write a function to calculate mean ,meadian,SD,varience
    def _mean(*args):
        _count = 0
        _sum =0
        for i in args:
            _sum +=i
            _count +=1
            m = _sum/_count
        return m

    #print(_mean(1,2,3))
    

    def _median(*args):
        sorted_args = sorted(args)
        n = len(sorted_args)
        if n % 2 != 0:
            _median = sorted_args[n//2]
        else:
            mid1 = sorted_args[(n//2)-1]
            mid2 = sorted_args[n//2]
            _median = (mid1 + mid2)/2
        return _median


    #print(_median(1,2,3,4,5,6))   #if even 3.5 else 4

    def _variance(*args): 
        n = len(args)
        if n < 2:
            return 0
        mean = sum(args)/n
        squared_diff_sum = sum((x - mean)**2 for x in args)
        variance = squared_diff_sum/(n-1)
        return variance

    #print(_variance(2,4,6,7,8,9))  # 6.8

    def _sd(*args):
        n = len(args)
        if n < 2:
            return 0
        mean =sum(args)/n
        squared_diff_sum = sum((x - mean)**2 for x in args)
        variance = squared_diff_sum/(n-1)
        sd = variance**0.5
        return sd

    #print(_sd(2,4,6,7,8,9))
print(f'mean:{operations._mean(2,4,6,7,8,9)}')
print(f'median:{operations._median(2,4,6,7,8,9)}')     
print(f'variance:{operations._variance(2,4,6,7,8,9)}')     
print(f'standard_deviation:{operations._sd(2,4,6,7,8,9)}')     