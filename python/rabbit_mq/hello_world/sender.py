#!/usr/bin/env python3

import pika


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    chan = connection.channel()
    chan.queue_declare(queue="hello")
    chan.basic_publish(exchange='', routing_key="hello", body="hello world")
    print("msg send")
    chan.close()


if __name__ == '__main__':
    main()
