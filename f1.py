 print("Hello world")
def palindrome(x):
  y=str(x)
  if str(x)==y[::-1]:
    print(x," is palindrome.")
  else:
    print(x," is not palindrome")
palindrome(12321)
