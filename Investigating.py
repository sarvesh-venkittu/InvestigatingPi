# MATH260 Final Project : Investigating Pi
# Sarvesh Venkittu (srv21)
# May 3, 2025

import numpy as np
import time 

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

def monte_carlo(trials):
    inside_circle = 0
    for _ in range(trials):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1
    pi_estimate = (inside_circle / trials) * 4
    return pi_estimate

def run_comparison(num_runs=10, trials_per_run=100000):
    buffon_times = []
    monte_times = []
    buffon_pis = []
    monte_pis = []

    for _ in range(num_runs):
        start = time.time()
        pi_buffon = buffon_needle(trials_per_run)
        end = time.time()
        buffon_times.append(end - start)
        buffon_pis.append(pi_buffon)

        start = time.time()
        pi_monte = monte_carlo(trials_per_run)
        end = time.time()
        monte_times.append(end - start)
        monte_pis.append(pi_monte)

    return buffon_times, monte_times, buffon_pis, monte_pis