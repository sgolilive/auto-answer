from typing import Iterator

from ingestion.content.generators.BaseGenerator import BaseGenerator
from ingestion.content.generators.web_development import WebDevelopment
from ingestion.content.generators.system_design import SystemDesign
from ingestion.content.generators.stats import AdvancedMathematics
from ingestion.content.generators.space import SpaceTechnology
from ingestion.content.generators.sociology import Sociology
from ingestion.content.generators.science import Science
from ingestion.content.generators.robotics import Robotics
from ingestion.content.generators.quantum_computing import QuantumComputing
from ingestion.content.generators.psychiatry import Psychiatry
from ingestion.content.generators.ps import Pharmaceutical
from ingestion.content.generators.programming import ProgGenerator
from ingestion.content.generators.physics import PhysicsGenerator
from ingestion.content.generators.philosophy import Philosophy
from ingestion.content.generators.os import OperatingSystems
from ingestion.content.generators.nuro import Neuroscience
from ingestion.content.generators.nlp import LLMNLP
from ingestion.content.generators.networking import Networking
from ingestion.content.generators.nano_tech import Nanotech
from ingestion.content.generators.mobile_development import MobileDevelopment
from ingestion.content.generators.meteorology import Meteorology
from ingestion.content.generators.me import MaterialEngineering
from ingestion.content.generators.mb import MarineBiology
from ingestion.content.generators.maths import Mathematics
from ingestion.content.generators.management import Management
from ingestion.content.generators.lr import LogicalReasoning
from ingestion.content.generators.legal import LegalStudies
from ingestion.content.generators.iot_2 import EdgeComputing
from ingestion.content.generators.iot import IoT
from ingestion.content.generators.investment import FinanceInvestment
from ingestion.content.generators.hci import HCI
from ingestion.content.generators.hc import HealthCare
from ingestion.content.generators.gs import EnergySystems
from ingestion.content.generators.finance import Finance
from ingestion.content.generators.evs import EnvironmentalScience
from ingestion.content.generators.ethics import Ethics
from ingestion.content.generators.energey import RenewableEnergy
from ingestion.content.generators.em import PhysicsEngineeringMechanics
from ingestion.content.generators.economics import Economics
from ingestion.content.generators.ds import DataScienceAnalytics
from ingestion.content.generators.devops import CloudDevOps
from ingestion.content.generators.de import DataEngineering
from ingestion.content.generators.database import Database
from ingestion.content.generators.cyber_security import CyberSecurity
from ingestion.content.generators.chemistry import Chemistry
from ingestion.content.generators.ce import ChemicalEngineering
from ingestion.content.generators.block_chain import BlackChain
from ingestion.content.generators.bio_tech import BioTechnologyAndGeneticEngineering
from ingestion.content.generators.astronomy import  AstronomyAndAstrophysics
from ingestion.content.generators.ar import ARVR
from ingestion.content.generators.ap import AstrophysicsAndSpaceExploration
from ingestion.content.generators.ai_2 import AIRobotics
from ingestion.content.generators.ai import AIML
from ingestion.content.generators.ag import AgriSciAndFoodTech

def get_generators() -> Iterator[dict]:
    yield from [
        {'gen': WebDevelopment(), 'st': 1, 'ed': 2001},
        {'gen': SystemDesign(), 'st': 2001, 'ed': 4001},
        {'gen': AdvancedMathematics(), 'st': 4001, 'ed': 6001},
        {'gen': SpaceTechnology(), 'st': 6001, 'ed': 8001},
        {'gen': Sociology(), 'st': 8001, 'ed': 10001},
        {'gen': Science(), 'st': 10001, 'ed': 12001},
        {'gen': Robotics(), 'st': 12001, 'ed': 14001},
        {'gen': QuantumComputing(), 'st': 14001, 'ed': 16001},
        {'gen': Psychiatry(), 'st': 16001, 'ed': 18001},
        {'gen': Pharmaceutical(), 'st': 18001, 'ed': 20001},
        {'gen': ProgGenerator(), 'st': 20001, 'ed': 22001},
        {'gen': PhysicsGenerator(), 'st': 22001, 'ed': 24001},
        {'gen': Philosophy(), 'st': 24001, 'ed': 26001},
        {'gen': OperatingSystems(), 'st': 26001, 'ed': 28001},
        {'gen': Neuroscience(), 'st': 28001, 'ed': 30001},
        {'gen': LLMNLP(), 'st': 30001, 'ed': 32001},
        {'gen': Networking(), 'st': 32001, 'ed': 34001},
        {'gen': Nanotech(), 'st': 34001, 'ed': 36001},
        {'gen': MobileDevelopment(), 'st': 36001, 'ed': 38001},
        {'gen': Meteorology(), 'st': 38001, 'ed': 40001},
        {'gen': MaterialEngineering(), 'st': 40001, 'ed': 42001},
        {'gen': MarineBiology(), 'st': 42001, 'ed': 44001},
        {'gen': Mathematics(), 'st': 44001, 'ed': 46001},
        {'gen': Management(), 'st': 46001, 'ed': 48001},
        {'gen': AstronomyAndAstrophysics(), 'st': 48001, 'ed': 50001},
        {'gen': BioTechnologyAndGeneticEngineering(), 'st': 50001, 'ed': 52001},
        {'gen': BlackChain(), 'st': 52001, 'ed': 54001},
        {'gen': ChemicalEngineering(), 'st': 54001, 'ed': 56001},
        {'gen': Chemistry(), 'st': 56001, 'ed': 58001},
        {'gen': CyberSecurity(), 'st': 58001, 'ed': 60001},
        {'gen': Database(), 'st': 60001, 'ed': 62001},
        {'gen': DataEngineering(), 'st': 62001, 'ed': 64001},
        {'gen': CloudDevOps(), 'st': 64001, 'ed': 66001},
        {'gen': DataScienceAnalytics(), 'st': 66001, 'ed': 68001},
        {'gen': Economics(), 'st': 68001, 'ed': 70001},
        {'gen': PhysicsEngineeringMechanics(), 'st': 70001, 'ed': 72001},
        {'gen': RenewableEnergy(), 'st': 72001, 'ed': 74001},
        {'gen': Ethics(), 'st': 74001, 'ed': 76001},
        {'gen': EnvironmentalScience(), 'st': 76001, 'ed': 78001},
        {'gen': Finance(), 'st': 78001, 'ed': 80001},
        {'gen': EnergySystems(), 'st': 80001, 'ed': 82001},
        {'gen': HealthCare(), 'st': 82001, 'ed': 84001},
        {'gen': HCI(), 'st': 84001, 'ed': 86001},
        {'gen': FinanceInvestment(), 'st': 86001, 'ed': 88001},
        {'gen': IoT(), 'st': 88001, 'ed': 90001},
        {'gen': EdgeComputing(), 'st': 90001, 'ed': 92001},
        {'gen': LegalStudies(), 'st': 92001, 'ed': 94001},
        {'gen': LogicalReasoning(), 'st': 94001, 'ed': 96001},
        {'gen': ARVR(), 'st': 96001, 'ed': 98001},
        {'gen': AstrophysicsAndSpaceExploration(), 'st': 98001, 'ed': 100001},
        {'gen': AIRobotics(), 'st': 100001, 'ed': 102001},
        {'gen': AIML(), 'st': 102001, 'ed': 104001},
        {'gen': AgriSciAndFoodTech(), 'st': 104001, 'ed': 106001},
    ]