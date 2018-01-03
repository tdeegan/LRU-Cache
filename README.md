# LRU-Cache

'lru_cache.py' uses a least recently used cache to speed up function calls attempting to retrieve text from the web.  

The least recently used cache function acts as a parameterized decorator for the function being called repeatedly.  

The length of the text in each instance is displayed followed by the cache information.

A "hit" is defined as an instance where the program was able to retrieve the necessary information from the cache and avoid a costly function call.
