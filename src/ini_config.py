"""Load configuration from .ini file."""
import configparser

import os

config = configparser.ConfigParser()
if os.environ.get("data_dir") is None:
    filename = 'settings/config.ini'
else:
    filename = os.path.join(os.environ.get("data_dir"), 'config.ini')

config.read(filename)

settings__enable_mqtt = config.getboolean('settings', 'enable_mqtt', fallback=False)
settings__enable_serial_driver = config.getboolean('settings', 'enable_serial_driver', fallback=True)


mqtt__host = config.get('mqtt', 'host', fallback='0.0.0.0')
mqtt__port = config.getint('mqtt', 'port', fallback=1883)
mqtt__keepalive = config.getint('mqtt', 'keepalive', fallback=60)
mqtt__qos = config.getint('mqtt', 'qos', fallback=1)
mqtt__retain = config.getboolean('mqtt', 'retain', fallback=False)
mqtt__attempt_reconnect_on_unavailable = config.getboolean('mqtt', 'attempt_reconnect_on_unavailable', fallback=True)
mqtt__attempt_reconnect_secs = config.getint('mqtt', 'attempt_reconnect_secs', fallback=5)
mqtt__topic = config.get('mqtt', 'topic', fallback='lora_raw')
mqtt__debug = config.getboolean('mqtt', 'debug', fallback=False)
mqtt__debug_topic = config.get('mqtt', 'debug_topic', fallback='debug_lora_raw')
