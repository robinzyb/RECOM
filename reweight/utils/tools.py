# collect of misc function
import json
import numpy as np
import matplotlib.pyplot as plt
from reweight.reweight import fancy_print


def ipi_extra(arg):
    """
    function to extract the scaled potential from ipi extra file
    """
    extra_file = arg.ipi_extra_file
    fancy_print("find file {0}".format(extra_file))
    pot_num = arg.pot_num
    fancy_print("we have {0} potentials".format(pot_num))
    if arg.factor :
        unit_conversion = arg.factor
    else:
        unit_conversion = 1.0

    fancy_print("extracting the potential")
    fr = open(extra_file, "r")
    frame_pot_list = []
    for idx, line in enumerate(fr.readlines()):
        if (idx%2 == 0):
            continue
        else:
            info = json.loads(line)
            committee = info["committee"]
            ml_pot = []
            for i in range(pot_num):
                ml_pot.append(committee[i]["v"])
            frame_pot_list.append(ml_pot)
    fr.close()
    #save file
    frame_pot_list = np.array(frame_pot_list)*unit_conversion
    np.savetxt("ml_pot.dat", frame_pot_list)
    fancy_print("save file to ml_pot.dat")
    fancy_print("Finished")

def plot_example01(data1,
                   data2,
                   data3,
                   x
                   ):
    fig, axis = plt.subplots(2, 2, figsize = (15, 15))
    for idx, ax in enumerate(axis.flatten()):
        ax.plot(x, data3[idx], label = "Single Traj")
        ax.plot(x, data1[idx], label = "Direct Reweight")
        ax.plot(x, data2[idx], label = "Cumulant Reweight")
        ax.set_xlabel("r[Angstrom]", fontsize=15)
        ax.set_ylabel("g(r)", fontsize=15)
        ax.set_title("NN {0}".format(idx+1), fontsize=20)
        ax.tick_params(labelsize=15)
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc=(0.18, 0.93), prop = {"size":20}, ncol=3, frameon=False)
    plt.savefig("./water_gr_contrast.png", format="png", dpi=200)

def plot_uncertainty(data1,
                     uncertainty,
                     x,
                     title
                     ):
    plt.figure(figsize=(10, 10))
    plt.xlabel("r[Angstrom]", fontsize=20)
    plt.ylabel("g(r)", fontsize=20)
    plt.tick_params(labelsize=15)
    plt.plot(x, data1, label = "Committee")
    plt.fill_between(x, data1-uncertainty, data1+uncertainty, facecolor='r', alpha=0.5, label = "Uncertainty")
    plt.title(title, fontsize=25)
    plt.legend(fontsize = 20, frameon=False)
    plt.savefig("./gr_uncertainty.png", format="png", dpi=200)

def plot_example02(data1,
                   data2,
                   data3,
                   x
                   ):
    fig, axis = plt.subplots(3, 2, figsize = (15, 22.5))
    for idx, ax in enumerate(axis.flatten()):
        if idx == 5:
            break
        ax.plot(x, data3[idx], label = "Single Traj")
        ax.plot(x, data1[idx], label = "Direct Reweight")
        ax.plot(x, data2[idx], label = "Cumulant Reweight")
        ax.set_xlabel("r[Angstrom]", fontsize=15)
        ax.set_ylabel("g(r)", fontsize=15)
        ax.set_title("NN {0}".format(idx+1), fontsize=20)
        ax.tick_params(labelsize=15)
    handles, labels = ax.get_legend_handles_labels()
    fig.legend(handles, labels, loc=(0.18, 0.93), prop = {"size":20}, ncol=3, frameon=False)
    plt.savefig("./phenol_gr_contrast.png", format="png", dpi=200)

