import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    password='password'
)

r.set('foo', 'bar')
value = r.get('foo')
print(value)  # bar

print("Ich liebe dich!!!")