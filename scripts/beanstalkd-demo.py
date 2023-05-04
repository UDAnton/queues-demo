import logging
import timeit
import greenstalk

from faker import Faker

logging.basicConfig(level=logging.INFO, filemode='w', format='%(name)s - %(levelname)s - %(message)s')
fake = Faker()

massage_number = 1000

greenstalk_client = greenstalk.Client(('localhost', 11300))


def write_message():
    message = fake.address()
    greenstalk_client.put(message)


def read_message():
    message = greenstalk_client.reserve()


def run_benchmark(run_num):
    write_results = timeit.timeit(write_message, number=run_num)
    logging.info(f"Total write time: {write_results} seconds")

    read_results = timeit.timeit(read_message, number=run_num)
    logging.info(f"Total read time: {read_results} seconds")


logging.info(f'Test {massage_number} read/write operations with Beanstalkd')
run_benchmark(massage_number)

greenstalk_client.close()
