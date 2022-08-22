import os,sys



Demon = """
cd $HOME
cd DARK-FB
mv data $HOME
mv results $HOME
cd
rm -rf DARK-FB
git clone https://github.com/CyberDemon404/DARK-FB
cd $HOME
mv data DARK-FB
mv results DARK-FB
cd DARK-FB
"""

print(" |-->Under maintenance bro....")
os.system(Demon)
print(' |')
print(' |')
print(' |-->Updating please wait ...')
print(' |-->Run again : python main.py')
os.sys.exit()

