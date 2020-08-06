# REweight COMmittee(RECOM)

## Introduction

Developer: Yongbin Zhuang

A simple python package to reweight quantity from committee simulation

## Installation

```
pip install .
```



## Usage

### Prepare

Prepare file: `config.json`, `ml_pot.dat`, `quantity.dat`

`ml_pot.dat`: store the potential value in a matrix, so if you have 4 committee potentials, the shape will be (frame_number, 4), the potential unit must be **eV**.

`quantity.dat`: store the quantity value for every frame in matrix, so if we have gr with 200 bins, that is 200 quantities for one frame, the shape will be (frame_number, 200)

`config.json`:

```json
{                                                          
   "pot_file": "./input/ml_pot.dat",                                             
   "quant_file": "./input/gr_list_O_O.dat",                                      
   "temp": 300,                                                                  
   "reweight_method": "Direct",                                                  
   "new_alpha": 3.15,                                                             
   "old_alpha": 3.15                                                             
 }
```

"pot_file": path to ml_pot

"quant_file": path to quantity file

"temp": temperature in kelvin

"reweight_method": the method used to reweight the potential, you can choose `Direct` or `Asymptotic`

"new_alpha": new alpha to rescale the potential, if you don't want to rescale it again, then just set same value in `new_alpha` and `old_alpha`

"old_alpha": the alpha value corresponding to the ml_pot.dat

### Command Usage

Show help

```bash
recom -h
```

Run the reweight

```bash
recom run config.json
```

Extract the potential energy from ipi `extra` file

```bash
recom extract simulation.extra_0 4
```

If a conversion of energy unit is needed

```bash
#this will multiply the energy with 27.2114
recom extract simulation.extra_0 4 --factor 27.2114
```



