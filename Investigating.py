# MATH260 Final Project : Investigating Pi
# Sarvesh Venkittu (srv21)
# May 3, 2025

import numpy as np
import matplotlib.pyplot as plt
import time
import math

# Buffon's Needle Simulation
def buffon_needle(trials, needle_length=1.0, line_distance=2.0):
    cross_count = 0
    for _ in range(trials):
        angle = np.random.uniform(0, np.pi / 2)  # radians
        distance = np.random.uniform(0, line_distance / 2)
        if distance <= (needle_length / 2) * np.sin(angle):
            cross_count += 1
    if cross_count == 0:
        return float('inf')  # Avoid division by zero
    pi_estimate = (2 * needle_length * trials) / (cross_count * line_distance)
    return pi_estimate

# Monte Carlo Simulation
def monte_carlo(trials):
    inside_circle = 0
    for _ in range(trials):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)
        if x ** 2 + y ** 2 <= 1:
            inside_circle += 1
    pi_estimate = (inside_circle / trials) * 4
    return pi_estimate

# Run both methods multiple times and record runtimes and results
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

# Plotting function
def plot_results(buffon_times, monte_times, buffon_pis, monte_pis):
    methods = ['Buffon\'s Needle', 'Monte Carlo']

    # Runtime plot
    avg_times = [np.mean(buffon_times), np.mean(monte_times)]
    std_times = [np.std(buffon_times), np.std(monte_times)]

    plt.figure(figsize=(10, 5))
    plt.bar(methods, avg_times, yerr=std_times, capsize=10, color=['skyblue', 'lightgreen'])
    plt.ylabel('Average Runtime (s)')
    plt.title('Average Runtime Comparison')
    plt.grid(axis='y')
    plt.show()
    plt.savefig("Runtime.png")
    
    # Pi approximation plot
    avg_pis = [np.mean(buffon_pis), np.mean(monte_pis)]
    std_pis = [np.std(buffon_pis), np.std(monte_pis)]

    plt.figure(figsize=(10, 5))
    plt.bar(methods, avg_pis, yerr=std_pis, capsize=10, color=['salmon', 'gold'])
    plt.axhline(y=math.pi, color='black', linestyle='--', label='Actual π')
    plt.ylabel('Estimated π')
    plt.title('π Approximation Comparison')
    plt.legend()
    plt.grid(axis='y')
    plt.show()
    plt.savefig("Estimation.png")

# Run and plot
buffon_times, monte_times, buffon_pis, monte_pis = run_comparison(num_runs=10, trials_per_run=100000)
plot_results(buffon_times, monte_times, buffon_pis, monte_pis)
