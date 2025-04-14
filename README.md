# Investigating π
Sarvesh Venkittu's Duke University MATH260 Final Project

## Description
Approximating the mathematical constant π has been an area of interest in mathematics for centuries. Various methods, both deterministic and probabilistic, have been developed to estimate π with increasing accuracy. Two well-known probabilistic methods are Buffon’s Needle and the Monte Carlo Unit Circle method. This project focuses on comparing these two approaches in terms of accuracy, efficiency, and computational complexity.

## Background - Key Vocabulary
- Buffon’s Needle: A probability-based method for estimating π by dropping a needle onto a plane with parallel lines and analyzing the probability of the needle crossing a line.
- Monte Carlo Simulation: A computational technique that uses repeated random sampling to estimate numerical results, commonly applied to approximate π. 
- Unit Circle Method: A Monte Carlo technique where points are randomly placed in a square, and the proportion falling inside an inscribed quarter-circle is used to estimate π.
- Probabilistic Methods: Techniques that use randomness and statistical principles to estimate numerical values.
- Deterministic Methods: Methods that use fixed, non-random algorithms to compute values with exact precision.

## Features
The methods used and their descriptions is as follows:

- Buffon’s Needle Simulation: This method is based on a classical probability problem proposed by Georges-Louis Leclerc, Comte de Buffon. A needle of a certain length is dropped randomly onto a plane with equally spaced parallel lines. By analyzing the probability of the needle crossing one of the lines, we can estimate the value of π. The probability of a crossing is proportional to the sine of the angle at which the needle falls, and this relationship allows for π to be estimated from a large number of trials.
- Monte Carlo Simulation: This method uses random sampling within a unit square to estimate π. Random points are generated in the square, and we count how many fall inside the quarter-circle inscribed within the square. The ratio of points inside the circle to the total number of points approximates π/4, so multiplying by 4 yields an estimate for π. This method is conceptually simple and well-suited for visualization and statistical analysis.
The comparison and graphing methods used are as follows:
- Runtime Comparison: Each method was run multiple times (default 10 runs), with the same number of trials per run (100,000). The time taken for each run was recorded using Python’s time module. These runtimes were averaged, and their standard deviations were calculated to assess performance variability. A bar chart was generated to visualize the average runtime for each method, including error bars to show standard deviation.
- π Estimation Accuracy: The value of π estimated by each method in every run was recorded. From these values, the mean and standard deviation of the π estimates were calculated. A bar chart was created to compare the average estimated value of π for each method, again using error bars to display standard deviation. A horizontal dashed line representing the actual value of π (from Python’s math.pi) was also included to visually assess accuracy and bias.
## Usage
To run this program, download the Investigating.py file to a IDE of your choice. Click "run" and enjoy!
## Testing
The following test cases were run to ensure the validity of the program:

1. Basic Functionality Test
- Description: Ran both buffon_needle() and monte_carlo() with a small number of trials (e.g., 100 or 1,000).
- Purpose: To confirm that both functions execute without errors and return a numerical estimate for π.
- Expected Result: Reasonable estimates near π with higher variance due to fewer trials.
- Outcome: Both methods returned valid π estimates and behaved as expected.
2. Zero Crossings Edge Case (Buffon’s Needle)
- Description: Observed behavior when the number of needle crossings was zero.
- Purpose: To check that division by zero is handled safely in Buffon’s method.
- Expected Result: Function should return float('inf') instead of crashing.
- Outcome: Confirmed—function gracefully handles the zero-crossing scenario.
3. High Trial Count Test
- Description: Used a large number of trials (e.g., 1,000,000) for both methods.
- Purpose: To verify scalability and convergence of the π approximation to the true value.
- Expected Result: π estimate should converge closely to the actual value (~3.14159).
- Outcome: π estimates were accurate to 2–3 decimal places, demonstrating statistical convergence.
4. Runtime Consistency Test
- Description: Repeated runs using the same number of trials to measure variation in runtime.
- Purpose: To ensure that performance is consistent and does not vary erratically.
- Expected Result: Runtime should remain within a predictable range across runs.
- Outcome: Observed consistent timing with minor variance due to system processes and randomness.
5. Graphing Validation
- Description: Verified that runtime and estimation graphs generate and save properly.
- Purpose: To ensure the visual output matches the computed data.
- Expected Result: Graphs should appear with appropriate labels, titles, and error bars.
- Outcome: Both plots were generated accurately and saved as "Runtime.png" and "Estimation.png".
