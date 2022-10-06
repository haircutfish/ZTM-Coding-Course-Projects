from functools import reduce

#1 Capitalize all of the pet names and print the list
def caps(item):
    return item.title()

my_pets = ['sisi', 'bibi', 'titi', 'carla']

print(list(map(caps,my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
sorted_list = []

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

my_numbers.sort()

print(list(zip(my_strings,my_numbers)))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def over_fifty(item):
    return item > 50

print(list(filter(over_fifty, scores)))


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def combine(com, num):
    # print(com, num)
    return com + num

print(reduce(combine,my_numbers + scores,0)) #456



                /\                                  /\              
               |  \                                /  |                  
               |    \            / \             /    |          
               |     \      /\  /   \  / \      /     |           
               |       \ ^ /  \/     \/   \ ^ /       | 
               |                                      |      
               /                                       \                
              /            \                /           \             
             /            | \              / |           \        
            /             |  \            /  |            \           
           /              |  @\          /@  |             \          
          /               |    \        /    |              \        
         /                 \___/        \___/                \       
        /                                                     \            
       /               |\______________________/|              \         
      /      \         |   |   |   |   |   |    |        /\     \        
     /      / \        |   |   |   |   |   |    |       /  \     \    
    /      /   \       |   |   |   |   |   |    |      /    \     \      
   /      /     \       \  |   |   |   |   |   /      /      \     \     
  /      \       \       \_|___|___|___|___|__/      /       /      \  
   \/\/\/        /\                                 /\        \/\/\/  
                /  \                               /  \               
               |                                       |       
               |         \____________________/        |      
                \          |              |          /       
                <_________/                \_________> 
