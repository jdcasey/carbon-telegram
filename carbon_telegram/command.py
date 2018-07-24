import os.path
import sys
import click
import carbon_telegram.config
import carbon_telegram.network

@click.command()
@click.option('--config', '-c', help='Alternative config YAML')
def recv(config):
    cfg = carbon_telegram.config.load(config)

@click.command()
@click.argument('metric_name')
@click.argument('metric_value')
@click.argument('metric_time_seconds')
@click.option('--config', '-c', help='Alternative config YAML')
def send(args, config, session, delete_log=None, debug=False):
    config = config.load()
