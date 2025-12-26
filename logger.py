import logging
#from logging.handlers import RotatingFileHandler

def get_logger(name: str):
    logger = logging.getLogger(name)

    if not logger.handlers:  # Prevent adding multiple handlers
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        stream_handler = logging.StreamHandler()  # Logs to stdout
        # file_handler = RotatingFileHandler(
        #     mode="a",
        #     filename="logs/" + name + ".log",
        #     maxBytes=1024*1024*50,
        #     backupCount=5
        # )
        #file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        logger.addHandler(stream_handler)
        #logger.addHandler(file_handler)

    return logger