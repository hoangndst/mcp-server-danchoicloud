from .server import serve
import asyncio

def main():
    """
    Main function to run the server.
    """
    asyncio.run(server.serve())

if __name__ == "__main__":
    main()
