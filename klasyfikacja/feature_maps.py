gender_map = {"KOBIETA": -1, "MEZCZYZNA": 1}
income_map = {"NISKIE": -1, "SREDNIE": 0, "WYSOKIE": 1}
education_map = {"PODSTAWOWE": -1, "SREDNIE": 0, "WYZSZE": 1}
employment_map = {"BEZROBOTNY": -2, "SAMOZATRUDNIENIE": -1, "UMOWA_O_DZIELO": 0, "UMOWA_NA_CZAS_OKRESLONY": 1,
                  "UMOWA_NA_CZAS_NIEOKRESLONY": 2}
age_map = {"od_20_do_30": -2, "od_30_do_40": -1, "od_40_do_50": 0, "od_50_do_60": 1, "powyzej_60": 2}
feature_map_list = [gender_map, income_map, education_map, employment_map, age_map]