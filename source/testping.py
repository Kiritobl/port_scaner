from pythonping import ping

def check_online(ip: str):
    message = ping(ip)
    print(message)
    success_ping = "Reply"
    if success_ping in str(message):
        return 1
    else:
        return 0

print(check_online('110.242.68.66'))