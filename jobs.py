import pandas as pd
import numpy
import re

file = pd.read_csv("works.csv", header=0, index_col=False)

administration = r'(.*менедж.*)|(.*директ.*)|(.*секретар.*)|(.*управ.*)'
studies = r'(.*педагог.*)|(.*преподават.*)|(.*учител.*)|(.*воспита.*)'
law = r'(.*юри.*)|(.*адвокат.*)'
finance = r'(.*эконом.*)|(.*банк.*)|(.*финанс.*)|(.*бухгалтер.*)'
technic = r'(.*техн.*)|(.*инженер.*)|(.*разработ.*)|(.*меха.*)|(.*матем.*)'
trade = r'(.*прода.*)|(.*касси.*)|(.*маркето.*)'


def get_managers_qualification(qualification_regex):
    return managers[managers.qualification.str.contains(qualification_regex, case=False, flags=re.IGNORECASE, na=False)]


# Из файла works.csv выбираем всех менеджеров, у которых написана квалификация.
managers = file[file.jobTitle.str.contains(administration, case=False, flags=re.IGNORECASE, na=False)]
managers = managers[managers.qualification.dropna()]
total_managers = managers.shape[0]


# Создаём переменные, в которых будет хранится список менеджеров с определённой квалификацией:

law_managers = get_managers_qualification(law) # В сфере юриспруденции
finance_managers = get_managers_qualification(finance) # В сфере финансов
administration_managers = get_managers_qualification(administration) # В управленческой сфере
trade_managers = get_managers_qualification(trade) # В сфере торговли
technic_managers = get_managers_qualification(technic) # В технической сфере
studies_managers = get_managers_qualification(studies) # В сфере педагогики

managers.sort()
print(managers)

count_by_name = {'Юриспруденция': law_managers.shape[0], 'Экономика': finance_managers.shape[0],
                 'Управление': administration_managers.shape[0], 'Торговля': trade_managers.shape[0],
                 'Инженеры и технологи': technic_managers.shape[0], 'Педагоги': studies_managers.shape[0]}

