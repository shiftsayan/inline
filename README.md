# Inline

Easily generate images of your LaTeX equations for your non-LaTeX documents and presentations!

Inline is a Python script that allows you to input a few lines of LaTeX and render a standalone PNG from it, that you can insert into other applications such as Google Docs and Sheets. This can be extremely useful if you are making a poster or a large document with a few mathematical equations, but you would still prefer the versatility of a word processor.

Though you interact with Inline via a Python script, it does most of the heavy lifting via shell commands run using `os.system`. The rendered image is saved to your desktop and copied to your clipboard.

### Dependancies
* `python` and a couple packages part of the Python Standard Library
* `LaTeX` for compiling
* `dvipng` for conversion to PNG
* `osascript` for copying the resulting PNG to the clipboard

I believe macOS comes with installations of `dvipng` and `osascript`, so you'll only need to install `LaTeX`. `brew cask install mactex` should do the trick.

### Use
* Run `python inline.py`.
* Input your LaTeX source into the `vim`
* That's it!

The rendered image is saved to your desktop and copied to your clipboard.
