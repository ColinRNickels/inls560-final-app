# Ideas for text-based final project interfaces.
# You'll need a menu of some sort, controlled by a main loop.
# These examples show the beginning of how you could do this.

# You can use triple quotes to render newlines intuitively.
options = """1 - Main Menu
2 - Option 2
3 - Option C"""

# This is a simple example of what an option function might look like
def option2():
  print("This is option 2")
  input("Press enter...")

# The variable for our while loop  
going = True

while going:
  print(options)
  choice = input("what is your choice? ")
  if choice == "2":
    option2()
  elif choice == "exit":
    going = False
    
# This only happens if you exit.
print("Goodbye.")
