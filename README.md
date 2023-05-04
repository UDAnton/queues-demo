## Queues demo

The demo is written in python 3 and uses docker-compose to run Redis and Beanstalkd.

---

## How to run
1. Start up docker containers: ```docker-compose up -d```;
2. Install libs ```pip install redis Faker```;
3. Run scripts to test redis and beanstalkd queues performance: 
    ```
    python3 beanstalkd-demo.py
    python3 redis-rpush-and-blpop-demo.py
    ```

---
## Results

### Write operations

|Number of messages  |Redis RDB     |Redis AOF     |Beanstalkd    |
|-------------------:|-------------:|-------------:|-------------:|
|1000 messages       |1.3349 sec    |1.3531 sec    |1.0150 sec    |
|5000 messages       |5.7716 sec    |5.9535 sec    |5.7224 sec    |
|10000 messages      |10.2262 sec   |12.0426 sec   |10.9831 sec   |
|20000 messages      |21.3128 sec   |20.9213 sec   |24.1620 sec   |


### Read operations

|Number of messages  |Redis RDB     |Redis AOF    |Beanstalkd    |
|-------------------:|-------------:|------------:|-------------:|
|1000 messages       |0.8011 sec    |1.0714 sec   |1.0044 sec    |
|5000 messages       |4.6192 sec    |5.1997 sec   |4.1279 sec    |
|10000 messages      |8.0135 sec    |9.6971 sec   |8.3014 sec    |
|20000 messages      |15.7321 sec   |17.9059 sec  |18.0273 sec   |
