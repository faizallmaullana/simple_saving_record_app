from app import api
from app.controllers.edit_data import Incomes_Resource, Outcomes_Resource
from app.controllers.get_sum import GetSumIncomeResource



def adding_api_path():
    api.add_resource(Incomes_Resource, "/api/income")
    api.add_resource(Outcomes_Resource, "/api/outcome")
    api.add_resource(GetSumIncomeResource, "/api/getSumIncome")