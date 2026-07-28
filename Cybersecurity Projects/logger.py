from datetime import datetime

def log_threat(message):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("scan_log.txt", "a") as log:
        log.write(f"[{time}] {message}\n")