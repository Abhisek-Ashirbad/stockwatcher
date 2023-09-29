# ============================================================================= 
#-*- coding: utf-8 -*-
# =============================================================================
# Created By  : Abhisek Ashirbad Sethy
# Created On  : 29/09/2023
# © Copyright by Abhisek Ashirbad Sethy
# =============================================================================

# Imports
from pydantic import BaseModel

class IncomeStatement(BaseModel):
    revenue: float
    operating_expense: float
    net_income: float
    net_profit_margin: float
    earnings_per_share: float
    ebitda: float
    effective_tax_rate: float

    def __init__(self, revenue: float, operating_expense: float, net_income: float,\
                 net_profit_margin: float, earnings_per_share: float, ebitda: float,\
                 effective_tax_rate: float):
        self.revenue = revenue
        self.operating_expense = operating_expense
        self.net_income = net_income
        self.net_profit_margin = net_profit_margin
        self.earnings_per_share = earnings_per_share
        self.ebitda = ebitda
        self.effective_tax_rate = effective_tax_rate