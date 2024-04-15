import time
import redis


client = redis.Redis(host='redis-server', port=6000)

def publish_val():
    retries = 5
    count = 0
    while True:
        try:
            client.publish('pub_sub_channel', count)
            count += 1
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
        
        time.sleep(5)

def main(): 
    publish_val()


if __name__=="__main__": 
    main()
