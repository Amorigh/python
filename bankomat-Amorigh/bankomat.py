#!/usr/bin/env python3
from sys import stdout, stderr

############################################################################
while True:
    try:
        line = input("bankomat>> ")
        amount = int(line)
        main(amount)
    except EOFError:
        exit(0)
    except KeyboardInterrupt:
        stderr.write("Program byl přerušen z klávecnice.")
        exit(1)
    except ValueError:
        stdout.write("ERROR\n")



class Bankomat():
    TREZORFILE = "trezor.txt"
    trezor = {}
    
    def read():
        with open(self.TREZORFILE, 'r') as f:
            while line := f.readline():
                bill, count = line.split()
                self.trezor[int(bill)] = int(count)

    def write():
        pass

    def make(amount):
        return 0


if __name__ == "__main__":
    exit(main())
