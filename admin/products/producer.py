import pika, json

params = pika.URLParameters('amqps://zvihcfla:Vmkzg4_yzGDL2Ldh6Dkq7gLVNhzqTTOQ@orangutan.rmq.cloudamqp.com/zvihcfla')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
  properties = pika.BasicProperties(method)
  channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)