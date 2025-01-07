#Equity-Option-Pricing-and-Greeks-Calculation
This project provides implementations for pricing equity options and calculating their Greeks (Delta and Gamma) using the Black-Scholes-Merton (BSM) model. Additionally, it includes functionality to price forward contracts on equities. The main objective is to model the financial instruments and use their properties for pricing and sensitivity analysis.

## Key Features

- **Equity Class**: Models the underlying equity, including its spot price, dividend yield, and volatility.
- **EquityOption Class**: Models an equity option, including strike price, time to maturity, and option type (put or call).
- **BSM Pricer**: Implements the Black-Scholes-Merton model for pricing call and put options.
- **Greeks Calculation**: Implements functions to calculate Delta and Gamma for equity options.
- **Forward Contract Pricer**: Models and prices equity forward contracts.

## Modules

### `Equity` Class
This class models the underlying equity with the following attributes:
- `spot`: The spot price of the equity.
- `dividend_yield`: The dividend yield of the equity.
- `volatility`: The volatility of the equity.
