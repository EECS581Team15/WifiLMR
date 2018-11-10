"""Main entry point for radiomanager"""

import radiomanager

if __name__ == "__main__":
    radiomanager.app.run("0.0.0.0", 8000, debug=True)