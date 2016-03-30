import tellurium as te

# roadrunner version:
# 1.4.3; Compiler: clang "6.0 (clang-600.0.56)", C++ version: 199711; JIT Compiler: LLVM-3.5; Date: Feb 24 2016, 10:47:54; LibSBML Version: 5.11.0

r = te.loada('''
   J0:     -> x; 0.5 + vmax*x^n \
             / (10^6 + x^n)
   J1: x   ->  ; k*x

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
plt.show()
