#import reweight object
from reweight import Reweight
#load the configure file as dict
config_file = "./config.json"
phenol = Reweight(config_file)
phenol.run()
