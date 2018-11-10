"""Main entry point for radiomanager"""

import radiomanager.api

if __name__ == "__main__":
    app = radiomanager.api.Application()
    app.run()