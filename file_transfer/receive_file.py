import socket


def main():
    """Receive a file from a server using TCP socket."""
    host = socket.gethostname()
    port = 12312
    filename = "received_file.txt"

    print(f"Connecting to server at {host}:{port}...")

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            print("Connected to server ✅")
            sock.sendall(b"Hello server!")

            with open(filename, "wb") as out_file:
                print(f"Receiving data and saving to '{filename}'...")
                total_bytes = 0
                while True:
                    data = sock.recv(1024)
                    if not data:
                        break
                    out_file.write(data)
                    total_bytes += len(data)

            print(f"✅ Successfully received the file ({total_bytes} bytes)")
    except ConnectionRefusedError:
        print("❌ Connection failed: server not running or port closed.")
    except OSError as e:
        print(f"❌ OS error occurred: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
    finally:
        print("Connection closed.")


if __name__ == "__main__":
    main()
