#!/usr/bin/env python
# coding=utf-8
import pika, sys, os

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host = '192.168.2.137',
    port = 5672,
    credentials=pika.PlainCredentials(
        username='admin',
        password='admin'
)))
channel = connection.channel()

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
channel.start_consuming()
