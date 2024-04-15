import time
import redis


client = redis.Redis(host='redis-server', port=6000)

def set_incr_val():
    retries = 5
    count = 0
    while True:
        try:
            client.set('get_set_val', count)
            count += 1
            time.sleep(5)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
        
        time.sleep(1)

def main(): 
    set_incr_val()


if __name__=="__main__": 
    main()
