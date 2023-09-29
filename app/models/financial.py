# ============================================================================= 
#-*- coding: utf-8 -*-
# =============================================================================
# Created By  : Abhisek Ashirbad Sethy
# Created On  : 29/09/2023
# © Copyright by Abhisek Ashirbad Sethy
# =============================================================================

# Imports
from pydantic import BaseModel
from income_statement import IncomeStatement


class Financial(BaseModel):
    income_statement: IncomeStatement
    balance_sheet: BalanceSheet
    cash_flow: CashFlow

    def __init__(self, income_statement: IncomeStatement, balance_sheet: BalanceSheet,\
                  cash_flow: CashFlow):
        self.income_statement = income_statement
        self.balance_sheet = balance_sheet
        self.cash_flow = cash_flow