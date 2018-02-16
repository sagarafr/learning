#!/usr/bin/env python3

import pika
import time


def callback(chan, method, properties, body):
    print("recv [{}]".format(body))
    time.sleep(len(body) / 5)
    print("done")
    chan.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    chan = connection.channel()
    chan.queue_declare(queue="hello", durable=True)
    # Limit the to 1 msg
    chan.basic_qos(prefetch_count=1)
    chan.basic_consume(consumer_callback=callback, queue="hello")
    print("waiting for msg. End up with Ctrl + C")
    chan.start_consuming()
    chan.close()


if __name__ == '__main__':
    main()
