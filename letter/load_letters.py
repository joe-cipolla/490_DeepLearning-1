from .Letter import Letter

def load_letters(letters_to_load=['all'], size=81, use_variants=0):
    """ Load all letters of given size (25, 81, etc)
    :param letters_to_load:
    :param size: number of pixels in letter image
    :param use_variants: boolean indicating to include variant letters or not
    :return: number of unique letters and a list of Letter objects
    """
    from os import listdir
    from os.path import dirname
    basedir = dirname('/Users/joecipolla/Documents/Reference/Education/490-Deep_Learning/letter_mgmt')

    if size == 25:
        alpha_dir = basedir + '/5x5_alphabet/'
    elif size == 81:
        alpha_dir = basedir + '/9x9_alphabet/'

    if letters_to_load[0] == 'all':
        letters_to_load = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
                           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    letters = [f for f in listdir(alpha_dir) if f[0] != '.']
    letter_objects = []

    for letter in letters:
        if letter in letters_to_load:
            letter_dir = alpha_dir + letter + '/'
            for instance in [f for f in listdir(letter_dir)]:
                first_instance = str(letter) + "_0.letter"
                if (use_variants == 0) and (str(instance) != first_instance):
                    pass
                else:
                    instance_array = []
                    with open(letter_dir + instance) as f:
                        for line in f:
                            if '#' not in line:
                                instance_array.extend(line.replace(' ', '').replace(',', '').replace('\n', ''))
                    letter_objects.append(Letter([int(x) for x in instance_array], letter))

    return len(letters_to_load), letter_objects
