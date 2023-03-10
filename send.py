import pika

credentials = pika.PlainCredentials('admin', 'admin')
params = pika.ConnectionParameters('127.0.0.1', 5672, '/', credentials)
connection = pika.BlockingConnection(params)
channel = connection.channel()


channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print(" [x] Sent 'Hello World'")


connection.close()