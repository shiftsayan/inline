#########################
######## Imports ########
#########################

import os

#########################
### Helper Functions ####
#########################

def fetch():
    '''
    Get input from user via Vi
    '''
    os.system('vim ' + os.path.realpath("input"))

def populate():
    '''
    Save user input into LaTeX document
    '''
    content  = open("input", 'r').read()
    skeleton = open("template.tex", 'r')
    document = skeleton.read().replace('[[placeholder]]', content)
    skeleton.close()
    skeleton = open("template.tex", 'w+')
    skeleton.write(document)
    skeleton.close()

def render():
    return

def save():
    return

def restore():
    '''
    Restore input and template to original states
    '''
    content = open("input", 'w+')
    content.write("")
    os.remove(os.path.realpath("template.tex"))
    os.system("cp " + os.path.realpath("template_backup.tex") + " " + os.path.realpath("template.tex"))

#########################
##### Main Function #####
#########################

def main():
    fetch()
    populate()
    # render()
    # save()
    restore()

if __name__ == '__main__':
    main()
