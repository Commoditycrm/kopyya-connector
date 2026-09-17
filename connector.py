# PyInstaller entry point. __main__.py can't be frozen directly: its relative
# import has no parent package when run as a top-level script.
from kopyya_connector.app import main

if __name__ == "__main__":
    main()
