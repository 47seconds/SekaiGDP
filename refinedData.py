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

import pandas as pd

pd.set_option('future.no_silent_downcasting', True)

def refine_data_into_float(data):
    for i in range(180):
        for j in range(1, 24):
            data.iloc[i,j] = float(str(data.iloc[i,j]).replace(",", ""))

def check_last_5_years(data, i):
    last_5_years = data.iloc[:, -5:].fillna(0)  # Fill NaN with 0
    row_data = last_5_years.iloc[i]
    sum = 0
    for j in range(-5,0):
        sum = sum + float(row_data.iloc[j])
    if sum == 0:
        # print(f"Missing Data for: {i}: {data.iloc[i, 0]}")
        return i
    else:
        return "OK"

def main():
    data = pd.read_csv("./data/GDPdata1999_2022.csv")

    data.columns = [str(col).strip() for col in data.columns]
    refine_data_into_float(data)
    
    missing_data_countries_index = []
    
    for i in range(180):
       if check_last_5_years(data, i) != "OK":
           result = check_last_5_years(data, i)
           missing_data_countries_index.append(result)
    
    # print(data.head())
    data = data.drop(missing_data_countries_index)
    # print(data.head())
    data = data.reset_index(drop=True)
    # print(data.head())
    
    return data

if __name__ == "__main__":
    main()