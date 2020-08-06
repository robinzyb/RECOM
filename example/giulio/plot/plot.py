from utils.tools import plot_example01, plot_uncertainty
import matplotlib.pyplot as plt
import numpy as np
#direct_reweight = np.loadtxt("../direct_reweight_quantity.dat").T
asym_reweight = np.loadtxt("../asymptotic_reweight_quantity.dat").T

#asym_reweight_3 = np.loadtxt("../asymptotic_reweight_quantity_alpha3.dat").T

#gr1 = np.loadtxt("../other_data/gr_1_O-O.dat", usecols=1).T
#gr2 = np.loadtxt("../other_data/gr_2_O-O.dat", usecols=1).T
#gr3 = np.loadtxt("../other_data/gr_3_O-O.dat", usecols=1).T
#gr4 = np.loadtxt("../other_data/gr_4_O-O.dat", usecols=1).T
#x = np.loadtxt("../other_data/gr_4_O-O.dat", usecols=0).T

#grs = np.vstack((gr1, gr2, gr3, gr4))
#plot_example01(direct_reweight, asym_reweight, grs, x)

x = np.linspace(0, 6, 200)
dev = asym_reweight.std(axis=0)
np.savetxt("yb_dev.dat", dev)
reweight_mean = asym_reweight.mean(axis=0)
#reweight_3_mean = asym_reweight_3.mean(axis=0)
print(reweight_mean.shape)
com_md = np.loadtxt("../input/rdf.dat")
com_md = com_md.mean(axis=0)
#plt.figure(figsize =(10,10))
#plt.plot(x, com_md, label="com_md")
#plt.plot(x, reweight_mean, label="average from reweight alpha=4.33")
#plt.plot(x, reweight_3_mean, label="average from reweight alpha=4.33")
#plt.legend()
#plt.savefig("test.png",dpi=80)
plot_uncertainty(com_md, dev, x, "water O-O gr")
