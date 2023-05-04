import logging
import timeit

import redis
from faker import Faker

logging.basicConfig(level=logging.INFO, filemode='w', format='%(name)s - %(levelname)s - %(message)s')
fake = Faker()

massage_number = 1000

redis_client = redis.Redis(host='localhost', port=6379)


def write_message():
    redis_client.rpush('addresses', fake.address())


def read_message():
    redis_client.blpop(['addresses'])


def run_benchmark(run_num):
    write_results = timeit.timeit(write_message, number=run_num)
    logging.info(f"Total write time: {write_results} seconds")

    read_results = timeit.timeit(read_message, number=run_num)
    logging.info(f"Total read time: {read_results} seconds")


logging.info(f'Test {massage_number} read/write operations with Redis RPUSH/BLPOP')
run_benchmark(run_num=massage_number)

redis_client.close()
