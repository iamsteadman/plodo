import yaml
import os


def get_config(ctx):
    cwd = os.getcwd()
    filename = os.path.join(cwd, 'plodo.conf')
    if not os.path.exists(filename):
        ctx.fail('Config file not found.')

    try:
        return yaml.load(open(filename, 'r'))
    except yaml.YAMLError:
        ctx.fail('Config file invalid.')

    if not isinstance(options, dict):
        ctx.fail('Config file invalid.')


def get_rack(ctx, config, name):
    rack = config.get('racks', {}).get(name)
    if rack is None:
        ctx.fail('Rack "%s" could not be found' % name)

    return rack
