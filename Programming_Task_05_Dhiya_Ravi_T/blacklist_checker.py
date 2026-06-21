def main():
    blacklisted_ips = ["192.168.1.10", "10.0.0.5", "172.16.1.100", "192.168.0.50"]

    print("=== Blacklisted IP Checker ===")
    print("Blacklisted IPs:", blacklisted_ips)

    user_ip = input("\nEnter an IP Address to check: ").strip()

    if user_ip in blacklisted_ips:
        print("IP Found in Blacklist")
    else:
        print("IP Not Found")


if __name__ == "__main__":
    main()