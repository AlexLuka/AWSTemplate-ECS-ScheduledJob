import os
import sys
import logging

from time import time, sleep


def init_logger(source, level=logging.DEBUG):
    logger = logging.getLogger(source)
    logger.setLevel(level)

    logger_handler = logging.StreamHandler(sys.stdout)
    logger_handler.setLevel(level)

    logger_formatter = logging.Formatter("[%(asctime)s][%(name)s][%(levelname)s] %(message)s")
    logger_handler.setFormatter(logger_formatter)

    logger.addHandler(logger_handler)
    return logger


def main():
    logger = init_logger(__name__, level=logging.DEBUG)
    logger.info(f"Starting the main application")
    logger.info(f"Code version: https://github.com/AlexLuka/AWSTemplate-ECS-ScheduledJob/tree/"
                f"{os.environ.get('GITHUB_SHA', 'GITHUB_SHA_NOT_FOUND')}")

    n = 0
    n_max = 60
    delay_sec = 1

    t = time()
    while n < n_max:
        sleep(delay_sec)
        n += delay_sec

    t = time() - t
    logger.info(f"Application took {t:.3f} seconds to complete")
    logger.info(f"Application supposed to run for {n_max:.3f} seconds")
    logger.info(f"Delta: {t - n_max:.3f}")


if __name__ == "__main__":
    main()
