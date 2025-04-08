# MATH260 Final Project : Investigating Pi
# Sarvesh Venkittu (srv21)
# May 3, 2025

import numpy as np


def buffon_needle(trials, needle_length=0.5, line_distance=1.0):
    cross_count = 0
    for _ in range(trials):
        angle = np.random.uniform(0, np.pi / 2)  
        distance = np.random.uniform(0, line_distance / 2)
        if distance <= (needle_length / 2) * np.sin(angle):
            cross_count += 1
    if cross_count == 0:
        return float('inf') 
    pi_estimate = (2 * needle_length * trials) / (cross_count * line_distance)
    return pi_estimate