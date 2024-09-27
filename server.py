import socket
import sys
from datetime import datetime

def start_server(port):
    # Створюємо сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', port))
    print(f"Сервер запущено на порту {port}")

    try:
        while True:
            # Отримуємо повідомлення від клієнта
            data, address = server_socket.recvfrom(1024)
            message = data.decode('utf-8')

            # Генеруємо відповідь
            current_time = datetime.now().strftime('%H:%M:%S, %d-%m-%Y')
            response = f"Your message was: {message} at {current_time}\n"

            # Відправляємо відповідь назад
            server_socket.sendto(response.encode('utf-8'), address)
            print(f"Отримано повідомлення: {message} від {address}, відправлено відповідь")
    except KeyboardInterrupt:
        print("\nСервер зупинено")
    finally:
        server_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Використання: python server.py <port>")
        sys.exit(1)

    port = int(sys.argv[1])
    start_server(port)
