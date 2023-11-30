def main():
    inp: str = input("IPv4 Address: ").strip()
    print(validate(inp))

def validate(ip: str):
    try:
        split_ip: list[str] = ip.split(".")

        if len(split_ip) < 4 or len(split_ip) > 4:
            return False

        for s in split_ip:
            if int(s) > 255:
                return False

    except ValueError:
        return False
    return True

if __name__ == "__main__":
    main()