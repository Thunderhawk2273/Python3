#A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using pip package manager(or Anaconda) as well as custom modules

import datetime
from datetime import date
import time
from time import time


#Today = datetime.date.today()
today = date.today()
timestamp = time()


print(timestamp)