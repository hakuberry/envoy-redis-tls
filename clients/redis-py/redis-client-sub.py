import time
import redis


client = redis.Redis(host='redis-server', port=6000)
p = client.pubsub()

def get_val():
    retries = 5

    try:

        p.subscribe('pub_sub_channel')

        for message in p.listen():
            print(message)
    except redis.exceptions.ConnectionError as exc:
        if retries == 0:
            raise exc
        retries -= 1
        time.sleep(1)

def main(): 
    get_val()


if __name__=="__main__": 
    main()
