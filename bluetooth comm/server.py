import bluetooth
from pyfcm import FCMNotification
import netifaces as ni



def getIP():
    iface = "wlp3s0"
    ni.ifaddresses(iface)
    ip = ni.ifaddresses(iface)[ni.AF_INET][0]['addr']
    ip = "172.17.60.121"
    return ip

def sendNotification():
        push_service = FCMNotification(api_key="AAAAXVKY1K4:APA91bEfdiunFvYRfB5WDRmlPVH_vam_58wm0gEtgFkmkB05e0lSxo6qT3yDgZ7nEja1JyaTiqROmzOj0y6y7b489gKHNHk7ytD3-QAifKMfs-fk0XtcZHRaFfa8u-XkdGwEt-N7UpKR")
        registration_id = "dT1-oELeodM:APA91bGIchUnyKj-TsV77IXQCSb5xoXW6qBKY8VU1lcWQfx7zejX3RCCwRgRO6vX9ynmzWQpK4xj5UvnnJsNDM0b05K4fHLNJTENwoK8kkG-7mkw40_jZFuzV4_2ySPRrNUuS1xIYHNG"

        message_title = "Redundant Notification"
        message_body = "Redundancy is at the door"

        data_message = {
        "Person": "Redundancy",
        "Picture": "http://" + getIP() + "images/myfile.jpg"
        }

        result = push_service.notify_single_device(
        registration_id=registration_id,
        message_title=message_title,
        message_body=message_body,
        data_message=data_message
        )
        print result;

def main():
    server_sock=bluetooth.BluetoothSocket( bluetooth.L2CAP )
    port = 0x1001
    server_sock.bind(("",port))
    server_sock.listen(1)

    client_sock,address = server_sock.accept()
    print("Accepted connection from ",address)

    s = 512
    data = client_sock.recv(1024*s)
    f = open("images/myfile.jpg", "wb")
    try:
        f.write(data)
        while data:
            print(".")
            data = client_sock.recv(1024*s)
            f.write(data)
            f.flush()
    finally:
        f.close()
        sendNotification()

    client_sock.close()
    server_sock.close

main()
