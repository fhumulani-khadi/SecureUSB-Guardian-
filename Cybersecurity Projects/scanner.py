import os
from hashing import hash_file
from logger import log_threat

def scan_usb(usb_path):

    suspicious_extensions = [".exe", ".bat", ".vbs", ".ps1", ".cmd", ".scr"]

    # Example malware hashes
    known_malware_hashes = [
        "44d88612fea8a8f36de82e1278abb02f"
    ]

    threat_count = 0

    print("🔍 Scanning USB...\n")

    for root, dirs, files in os.walk(usb_path):

        for file in files:

            file_path = os.path.join(root, file)

            print("Checking:", file)

            # Check suspicious extension
            if file.lower().endswith(tuple(suspicious_extensions)):

                file_hash = hash_file(file_path)

                message = f"Suspicious file detected: {file} | Hash: {file_hash}"

                print("⚠️", message)

                log_threat(message)

                threat_count += 1

            # Check malware hash
            file_hash = hash_file(file_path)

            if file_hash in known_malware_hashes:

                message = f"Known malware detected: {file}"

                print("🚨", message)

                log_threat(message)

                threat_count += 1

    print(f"\n⚠️ Total threats detected: {threat_count}")
    print("✅ Scan completed.")