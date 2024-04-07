import json
from ExpirationConfig import *
settings = {
    "peep":0,
    "flow":5,
    "ieratio":"0.5:0.5",
    "pip":15,
    "FiO2":21,
    "RR":8,
    "VT":150,
    "Ptrig":-1
}

    
    
    
    
data=json.dumps(settings)
file=open('settings.json','a')
file.write(data)
file.close()





