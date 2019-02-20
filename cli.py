#!/usr/bin/env python
import optparse

def main():
    p = optparse.OptionParser()
    p.add_option('--person', '-p', default="world")
    p.add_option('--message', '-M', default="Hello")
    options, arguments = p.parse_args()
    print(options.message, options.person)

if __name__ == '__main__':
    main()
