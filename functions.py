FILEPATH = 'todos.txt'
def get_todos(filepath=FILEPATH):
	"""Open a file and read todos"""
	with open(filepath, 'r') as file_local:
		todos_local = file_local.readlines()
	return todos_local


def write_todos(todos_to_write, filepath=FILEPATH):
	"""Writes to-do list in a file"""
	with open(filepath, 'w') as fw:
		fw.writelines(todos_to_write)
