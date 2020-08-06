from utils.tools import plot_example02, plot_uncertainty
import matplotlib.pyplot as plt
import numpy as np
#direct_reweight = np.loadtxt("../direct_reweight_quantity.dat").T
asym_reweight = np.loadtxt("../asymptotic_reweight_quantity_alpha5.dat").T
#asym_reweight_5 = np.loadtxt("../asymptotic_reweight_quantity_alpha5.dat").T

#gr1 = np.loadtxt("../other_data/gr_1_He-O.dat", usecols=1).T
#gr2 = np.loadtxt("../other_data/gr_2_He-O.dat", usecols=1).T
#gr3 = np.loadtxt("../other_data/gr_3_He-O.dat", usecols=1).T
#gr4 = np.loadtxt("../other_data/gr_4_He-O.dat", usecols=1).T
#gr5 = np.loadtxt("../other_data/gr_5_He-O.dat", usecols=1).T
x = np.linspace(0,7, 100)

#grs = np.vstack((gr1, gr2, gr3, gr4, gr5))
#plot_example02(direct_reweight, asym_reweight, grs, x)

dev = asym_reweight.std(axis=0)
reweight_mean = asym_reweight.mean(axis=0)
#reweight_5_mean = asym_reweight_5.mean(axis=0)
com_md = np.loadtxt("../input/pdf_all_1_by_1.dat")
com_md = com_md.mean(axis=0)

plt.figure(figsize =(10,10))
plt.plot(x, com_md, label="com_md")
plt.plot(x, reweight_mean, label="average from reweight alpha=5.7957")
#plt.plot(x, reweight_5_mean, label="average from reweight alpha=5.7957")
plt.legend()
plt.savefig("test.png",dpi=80)

plot_uncertainty(com_md, dev, x, "Methanesulfonic OxygenO-Phenol Oxygen gr")
