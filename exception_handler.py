def check_for_exception(index, constant):
  if index >= len(constant):
    raise Exception('Index out of range: ',index)