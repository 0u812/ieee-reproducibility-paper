# Python 2.7.10
# Figure 2 source from Medley, Goldberg, and Karr: Guidelines for reproducibly building and simulating systems biology models
# Author: J Kyle Medley
# Uses Tellurium for Mac OS X 10.10
# Download: https://sourceforge.net/projects/pytellurium/files/Tellurium-1.3/1.3.3/Tellurium-1.3.3-Spyder-2.3.8-OSX.dmg/download


import tellurium as te

# roadrunner version:
# 1.4.4; Compiler: clang "3.7.0 (tags/RELEASE_370/final)", C++ version: 199711; JIT Compiler: LLVM-3.5; Date: May  9 2016, 11:38:08; LibSBML Version: 5.12.0

r = te.loada('''
   v1:     -> x; 0.5 + vmax*x^n \
             / (10^6 + x^n)
   v2: x   ->  ; k*x

   x = 24
   n = 4
   vmax = 10
   k = 0.125
''')

r.setIntegrator('gillespie')
r.getIntegrator().setValue('seed', 100)

results = []
for k in range(50):
  r.reset()
  p = r.simulate(0,30)
  results.append(p)
  r.plot(p, show=False, loc=None, color='black', alpha=0.5)
import matplotlib.pyplot as plt
plt.xlabel('time $(s)$')
plt.ylabel('$x$ $(\mu \mathrm{M})$')
plt.show()
