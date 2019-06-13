import sys

if __name__ == "__main__":
    attendees = ' '.join(sys.argv[1:]) or "world"
    print("Hello, {}!".format(attendees) )


