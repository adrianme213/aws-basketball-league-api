import logging


def create_logger_with_filename(filename, logging_level=logging.INFO):
    """
    Create a logger instance using filename, logging level set at logging.INFO by default.
    :param filename: string - filename for the logger creation
    :return: logger: object - logger instance
    """
    # Create Logger
    logger: logging.Logger = logging.getLogger(filename)
    logger.setLevel(logging_level)

    # Console Handler
    ch: logging.StreamHandler = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch_format: logging.StrFormatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(ch_format)

    # Add Console Handler to Logger
    logger.addHandler(ch)

    return logger
