from subprocess import Popen, PIPE


# process = Popen(['python', 'process_file.py', '--i1=0', '--i2=10'], stdout=PIPE, stderr=PIPE)
# stdout, stderr = process.communicate()
# print(stdout)

import argparse
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--start', type=int)
parser.add_argument('--sz-range', default=1000, type=int)
parser.add_argument('--nb-runs', default=10, type=int)
args = parser.parse_args()

from subprocess import Popen
command = ['python', 'process_file.py', '--i1=0', '--i2=50']
commands = [command] * 1
commands = []
nb_runs = args.nb_runs
sz_range = args.sz_range
for i in range(nb_runs):
    i1 = args.start + (i + 0) * sz_range
    i2 = args.start + (i + 1) * sz_range
    commands.append([
        'python', 
        'process_file.py', 
        '--i1={}'.format(i1), 
        '--i2={}'.format(i2)
    ])

print(commands)

procs = [ Popen(i) for i in commands ]
for p in procs:
   p.wait()
