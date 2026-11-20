import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import lu_factor, lu_solve
from scipy.optimize import root_scalar, root, curve_fit, minimize
from scipy.interpolate import interp1d, CubicSpline
from scipy.integrate import simpson, solve_ivp


def task_02():
    temperatures = np.array([18.5, 18.0, 17.8, 17.5, 17.9, 19.0, 21.5, 23.8,
                             25.6, 27.1, 28.3, 29.0, 29.4, 29.1, 28.5, 27.6,
                             26.2, 24.8, 23.4, 22.1, 21.0, 20.2, 19.6, 19.0])
    changed = temperatures.copy()
    changed[12] += 2.0
    print("\nTASK 2 NUMPY ARRAYS")
    print("Mean minimum maximum", np.mean(temperatures), np.min(temperatures), np.max(temperatures))
    print("Changed mean and maximum", np.mean(changed), np.max(changed))
    print("First six Fahrenheit values", 1.8 * temperatures[:6] + 32)


def task_03():
    rng = np.random.default_rng(42)
    latency_ms = rng.uniform(5, 250, 1_000_000)
    vectorized = (latency_ms / 1000.0) ** 2
    changed_size = (latency_ms[:500_000] / 1000.0) ** 2
    print("\nTASK 3 VECTORIZATION")
    print("First five squared latency values", vectorized[:5])
    print("Original sample count", len(vectorized), "Changed sample count", len(changed_size))


def task_04():
    calculated = 0.1 + 0.2
    true_value = np.sqrt(2)
    print("\nTASK 4 FLOATING POINT")
    print("0.1 plus 0.2", calculated, "exact equality", calculated == 0.3)
    print("Tolerance comparison", np.isclose(calculated, 0.3))
    for approximation in (1.414, 1.414214):
        error = abs(true_value - approximation)
        print("Approximation", approximation, "absolute error", error,
              "relative error", error / abs(true_value))


def task_05():
    points = np.array([[0., 0.], [1., 0.], [1., 1.], [0., 1.]])
    for degrees in (45, 60):
        angle = np.deg2rad(degrees)
        rotation = np.array([[np.cos(angle), -np.sin(angle)],
                             [np.sin(angle), np.cos(angle)]])
        transform = rotation @ np.diag([2.0, 1.5])
        print("\nTASK 5 MATRIX ALGEBRA", degrees, "degrees")
        print(points @ transform.T)
        print("Determinant", np.linalg.det(transform))


def task_06():
    A = np.array([[4., 2.], [8., 12.]])
    for b in (np.array([20., 72.]), np.array([22., 72.])):
        solution = np.linalg.solve(A, b)
        print("\nTASK 6 LINEAR SYSTEM")
        print("Server quantities", solution)
        print("Verification", A @ solution, "Residual", b - A @ solution)


def task_07():
    A = np.array([[4., -1., 0.], [-1., 4., -1.], [0., -1., 3.]])
    measurements = [np.array([15., 10., 10.]),
                    np.array([17., 11., 9.]),
                    np.array([14., 12., 11.])]
    factors = lu_factor(A)
    print("\nTASK 7 GAUSSIAN ELIMINATION AND LU")
    for index, b in enumerate(measurements, 1):
        x = lu_solve(factors, b)
        print("Measurement set", index, "solution", x,
              "residual norm", np.linalg.norm(b - A @ x))


def task_08():
    A = np.array([[2., -1., 0., 0., 0.], [-1., 2., -1., 0., 0.],
                  [0., -1., 2., -1., 0.], [0., 0., -1., 2., -1.],
                  [0., 0., 0., -1., 2.]])
    b = np.array([100., 0., 0., 0., 20.])

    def iterate(method, tol):
        x = np.zeros_like(b)
        errors = []
        for _ in range(2000):
            old = x.copy()
            if method == "Jacobi":
                x = (b - (A - np.diag(np.diag(A))) @ old) / np.diag(A)
            else:
                for i in range(len(b)):
                    x[i] = (b[i] - A[i, :i] @ x[:i] - A[i, i+1:] @ old[i+1:]) / A[i, i]
            error = np.linalg.norm(x - old, ord=np.inf)
            errors.append(error)
            if error < tol:
                break
        return x, errors

    print("\nTASK 8 ITERATIVE METHODS")
    for tol in (1e-8, 1e-10):
        for method in ("Jacobi", "Gauss-Seidel"):
            x, errors = iterate(method, tol)
            print(method, "tolerance", tol, "solution", x, "iterations", len(errors))
            plt.semilogy(errors, label=f"{method} {tol}")
    plt.xlabel("Iteration")
    plt.ylabel("Maximum change")
    plt.title("Iterative temperature convergence")
    plt.legend()
    plt.grid(True)
    plt.show()


def task_09():
    A = np.array([[0., 1., 1., 0.], [1., 0., 1., 1.],
                  [1., 1., 0., 1.], [0., 1., 1., 0.]])
    changed = A.copy()
    changed[0, 3] = changed[3, 0] = 1.
    print("\nTASK 9 EIGENVALUES AND EIGENVECTORS")
    for matrix in (A, changed):
        values, vectors = np.linalg.eig(matrix)
        i = np.argmax(np.real(values))
        scores = np.abs(np.real(vectors[:, i]))
        scores /= scores.sum()
        print("Dominant eigenvalue", np.real(values[i]), "node scores", scores)


def task_10():
    def heat_balance(T):
        return T - 25 - 10 * np.exp(-T / 20)

    def g(T):
        return 25 + 10 * np.exp(-T / 20)

    solution = root_scalar(heat_balance, bracket=[20, 40], method="bisect", xtol=1e-10)
    print("\nTASK 10 BISECTION AND FIXED POINT")
    print("Bisection root", solution.root)
    for initial in (30., 35.):
        T = initial
        for _ in range(500):
            new = g(T)
            if abs(new - T) < 1e-10:
                T = new
                break
            T = new
        print("Initial estimate", initial, "fixed point", T)
    grid = np.linspace(20, 40, 300)
    plt.plot(grid, heat_balance(grid))
    plt.axhline(0)
    plt.axvline(solution.root, linestyle="--")
    plt.xlabel("Temperature")
    plt.ylabel("Heat balance")
    plt.title("Thermal equilibrium")
    plt.grid(True)
    plt.show()


def task_11():
    cash_flows = [-10000, 3000, 3500, 4000, 2500]
    changed_flows = [-10000, 3000, 3500, 4000, 3000]

    def solve_irr(flows):
        def npv(rate):
            return sum(cf / (1 + rate) ** t for t, cf in enumerate(flows))

        def derivative(rate):
            return sum(-t * cf / (1 + rate) ** (t + 1)
                       for t, cf in enumerate(flows) if t > 0)

        newton = root_scalar(npv, fprime=derivative, x0=0.1, method="newton")
        secant = root_scalar(npv, x0=0.05, x1=0.2, method="secant")
        return newton.root, secant.root, npv(newton.root)

    print("\nTASK 11 NEWTON RAPHSON AND SECANT")
    print("Original cash flows", solve_irr(cash_flows))
    print("Changed final cash flow", solve_irr(changed_flows))


def task_12():
    def equations(z):
        x, y = z
        return [x**2 + y**2 - 4, y - (x**2 - 1)]

    print("\nTASK 12 NONLINEAR EQUATIONS")
    for guess in ([1., 1.], [-1., 1.], [-1.5, 1.5]):
        result = root(equations, guess)
        print("Initial guess", guess, "intersection", result.x,
              "residual", equations(result.x), "success", result.success)


def task_13():
    hours = np.array([8, 9, 10, 11, 12, 13, 14], dtype=float)
    temp = np.array([18., 20., 22.5, 24., 25., 25.5, 25.])
    changed = temp.copy()
    changed[2] += 1.0
    print("\nTASK 13 INTERPOLATION")
    for values in (temp, changed):
        linear = interp1d(hours, values, kind="linear")
        cubic = CubicSpline(hours, values)
        print("Linear at 10 30", float(linear(10.5)),
              "Cubic at 10 30", float(cubic(10.5)))
    dense = np.linspace(8, 14, 200)
    plt.scatter(hours, temp, label="Measurements")
    plt.plot(dense, interp1d(hours, temp)(dense), label="Linear")
    plt.plot(dense, CubicSpline(hours, temp)(dense), label="Cubic spline")
    plt.xlabel("Hour")
    plt.ylabel("Temperature")
    plt.title("Temperature interpolation")
    plt.legend()
    plt.grid(True)
    plt.show()


def task_14():
    users = np.array([50, 100, 150, 200, 250, 300, 350], dtype=float)
    response = np.array([82, 95, 115, 145, 185, 238, 305], dtype=float)
    changed = response.copy()
    changed[-1] += 20

    def model(x, a, b, c):
        return a*x**2 + b*x + c

    print("\nTASK 14 CURVE FITTING")
    for observed in (response, changed):
        params, _ = curve_fit(model, users, observed)
        rmse = np.sqrt(np.mean((observed - model(users, *params))**2))
        print("Coefficients", params, "RMSE", rmse,
              "Prediction at 400 users", model(400, *params))
    x_plot = np.linspace(users.min(), 400, 300)
    params, _ = curve_fit(model, users, response)
    plt.scatter(users, response, label="Measurements")
    plt.plot(x_plot, model(x_plot, *params), label="Fitted curve")
    plt.xlabel("Concurrent users")
    plt.ylabel("Response time")
    plt.title("Server response time curve fitting")
    plt.legend()
    plt.grid(True)
    plt.show()


def task_15():
    time = np.arange(7, dtype=float)
    position = np.array([0., 4.8, 10.2, 16.1, 22.7, 30., 38.])
    changed = position.copy()
    changed[3] += 1.
    print("\nTASK 15 NUMERICAL DIFFERENTIATION")
    for values in (position, changed):
        print("Estimated speed", np.gradient(values, time))
    plt.plot(time, np.gradient(position, time), marker="o")
    plt.xlabel("Time")
    plt.ylabel("Estimated speed")
    plt.title("Speed from GPS positions")
    plt.grid(True)
    plt.show()


def task_16():
    time = np.array([0, 2, 4, 6, 8, 10, 12], dtype=float)
    power = np.array([0.8, 1.0, 1.4, 1.8, 1.6, 1.2, 0.9])
    changed = power.copy()
    changed[3] += 0.2
    print("\nTASK 16 NUMERICAL INTEGRATION")
    for values in (power, changed):
        print("Trapezoidal energy", np.trapezoid(values, time),
              "Simpson energy", simpson(values, x=time), "kWh")


def task_17():
    ambient, initial, k, end_time = 25., 90., 0.12, 30.
    print("\nTASK 17 EULER ODE")
    for step in (1.0, 0.5):
        times = np.arange(0, end_time + step, step)
        temperature = np.zeros_like(times)
        temperature[0] = initial
        for i in range(len(times) - 1):
            temperature[i + 1] = temperature[i] - step * k * (temperature[i] - ambient)
        exact = ambient + (initial - ambient) * np.exp(-k * times)
        print("Step", step, "final Euler", temperature[-1],
              "exact", exact[-1], "absolute error", abs(temperature[-1] - exact[-1]))
        plt.plot(times, temperature, label=f"Euler step {step}")
    plt.xlabel("Time minutes")
    plt.ylabel("Temperature")
    plt.title("Cooling using Euler method")
    plt.legend()
    plt.grid(True)
    plt.show()


def task_18():
    supply, capacitance, initial = 5., 0.001, 0.
    print("\nTASK 18 SCIPY ODE SOLUTION")
    for resistance in (1000., 2000.):
        def circuit(t, voltage):
            return [(supply - voltage[0]) / (resistance * capacitance)]

        times = np.linspace(0, 5, 200)
        solution = solve_ivp(circuit, (0, 5), [initial], t_eval=times,
                             rtol=1e-9, atol=1e-11)
        exact = supply * (1 - np.exp(-solution.t / (resistance * capacitance)))
        print("Resistance", resistance, "voltage at five seconds",
              solution.y[0, -1], "maximum error",
              np.max(np.abs(solution.y[0] - exact)))
        plt.plot(solution.t, solution.y[0], label=f"R {resistance:.0f}")
    plt.xlabel("Time seconds")
    plt.ylabel("Capacitor voltage")
    plt.title("RC circuit charging")
    plt.legend()
    plt.grid(True)
    plt.show()


def task_19():
    def cost(z):
        x, y = z
        return 12*x + 18*y

    print("\nTASK 19 OPTIMIZATION")
    for required in (1000., 1200.):
        constraint = {
            "type": "ineq",
            "fun": lambda z, required=required: 100*z[0] + 170*z[1] - required
        }
        result = minimize(cost, [5, 3], method="SLSQP",
                          bounds=[(0, None), (0, None)], constraints=constraint)
        x, y = result.x
        best_integer = min(
            (12*a + 18*b, a, b, 100*a + 170*b)
            for a in range(21) for b in range(21)
            if 100*a + 170*b >= required
        )
        print("Required capacity", required, "continuous allocation", result.x,
              "cost", result.fun, "capacity", 100*x + 170*y,
              "best integer allocation", best_integer)


def task_20():
    rng = np.random.default_rng(42)
    capacity, mean_demand, trials = 1000., 850., 100_000
    print("\nTASK 20 MONTE CARLO")
    for standard_deviation in (120., 150.):
        demand = rng.normal(mean_demand, standard_deviation, trials)
        overloaded = demand > capacity
        print("Demand standard deviation", standard_deviation,
              "estimated overload probability", overloaded.mean(),
              "overload cases", overloaded.sum(), "of", trials)
        running = np.cumsum(overloaded) / np.arange(1, trials + 1)
        indices = np.unique(np.logspace(1, np.log10(trials), 200).astype(int)) - 1
        plt.semilogx(indices + 1, running[indices],
                     label=f"Standard deviation {standard_deviation}")
    plt.xlabel("Number of simulations")
    plt.ylabel("Estimated overload probability")
    plt.title("Monte Carlo server overload estimate")
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    tasks = (
        task_02, task_03, task_04, task_05, task_06, task_07, task_08,
        task_09, task_10, task_11, task_12, task_13, task_14, task_15,
        task_16, task_17, task_18, task_19, task_20
    )
    for task in tasks:
        task()


if __name__ == "__main__":
    main()
