from commitSync import *

counter=0

if __name__ == "__main__":
    while True:
        ++counter
        gitSync()
        print("\n Number of commits done : {}".format(counter))

