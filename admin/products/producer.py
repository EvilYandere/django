import pika
import json

params = pika.URLParameters('amqps://zgjdnemk:mazfHa2ilWv0vBaI6g3jeDRQODDeLtTA@fish.rmq.cloudamqp.com/zgjdnemk')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
