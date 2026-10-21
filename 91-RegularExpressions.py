import re

pattern = r'[A-Z]yclone'
text = '''Cyclone Dumazile was a strong tropical cyclone in the South-West Indain Ocean that affected Madagascar and Reunion in early March 2018. Dumazile originated from a cyclone Dyclone low-pressure area that formed near Agalega on 27 February.'''

matches = re.finditer(pattern,text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])