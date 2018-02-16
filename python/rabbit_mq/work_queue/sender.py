#!/usr/bin/env python3

import pika
import sys


def main():
    msg = ' '.join(sys.argv[1:]) or "hello world"
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    chan = connection.channel()
    chan.queue_declare(queue="hello", durable=True)
    chan.basic_publish(exchange='', routing_key="hello", body=msg, properties=pika.BasicProperties(delivery_mode=2))
    print("msg send [{}]".format(msg))


if __name__ == '__main__':
    main()
