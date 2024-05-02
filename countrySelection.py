import refinedData

data = refinedData.main()
countries = data.iloc[:, 0].tolist()

def country_selection(countries):
    print("Available countries:")
    for idx, country in enumerate(countries):
        print(f"{idx + 1}: {country}")
    selected_index = int(input("Enter the number corresponding to your country of choice: ")) - 1
    selected_country = countries[selected_index]
    return selected_country

def countryGDP(selected_country):
    country_gdp_data = data[data.iloc[:, 0] == selected_country]
    gdp_values = country_gdp_data.iloc[0, 1:].values
    return gdp_values

def main():
    selected_country = country_selection(countries)
    years = data.columns[1:].tolist()
    gdp_values = countryGDP(selected_country)
    return [years, gdp_values, selected_country]
    
    
if __name__ == "__main__":
    main()