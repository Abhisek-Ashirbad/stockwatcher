# ============================================================================= 
#-*- coding: utf-8 -*-
# =============================================================================
# Created By  : Abhisek Ashirbad Sethy
# Created On  : 29/09/2023
# © Copyright by Abhisek Ashirbad Sethy
# =============================================================================

# Imports
from pydantic import BaseModel
from financial import Financial

class Stock(BaseModel):
    financial: Financial

    def __init__(self, financial: Financial):
        self.financial = financial