import logging
import coloredlogs

logger = logging.getLogger(__name__)  # get a specific logger object
coloredlogs.install(level='DEBUG')  # install a handler on the root logger with level debug
coloredlogs.install(level='DEBUG', logger=logger)  # pass a specific logger object
coloredlogs.install(
    level='DEBUG', logger=logger,
    fmt='%(asctime)s.%(msecs)03d %(filename)s:%(lineno)d %(levelname)s | msg: "%(message)s"'
)

if __name__ == '__main__':
    logger.debug('its OK')