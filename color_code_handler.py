# This file contains methods to retrieve information about color and pair number
from constants import MAJOR_COLORS, MINOR_COLORS

def get_color_from_pair_number(pair_number):
  zero_based_pair_number = pair_number - 1
  major_index = zero_based_pair_number // len(MINOR_COLORS)
  exception_handler.check_for_index_exception(major_index,MAJOR_COLORS)
  minor_index = zero_based_pair_number % len(MINOR_COLORS)
  exception_handler.check_for_index_exception(minor_index,MINOR_COLORS)  
  return MAJOR_COLORS[major_index], MINOR_COLORS[minor_index]

def get_pair_number_from_color(major_color, minor_color):
  try:
    major_index = MAJOR_COLORS.index(major_color)
  except ValueError:
    raise Exception('Major index out of range')
  try:
    minor_index = MINOR_COLORS.index(minor_color)
  except ValueError:
    raise Exception('Minor index out of range')
  return major_index * len(MINOR_COLORS) + minor_index + 1
