import time
import datetime
from git import Git

buffer_size = 0
g = Git('./home/chad/Repos/GTClash-Collector-Sim')
with open('/home/chad/Repos/GTClash-Collector-Sim/output.log', 'a', buffering=1) as f:
    while True:
        f.write(f'{datetime.datetime.now()}\n')
        f.write(f'  - v{g.describe()}\n')
        time.sleep(2)

