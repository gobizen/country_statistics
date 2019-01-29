from country_stats import CountryStatBase
from args_parser_country_stat import ArgsParser
import matplotlib.pyplot as plt
import time

class CountryStatistics(object):

    def __init__(self, args):
        self.args = args
        self.stat_base = CountryStatBase()

    def top_ten_countries_by_area(self):
        self.stat_base.top_country_by_area(False)

    def top_small_ten_countries_by_area(self):
        self.stat_base.top_country_by_area(True)

    def top_ten_countries_by_account_balance(self):
        self.stat_base.top_country_account_balance(False)

    def last_ten_countries_by_account_balance(self):
        self.stat_base.top_country_account_balance(True)

    def top_ten_dept_countries(self):
        self.stat_base.country_dept_to_foreign_countries(False)

    def top_ten_min_dept_countries(self):
        self.stat_base.country_dept_to_foreign_countries(True)

    def top_ten_electricity_consumption_countries(self):
        self.stat_base.top_ten_electricity_consumption_countries(False)

    def top_ten_electricity_min_consumption_countries(self):
        self.stat_base.top_ten_electricity_consumption_countries(True)

    def high_electricity_consumption_vs_production(self):
        self.stat_base.electricity_using_with_respect_to_production(False)

    def reverse_high_electricity_consumption_vs_production(self):
        self.stat_base.electricity_using_with_respect_to_production(True)

    def high_production_vs_electricity_consumption(self):
        self.stat_base.country_spending_more_power_then_production(False, False)

    def versa_high_production_vs_electricity_consumption(self):
        self.stat_base.country_spending_more_power_then_production(False, True)

    def countries_high_death_by_hiv_aids(self):
        self.stat_base.people_death_by_hiv(False)

    def countries_low_death_by_hiv_aids(self):
        self.stat_base.people_death_by_hiv(True)

    def countries_people_living_with_aids_high(self):
        self.stat_base.people_living_with_aids(False)

    def countries_people_living_with_aids_low(self):
        self.stat_base.people_living_with_aids(True)

    def country_has_longest_roadways(self):
        self.stat_base.country_has_long_or_short_roadways(False)

    def country_has_shortest_roadways(self):
        self.stat_base.country_has_long_or_short_roadways(True)

    def country_making_more_imports(self):
        self.stat_base.country_doing_more_imports(False)

    def country_making_less_imports(self):
        self.stat_base.country_doing_more_imports(True)

    def country_has_most_internet_users(self):
        self.stat_base.country_internet_users_stat(False)

    def country_has_less_internet_users(self):
        self.stat_base.country_internet_users_stat(True)

    def country_has_high_labor_heads(self):
        self.stat_base.country_labor_force_stat(False)

    def country_has_less_labor_heads(self):
        self.stat_base.country_labor_force_stat(True)

    def country_spending_more_for_military_services(self):
        self.stat_base.country_spending_expenditures_for_military(False)

    def country_spending_less_for_military_services(self):
        self.stat_base.country_spending_expenditures_for_military(True)

    def country_spend_high_percent_from_gdp_for_military(self):
        self.stat_base.country_spending_expenditures_for_military_from_gdp(False)

    def country_spend_low_percent_from_gdp_for_military(self):
        self.stat_base.country_spending_expenditures_for_military_from_gdp(True)

    def high_oil_consumption_countries(self):
        self.stat_base.top_oil_consumption_countries(False)

    def low_oil_consumption_countries(self):
        self.stat_base.top_oil_consumption_countries(True)

    def high_populated_countries(self):
        self.stat_base.population_rank(False)

    def low_populated_countries(self):
        self.stat_base.population_rank(True)

    def long_railway_line_countries(self):
        self.stat_base.railway_line_stat(False)

    def short_railway_line_countries(self):
        self.stat_base.railway_line_stat(True)

    def most_unemployed_people_countries(self):
        self.stat_base.top_unemployemnt_countries(False)

    def less_unemployed_people_countries(self):
        self.stat_base.top_unemployemnt_countries(True)

    def top_mobiles_users_countries(self):
        self.stat_base.top_mobile_users_country(False)

    def least_mobiles_users_countries(self):
        self.stat_base.top_mobile_users_country(True)

    def top_oil_production_countries(self):
        self.stat_base.oil_production_country_rank(False)

    def least_oil_production_countries(self):
        self.stat_base.oil_production_country_rank(True)

    def consumption_vs_producing_oil(self):
        self.stat_base.consuming_vs_production_oil_vice_versa(False)

    def versa_consumption_vs_producing_oil(self):
        self.stat_base.consuming_vs_production_oil_vice_versa(True)

    def top_industrial_production_grouth(self):
        self.stat_base.industrial_production_grouth_top_countries(False)

    def least_industrial_production_grouth(self):
        self.stat_base.industrial_production_grouth_top_countries(True)


    def trigger_function_asper_args(self):
        if (self.args.account_balance and not self.args.ascending):
            self.top_ten_countries_by_account_balance()

        if (self.args.account_balance and self.args.ascending):
            self.last_ten_countries_by_account_balance()

        if (self.args.area and not self.args.ascending):
            self.top_ten_countries_by_area()

        if (self.args.area and self.args.ascending):
            self.top_small_ten_countries_by_area()

        if (self.args.dept and not self.args.ascending):
            self.top_ten_dept_countries()

        if (self.args.dept and self.args.ascending):
            self.top_ten_min_dept_countries()

        if (self.args.electricity_consumption and not self.args.ascending):
            self.top_ten_electricity_consumption_countries()

        if (self.args.electricity_consumption and not self.args.ascending):
            self.top_ten_electricity_min_consumption_countries()

        if (self.args.electric_spend_than_prod and not self.args.ascending):
            self.high_electricity_consumption_vs_production()

        if (self.args.electric_spend_than_prod and self.args.ascending):
            self.reverse_high_electricity_consumption_vs_production()

        if (self.args.electric_vs_production and not self.args.ascending):
            self.high_production_vs_electricity_consumption()

        if (self.args.electric_vs_production and self.args.ascending):
            self.versa_high_production_vs_electricity_consumption()

        if (self.args.death_by_hiv and not self.args.ascending):
            self.countries_high_death_by_hiv_aids()

        if (self.args.death_by_hiv and self.args.ascending):
            self.countries_low_death_by_hiv_aids()

        if (self.args.hiv_living and not self.args.ascending):
            self.countries_people_living_with_aids_high()

        if (self.args.hiv_living and self.args.ascending):
            self.countries_people_living_with_aids_low()

        if (self.args.highways and not self.args.ascending):
            self.country_has_longest_roadways()

        if (self.args.highways and self.args.ascending):
            self.country_has_shortest_roadways()

        if (self.args.imports and not self.args.ascending):
            self.country_making_more_imports()

        if (self.args.imports and self.args.ascending):
            self.country_making_less_imports()

        if (self.args.internet and not self.args.ascending):
            self.country_has_most_internet_users()

        if (self.args.internet and self.args.ascending):
            self.country_has_less_internet_users()

        if (self.args.labor and not self.args.ascending):
            self.country_has_high_labor_heads()

        if (self.args.labor and self.args.ascending):
            self.country_has_less_labor_heads()

        if (self.args.military and not self.args.ascending):
            self.country_spending_more_for_military_services()

        if (self.args.military and self.args.ascending):
            self.country_spending_less_for_military_services()

        if (self.args.military_gdp and not self.args.ascending):
            self.country_spend_high_percent_from_gdp_for_military()

        if (self.args.military_gdp and self.args.ascending):
            self.country_spend_low_percent_from_gdp_for_military()

        if (self.args.oil_consumption and not self.args.ascending):
            self.high_oil_consumption_countries()

        if (self.args.oil_consumption and self.args.ascending):
            self.low_oil_consumption_countries()

        if (self.args.population and not self.args.ascending):
            self.high_populated_countries()

        if (self.args.population and self.args.ascending):
            self.low_populated_countries()

        if (self.args.railway and not self.args.ascending):
            self.long_railway_line_countries()

        if (self.args.railway and self.args.ascending):
            self.short_railway_line_countries()

        if (self.args.unemployment and not self.args.ascending):
            self.most_unemployed_people_countries()

        if (self.args.unemployment and self.args.ascending):
            self.less_unemployed_people_countries()

        if (self.args.mobile and not self.args.ascending):
            self.top_mobiles_users_countries()

        if (self.args.mobile and self.args.ascending):
            self.least_mobiles_users_countries()

        if (self.args.oil_production and not self.args.ascending):
            self.top_oil_production_countries()

        if (self.args.oil_production and not self.args.ascending):
            self.least_oil_production_countries()

        if (self.args.consuming_vs_production and not self.args.versa):
            self.consumption_vs_producing_oil()

        if (self.args.consuming_vs_production and self.args.versa):
            self.versa_consumption_vs_producing_oil()

        if (self.args.industrial_production_grouth and not self.args.ascending):
            self.top_industrial_production_grouth()

        if (self.args.industrial_production_grouth and self.args.ascending):
            self.least_industrial_production_grouth()

        else:
            print('Hey I have no option this kind as of now :(')
        # time.sleep(5)
        plt.show()

if __name__ == '__main__':
    args_parse = ArgsParser()
    args = args_parse.arguments()
    cs = CountryStatistics(args)
    cs.trigger_function_asper_args()
