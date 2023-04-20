import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Regular expression to match an IPv4 address
    ipv4_regex = r"^([01]?\d{1,2}|2[0-4]\d|25[0-5])\.([01]?\d{1,2}|2[0-4]\d|25[0-5])\.([01]?\d{1,2}|2[0-4]\d|25[0-5])\.([01]?\d{1,2}|2[0-4]\d|25[0-5])$"
    if re.search(ipv4_regex, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
