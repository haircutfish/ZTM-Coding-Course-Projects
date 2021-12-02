from functools import reduce

# 1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


def caps(item):
    return item.upper()

print(list(map(caps, my_pets)))

# 2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5, 4, 3, 2, 1]

new_numbers = sorted(my_numbers, reverse=False)

print(list(zip(my_strings, new_numbers)))
# 3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


def above_ave(item):
    return item > 50


print(list(filter(above_ave, scores)))


# 4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

new_list = list(set(my_numbers + scores))

def accumulator(acc, item):
    print(acc , item)
    return acc + item

print(reduce(accumulator, new_list, 0)) #456



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
