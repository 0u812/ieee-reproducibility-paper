import tellurium as te

# Using roadrunner develop branch, commit f913e5818acc63337ed825b771f2f04fa3ee5c10

r = te.loada('''
       -> x; 0.5 + vmax*x^n \
             / (10^6 + x^n)
   x   ->  ; k*x

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
r.showPlot()
