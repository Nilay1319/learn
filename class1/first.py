# This program is to add two integers. Keep asking the user for inputs
# until user has entered correct integers. 
redo=1  # This is the variable which will keep track of valid integers
while(redo):
    redo=0  #first assumption is that user will enter integers only
    no1=input('Enter No 1:')
    no2=input('Enter No 2:')
    try:
      no1=int(no1)
    except ValueError:
      redo=1  # Since no1 was entered incorrectly, enable redo flag
    try:
      no2=int(no2)
    except ValueError:
      redo=1  # Since no2 was entered incorrectly, enable redo flag
    if(redo):
      # Don't exit the while loop, redo again and ask user for numbers
      print('Please enter correct integers')
    else:
      # Everything looks ok, do the addition and exit      
      redo=0
      mysum=no1+no2
      print('sum is: ',mysum)
