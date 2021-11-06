import os

def play_sound(numbers = '0', conditions = 'new', exceptions = 'none'):
    
    if exceptions == 'not_found':
        file_exceptions = '/home/rory/Inventory-Management-main/audio-numbers/{}.mp3'.format(exceptions)
        os.system('mpg123 -q ' + file_exceptions)
    else:
        if conditions == 'new':
            file_numbers = '/home/rory/Inventory-Management-main/audio-numbers/{}.mp3 '.format(numbers)
            file_conditions = '/home/rory/Inventory-Management-main/audio-numbers/{}.mp3'.format(conditions)
            os.system('mpg123 -q ' + file_numbers + file_conditions)
        else:
            file_numbers = '/home/rory/Inventory-Management-main/audio-numbers/{}.mp3 '.format(numbers)
            file_conditions = '/home/rory/Inventory-Management-main/audio-numbers/{}.mp3'.format('used')
            os.system('mpg123 -q ' + file_numbers + file_conditions)