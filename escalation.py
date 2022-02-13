import argparse


parser = argparse.ArgumentParser(description='Scan the machine for possible privilege escalation attacks')
parser.add_argument('-d', '--directory', help='Directories separated with "," where modules are stored', required=False)
parser.add_argument('-o', '--output', help='Output directory where output is stored', required=False)
args = parser.parse_args()

output = '.'
directory_modules = './modules/'


def show_banner():
    print("""
 ______               _       _   _                                 
|  ____|             | |     | | (_)            
| |__   ___  ___ __ _| | __ _| |_ _  ___  _ __  
|  __| / __|/ __/ _` | |/ _` | __| |/ _ \| '_ \ 
| |____\__ \ (_| (_| | | (_| | |_| | (_) | | | |
|______|___/\___\__,_|_|\__,_|\__|_|\___/|_| |_| 
""" ,end='')

show_banner()


