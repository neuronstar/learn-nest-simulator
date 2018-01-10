import sys
import nest
import matplotlib.pyplot as plt
import numpy as np

#vth = float( (sys.argv)[1] )
vth=15.0

freq_curr = []
curr = []




for ext_curr in np.arange(300, 1000, 10):
   neuron_exp = nest.Create("iaf_psc_exp")

   multimeter = nest.Create("multimeter", params={"withtime":True, "record_from":["V_m"]})
   spikedetector = nest.Create("spike_detector", params={"withgid":True,"withtime":True })
   nest.SetStatus( neuron_exp, {"V_m":0.0, "V_reset":0.0, "E_L":0.0,  "V_th":vth ,"C_m": 250.0, "tau_m":10.0,"I_e": float(ext_curr)})
   nest.Connect(multimeter, neuron_exp)
   nest.Connect(neuron_exp, spikedetector)

   nest.Simulate(1000)

   t_exp = nest.GetStatus(multimeter)[0]["events"]["times"][::]
   vm_exp = nest.GetStatus(multimeter)[0]["events"]["V_m"][::]
   spiketime = nest.GetStatus(spikedetector,keys="events")[0]["times"]

   freq_curr.append( len(spiketime)/1000.0 )
   curr.append( ext_curr )

   nest.ResetNetwork()


print(freq_curr)



plt.plot( curr , freq_curr, label="Exp")
plt.title(" $V_{th}$: "+str(vth) ) 
plt.xlabel("$I_e$")
plt.ylabel("$f$")
plt.legend()
plt.show()
