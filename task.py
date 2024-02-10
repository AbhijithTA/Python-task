def print_custom_pattern():

  num_rows = int(input("Enter the number of rows: "))
  num_columns = int(input("Enter the number of columns: "))

  columns=(num_columns//2)+1

  print(" ___" + "     ___" * (columns - 1))
  
  for _ in range(num_rows):
      print("/   " + "\___/   " * (columns - 1) + "\\")
      print("\\___/   " * (columns))



print_custom_pattern()