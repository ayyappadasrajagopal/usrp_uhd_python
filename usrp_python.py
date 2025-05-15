# -*- coding: utf-8 -*-
"""
Created on Thu May 15 14:32:07 2025

@author: HP
"""

import uhd
import numpy as np
import matplotlib.pyplot as plt

# Set USRP parameters
usrp = uhd.usrp.MultiUsrp()
center_freq = 100e6  # 100 MHz
sample_rate = 1e6   # 1 MHz
gain = 20

# Configure USRP
usrp.set_rx_freq(uhd.libpyuhd.tune_request(center_freq), 0)
usrp.set_rx_rate(sample_rate, 0)
usrp.set_rx_gain(gain, 0)

# Receive data
num_samps = 10000
rx_data = usrp.recv_num_samps(num_samps, sample_rate, 0)

# Plot the received data
plt.plot(np.abs(rx_data[0]))
plt.xlabel("Sample")
plt.ylabel("Magnitude")
plt.title("Received Data from USRP")
plt.show()