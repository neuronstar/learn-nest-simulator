
import sys
import nest
import matplotlib.pyplot as plt

w =float( (sys.argv)[1] )

neuron_alpha = nest.Create("iaf_psc_alpha")
neuron_exp = nest.Create("iaf_psc_exp")

spg = nest.Create("spike_generator", params={"spike_times":[200.0, 500.0], "spike_weights":[w, 2*w]})

multimeter = nest.Create("multimeter", params={"withtime":True, "record_from":["V_m"]})


nest.Connect(spg,neuron_alpha)
nest.Connect(spg,neuron_exp)
nest.Connect(multimeter, neuron_alpha)
nest.Connect(multimeter, neuron_exp)

nest.Simulate(1000)

t_alpha = nest.GetStatus(multimeter)[0]["events"]["times"][::2]
t_exp = nest.GetStatus(multimeter)[0]["events"]["times"][1::2]
vm_alpha = nest.GetStatus(multimeter)[0]["events"]["V_m"][::2]
vm_exp = nest.GetStatus(multimeter)[0]["events"]["V_m"][1::2]

plt.plot(t_alpha, vm_alpha, label="Alpha")
plt.plot(t_exp, vm_exp, label="Exp")
plt.title("Spike Weight: "+ str(w) ) 
plt.ylim([-71,-40])
plt.xlabel("$t$")
plt.ylabel("$V_m$")
plt.legend()
plt.show()
