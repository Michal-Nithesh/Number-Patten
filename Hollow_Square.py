def hollow_square(rows):
  for i in range(rows):
    if i == 0 or i == rows -1:
      print("*" * rows)
    else:
      print("*" + " " * (rows -2) + "*")

hollow_square(5)
