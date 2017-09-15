#!/usr/bin/env python3
import sys
import registry_authz.webserver.routing


def main(args):
    """
        Main thing to run
    """
    print("Hi! This does nothing")
    registry_authz.webserver.routing.run()

def run():
    """Entry point for console_scripts
    """
    main(sys.argv[1:])


if __name__ == '__main__':
    run()
