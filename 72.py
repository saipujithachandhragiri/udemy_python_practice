# Create a script that let the user type in a search term and then the program opens the browser and searches the term on Google.

import webbrowser

search = input('Search:')
webbrowser.open('https://google.com/search?q=%s'%search)