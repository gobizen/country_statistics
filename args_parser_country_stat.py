import argparse


class ArgsParser(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser(description= """
        This is a statistics program will give you graph representation
        of the data. Specifically we have used country facts to show the statistics
        Information.
        """)
        self.help_context = {
        'area': 'This function will plot graph for top ten ↑↓ countries by area.',
        'account_balance': 'This function will give top 10 countries holds ↑↓ account balance.',
        'dept': 'will give you pictorial representation of dept data countrywise, ↑↓.',
        'electricity_consumption': 'Electricity consumption country wise, ↑↓',
        'electric_consumption_vs_production': 'This function will plot which is more, high consuming vs production.',
        'electric_production_vs_consumption': 'This function will plot which is more, high production vs comsumption.',
        'hiv_death': 'Country where people affeced and death because of HIV/AIDS. ↑↓',
        'hiv_living': 'Country where people affeced by HIV/AIDS. ↑↓',
        'highways': 'Country has longest nation highways. ↑↓',
        'import': 'Company imports detail graph. ↑↓',
        'labor': 'Country has high labour heads. ↑↓',
        'internet': 'Top 10 internet user Country. ↑↓',
        'military': 'Country spending high in military. ↑↓',
        'military_gdp': 'Country spending high in military with respect to GDP. ↑↓',
        'oil_consume': 'Country consuming more oil. ↑↓',
        'railway': 'long/short railway line top 10 countries. ↑↓',
        'unemployment': 'unemployment rate by countries. ↑↓',
        'mobile': 'Top 10 mobile user Country. ↑↓',
        'oil_stat': 'oil production vs consumption. ↔',
        'oil_prod': 'Country producing more/less Oil. ↑↓',
        'production_industries': 'Country producion grouth. ↑↓',
        'sort': 'This BOOL will change the view top 10 or least 10. SYMBOL -> ↑↓',
        'versa': 'front and forth (VS)',
        'population': 'it will show polpulation stat. ↑↓',
        }


    def arguments(self):
        self.parser.add_argument('-ar', '--area', default=False, action='store_true', help= self.help_context['area'])
        self.parser.add_argument('-ab', '--account_balance', default=False, action='store_true', help= self.help_context['account_balance'])
        self.parser.add_argument('-d', '--dept', default=False, action='store_true', help= self.help_context['dept'])
        self.parser.add_argument('-ec', '--electricity_consumption', default=False, action='store_true', help= self.help_context['electricity_consumption'])
        self.parser.add_argument('-ep', '--electric_vs_production', default=False, action='store_true', help= self.help_context['electric_consumption_vs_production'])
        self.parser.add_argument('-es', '--electric_spend_than_prod', default=False, action='store_true', help= self.help_context['electric_production_vs_consumption'])
        self.parser.add_argument('-dhiv', '--death_by_hiv', default=False, action='store_true', help= self.help_context['hiv_death'])
        self.parser.add_argument('-lhiv', '--hiv_living', default=False, action='store_true', help= self.help_context['hiv_living'])
        self.parser.add_argument('-hw', '--highways', default=False, action='store_true', help= self.help_context['highways'])
        self.parser.add_argument('-im', '--imports', default=False, action='store_true', help= self.help_context['import'])
        self.parser.add_argument('-l', '--labor', default=False, action='store_true', help= self.help_context['labor'])
        self.parser.add_argument('-i', '--internet', default=False, action='store_true', help= self.help_context['internet'])
        self.parser.add_argument('-m', '--military', default=False, action='store_true', help= self.help_context['military'])
        self.parser.add_argument('-mgdp', '--military_gdp', default=False, action='store_true', help= self.help_context['military_gdp'])
        self.parser.add_argument('-oc', '--oil_consumption', default=False, action='store_true', help= self.help_context['oil_consume'])
        self.parser.add_argument('-p', '--population', default=False, action='store_true', help=self.help_context['population'])
        self.parser.add_argument('-r', '--railway', default=False, action='store_true', help= self.help_context['railway'])
        self.parser.add_argument('-u', '--unemployment', default=False, action='store_true', help= self.help_context['unemployment'])
        self.parser.add_argument('-mo', '--mobile', default=False, action='store_true', help= self.help_context['mobile'])
        self.parser.add_argument('-o', '--oil_production', default=False, action='store_true', help= self.help_context['oil_prod'])
        self.parser.add_argument('-cp', '--consuming_vs_production', default=False, action='store_true', help= self.help_context['oil_consume'])
        self.parser.add_argument('-ip', '--industrial_production_grouth', default=False, action='store_true', help= self.help_context['production_industries'])
        self.parser.add_argument('-asc', '--ascending', default=False, action='store_true', help='')
        self.parser.add_argument('-v', '--versa', default=False, action='store_true')
        return self.parser.parse_args()

    def vaidation(self):
        pass

if __name__ == '__main__':
    ap = ArgsParser()
    print(ap.arguments())