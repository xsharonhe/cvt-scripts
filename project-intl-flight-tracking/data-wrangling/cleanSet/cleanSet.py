def cleanSet(dom_flight, intl_flight, name_combined, name_dom, name_intl, name_total):
    """
    :param dom_flight: domestic file, intl_flight: international file
    :param name_combined: combined name dataframe (str), name_dom: column name of domestic (str)
    :param name_intl: column name of international, name_total: column name of total (str)
    """
    dom_flight.drop(dom_flight.tail(1).index,inplace=True) # drop last column
    # RENAME COLUMNS
    dom_flight.index.name = 'Period'
    dom_flight.rename(columns={'Unit: (000)': 'Total(DOM)'}, inplace=True)
    # CLEANUP DATA
    dom_flight['PERIOD'] = dom_flight.index
    dom_flight['PERIOD'] = dom_flight['PERIOD'].astype(str).str[1:]
    dom_flight.set_index('PERIOD')
    dom_flight['Total(DOM)'] = dom_flight['Total(DOM)'].astype(str).str[:-1]
    dom_flight.set_index('PERIOD', inplace=True)
    # IMPORT BTS INTERNATIONAL DATA DEPARTURES PERFORMED
    intl_flight.drop(intl_flight.tail(1).index,inplace=True)
    # RENAME COLUMNS
    intl_flight.index.name = 'Period'
    intl_flight.rename(columns={'Unit: (000)': 'Total(INTL)'}, inplace=True)
    # CLEANUP DATA
    intl_flight['PERIOD'] = intl_flight.index
    intl_flight['PERIOD'] = intl_flight['PERIOD'].astype(str).str[1:]
    intl_flight.set_index('PERIOD')
    intl_flight['Total(INTL)'] = intl_flight['Total(INTL)'].astype(str).str[:-1]
    intl_flight.set_index('PERIOD', inplace=True)
    # CREATE COMBINED FLIGHT DATAFRAME
    name_combined = dom_flight.copy()
    name_combined['Total(INTL)'] = intl_flight['Total(INTL)']
    name_combined['TOTAL'] = name_combined['Total(DOM)'].astype(int) + name_combined['Total(INTL)'].astype(int)

    # RENAME
    name_combined.rename(columns={'Total(DOM)': name_dom,
                                   'Total(INTL)': name_intl,
                                   'TOTAL': name_total}, inplace=True)
    return name_combined

