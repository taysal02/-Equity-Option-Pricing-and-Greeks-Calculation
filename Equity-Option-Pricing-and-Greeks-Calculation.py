#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 13:12:43 2024

@author: Tayyib Salawu
"""

import numpy as np
from scipy.stats import norm

class Equity:
    def __init__(self, spot, dividend_yield, volatility):
        self.spot = spot
        self.dividend_yield = dividend_yield
        self.volatility = volatility
        
    def __eq__(self, other):
        if isinstance(other, Equity):
            return (self.spot == other.spot and self.dividend_yield == other.dividend_yield and self.volatility == other.volatility)
        return False
    
class EquityOption:
    def __init__(self, strike, time_to_maturity, put_call):
        self.strike = strike
        self.time_to_maturity = time_to_maturity
        self.put_call = put_call
        
    def __eq__(self, other):
        if isinstance(other, EquityOption):
            return (self.strike == other.strike and self.time_to_maturity == other.time_to_maturity and self.put_call == other.put_call)
        return False
    
def bsm_pricer(underlying, option, rate):
    S = underlying.spot
    K = option.strike
    r = rate
    q = underlying.dividend_yield
    T = option.time_to_maturity
    sigma = underlying.volatility
    
    d1 = (np.log(S/K) + (r - q + (sigma**2/2))*T) / (sigma * np.sqrt(T))
    d2 = d1 - (sigma * np.sqrt(T))
    
    if option.put_call == "call":
        price = (S * np.exp(-q * T) * norm.cdf(d1)) - (K * np.exp(-r * T) * norm.cdf(d2))
    elif option.put_call == "put":
        price = (K * np.exp(-r * T) * norm.cdf(-d2)) - (S * np.exp(-q * T) * norm.cdf(-d1))
    else:
        ValueError("Invalid Option Type. Should either be 'put' or 'call'.")
        
    return price
        
def bsm_delta(underlying, option, rate):
    S = underlying.spot
    h = 0.001 * S
    
    bumped_up = Equity(S + h, underlying.dividend_yield, underlying.volatility)
    bumped_down = Equity(S - h, underlying.dividend_yield, underlying.volatility)
    
    price_up = bsm_pricer(bumped_up, option, rate)
    price_down = bsm_pricer(bumped_down, option, rate)
    
    delta = (price_up - price_down) / 2*h
    return delta

def bsm_gamma(underlying, option, rate):
    S = underlying.spot
    h = 0.001 * S
    
    bumped_up = Equity(S + h, underlying.dividend_yield, underlying.volatility)
    bumped_down = Equity(S - h, underlying.dividend_yield, underlying.volatility)
    
    price_up = bsm_pricer(bumped_up, option, rate)
    price_down = bsm_pricer(bumped_down, option, rate)
    price = bsm_pricer(underlying, option, rate)
    gamma = (price_up - 2*price + price_down) / (h**2)
    return gamma

class EquityForward:
    def __init__(self, strike, time_to_maturity):
        self.strike = strike
        self.time_to_maturity = time_to_maturity
        
    def __eq__(self, other):
        if isinstance(other, EquityForward):
            return (self.strike == other.strike and self.time_to_maturity == other.time_to_maturity)
        return False

def fwd_pricer(underlying, option, rate):
    S = underlying.spot
    r = rate
    T = option.time_to_maturity
    q = underlying.dividend_yield
    
    price = S * np.exp((r - q)*T)
    return price


# Create Equity object
stock = Equity(spot=100, dividend_yield=0.02, volatility=0.2)

# Create EquityOption objects
call_option = EquityOption(strike=105, time_to_maturity=1, put_call="call")
put_option = EquityOption(strike=105, time_to_maturity=1, put_call="put")

# Test bsm_pricer
try:
    call_price = bsm_pricer(stock, call_option, rate=0.05)
    put_price = bsm_pricer(stock, put_option, rate=0.05)
    print(f"Call Option Price: {call_price}")
    print(f"Put Option Price: {put_price}")
except Exception as e:
    print(f"Error in bsm_pricer: {e}")

# Test bsm_delta
try:
    call_delta = bsm_delta(stock, call_option, rate=0.05)
    print(f"Call Delta: {call_delta}")
except Exception as e:
    print(f"Error in bsm_delta: {e}")

# Test bsm_gamma
try:
    call_gamma = bsm_gamma(stock, call_option, rate=0.05)
    print(f"Call Gamma: {call_gamma}")
except Exception as e:
    print(f"Error in bsm_gamma: {e}")

# Test fwd_pricer
try:
    forward_contract = EquityForward(strike=105, time_to_maturity=1)
    forward_price = fwd_pricer(stock, forward_contract, rate=0.05)
    print(f"Forward Price: {forward_price}")
except Exception as e:
    print(f"Error in fwd_pricer: {e}")

    
    
        