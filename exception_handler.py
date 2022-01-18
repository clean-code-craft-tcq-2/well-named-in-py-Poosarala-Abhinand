# This file contains methods for checking exceptions

def check_for_index_exception(index, constant):
  if index >= len(constant):
    raise Exception('Index out of range: ',index)
