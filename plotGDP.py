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

import model
import matplotlib.pyplot as plt

def plot_country_GDP_graph(selected_country_data, forecast_results, selected_country_name):
    # Determine the complete range of years from the earliest given year to the latest forecasted year
    min_year = selected_country_data.index.min()
    max_year = forecast_results["Year"].max()
    all_years = list(range(min_year, max_year + 1))

    plt.figure(figsize=(10, 6))

    # Plot the given data with solid blue lines and circles
    plt.plot(
        selected_country_data.index,
        selected_country_data["GDP_value"],
        marker='o',
        linestyle='-',
        color='b',
        label="Given Data"
    )

    # Plot the forecasted data with red dots and no lines
    plt.plot(
        forecast_results["Year"],
        forecast_results["GDP_value"],
        marker='o',
        linestyle='None',
        color='r',
        label="Forecasted Data"
    )

    # Annotate the forecasted points with their GDP values
    for _, row in forecast_results.iterrows():
        plt.text(
            row["Year"], row["GDP_value"],
            f"{row['GDP_value']:.2f}",
            color='red',
            ha='center',
            va='bottom'
        )

    # Set x-axis ticks to cover all years
    plt.xticks(all_years)

    # Add labels, grid, title, and legend
    plt.xlabel("Year")
    plt.ylabel("GDP (in billion dollars)")
    plt.title(f"GDP Over the Years for {selected_country_name}")
    plt.grid(True)
    plt.legend()

    # Show the plot
    plt.show()
    
def main():
    model_data = model.main()
    plot_country_GDP_graph(model_data[0], model_data[1], model_data[2])

if __name__ == "__main__":
    main()