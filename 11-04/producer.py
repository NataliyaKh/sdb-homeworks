#!/usr/bin/env python
# coding=utf-8
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='192.168.123.13',
    port=5672, 
    credentials=pika.PlainCredentials(
        username='admin',
        password='admin'
)))
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello Netology!')

connection.close()
