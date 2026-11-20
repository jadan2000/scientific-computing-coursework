JIBRIL ADAN
BSCCS252604254

BIT 2118 SCIENTIFIC COMPUTING

TASK 2 NUMPY ARRAYS AND NUMERICAL COMPUTATION

Inputs are twenty four hourly temperature readings in degrees Celsius
The operations are mean minimum maximum and Celsius to Fahrenheit conversion using F equals 1 point 8 times C plus 32
The program stores the readings in a NumPy array and calculates the daily statistics
The changed input is the afternoon reading which is increased by two degrees
The daily mean and maximum increase while the minimum remains unchanged if the altered reading is not the minimum
The output describes the daily temperature pattern and gives converted Fahrenheit readings
The related case estimates daily water consumption from hourly meter readings using array totals and summary statistics

TASK 3 MATHEMATICAL FUNCTIONS AND VECTORIZATION

Inputs are one million simulated network latency measurements in milliseconds
The operations convert milliseconds to seconds and square every measurement
The vectorized expression performs the same calculation over the complete array
The changed parameter is the number of measurements which is reduced from one million to five hundred thousand for comparison
The output contains sample squared latency values and execution times
The vectorized calculation avoids the overhead of a Python loop and is suitable for repeated operations on large datasets
The related case processes one million electricity sensor readings and calculates squared deviations from the average

TASK 4 FLOATING POINT ARITHMETIC AND NUMERICAL ERRORS

Inputs are decimal values and an approximation to the square root of two
The operations compare floating point values and calculate absolute and relative error
The changed parameter is the approximation precision which is increased from three decimal places to six decimal places
The absolute and relative errors become smaller as the approximation improves
The output demonstrates why exact equality is unreliable for many floating point calculations
The related case checks whether bank transaction totals agree within a defined numerical tolerance

TASK 5 MATRIX ALGEBRA AND MATRIX OPERATIONS

Inputs are four two dimensional points and a rotation angle of forty five degrees with separate scale factors
The operations construct scaling and rotation matrices and multiply them to transform coordinates
The changed parameter is the rotation angle which is increased to sixty degrees
The transformed coordinates change because the object rotates further while retaining its scale
The determinant indicates whether the transformation matrix is invertible
The related case transforms map coordinates from one local reference frame to another

TASK 6 SOLUTION OF SYSTEMS OF LINEAR EQUATIONS

Inputs are the CPU and memory requirements of two server types and the observed resource totals
The operation solves the matrix equation Ax equals b
The changed input is the total CPU capacity which is increased while memory demand stays constant
The solution gives the quantities of each server type needed to satisfy the equations
The residual verifies the accuracy of the numerical solution
The related case estimates quantities of two ingredients needed to meet production and cost constraints

TASK 7 GAUSSIAN ELIMINATION AND LU DECOMPOSITION

Inputs are a coefficient matrix and three measurement vectors
The operation factors the matrix into lower and upper triangular factors and reuses them to solve each system
The changed input is the second measurement vector which is increased by one unit in its first component
The resulting solution changes to reflect the new measurements while the matrix factorization remains reusable
A small residual indicates that the calculated solution satisfies the original equations
The related case repeatedly solves an electrical network model as measured current values change

TASK 8 ITERATIVE METHODS FOR LINEAR SYSTEMS

Inputs are a five by five coefficient matrix a boundary influence vector a starting estimate and a tolerance
The operations are Jacobi and Gauss Seidel iteration
The changed parameter is the tolerance which is tightened from one times ten to the power negative eight to one times ten to the power negative ten
A tighter tolerance generally requires more iterations and produces a more precise estimate
The convergence graph shows the maximum change decreasing as iterations proceed
The related case estimates steady state temperatures at points in a building heating system

TASK 9 EIGENVALUES AND EIGENVECTORS

Inputs are an adjacency matrix describing connections between four network nodes
The operation calculates eigenvalues and eigenvectors and normalizes the dominant eigenvector
The changed input adds a connection between two previously unconnected nodes
The dominant eigenvector scores change because the network structure has changed
A higher normalized score indicates a node with greater eigenvector based influence
The related case estimates the relative importance of web pages connected by hyperlinks

TASK 10 BISECTION AND FIXED POINT METHODS

Inputs are a heat balance function and a bracket from twenty to forty degrees Celsius
The operations find a root using bisection and fixed point iteration
The changed parameter is the initial fixed point estimate which is changed from thirty to thirty five
A suitable convergent fixed point formulation approaches the same equilibrium value
The graph crosses zero at the equilibrium temperature
The related case finds the temperature at which a refrigeration system reaches thermal balance

TASK 11 NEWTON RAPHSON AND SECANT METHODS

Inputs are an initial investment and a sequence of annual cash flows
The operation finds the rate that makes net present value equal to zero
The changed input is the final cash flow which is increased by five hundred currency units
The internal rate of return changes because the cash flow pattern changes
The output compares Newton Raphson and secant estimates and checks the net present value
The related case calculates the interest rate for a small business investment proposal

TASK 12 POLYNOMIAL AND NONLINEAR EQUATION SOLVING

Inputs are a circle equation and a parabola equation with two starting guesses
The operation solves two nonlinear equations simultaneously
The changed parameter is the starting guess which is moved closer to the negative intersection
The solver converges to the intersection associated with the starting guess when convergence is successful
The residual values should be close to zero
The related case finds the point where a road curve intersects a circular boundary

TASK 13 INTERPOLATION

Inputs are hourly temperature observations from eight in the morning to two in the afternoon
The operations estimate intermediate values using linear interpolation and cubic splines
The changed input is one measured temperature which is increased by one degree
The interpolated estimates around that measurement change accordingly
The graph compares the measured points with the two interpolated curves
The related case estimates missing rainfall measurements between recorded observation times

TASK 14 CURVE FITTING AND APPROXIMATION

Inputs are concurrent user counts and measured server response times
The operation fits a quadratic model using least squares
The changed input is the response time at the highest observed load which is increased by twenty milliseconds
The fitted coefficients and predicted response time change to reflect the altered observation
The root mean squared error measures the typical size of model residuals
The related case fits a demand curve to daily customer counts and sales

TASK 15 NUMERICAL DIFFERENTIATION

Inputs are GPS position measurements and their observation times
The operation estimates speed using forward central and backward finite differences
The changed input is one position measurement which is increased by one metre
The speed estimates at nearby times change because the local position differences change
The graph shows the estimated speed over time
The related case estimates the acceleration of a moving vehicle by differentiating measured speed

TASK 16 NUMERICAL INTEGRATION

Inputs are power readings in kilowatts at two hour intervals
The operations estimate total energy using the trapezoidal and Simpson rules
The changed input is the middle power reading which is increased by zero point two kilowatts
The estimated total energy increases because the measured power is higher over part of the interval
The output compares the two numerical estimates in kilowatt hours
The related case estimates total water volume delivered by integrating flow rate over time

TASK 17 ORDINARY DIFFERENTIAL EQUATIONS USING EULER METHOD

Inputs are ambient temperature initial temperature cooling constant and time step
The operation advances Newton law of cooling using Euler updates
The changed parameter is the time step which is reduced from one minute to zero point five minutes
The smaller step generally improves the approximation while increasing the number of calculations
The graph compares the numerical temperature with the exact cooling curve
The related case models the cooling of stored food after removal from a refrigerator

TASK 18 NUMERICAL SOLUTION OF ODES USING SCIPY

Inputs are supply voltage resistance capacitance initial voltage and time interval
The operation solves the RC circuit differential equation using solve_ivp
The changed parameter is the resistance which is increased from one thousand to two thousand ohms
The larger resistance increases the time constant and the capacitor charges more slowly
The graph compares the numerical solution with the exact charging curve
The related case models the charging behaviour of a battery monitoring circuit

TASK 19 NUMERICAL OPTIMIZATION

Inputs are two server allocation variables their unit costs their capacities and a minimum capacity requirement
The operation minimizes total cost subject to a capacity constraint and non negative bounds
The changed parameter is the required capacity which is increased from one thousand to twelve hundred units
The optimized allocation and minimum cost change to meet the higher requirement
The integer search compares whole server combinations where fractional servers are not practical
The related case minimizes transport cost while meeting a delivery capacity requirement

TASK 20 RANDOM NUMBERS AND MONTE CARLO METHODS

Inputs are server capacity mean demand demand standard deviation and one hundred thousand random trials
The operation simulates demand and estimates overload probability from the fraction of trials above capacity
The changed parameter is the standard deviation which is increased from one hundred and twenty to one hundred and fifty
The estimated overload probability increases because demand becomes more variable
The convergence graph shows the running probability estimate stabilizing as the number of trials grows
The related case estimates the probability that daily electricity demand exceeds available supply

OUTPUT INTERPRETATION

Numerical outputs are estimates based on the stated input data and mathematical assumptions
A small residual indicates that a computed solution satisfies the model equations closely
A fitted curve describes the observed trend but does not guarantee accurate predictions outside the measured range
Interpolation estimates values between measured points and should not be treated as new measurements
Numerical integration estimates accumulated quantities from sampled data
Monte Carlo estimates become more stable as the number of simulations increases

ASSUMPTIONS

The example measurements are illustrative
The mathematical models are assumed to represent the simplified real world situations described in each task
Input units are consistent within each calculation
The optimization model allows fractional allocations for its continuous solution and separately checks integer allocations
Random simulations use a fixed seed so that results can be reproduced
