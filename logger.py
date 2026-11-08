import logging
from pathlib import Path


# Logbestand aanmaken in de projectmap
LOG_DIR = Path(__file__).resolve().parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "wine_explorer.log"


# Centrale logging configuratie
logger = logging.getLogger("wine_explorer")
logger.setLevel(logging.WARNING)

if not logger.handlers:
    file_handler = logging.FileHandler(
        LOG_FILE,
        encoding="utf-8"
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.propagate = False


def get_logger(module_name: str) -> logging.Logger:
    """
    Geeft een logger terug voor de opgegeven module.

    :param module_name: Naam van de module die logging gebruikt.
    :type module_name: str
    :return: Logger voor de betreffende module.
    :rtype: logging.Logger
    """
    return logging.getLogger(f"wine_explorer.{module_name}")