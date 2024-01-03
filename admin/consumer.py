import json, pika, os, django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin.settings')
django.setup()


from products.models import Product


params = pika.URLParameters('some_key')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Получил сообщение')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes += 1
    product.save()
    print('Количество лайков увеличено')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

channel.start_consuming()

channel.close()
