#!/usr/bin/env python3
import pika
import sys
import signal

def connection_timeout_handler(signum, frame):
    raise TimeoutError("Connection attempt timed out (exceeded 2 seconds)")

def main():
    # Set an alarm for 5 seconds to prevent hanging during connection
    signal.signal(signal.SIGALRM, connection_timeout_handler)
    signal.alarm(2)

    credentials = pika.PlainCredentials('myuser', 'tester12345')
    parameters = pika.ConnectionParameters(
        'localhost', 
        5672, 
        'myvhost', 
        credentials,
        socket_timeout=2  # additional safeguard via socket timeout
    )

    try:
        connection = pika.BlockingConnection(parameters)
    except (TimeoutError, pika.exceptions.AMQPConnectionError) as e:
        print("Error: Could not establish connection within 2 seconds:", e)
        sys.exit(1)
    finally:
        # Cancel the alarm if connection was successful
        signal.alarm(0)

    channel = connection.channel()

    # Declare test exchange (using direct exchange type)
    exchange_name = 'test_exchange'
    channel.exchange_declare(exchange=exchange_name, exchange_type='direct', durable=True)

    # Declare test queue with TTL (3600 seconds = 3600000 ms)
    queue_name = 'test_queue'
    ttl_ms = 3600 * 1000  # TTL in milliseconds
    arguments = {
        'x-message-ttl': ttl_ms
    }
    channel.queue_declare(queue=queue_name, durable=True, arguments=arguments)

    # Bind the queue to the exchange using a routing key
    routing_key = 'test_key'
    channel.queue_bind(queue=queue_name, exchange=exchange_name, routing_key=routing_key)

    # Publish sample messages to the test exchange
    for i in range(5):
        message = f"Sample message {i+1}"
        channel.basic_publish(
            exchange=exchange_name,
            routing_key=routing_key,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2  # Make message persistent
            )
        )
        print(f"Sent: {message}")

    # Close connection
    connection.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted by user")
        sys.exit(0)

