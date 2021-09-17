from distributed_lru_cache.cache import LRUCache

# capacity: The capacity of the cache instance (128 by default)
# cache_name: The name of the cache instance to create ('lrucache' by default)
# redis_host: The host name of redis server ('localhost' by default)
# redis_port: The port of redis server (6379 by default)
# redis_db: The database to use on redis (0 by default)
# ttl: time to live, the expiration time (0 by default = No expiration)

lru = LRUCache(capacity=2, cache_name='lrucache', redis_host='localhost', redis_port=6379, redis_db=0, ttl=5)

# The item is created/updated on the queue using a dictionary
# LRU cache is updated (item is bumped up if it already exists)
# Validates the capacity of the cache and remove the Last Recently Used key if no more space is found using the popleft() command
# Validates if the key is in the cache instance and remove that key in order to create it again:
#    - Create the key again on the local instance and redis
# If a ttl(Time to live) was given, the item will expire in that amount of time

lru.put('10', '1')
lru.put('20', '1', ttl=1)

# LRU cache is checked for item, if it exists item is returned (item is bumped up) and the queue using the following steps:
# - Remove the item from the queue
# - Remove the key from redis hash
# - Append the node again on the queue
# - Create the key on redis hash again
# - Obtain the value from the node/key and the value is returned

lru.get('10')

# put: To create a cache item into the cache instance could have an extra argument (ttl) to expire this specific item
# get: The obtain a cache item altering the order of the items
# peek: The obtain a cache item without altering the order of the items
# set_redis_conn: To instantiate a specific redis connection after the item creation
# clear_cache_instance: To clear the entire cache instance



