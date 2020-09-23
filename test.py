def is_divide_by(number, a, b):
  temp = number % a;
  if (temp != 0):
    return False;
  temp = number % b;
  if (temp != 0):
    return False;
  return True;