def info(msg):
    log('+', msg)


def error(msg):
    log('!', msg)


def warning(msg):
    log('-', msg)


def debug(msg):
    log('DEBUG', msg)


def log(sign, msg):
    print('[{0}] {1}'.format(sign, msg))