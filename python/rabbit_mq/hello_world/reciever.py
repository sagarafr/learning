#!/usr/bin/env python3

import pika


def callback(chan, method, properties, body):
    print("recv [{}]".format(body))


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    chan = connection.channel()
    chan.queue_declare(queue="hello")
    chan.basic_consume(consumer_callback=callback, queue="hello", no_ack=True)
    print("waiting for msg. End up with Ctrl + C")
    chan.start_consuming()
    chan.close()


if __name__ == '__main__':
    main()
