import sys
import nest
import matplotlib.pyplot as plt

ext_curr =float( (sys.argv)[1] )

neuron_cond_exp = nest.Create("iaf_cond_exp")
neuron_exp = nest.Create("iaf_psc_exp")

# spg = nest.Create("spike_generator", params={"spike_times":[200.0, 500.0], "spike_weights":[w, 2*w]})

multimeter = nest.Create("multimeter", params={"withtime":True, "record_from":["V_m"]})


nest.SetStatus(neuron_cond_exp, {"I_e": ext_curr})

#nest.Connect(spg,neuron_alpha)
#nest.Connect(spg,neuron_exp)
nest.Connect(multimeter, neuron_cond_exp)
nest.Connect(multimeter, neuron_exp)

nest.Simulate(1000)

t_cond_exp = nest.GetStatus(multimeter)[0]["events"]["times"][::2]
t_exp = nest.GetStatus(multimeter)[0]["events"]["times"][1::2]
vm_cond_exp = nest.GetStatus(multimeter)[0]["events"]["V_m"][::2]
vm_exp = nest.GetStatus(multimeter)[0]["events"]["V_m"][1::2]

plt.plot(t_cond_exp, vm_cond_exp, label="Cond_Exp")
plt.plot(t_exp, vm_exp, label="Exp")
plt.title("Member Potential: "+ str(ext_curr) ) 
plt.ylim([-71,-40])
plt.xlabel("$t$")
plt.ylabel("$V_m$")
plt.legend()
plt.show()
