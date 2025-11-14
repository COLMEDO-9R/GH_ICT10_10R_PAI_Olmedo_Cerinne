# Students Club
from pyscript import display

Art_Club = {'Amanda Yao', 'Shalanie Garabiles', 'Vada Agena'}
COCC = {'Aisha Ledesma', 'Koby Baylon', 'Maryam Ledesma'}

display('Art Club Members:', target='output')
display(Art_Club, target='output')

display('COCC Members:', target='output')
display(COCC, target='output')

display('(At least one club):', target='output')
display(Art_Club | COCC, target="output")

display('(Both clubs):', target='output')
display(Art_Club & COCC, target='output')

display('Only in Art Club:', target='output')
display(Art_Club - COCC, target='output')

display('Only in COCC:', target='output')
display(COCC - Art_Club, target='output')

display('Exactly One Club:', target='output')
display(Art_Club ^ COCC, target='output')


