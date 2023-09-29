# ============================================================================= 
#-*- coding: utf-8 -*-
# =============================================================================
# Created By  : Abhisek Ashirbad Sethy
# Created On  : 29/09/2023
# © Copyright by Abhisek Ashirbad Sethy
# =============================================================================

# Imports
from dotenv import load_dotenv
import os

#Load the environment variables from .env file.
load_dotenv()
HOST = os.getenv("MICROSERVICE_HOST")
PORT = int(os.getenv("MICROSERVICE_PORT"))
