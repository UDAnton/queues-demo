import logging
import timeit

import redis
from faker import Faker

logging.basicConfig(level=logging.INFO, filemode='w', format='%(name)s - %(levelname)s - %(message)s')
fake = Faker()

redis_client = redis.Redis(host='localhost', port=6379)
massage_number = 1000


def publish_message():
    redis_client.publish('channel', fake.address())


def subscribe_message():
    pubsub = redis_client.pubsub(ignore_subscribe_messages=True)
    pubsub.subscribe('channel')
    message = pubsub.get_message()


def run_benchmark(run_num):
    write_results = timeit.timeit(publish_message, number=run_num)
    logging.info(f"Total write time: {write_results} seconds")

    read_results = timeit.timeit(subscribe_message, number=run_num)
    logging.info(f"Total read time: {read_results} seconds")


logging.info(f'Test {massage_number} read/write operations with Redis Pub/Sub')
run_benchmark(run_num=massage_number)

redis_client.close()
