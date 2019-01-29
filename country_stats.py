#!/home/ad.msystechnologies.com/vchandrasekaran/PycharmProjects/country_stats/venv/bin/spark-submit

from pyspark.sql import SparkSession
import matplotlib.pyplot as plt
from csv_schema import schema

COLOR_RED = 'r'


class CountryStatBase(object):
    def __init__(self):
        spark_session = SparkSession.builder.appName('Country & Statistics').getOrCreate()
        self.country_stat_df = spark_session.read.format("csv").option("header", "true").load(
            './resources/factbook.csv', schema=schema)

    def sort_and_filter_by_field(self, filter_by, ascending=False, selection_fields=[], data_frame=None):
        data_frame = self.country_stat_df if data_frame == None else data_frame
        sorted_list_df = data_frame.sort(data_frame[filter_by], ascending=ascending)
        selection_fields.append(filter_by)
        countries_df = sorted_list_df.select(sorted_list_df.country, *selection_fields).na.drop(how='any',
                                                                                                subset=[filter_by])
        return countries_df

    def top_country_by_area(self, ascending=False):
        largest_countries_df = self.sort_and_filter_by_field('area', ascending)
        top_largest_countries = largest_countries_df.limit(10).toPandas().sort_values(by='area',
                                                                                      ascending=not ascending)
        ax = top_largest_countries.plot.barh(x='country', color=COLOR_RED)
        ax.set_title('Top 10 Countries in the world by Area.')
        ax.set_xlabel('Area in Sq Kms')
        ax.set_yticklabels(top_largest_countries['country'])
        # plt.show()

    def top_country_account_balance(self, ascending=False):
        top_countries_df = self.sort_and_filter_by_field('current_account_balance', ascending)
        top_rich_or_poor_countries = top_countries_df.limit(10).toPandas().sort_values(by='current_account_balance',
                                                                                       ascending=not ascending)
        ax = top_rich_or_poor_countries.plot.barh(x='country', color=COLOR_RED)
        key_word = 'Highest' if not ascending else 'Lowest'
        ax.set_title('Top 10 %s Account Balance Countries.' % key_word)
        ax.set_xlabel('In USD')
        ax.set_yticklabels(top_rich_or_poor_countries['country'])
        # plt.show()

    def country_dept_to_foreign_countries(self, ascending=False):
        dept_countries_df = self.sort_and_filter_by_field('debt_external', ascending)
        top_rich_or_poor_countries = dept_countries_df.limit(10).toPandas().sort_values(by='debt_external',
                                                                                        ascending=not ascending)
        ax = top_rich_or_poor_countries.plot.barh(x='country', color=COLOR_RED)
        key_word = 'Low' if ascending else 'High'
        ax.set_title('Top 10 %s debt Countries.' % key_word)
        ax.set_xlabel('In USD')
        ax.set_yticklabels(top_rich_or_poor_countries['country'])
        # plt.show()

    def top_ten_electricity_consumption_countries(self, ascending= False):
        electricity_consumption_countries_df = self.sort_and_filter_by_field('electricity_consumption_kWh', ascending, [])
        print(electricity_consumption_countries_df.show())
        top_electricity_consumption_countries = electricity_consumption_countries_df.limit(10).toPandas().sort_values(by='electricity_consumption_kWh', ascending=not ascending)
        ax = top_electricity_consumption_countries.plot.barh(x='country', color=COLOR_RED)
        key_word = 'Low' if ascending else 'High'
        ax.set_title('Top 10 %s Electricity Consumption Countries.' % key_word)
        ax.set_xlabel('In Kw/h')
        ax.set_yticklabels(top_electricity_consumption_countries['country'])
        # plt.show()

    def electricity_using_with_respect_to_production(self, ascending=False):
        electricity_consumption_countries_df = self.sort_and_filter_by_field('electricity_consumption_kWh', ascending,
                                                                             ['electricity_production_kWh'])
        top_electricity_consumption_countries = electricity_consumption_countries_df.limit(10).toPandas().sort_values(
            by='electricity_consumption_kWh', ascending=not ascending)
        ax = top_electricity_consumption_countries.plot(x="country", y=["electricity_consumption_kWh",
                                                                        "electricity_production_kWh", ], kind="barh")
        ax.set_title('Top 10 Countries spending Electricity Comparing with Production.')
        ax.set_xlabel('In Kw/h')
        # plt.show()

    def country_spending_more_power_then_production(self, ascending=False, versa=False):
        if not versa:
            df_country_spending_more = self.country_stat_df.filter(
                self.country_stat_df['electricity_consumption_kWh'] > self.country_stat_df[
                    'electricity_production_kWh'])
        else:
            df_country_spending_more = self.country_stat_df.filter(
                self.country_stat_df['electricity_consumption_kWh'] < self.country_stat_df[
                    'electricity_production_kWh'])
        filtered_dataframe = self.sort_and_filter_by_field('electricity_consumption_kWh', ascending,
                                                           ['electricity_production_kWh'],
                                                           data_frame=df_country_spending_more)
        ax = filtered_dataframe.limit(10).toPandas().sort_values(by='electricity_consumption_kWh').plot(x="country", y=[
            "electricity_consumption_kWh", "electricity_production_kWh", ], kind="barh")
        title = 'High Power Generation VS Power Consumption' if not versa else 'High Power Consumption VS Power Production'
        ax.set_title(title)
        ax.set_xlabel('In Kw/h')
        ax.set_ylabel('Country')
        # plt.show()

    def people_death_by_hiv(self, ascending=False):
        death_by_hiv_countries_df = self.sort_and_filter_by_field('HIV_AIDS_deaths', ascending)
        df_top_countries_people_death_by_hiv = death_by_hiv_countries_df.limit(10).toPandas().sort_values(
            by='HIV_AIDS_deaths', ascending=not ascending)
        key_word = 'Highest' if not ascending else 'Lowest'
        ax = df_top_countries_people_death_by_hiv.plot.barh(x='country', color=COLOR_RED)
        ax.set_title('Top 10 Countries People death by HIV/AIDS- %s' % key_word)
        ax.set_xlabel('HEAD COUNT')
        ax.set_ylabel('Country')
        # plt.show()

    def people_living_with_aids(self, ascending=False):
        living_with_hiv_countries_df = self.sort_and_filter_by_field('people_living_with_HIV_AIDS', ascending)
        df_top_countries_people_living_with_hiv = living_with_hiv_countries_df.limit(10).toPandas().sort_values(
            by='people_living_with_HIV_AIDS', ascending=not ascending)
        key_word = 'Highest' if not ascending else 'Lowest'
        ax = df_top_countries_people_living_with_hiv.plot.barh(x='country', color=COLOR_RED)
        ax.set_title('Top 10 Countries People Living with HIV/AIDS- %s' % key_word)
        ax.set_xlabel('HEAD COUNT')
        ax.set_ylabel('Country')
        # plt.show()

    def country_has_long_or_short_roadways(self, ascending=False):
        country_road_length_filtered = self.sort_and_filter_by_field('highways_km', ascending)
        highway_df = country_road_length_filtered.limit(10).toPandas().sort_values(
            by='highways_km', ascending=not ascending)
        key_word = 'Longest' if not ascending else 'Shortest'
        ax = highway_df.plot.barh(x='country', color=COLOR_RED)
        ax.set_title('Top 10 Countries which has %s HighWays' % key_word)
        ax.set_xlabel('KMs')
        ax.set_ylabel('Country')
        # plt.show()

    def country_doing_more_imports(self, ascending=False):
        country_imports_filtered = self.sort_and_filter_by_field('imports', ascending)
        imports_df = country_imports_filtered.limit(10).toPandas().sort_values(
            by='imports', ascending=not ascending)
        key_word = 'Highest' if not ascending else 'Lowest'
        ax = imports_df.plot.barh(x='country', color=COLOR_RED)
        ax.set_title('Top 10 Countries which imports- %s' % key_word)
        ax.set_xlabel('Units')
        ax.set_ylabel('Country')
        # plt.show()

    def country_internet_users_stat(self, ascending=False):
        country_internet_users_filtered = self.sort_and_filter_by_field('internet_users', ascending)
        internet_users_df = country_internet_users_filtered.limit(10).toPandas().sort_values(
            by='internet_users', ascending=not ascending)
        key_word = 'Highest' if not ascending else 'Lowest'
        ax = internet_users_df.plot.barh(x='country', color=COLOR_RED)
        ax.set_title('Top 10 Countries has- %s internet Users' % key_word)
        ax.set_xlabel('HEAD COUNT')
        ax.set_ylabel('Country')
        # plt.show()

    def country_labor_force_stat(self, ascending=False):
        country_lobor_filtered = self.sort_and_filter_by_field('labor_force', ascending)
        labor_force_df = country_lobor_filtered.limit(10).toPandas().sort_values(
            by='labor_force', ascending=not ascending)
        key_word = 'Highest' if not ascending else 'Lowest'
        ax = labor_force_df.plot.barh(x='country', color=COLOR_RED)
        ax.set_title('Top 10 Countries has- %s Labor Force' % key_word)
        ax.set_xlabel('HEAD COUNT')
        ax.set_ylabel('Country')
        # plt.show()

    def country_spending_expenditures_for_military(self, ascending=False):
        country_spending_expenditures_for_military_filtered = self.sort_and_filter_by_field(
            'military_expenditures_dollar_figure', ascending)
        expenditure_df = country_spending_expenditures_for_military_filtered.limit(10).toPandas().sort_values(
            by='military_expenditures_dollar_figure', ascending=not ascending)
        key_word = 'Highest' if not ascending else 'Lowest'
        ax = expenditure_df.plot.barh(x='country', color=COLOR_RED)
        ax.set_title('Top 10 Countries spending- %s for Military' % key_word)
        ax.set_xlabel('USD')
        ax.set_ylabel('Country')
        # plt.show()

    def country_spending_expenditures_for_military_from_gdp(self, ascending=False):
        country_spending_expenditures_for_military_from_gdp_filtered = self.sort_and_filter_by_field(
            'military_expenditures_percent_of_GDP_percent', ascending)
        expenditure_df = country_spending_expenditures_for_military_from_gdp_filtered.limit(10).toPandas().sort_values(
            by='military_expenditures_percent_of_GDP_percent', ascending=not ascending)
        key_word = 'Highest' if not ascending else 'Lowest'
        ax = expenditure_df.plot.barh(x='country', color=COLOR_RED)
        ax.set_title('Top 10 Countries spending- %s for Military from it\'s GDP' % key_word)
        ax.set_xlabel('%')
        ax.set_ylabel('Country')
        # plt.show()

    def top_oil_consumption_countries(self, ascending=False):
        oil_consumption_by_countries = self.sort_and_filter_by_field('oil_consumption_bbl_day', ascending)
        expenditure_df = oil_consumption_by_countries.limit(10).toPandas().sort_values(
            by='oil_consumption_bbl_day', ascending=not ascending)
        key_word = 'More' if not ascending else 'Less'
        ax = expenditure_df.plot.barh(x='country', color=COLOR_RED)
        ax.set_title('Top 10 Countries Consuming- %s OIL' % key_word)
        ax.set_xlabel('BBL/Day')
        ax.set_ylabel('Country')
        # plt.show()

    def population_rank(self, ascending=False):
        population_filtered = self.sort_and_filter_by_field('population', ascending)
        population_df = population_filtered.limit(10).toPandas().sort_values(
            by='population', ascending=not ascending)
        key_word = 'Highest' if not ascending else 'Lowest'
        ax = population_df.plot.barh(x='country', color=COLOR_RED)
        ax.set_title('Top 10 Countries- %s Population Rank' % key_word)
        ax.set_xlabel('HEAD COUNT')
        ax.set_ylabel('Country')
        # plt.show()

    def railway_line_stat(self, ascending=False):
        railway_filtered = self.sort_and_filter_by_field('railways_km', ascending)
        railway_df = railway_filtered.limit(10).toPandas().sort_values(
            by='railways_km', ascending=not ascending)
        key_word = 'Longest' if not ascending else 'Shortest'
        ax = railway_df.plot.barh(x='country', color=COLOR_RED)
        ax.set_title('Top 10 Countries which has %s RAILWAY tracks' % key_word)
        ax.set_xlabel('KMs')
        ax.set_ylabel('Country')
        # plt.show()

    def top_unemployemnt_countries(self, ascending=False):
        unemployment_filtered = self.sort_and_filter_by_field('unemployment_rate_percent', ascending)
        unemployment_df = unemployment_filtered.limit(10).toPandas().sort_values(
            by='unemployment_rate_percent', ascending=not ascending)
        key_word = 'Highest' if not ascending else 'Lowest'
        ax = unemployment_df.plot.barh(x='country', color=COLOR_RED)
        ax.set_title('Top 10 Countries which has %s Unemployemnt rate' % key_word)
        ax.set_xlabel('%')
        ax.set_ylabel('Country')
        # plt.show()

    def top_mobile_users_country(self, ascending=False):
        mobile_users_filter = self.sort_and_filter_by_field('telephones_mobile_cellular', ascending)
        mobile_users_df = mobile_users_filter.limit(10).toPandas().sort_values(
            by='telephones_mobile_cellular', ascending=not ascending)
        key_word = 'Highest' if not ascending else 'Lowest'
        ax = mobile_users_df.plot.barh(x='country', color=COLOR_RED)
        ax.set_title('Top 10 Countries which has %s Mobile phone users' % key_word)
        ax.set_xlabel('HEAD COUNT')
        ax.set_ylabel('Country')
        # plt.show()

    def oil_production_country_rank(self, ascending=False):
        oil_production_filter = self.sort_and_filter_by_field('oil_production_bbl_day', ascending)
        oil_production_df = oil_production_filter.limit(10).toPandas().sort_values(
            by='oil_production_bbl_day', ascending=not ascending)
        key_word = 'Highest' if not ascending else 'Lowest'
        ax = oil_production_df.plot.barh(x='country', color=COLOR_RED)
        ax.set_title('Top 10 Countries Producing OIl- %s' % key_word)
        ax.set_xlabel('BBL/Day')
        ax.set_ylabel('Country')
        # plt.show()

    def consuming_vs_production_oil_vice_versa(self, versa=False):
        if not versa:
            df_country_consuming_more = self.country_stat_df.filter(
                self.country_stat_df['oil_consumption_bbl_day'] > self.country_stat_df['oil_production_bbl_day'])
        else:
            df_country_consuming_more = self.country_stat_df.filter(
                self.country_stat_df['oil_consumption_bbl_day'] < self.country_stat_df['oil_production_bbl_day'])
        filtered_dataframe = self.sort_and_filter_by_field('oil_consumption_bbl_day', False, ['oil_production_bbl_day'],
                                                           data_frame=df_country_consuming_more)
        ax = filtered_dataframe.limit(10).toPandas().sort_values(by='oil_consumption_bbl_day').plot(x="country", y=[
            "oil_consumption_bbl_day", "oil_production_bbl_day", ], kind="barh")
        ax.set_title('Top 10 Countries spending Electricity irrespective to it\'s production.')
        ax.set_xlabel('In BBL/Day')
        ax.set_ylabel('Country')
        # plt.show()

    def industrial_production_grouth_top_countries(self, ascending=False):
        grouth_production_filter = self.sort_and_filter_by_field('industrial_production_growth_rate_percent', ascending)
        grouth_production_df = grouth_production_filter.limit(10).toPandas().sort_values(
            by='industrial_production_growth_rate_percent', ascending=not ascending)
        key_word = 'High' if not ascending else 'Low'
        ax = grouth_production_df.plot.barh(x='country', color=COLOR_RED)
        ax.set_title('Top 10 Countries Producion Grouth- %s' % key_word)
        ax.set_xlabel('BBL/Day')
        ax.set_ylabel('Country')
        # plt.show()


if __name__ == '__main__':
    c = CountryStatBase()
    c.electricity_using_with_respect_to_production(True)
    c.country_spending_more_power_then_production(True)
    plt.show()