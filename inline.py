#########################
######## Imports ########
#########################

import datetime
import os

#########################
### Helper Functions ####
#########################

def fetch():
    '''
    Get input from user via Vi
    '''
    content = open("input", 'w+')
    os.system('vim ' + os.path.realpath("input"))

def populate():
    '''
    Save user input into LaTeX document
    '''
    os.system("cp " + os.path.realpath("template.tex") + " " + os.path.realpath("inline.tex"))
    content  = open("input", 'r').read()
    skeleton = open("inline.tex", 'r')
    document = skeleton.read().replace('[[placeholder]]', content)
    skeleton.close()
    skeleton = open("inline.tex", 'w+')
    skeleton.write(document)
    skeleton.close()

def render():
    '''
    Compile .tex file to .png
    '''
    # .tex to .dvi
    print("Rendering LaTeX...")
    os.system("latex inline.tex >> /dev/null")
    # .dvi to .png
    print("Converting to PNG...")
    os.system("dvipng inline.dvi -D 8192 -bg 'rgb 1 1 1' -q >> /dev/null")

def save():
    '''
    Save .png to Desktop
    '''
    # Moving to desktop
    print("Moving to desktop...")
    os.system("mv " + os.path.realpath("inline1.png") + " ~/Desktop/" + datetime.datetime.now().isoformat() + ".png")

def clean():
    '''
    Remove compile-time files
    '''
    os.remove(os.path.realpath("inline.tex"))
    os.remove(os.path.realpath("inline.dvi"))
    os.remove(os.path.realpath("inline.aux"))
    os.remove(os.path.realpath("inline.log"))

#########################
##### Main Function #####
#########################

def main():
    fetch()
    populate()
    render()
    save()
    clean()

if __name__ == '__main__':
    main()
