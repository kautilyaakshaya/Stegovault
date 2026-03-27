import logging

logging.basicConfig(
    filename="stegovault.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s"
)

def log(msg):
    logging.info(msg)