import urllib.request
from functools import wraps
from collections import namedtuple

def lru_cache(maxsize = 128): #lru_cache is a function that returns a decorator, default maxsize 128
    
    hits = []
    misses = {}
    maxsize = maxsize
    currsize = len(misses)
    
    def cache_info():
        CacheInfo = namedtuple('CacheInfo',['hits','misses','maxsize','currsize'])
        c = CacheInfo(len(hits),len(misses),maxsize,len(misses))
        return c
    
    def decorator(func): #func is get_pep
        
        @wraps(func)
        def inner(n): 
                
            nonlocal hits
            nonlocal misses
            
            if(n in misses):
                hits.append(n)
                return misses[n]
            elif(currsize == maxsize):
                return 'Maximum capacity reached'
            else:
                misses[n] = func(n)
                return misses[n]     
         
        inner.cache_info = cache_info
                
        return inner
    
    return decorator

def main():
    
    @lru_cache(maxsize=32)
    def get_pep(num):
        'Retrieve text of a Python Enhancement Proposal'
        resource = 'http://www.python.org/dev/peps/pep-%04d/' % num

        try:
            with urllib.request.urlopen(resource) as s:
                return s.read()
        except urllib.error.HTTPError:
            return 'Not Found'
    for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
        pep = get_pep(n)
        print(n, len(pep))

    print(get_pep.cache_info())

if __name__ == "__main__":
    main()





    

    






    
    

    
    


    
    
    
    





















    

    


















        





        
        





    

    







    
    
    
    
    
    
    
    
    
    
    
    
    


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



