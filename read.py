import pika

credentials = pika.PlainCredentials('admin', 'admin')
params = pika.ConnectionParameters('127.0.0.1', 5672, '/', credentials)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(queue='hello',
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
