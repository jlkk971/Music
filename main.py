'''
Scope of this class is to assess the following tasks:

-calculate major and minor chords starting from each note
-calculate mixolidian and lidian equivalents of the C major scale
'''

import itertools
import numpy as np

def chords(root_note, type):

    note=['Do','Do#','Re','Re#','Mi','Fa','Fa#','Sol','Sol#','La','La#','Si']

    cycle=itertools.cycle(note)

    chord=[]
    third=0
    chord.append(root_note)
    counter=0

    if type=='major':
        third=4
    elif type=='minor':
        third=3
    else:
        raise NameError('should be major or minor')

    for elem in cycle:
        if elem==root_note:
            for item in cycle:
                counter=counter+1 
                if counter==third:           
                    chord.append(item)
                if counter==7:
                    chord.append(item)
                elif counter>7:
                    break
        elif len(chord)==3:
            break

    print(chord)
                
def scale(root_note, type=None):

    note=['Do','Do#','Re','Re#','Mi','Fa','Fa#','Sol','Sol#','La','La#','Si']

    cycle=itertools.cycle(note)

    chord=[]
    chord.append(root_note)
    counter=0

    major_scale_natural=[2,2,1,2,2,2,1]
    major_scale_natural=list(np.cumsum(major_scale_natural))


    major_scale_misolidian=[2,2,1,2,2,1,2]
    major_scale_misolidian=list(np.cumsum(major_scale_misolidian))

    print(major_scale_natural)

    for elem in cycle:
        if elem==root_note:
            for item in cycle:
                counter=counter+1  
                for i in major_scale_misolidian:
                    if counter==i:
                        chord.append(item)
                        break
                if counter>12:
                    break
        elif len(chord)==8:
            break

    print(chord)

print('changes made')

a=chords('Do','major')
b=scale('Sol')