JIBRIL ADAN
BSCCS252604254

BIT 2118 SCIENTIFIC COMPUTING
INDIVIDUAL REAL WORLD PROGRAM MODIFICATIONS

PURPOSE

This document records a different but related real world application for every practical task from 2 to 20. The examples use illustrative teaching data, stated assumptions, mathematical operations, outputs and interpretations. The programs are in code/real_world_cases.py.

Run the cases with python code/real_world_cases.py after installing the libraries in requirements.txt.

TASK 2 NUMPY ARRAYS AND NUMERICAL COMPUTATION

Real world case
A farm records water delivered by an irrigation line at six hourly intervals.

Assumptions and inputs
Each reading is litres delivered during one hour. Readings are complete and use the same unit. The readings are 12, 14, 13, 15, 16 and 14 litres. A ten percent allowance estimates leakage.

Operation and output
NumPy calculates total, mean and maximum. The total is 84 litres, mean is 14 litres per hour and peak is 16 litres per hour. Including ten percent leakage, required supply is 92.4 litres.

Interpretation and changed input
The readings indicate 84 litres delivered over six hours. Reducing the leakage allowance from ten percent to five percent changes estimated supply to 88.2 litres.

TASK 3 MATHEMATICAL FUNCTIONS AND VECTORIZATION

Real world case
A photo application normalizes pixel brightness before image processing.

Assumptions and inputs
The sample contains grayscale pixel intensities 35, 80, 120, 180 and 220. Eight bit intensity ranges from zero to 255. Exposure adjustment adds 15 and clips values to the valid range.

Operation and output
Each pixel is divided by 255 in one vectorized NumPy operation. Normalized values are approximately 0.1373, 0.3137, 0.4706, 0.7059 and 0.8627. Mean brightness is 0.4980.

Interpretation and changed input
The normalized values express relative brightness between zero and one. Increasing exposure by 15 raises the values. Vectorization applies the operation to all pixels without a Python loop.

TASK 4 FLOATING POINT ARITHMETIC AND NUMERICAL ERRORS

Real world case
An invoice system checks whether the sum of item prices agrees with the expected total.

Assumptions and inputs
Item prices are 19.99, 5.49 and 3.25 currency units. Expected total is 28.73. A difference up to one cent is accepted for this comparison.

Operation and output
The values are added using binary floating point and compared with NumPy isclose using an absolute tolerance of 0.01. The displayed computed total is 28.73 and the tolerance check returns True.

Interpretation and changed input
The computed amount agrees within one cent. Setting tolerance to zero requires exact equality and can fail for some binary floating point values. A real payment ledger should use decimal arithmetic and explicit currency rounding rules.

TASK 5 MATRIX ALGEBRA AND MATRIX OPERATIONS

Real world case
A warehouse robot converts points from its local coordinate frame to a warehouse coordinate frame.

Assumptions and inputs
The points are (1,0), (0,1) and (1,1). The robot rotates counterclockwise by 30 degrees and translates by (2,1) metres. Measurement noise is ignored.

Operation and output
A two dimensional rotation matrix multiplies each point and the translation vector is added. The transformed points are approximately (2.866,1.500), (1.500,1.866) and (2.366,2.366).

Interpretation and changed input
The coordinates describe the same points in the warehouse frame. Changing rotation to 60 degrees moves the first transformed point to approximately (2.500,1.866).

TASK 6 SOLUTION OF SYSTEMS OF LINEAR EQUATIONS

Real world case
A feed producer combines two ingredients to meet protein and carbohydrate targets.

Assumptions and inputs
Ingredient A supplies 20 protein units and 5 carbohydrate units per kilogram. Ingredient B supplies 10 protein units and 25 carbohydrate units per kilogram. The targets are 30 protein units and 35 carbohydrate units.

Operation and output
NumPy solves the simultaneous equations. The blend is approximately 0.889 kg of A and 1.222 kg of B. Substitution gives the target totals of 30 and 35 units.

Interpretation and changed input
The calculated blend meets both targets under the stated composition assumptions. Raising the carbohydrate target from 35 to 40 changes the required quantities; the program recalculates the solution.

TASK 7 GAUSSIAN ELIMINATION AND LU DECOMPOSITION

Real world case
A factory calculates production quantities as material orders change.

Assumptions and inputs
Two production lines use two shared materials. The fixed coefficient matrix has rows (3,1) and (1,2). Demand vectors are (10,8) and (11,8).

Operation and output
SciPy factors the matrix once into LU factors and reuses them. The first production solution is (2.4,2.8), and the second is (2.8,2.6).

Interpretation and changed input
Increasing the first material demand by one unit changes the production plan. Reusing the factorization avoids repeating decomposition when only the demand vector changes.

TASK 8 ITERATIVE METHODS FOR LINEAR SYSTEMS

Real world case
A building engineer estimates steady state temperatures in three connected indoor zones.

Assumptions and inputs
The simplified heat balance is a diagonally dominant system with matrix rows (4,-1,0), (-1,4,-1), (0,-1,3) and right hand side (50,30,20). Initial estimates are zero.

Operation and output
Gauss Seidel iteration updates the estimates using the newest available values. With tolerance 1e-8, estimates are approximately 16.0976, 14.3902 and 11.4634. The calculation converges in 13 iterations and residual infinity norm is about 2.04e-9.

Interpretation and changed input
The small residual indicates that the estimates closely satisfy the model equations. Tightening tolerance to 1e-10 requires a stricter stopping condition and may require more iterations.

TASK 9 EIGENVALUES AND EIGENVECTORS

Real world case
A community organisation studies member influence in a referral network.

Assumptions and inputs
A directed edge means one member refers another. The adjacency matrix rows are (0,1,1), (1,0,1) and (1,0,0). The dominant eigenvector is used as a simplified influence measure.

Operation and output
NumPy calculates eigenvalues and eigenvectors. The dominant eigenvector is normalized to scores approximately 0.3820, 0.3820 and 0.2361.

Interpretation and changed input
The first two members have equal scores in this example. Adding a referral edge from member three to member two changes the matrix and recalculates the scores. This mathematical measure does not prove personal importance or quality.

TASK 10 ROOT FINDING BISECTION AND FIXED POINT METHODS

Real world case
A small business finds the sales quantity at which revenue covers total cost.

Assumptions and inputs
Selling price is 45 currency units per item, variable cost is 25 per item and fixed cost is 600. All produced items are sold. Revenue is 45q and total cost is 600+25q.

Operation and output
Bisection finds the zero of revenue minus cost between zero and 100. The break even quantity is 30 items. A fixed point rearrangement gives q = fixed cost divided by 20 and converges to the same value.

Interpretation and changed input
The business must sell at least 30 items to cover the stated costs. Raising fixed cost to 700 raises break even quantity to 35 items.

TASK 11 NEWTON RAPHSON AND SECANT METHODS

Real world case
A small business evaluates the return on equipment investment.

Assumptions and inputs
Initial investment is -10000 currency units. Receipts are 3000, 3500 and 4000 at the ends of years one, two and three.

Operation and output
The net present value equation is solved for the rate that makes NPV zero. The estimated internal rate of return is approximately 2.3647 percent.

Interpretation and changed input
Increasing the final receipt by 500 raises the estimated return to approximately 4.5952 percent. A higher receipt increases the investment return under this cash flow model.

TASK 12 POLYNOMIAL AND NONLINEAR EQUATION SOLVING

Real world case
A road alignment is checked against a circular property boundary.

Assumptions and inputs
The boundary is x squared plus y squared equals 25. The road centreline is y equals 0.5x plus 1. The initial solver guess is (2,2).

Operation and output
SciPy root solves the two equations simultaneously. One intersection is approximately (4,3), with residuals close to zero.

Interpretation and changed input
The solution is a point satisfying both geometric equations. Changing the starting guess can lead a nonlinear solver toward a different intersection when multiple roots exist.

TASK 13 INTERPOLATION

Real world case
A water authority estimates a missing daily rainfall observation.

Assumptions and inputs
Rainfall readings are 4 mm on day 1, 8 mm on day 2, 14 mm on day 4 and 10 mm on day 5. Day 3 is missing.

Operation and output
Linear interpolation estimates day 3 rainfall as 11 mm.

Interpretation and changed input
The estimate lies halfway between the day 2 and day 4 observations. Raising the day 2 reading from 8 to 10 mm changes the day 3 estimate to 12 mm. An interpolated value is an estimate, not a new measurement.

TASK 14 CURVE FITTING AND APPROXIMATION

Real world case
A farm models crop yield in relation to fertilizer application.

Assumptions and inputs
Fertilizer amounts are 0, 10, 20, 30 and 40 kg per hectare. Corresponding yields are 2.0, 2.8, 3.5, 4.0 and 4.3 tonnes per hectare.

Operation and output
A quadratic least squares model is fitted. Predicted yield at 35 kg per hectare is approximately 4.169 tonnes per hectare. RMSE is approximately 0.0151 tonnes per hectare.

Interpretation and changed input
The model describes the trend in the sample. Increasing the final observed yield by 0.2 changes the fitted coefficients and prediction at 35 kg per hectare. Predictions beyond the observed range require caution.

TASK 15 NUMERICAL DIFFERENTIATION

Real world case
A vehicle monitoring system estimates acceleration from speed readings.

Assumptions and inputs
Speeds at times 0, 1, 2, 3 and 4 seconds are 0, 4, 9, 15 and 22 metres per second.

Operation and output
NumPy gradient estimates acceleration using finite differences. The estimates are 4, 4.5, 5.5, 6.5 and 7 metres per second squared.

Interpretation and changed input
The estimates describe the rate of change of speed. Changing the speed at 2 seconds from 9 to 10 m/s changes nearby acceleration estimates.

TASK 16 NUMERICAL INTEGRATION

Real world case
A water utility estimates the volume delivered by a pump from sampled flow rates.

Assumptions and inputs
Flow rates at 0, 5, 10, 15 and 20 minutes are 8, 10, 12, 11 and 9 litres per minute.

Operation and output
Simpson numerical integration estimates the delivered volume as approximately 208.33 litres.

Interpretation and changed input
The integral estimates accumulated water volume over the twenty minutes. Raising the middle flow reading by 1 litre per minute increases the estimate to approximately 211.67 litres.

TASK 17 ORDINARY DIFFERENTIAL EQUATIONS USING EULER METHOD

Real world case
A food storage operator estimates how quickly warm food cools in a cold room.

Assumptions and inputs
Ambient temperature is 22 C, initial food temperature is 70 C and cooling constant is 0.08 per minute. The model follows Newton cooling for ten minutes.

Operation and output
Euler updates temperature using the cooling differential equation. With a 0.5 minute step the estimate after ten minutes is approximately 43.216 C. The exact model value is approximately 43.568 C.

Interpretation and changed input
The food temperature approaches ambient temperature. Reducing the step to 0.25 minutes generally improves the Euler approximation by reducing step-size error.

TASK 18 NUMERICAL SOLUTION OF ODES USING SCIPY

Real world case
A water tank model estimates level as water enters and drains.

Assumptions and inputs
Initial level is 0.2 metres, inflow is 0.03 cubic metres per minute, drainage coefficient is 0.002 and tank area is 2 square metres. Outflow depends on the square root of water level.

Operation and output
SciPy solve_ivp integrates the level differential equation over 60 minutes. At 0, 15, 30, 45 and 60 minutes the estimated levels are approximately 0.2000, 0.4167, 0.6309, 0.8430 and 1.0534 metres.

Interpretation and changed input
The level rises because inflow exceeds outflow in this model. Increasing inflow to 0.04 cubic metres per minute produces a higher level trajectory.

TASK 19 NUMERICAL OPTIMIZATION

Real world case
A delivery company minimizes the cost of trips using two vehicle types.

Assumptions and inputs
Vehicle A costs 80 units per trip and carries 120 parcels. Vehicle B costs 110 units and carries 200 parcels. At least 500 parcels must be delivered.

Operation and output
SciPy minimizes total trip cost subject to capacity and nonnegative bounds. The continuous relaxation costs 275 units at 2.5 B trips. The best whole-trip plan is one A trip and two B trips, costing 300 units and carrying 520 parcels.

Interpretation and changed input
The continuous solution is a mathematical lower bound because fractional trips are not practical. The integer plan is operationally feasible. Raising required capacity changes the feasible combinations and minimum cost.

TASK 20 RANDOM NUMBERS AND MONTE CARLO METHODS

Real world case
An electricity provider estimates the risk that demand exceeds available supply.

Assumptions and inputs
Demand is modelled as a normal random variable with mean 900 kW. Available supply is 1000 kW. One hundred thousand trials are simulated with a fixed random seed.

Operation and output
Monte Carlo estimates overload probability as the fraction of simulated demand values above 1000 kW. At standard deviation 100 kW the estimate is approximately 15.9 percent. The program also tests standard deviation 140 kW.

Interpretation and changed input
Greater demand variability increases the chance of exceeding supply even when average demand remains unchanged. The estimate is simulation-based and becomes more stable with more trials.

GENERAL ASSUMPTIONS AND LIMITATIONS

All datasets are illustrative and deliberately small for teaching.
The mathematical models simplify real processes and omit factors not listed in each case.
Units are assumed consistent within each calculation.
Numerical estimates are not substitutes for field measurements or professional engineering decisions.
Interpolation estimates between measured values and should not be described as observed data.
Curve fitting describes the sample and does not guarantee reliable extrapolation.
The invoice example demonstrates floating point tolerance only; production financial systems should use decimal arithmetic and defined rounding rules.
The optimization example reports both a continuous relaxation and a practical integer plan.
Monte Carlo results depend on the assumed demand distribution and number of trials.
