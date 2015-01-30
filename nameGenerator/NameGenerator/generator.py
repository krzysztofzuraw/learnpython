import random

          
def generate_name(filename):
    names = []
    with open(filename) as name_file:
        for line in name_file.read().split('   '):
            names.append(line)
            
    return (random.choice(names))                        
