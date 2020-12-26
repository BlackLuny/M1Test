import os
from time import strftime, localtime
repo = r'/data/llvm/llvm-project'
compileCmd = r'cd '+  repo + r' && mkdir build && cd build && cmake -DLLVM_ENABLE_PROJECTS=clang -G "Unix Makefiles" ../llvm && make -j'
cleamCmd = r'cd '+  repo + r' && rm -rf build'

for x in range(1, 9):
    with open("log.txt", "a") as f:
        os.system(cleamCmd)
        tmpCmd = compileCmd + str(x)
        f.write("Start compile using " + str(x) + " threads:\n")
        f.write("Start time: " + strftime("%Y-%m-%d %H:%M:%S", localtime()) + "\n")
        os.system(tmpCmd)
        f.write("End time: " + strftime("%Y-%m-%d %H:%M:%S", localtime()) + "\n\n")
