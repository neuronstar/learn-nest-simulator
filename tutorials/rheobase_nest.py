import sys
import nest
import matplotlib.pyplot as plt

[ext_curr, vth] =[ float( (sys.argv)[1] ), float( (sys.argv)[2] )]




neuron_exp = nest.Create("iaf_psc_exp")
nest.SetStatus( neuron_exp, {"V_m":0.0, "V_reset":0.0, "E_L":0.0,  "V_th":vth ,"C_m": 250.0, "tau_m":10.0,"I_e":ext_curr})

print( nest.GetStatus(neuron_exp) )

multimeter = nest.Create("multimeter", params={"withtime":True, "record_from":["V_m"]})


nest.Connect(multimeter, neuron_exp)

nest.Simulate(1000)

t_exp = nest.GetStatus(multimeter)[0]["events"]["times"][::2]
vm_exp = nest.GetStatus(multimeter)[0]["events"]["V_m"][::2]

plt.plot(t_exp, vm_exp, label="Exp")
plt.title("$I_e$: "+ str(ext_curr)+" $V_{th}$: "+str(vth) ) 
plt.ylim([-1,70])
plt.xlabel("$t$")
plt.ylabel("$V_m$")
plt.legend()
plt.show()
