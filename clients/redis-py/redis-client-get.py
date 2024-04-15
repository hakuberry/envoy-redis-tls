import time
import redis


client = redis.Redis(host='redis-server', port=6000)

def get_val():
    retries = 5
    while True:
        try:
            print(client.get('get_set_val'), flush=True)
            time.sleep(1)
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(1)

def main(): 
    get_val()


if __name__=="__main__": 
    main()
