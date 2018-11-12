"""Main entry point for radiomanager"""

import sys
import argparse
import radiomanager

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug",
                        action="store_const",
                        const=True,
                        default=False,
                        dest="debug")
    parser.add_argument("--run-tests",
                        action="store_const",
                        const=True,
                        default=False,
                        dest="test")
    args = parser.parse_args(sys.argv[1:])
    if args.test:
        import unittest
        from radiomanager.tests.handshaking import TestPing, TestProvision
        unittest.main(argv=["app.py", "-v"])
    else:
        app = radiomanager.init_app()
        for rule in app.url_map.iter_rules():
            print(rule)
        app.run("0.0.0.0", 8000, debug=args.debug)
