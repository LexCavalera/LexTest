import os


TEMPLATES_PATH = os.sep.join([os.environ['PRODROOT'], 'site', 'templates'])


def get_template_path(template_filename):
    return os.sep.join([TEMPLATES_PATH, template_filename])
