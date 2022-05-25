import os

def get_server_root_path():
	return os.path.dirname(os.path.abspath(__file__))


SERVER_ROOT_PATH = get_server_root_path()