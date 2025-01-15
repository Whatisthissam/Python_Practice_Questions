import logging

logging.basicConfig(filename="example.log", level=logging.DEBUG)

logging.info("This is an info message.")
logging.error("This is an error message.")

print("Log messages have been written to 'example.log'.")
