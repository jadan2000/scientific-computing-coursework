"""Additional individual real-world cases for BIT 2118 tasks 2 to 20.

Each case is a separate application from the corresponding practical example.
All data are illustrative and calculations are reproducible.
"""
from __future__ import annotations

import numpy as np
from scipy.linalg import lu_factor, lu_solve
from scipy.optimize import root_scalar, root, curve_fit, minimize
from scipy.interpolate import interp1d
from scipy.integrate import simpson, solve_ivp


def run_cases() -> None:
    # TASK 2: irrigation water readings in litres per hour
    flow = np.array([12, 14, 13, 15, 16, 14], dtype=float)
    print("\nTASK 2 | Irrigation flow")
    print(f"Total={flow.sum():.2f} L, mean={flow.mean():.2f} L/h, peak={flow.max():.2f} L/h")
    print(f"Supply with 10% leakage allowance={flow.sum() * 1.10:.2f} L")
    print(f"Supply with 5% leakage allowance={flow.sum() * 1.05:.2f} L")

    # TASK 3: vectorized image brightness normalization
    pixels = np.array([35, 80, 120, 180, 220], dtype=float)
    normalized = pixels / 255.0
    print("\nTASK 3 | Image pixel normalization")
    print("Normalized pixels:", np.round(normalized, 4))
    print("Mean brightness:", round(float(normalized.mean()), 4))
    print("Changed exposure +15:", np.round(np.clip((pixels + 15) / 255, 0, 1), 4))

    # TASK 4: floating point tolerance for an invoice total
    invoice_lines = np.array([19.99, 5.49, 3.25])
    computed, expected = float(invoice_lines.sum()), 28.73
    print("\nTASK 4 | Invoice total validation")
    print(f"Computed={computed:.12f}; expected={expected:.2f}")
    print("Within one cent:", bool(np.isclose(computed, expected, atol=0.01)))
    print("With zero tolerance:", bool(np.isclose(computed, expected, atol=0.0)))

    # TASK 5: warehouse robot coordinate transformation
    points = np.array([[1., 0.], [0., 1.], [1., 1.]])
    translation = np.array([2., 1.])
    def transform(degrees: float) -> np.ndarray:
        angle = np.deg2rad(degrees)
        rotation = np.array([[np.cos(angle), -np.sin(angle)],
                             [np.sin(angle), np.cos(angle)]])
        return points @ rotation.T + translation
    print("\nTASK 5 | Robot coordinate transformation")
    print("At 30 degrees:\n", np.round(transform(30), 4))
    print("First point at 60 degrees:", np.round(transform(60)[0], 4))

    # TASK 6: animal feed formulation from nutrient targets
    matrix = np.array([[20., 10.], [5., 25.]])
    target = np.array([30., 35.])
    blend = np.linalg.solve(matrix, target)
    changed_blend = np.linalg.solve(matrix, np.array([30., 40.]))
    print("\nTASK 6 | Animal feed formulation")
    print(f"Target 30 protein, 35 carbohydrate: A={blend[0]:.3f} kg, B={blend[1]:.3f} kg")
    print(f"Changed carbohydrate target 40: A={changed_blend[0]:.3f} kg, B={changed_blend[1]:.3f} kg")
    print("Verified original nutrient totals:", np.round(matrix @ blend, 3))

    # TASK 7: reuse LU factorization as factory orders change
    matrix = np.array([[3., 1.], [1., 2.]])
    factors = lu_factor(matrix)
    print("\nTASK 7 | Factory material balance")
    for demand in (np.array([10., 8.]), np.array([11., 8.])):
        print("Demand", demand, "production quantities", np.round(lu_solve(factors, demand), 4))

    # TASK 8: Gauss-Seidel steady-state room temperature calculation
    matrix = np.array([[4., -1., 0.], [-1., 4., -1.], [0., -1., 3.]])
    rhs = np.array([50., 30., 20.])
    def gauss_seidel(tolerance: float) -> tuple[np.ndarray, int, float]:
        x = np.zeros(3)
        for iteration in range(1, 1001):
            old = x.copy()
            for i in range(3):
                x[i] = (rhs[i] - matrix[i, :i] @ x[:i] -
                        matrix[i, i+1:] @ old[i+1:]) / matrix[i, i]
            if np.linalg.norm(x-old, ord=np.inf) < tolerance:
                return x, iteration, float(np.linalg.norm(matrix @ x-rhs, ord=np.inf))
        raise RuntimeError("Gauss-Seidel did not converge within 1000 iterations")
    print("\nTASK 8 | Building heat distribution")
    for tol in (1e-8, 1e-10):
        values, count, residual = gauss_seidel(tol)
        print(f"Tolerance={tol:g}, values={np.round(values, 6)}, iterations={count}, residual={residual:.3e}")

    # TASK 9: influence scores in a referral network
    adjacency = np.array([[0., 1., 1.], [1., 0., 1.], [1., 0., 0.]])
    def influence_scores(graph: np.ndarray) -> np.ndarray:
        vals, vecs = np.linalg.eig(graph)
        vector = np.real(vecs[:, np.argmax(np.real(vals))])
        vector = np.abs(vector)
        return vector / vector.sum()
    changed_graph = adjacency.copy()
    changed_graph[2, 1] = 1.
    print("\nTASK 9 | Community referral influence")
    print("Original scores:", np.round(influence_scores(adjacency), 4))
    print("After adding referral edge 3 to 2:", np.round(influence_scores(changed_graph), 4))

    # TASK 10: bisection and fixed-point break-even methods
    def profit(q: float, fixed_cost: float = 600.) -> float:
        return 45*q - (fixed_cost + 25*q)
    bis = root_scalar(profit, bracket=[0, 100], method="bisect")
    # q = (fixed cost)/(selling price - variable cost), written as a fixed point
    def fixed_point(fixed_cost: float, initial: float) -> tuple[float, int]:
        q = initial
        for n in range(1, 101):
            updated = fixed_cost / 20.0
            if abs(updated-q) < 1e-10:
                return updated, n
            q = updated
        raise RuntimeError("Fixed-point iteration did not converge")
    print("\nTASK 10 | Small business break-even")
    print("Bisection quantity:", round(float(bis.root), 4))
    print("Fixed-point quantity:", fixed_point(600., 20.)[0])
    print("Changed fixed cost 700, break-even:", root_scalar(
        lambda q: profit(q, 700.), bracket=[0, 100], method="bisect").root)

    # TASK 11: investment internal rate of return
    cashflows = [-10000., 3000., 3500., 4000.]
    def npv(rate: float, values: list[float]) -> float:
        return sum(cf/(1+rate)**i for i, cf in enumerate(values))
    rate = root_scalar(lambda r: npv(r, cashflows), bracket=[0., 1.], method="brentq").root
    changed = cashflows.copy()
    changed[-1] += 500
    changed_rate = root_scalar(lambda r: npv(r, changed), bracket=[0., 1.], method="brentq").root
    print("\nTASK 11 | Equipment investment return")
    print(f"Original IRR={rate:.4%}; increased final receipt IRR={changed_rate:.4%}")

    # TASK 12: road boundary intersection from nonlinear equations
    def equations(z: np.ndarray) -> list[float]:
        x, y = z
        return [x*x+y*y-25, y-0.5*x-1]
    solution = root(equations, [2., 2.])
    print("\nTASK 12 | Road alignment and circular boundary")
    print("Intersection:", np.round(solution.x, 5), "residual:", np.round(equations(solution.x), 8))
    changed_solution = root(equations, [-4., -1.])
    print("Alternative starting guess result:", np.round(changed_solution.x, 5))

    # TASK 13: interpolate a missing rainfall reading
    days = np.array([1, 2, 4, 5], dtype=float)
    rain = np.array([4., 8., 14., 10.])
    estimate = float(interp1d(days, rain)(3.))
    changed = rain.copy()
    changed[1] = 10.
    changed_estimate = float(interp1d(days, changed)(3.))
    print("\nTASK 13 | Rainfall gap estimation")
    print(f"Day 3 estimate={estimate:.2f} mm; changed day 2 reading estimate={changed_estimate:.2f} mm")

    # TASK 14: quadratic crop-yield curve fitting
    fertilizer = np.array([0, 10, 20, 30, 40], dtype=float)
    yield_t = np.array([2.0, 2.8, 3.5, 4.0, 4.3])
    def model(x: np.ndarray, a: float, b: float, c: float) -> np.ndarray:
        return a*x*x+b*x+c
    params, _ = curve_fit(model, fertilizer, yield_t)
    prediction = float(model(35, *params))
    changed_yield = yield_t.copy()
    changed_yield[-1] += 0.2
    changed_params, _ = curve_fit(model, fertilizer, changed_yield)
    print("\nTASK 14 | Fertilizer and crop yield")
    print(f"Predicted yield at 35 kg/ha={prediction:.3f} tonnes/ha")
    print(f"Changed final observation prediction={float(model(35, *changed_params)):.3f} tonnes/ha")
    print("RMSE:", float(np.sqrt(np.mean((yield_t-model(fertilizer, *params))**2))))

    # TASK 15: differentiate vehicle speed to estimate acceleration
    times = np.array([0., 1., 2., 3., 4.])
    speed = np.array([0., 4., 9., 15., 22.])
    changed_speed = np.array([0., 4., 10., 15., 22.])
    print("\nTASK 15 | Vehicle acceleration")
    print("Original acceleration:", np.round(np.gradient(speed, times), 3))
    print("Changed acceleration:", np.round(np.gradient(changed_speed, times), 3))

    # TASK 16: integrate water flow rate to estimate delivered volume
    time_min = np.array([0., 5., 10., 15., 20.])
    flow_lpm = np.array([8., 10., 12., 11., 9.])
    changed_flow = flow_lpm.copy()
    changed_flow[2] += 1.
    print("\nTASK 16 | Water delivery volume")
    print(f"Original={simpson(flow_lpm, x=time_min):.2f} L; changed={simpson(changed_flow, x=time_min):.2f} L")

    # TASK 17: Euler approximation for food cooling
    def euler_cooling(step: float) -> float:
        ambient, temperature, cooling, duration = 22., 70., 0.08, 10.
        for _ in range(round(duration/step)):
            temperature += step*(-cooling*(temperature-ambient))
        return temperature
    print("\nTASK 17 | Food cooling")
    print(f"Euler dt=0.5 min: {euler_cooling(0.5):.3f} C; dt=0.25 min: {euler_cooling(0.25):.3f} C")

    # TASK 18: solve water tank level ODE using SciPy
    def tank_model(inflow: float):
        drainage, area = 0.002, 2.0
        return lambda t, h: [(inflow-drainage*np.sqrt(max(h[0], 0.0)))/area]
    print("\nTASK 18 | Water tank level dynamics")
    for inflow in (0.03, 0.04):
        sol = solve_ivp(tank_model(inflow), (0, 60), [0.2], t_eval=[0, 15, 30, 45, 60])
        if not sol.success:
            raise RuntimeError(sol.message)
        print(f"Inflow={inflow:.2f} m3/min, levels={np.round(sol.y[0], 4)}")

    # TASK 19: optimize parcel delivery cost
    objective = lambda z: 80*z[0] + 110*z[1]
    constraint = {"type": "ineq", "fun": lambda z: 120*z[0]+200*z[1]-500}
    opt = minimize(objective, [2., 2.], method="SLSQP",
                   bounds=[(0, None), (0, None)], constraints=constraint)
    if not opt.success:
        raise RuntimeError(opt.message)
    integer_plan = min((80*a+110*b, a, b, 120*a+200*b)
                       for a in range(6) for b in range(4)
                       if 120*a+200*b >= 500)
    print("\nTASK 19 | Parcel delivery optimization")
    print(f"Continuous cost={opt.fun:.2f}; trips A={opt.x[0]:.3f}, B={opt.x[1]:.3f}")
    print("Best whole-trip plan (cost, A trips, B trips, capacity):", integer_plan)

    # TASK 20: Monte Carlo electricity demand risk
    rng = np.random.default_rng(2118)
    print("\nTASK 20 | Electricity supply risk")
    for deviation in (100., 140.):
        demand = rng.normal(900., deviation, 100_000)
        probability = float(np.mean(demand > 1000.))
        print(f"Demand standard deviation={deviation:.0f} kW; overload probability={probability:.4%}")


if __name__ == "__main__":
    run_cases()
