# 📈 Volatility Surface Project

This project focuses on constructing, visualizing, and analyzing the **volatility surface** of a specific stock using options data. A volatility surface captures how the market's expectations of future volatility vary by option strike price and time to expiration.

---

## 🔍 What Is a Volatility Surface?

A **volatility surface** is a 3D representation of implied volatility (IV) across:

- **Strike price** (x-axis)
- **Time to expiration** (y-axis)
- **Implied volatility** (z-axis)

It reflects the **market's pricing of risk** for options on a specific stock.

---

## ✅ Why It Matters

| Benefit                   | Explanation                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| 🎯 Realistic Pricing       | Models the actual market behavior better than constant-volatility models   |
| 🔎 Market Insight          | Reveals sentiment (fear, event anticipation, etc.) through skew/smile shapes |
| 🧪 Strategy Design         | Helps build and backtest profitable options strategies                      |
| 🛡️ Risk Management         | Essential for calculating Greeks like Vega and Gamma                        |
| 🧠 Quantitative Modeling   | Enables forecasting, machine learning, or arbitrage models on IV surfaces   |

---

## 📊 Example Use Cases

- Price options using realistic IV inputs  
- Visualize the volatility skew or smile  
- Detect mispriced options (volatility arbitrage)  
- Compare **implied vs realized volatility**  
- Study how market sentiment changes over time  

---

## 🚀 Next Steps

To get started:

1. Choose a stock (e.g., AAPL, TSLA)
2. Pull options data using [`yfinance`](https://pypi.org/project/yfinance/) or another data provider
3. Extract or calculate implied volatilities
4. Visualize the surface with `matplotlib`, `plotly`, or `plot_surface`
5. Analyze patterns and build models

---

## ? So how is Implied Volatility Calculated

Implied Volatility is the value of the volatility σ that satisfies an option pricing model. We will
use the Black-Schole Option Pricing Formula to calculate our value of σ. As there is not closed formula for
σ, we must solve it numerically in one or more of the following ways such as Newtons method, Bisection method
and other root finding algorithms.

We will begin using newtons method:

---

# 📈 Black-Scholes Option Pricing Formula

The price of a European call option can be given by the **Black-Scholes formula**:

`C = S₀ * N(d₁) - K * exp(-r * T) * N(d₂)`

Where:

- \( C \): Call option price  
- \( S_0 \): Current stock price  
- \( K \): Strike price  
- \( T \): Time to expiration (in years)  
- \( r \): Risk-free interest rate  
- \( \sigma \): Volatility of the stock (standard deviation of returns)  
- \( N(\cdot) \): Cumulative distribution function (CDF) of the standard normal distribution

The intermediate variables are:

\[
d_1 = \frac{\ln(S_0 / K) + (r + \frac{\sigma^2}{2})T}{\sigma \sqrt{T}}
\]

\[
d_2 = d_1 - \sigma \sqrt{T}
\]

---

## 🧠 Intuition

- The formula assumes **no arbitrage**, **constant interest rate**, and that the stock follows a **log-normal distribution**.
- It gives a theoretical fair price for a European-style option, which can be compared to actual market prices.
- The **implied volatility (IV)** can be backed out by solving the equation in reverse.

---

## 📦 Usage

You can use this formula to:

- Compute theoretical option prices.
- Extract **implied volatility** from market option prices.
- Visualize how option prices change with volatility, time, strike, etc.

---

# 🧮 Newton's Method

Newton's Method is a powerful technique used to find the **roots of a function**, i.e., the values of \( x \) for which \( f(x) = 0 \).

---

## 🔍 Purpose

The idea is to start with an **initial guess** for the root of a function and then refine that guess using the function's **tangent line**. The root of the tangent line is usually a better approximation of the actual root than the original guess. This process is **iterated** to improve the approximation.

---

## ✏️ Linear Approximation

For a differentiable function \( f(x) \), the **best linear approximation** near a point \( x_n \) is its **tangent line**:

\[
f(x) \approx f(x_n) + f'(x_n)(x - x_n)
\]

The **root** of this tangent line (i.e., where it intersects the \( x \)-axis) becomes the next approximation \( x_{n+1} \).

---

## 🔁 Iterative Formula

The update rule for Newton's Method is:

\[
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
\]

Each iteration usually brings the estimate closer to the actual root.

---

## 🧠 Convergence

- The method can be **started from any initial guess** \( x_0 \), although starting closer to a true root improves speed and reliability.
- It **typically converges** if \( f'(x_0) \ne 0 \).
- If the root has **multiplicity 1** and the function behaves nicely, convergence is at least **quadratic** — meaning the number of correct digits roughly **doubles with each step**.

---

## 🔗 References

- [Black-Scholes on Wikipedia](https://en.wikipedia.org/wiki/Black–Scholes_model)
- [Investopedia: Black-Scholes Model](https://www.investopedia.com/terms/b/blackscholes.asp)
- https://en.wikipedia.org/wiki/Newton%27s_method
- https://www.youtube.com/watch?v=A5w-dEgIU1M

---

