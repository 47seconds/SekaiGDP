''' 
      ## Build and maintained by:
  
                                 .x+=:.                                                     ..          .x+=:.   
        xeee    dL ud8Nu  :8c   z`    ^%                                                  dF           z`    ^%  
       d888R    8Fd888888L %8      .   <k                             u.      u.    u.   '88bu.           .   <k 
      d8888R    4N88888888cuR    .@8Ned8"      .u          .    ...ue888b   x@88k u@88c. '*88888bu      .@8Ned8" 
     @ 8888R    4F   ^""%""d   .@^%8888"    ud8888.   .udR88N   888R Y888r ^"8888""8888"   ^"*8888N   .@^%8888"  
   .P  8888R    d       .z8   x88:  `)8b. :888'8888. <888'888k  888R I888>   8888  888R   beWE "888L x88:  `)8b. 
  :F   8888R    ^     z888    8888N=*8888 d888 '88%" 9888 'Y"   888R I888>   8888  888R   888E  888E 8888N=*8888 
 x"    8888R        d8888'     %8"    R88 8888.+"    9888       888R I888>   8888  888R   888E  888E  %8"    R88 
d8eeeee88888eer    888888       @8Wou 9%  8888L      9888      u8888cJ888    8888  888R   888E  888F   @8Wou 9%  
       8888R      :888888     .888888P`   '8888c. .+ ?8888u../  "*888*P"    "*88*" 8888" .888N..888  .888888P`   
       8888R       888888     `   ^"F      "88888%    "8888P'     'Y"         ""   'Y"    `"888*""   `   ^"F     
    "*%%%%%%**~    '%**%                     "YP'       "P'                                  ""                  
   
   '''

import refinedData
import countrySelection
from statsmodels.tsa.holtwinters import ExponentialSmoothing
import pandas as pd

def forecast_gdp(data, years_to_forecast):
    # Fit an Exponential Smoothing model
    model = ExponentialSmoothing(
        data["GDP_value"], trend="additive", seasonal=None, initialization_method="estimated"
    )

    fitted_model = model.fit()

    # Forecast for the specified number of years
    forecast = fitted_model.forecast(years_to_forecast)

    # Create a DataFrame with forecasted results
    forecast_years = list(range(data.index.max() + 1, data.index.max() + years_to_forecast + 1))
    
    forecast_df = pd.DataFrame({
        "Year": forecast_years,
        "GDP_value": forecast,
    })

    return forecast_df

def main():
    data = refinedData.main()
    selected_country_name = countrySelection.main()[2]
    selected_country_data = data[data["Country"] == selected_country_name]

    selected_country_data = selected_country_data.melt(id_vars=["Country"], var_name="Year", value_name="GDP_value")
    selected_country_data["Year"] = pd.to_numeric(selected_country_data["Year"]).astype(int)
    selected_country_data["GDP_value"] = pd.to_numeric(selected_country_data["GDP_value"], errors='coerce').dropna()
    selected_country_data = selected_country_data.set_index("Year")
    
    years_to_forecast = int(input("Enter number of years of which you want forecast of: "))
    
    forecast_results = forecast_gdp(selected_country_data, years_to_forecast)
    # print("Forecast results:")
    # print(forecast_results)
    return [selected_country_data, forecast_results, selected_country_name]

if __name__ == "__main__":
    main()