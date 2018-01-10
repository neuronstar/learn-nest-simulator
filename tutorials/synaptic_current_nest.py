import sys
import nest
import matplotlib.pyplot as plt
import numpy as np

#vth = float( (sys.argv)[1] )
vth=15.0

freq = []
re_arr = []



for re in np.arange(100, 300, 10):
   neuron_exp = nest.Create("iaf_psc_exp")

   poisson_sti = nest.Create( "poisson_generator", params={"rate": 15000.})
   poisson_sti_ih = nest.Create( "poisson_generator", params={"rate": 15000.})
   
   multimeter = nest.Create("multimeter", params={"withtime":True, "record_from":["V_m"]})
   spikedetector = nest.Create("spike_detector", params={"withgid":True,"withtime":True })
   nest.SetStatus( neuron_exp, {"V_m":0.0, "V_reset":0.0, "E_L":0.0,  "V_th":vth ,"C_m": 250.0, "tau_m":10.0,"I_e": 374.0})

   nest.Connect(poisson_sti, neuron_exp, syn_spec={"weight":float(re)})
   nest.Connect(poisson_sti_ih, neuron_exp, syn_spec={"weight":float(re)})
   nest.Connect(neuron_exp, spikedetector)

   nest.Simulate(1000)

   t_exp = nest.GetStatus(multimeter)[0]["events"]["times"][::]
   vm_exp = nest.GetStatus(multimeter)[0]["events"]["V_m"][::]
   spiketime = nest.GetStatus(spikedetector,keys="events")[0]["times"]

   freq.append( len(spiketime)/1000.0 )
   re_arr.append( re )

   nest.ResetNetwork()


print(freq)



plt.plot( re_arr , freq, '.k', label="Exp")
plt.title(" $V_{th}$: "+str(vth) ) 
plt.xlabel("$I_e$")
plt.ylabel("$f$")
plt.legend()
plt.show()
