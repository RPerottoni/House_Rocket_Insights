import folium
import geopandas
import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

from folium.plugins import MarkerCluster
from streamlit_folium import folium_static

st.set_page_config( layout= 'wide' )

@st.cache(allow_output_mutation=True)
def get_data(path):
    df = pd.read_csv(path)
    return df

@st.cache( allow_output_mutation=True)
def get_geofile( url ):
    geofile = geopandas.read_file( url )
    return geofile
   
def features(df):
    df['selling price'] = df['selling price'].astype(np.int64)
    df['profit'] = df['profit'].astype(np.int64)
    return(df)

def set_new_columns(df):
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df['month']=df['date'].dt.month
    df['Buy It?'] = 'Standard'
    df['season'] = df['month'].apply(lambda x: 'summer' if (x > 5) & (x < 8) else
                                               'spring' if (x > 2) & (x < 5) else
                                               'fall' if (x > 8) & (x < 12) else
                                               'winter')

    df['basement'] = df['sqft_basement'].apply(lambda x: 'N' if x == 0
                                                             else 'S')        
    df['selling price'] = '0'
    df['profit'] = '0'
    return(df)

def data_correct(df):
    df.loc[df['bedrooms'] == 33 ] = df.loc[df['bedrooms'] == 33 ].replace([33],[3]) #! Substituindo o outlier
    df = df.drop_duplicates(subset = ['id'], keep = 'last') #! removendo duplicatas
    return(None)

def description(df):        
    st.header('HOUSE ROCKET COMPANY')

def business_problems(df, geofile):

#! Problema 1:
    st.header('Business Questions:')
    st.subheader('1. Which houses the company should buy and how much pay for them?')     
    st.write('**Premises**: Considering as a price reference the median price per region. Will be recomended buy houses where the price is smaller than the median price and the condition is higher than 3.')   
    df.copy()

    c1, c2 = st.columns((1,1))

    med_price = df[['zipcode','price']].groupby('zipcode').median().reset_index()
    df1 = pd.merge(med_price, df, on='zipcode', how='inner') #! Incluindo o valor da mediana em uma coluna, por zipcode.
    df1 = df1.rename(columns={'price_y': 'price', 'price_x':'price_median'}) #! Renomeando as colunas criadas pela função merge

    for i, row in df1.iterrows(): #! Verificação para recomendar a compra de imóveis
        if(row['price_median'] >= row['price']) & (row['condition'] > 3):
            df1.loc[i,'Buy It?'] = 'Yes'
        else:
            df1.loc[i,'Buy It?'] = 'No'

    answer_one = df1[df1['Buy It?'] == 'Yes']

    c1.dataframe(answer_one[['zipcode','id','price','Buy It?']], height=510) 

#! Base Map - Folium

    density_map = folium.Map( location=[answer_one['lat'].mean(), answer_one['long'].mean()], default_zoom_start=15 )

    marker_cluster = MarkerCluster().add_to( density_map )

    for name, row in answer_one.iterrows():
        folium.Marker( [row['lat'], row['long'] ],
            popup='Pay: R${0}. Buy it?{1}, zipcode:{2}, id:{3}'.format( row['price'],
                    row['Buy It?'],
                    row['zipcode'],
                    row['id'] ) ).add_to( marker_cluster )
    with c2:
        folium_static( density_map )
    
#! Problema 2: 
    st.subheader('2. When the company should resell and which should be the price?')
    
    st.write('**Premises**: The periods will be separated by the season and the price will be calculated considering the median price already done.')

    c3, c4 = st.columns((1,1))
    
    med_season = answer_one[['season','zipcode','price']].groupby(['zipcode','season']).median().reset_index()
    df2 = pd.merge(med_season, answer_one, on='zipcode', how='inner') #! Incluindo o valor da mediana em uma coluna.
    df2 = df2.rename(columns={'price_y': 'price', 'price_x':'price_season', 'season_x':'season'}) #! Renomeando as colunas criadas pela função merge.

    for i, row in df2.iterrows():
        if (row['price_season'] > row['price']):
            df2.loc[i, 'selling price'] =  row['price'] * 1.3
        else:
            df2.loc[i, 'selling price'] = row['price'] * 1.1    

    c3.dataframe(df2[['id','zipcode','season','selling price','price','Buy It?']],height=500)
    
    season_sell = df2[['season','selling price']].groupby('season').sum().reset_index()
    season_buy = round(df2[['season','price']].groupby('season').sum().reset_index(), 2)
    season_profit = pd.merge(season_sell, season_buy, on='season', how='inner')
    season_profit['profit'] = season_profit['selling price'] - season_profit['price']

    protwo = px.bar(season_profit, x='season', y='profit', color='profit', text='profit', height=550)
    protwo.update_traces(texttemplate='%{text:.2s}', textposition='outside')
    protwo.update_layout(title_text="Profit by Season", title_x=0.55)
    with c4:
        st.plotly_chart(protwo)

#! Problema 3:
    sellprice = df2[df2['Buy It?'] == 'Yes']['selling price'].sum()
    soldprice = df2[df2['Buy It?'] == 'Yes']['price'].sum()
    
    profit = round( sellprice - soldprice, 2)
    st.subheader('1.3: Results:')
    st.write('Following the recomendation, by buying at the correct price and selling the properties at the right moment, the maximum profit will be', profit, 'dollars.')
       
    return(df1,df2)

#! Hypothesis:

def hipothesys(df2):

    st.header('2: Hypothesis')
    
    c5, c6 = st.columns((1,1))
    c7, c8 = st.columns((1,1))
    c9, c10 = st.columns((1,1))
    c11, c12 = st.columns((1,1))
    c13, c14 = st.columns((1,1))
    
#! Hypothesis One:
    with c5:
        st.subheader('1. Proprerties that is water front are 20% more expensive.')
        avgwf = df2[df2['waterfront'] == 1 ]['price'].mean() #! Média de preço para imóveis com vista para água
        avgwfn = df2[df2['waterfront'] == 0]['price'].mean() #! Média de preço para imóveis sem vista para água

        if avgwf > avgwfn:
            iswater=round(((avgwf-avgwfn)*100/avgwf))
            isnotwater=100-iswater
            st.write('Hypothesis is true. Properties that are waterfront costs',iswater,'% more than the properties are not water front.')
        else:
            iswater=100-isnotwater
            isnotwater=((avgwfn-avgwf)*100/avgwfn)
            st.write('Hypothesis is False. Properties that are not waterfront costs',isnotwater,'% more than the properties are water front.')

        values = [iswater, isnotwater]
        labels = ['Is Water Front','Is Not Water Front']

        fig=px.pie(labels, values = values, names = labels, color=labels, color_discrete_map={'Is Water Front':'darkblue',
                                    'Is Not Water Front':'royalblue'})
        fig.update_layout(title_text="Hypothesis 1: Is Water Front vs Is Not Water Front", title_x=0.45)
        st.plotly_chart(fig)
 
#! Hypothesis Two:
    with c6:
        st.subheader('2. Proprerties that was built before 1955 are 50% cheaper.')
        
        avgantigo = round(df[df['yr_built'] < 1955 ]['price'].mean(),2)
        avgnovo = round(df[df['yr_built'] >= 1955 ]['price'].mean(),2)

        if avgnovo > avgantigo:
            new = round(((avgnovo-avgantigo)*100)/avgnovo,2)
            old = 0
            st.write('Hypothesis is true. Properties builted before 1955 are',new,'% more cheaper. But the difference is insignificant.')
        else:
            new = 0
            old = round(((avgantigo-avgnovo)*100)/avgantigo,2)
            st.write('Hypothesis is false. Properties builted after 1955',old,'% more cheaper. But the difference is insignificant.')

        htwo_line = ['Old','New']
        htwo_col=[avgantigo,avgnovo]
        htwo_res=pd.DataFrame(list(zip(htwo_line, htwo_col)), columns=['Age','Price'])

        figtwo = px.bar(htwo_res, x='Age', y='Price', color='Price', text='Price', height=450)
        figtwo.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        figtwo.update_layout(title_text="Hypothesis 2: New Properties vs Old Properties", title_x=0.45)
        st.plotly_chart(figtwo)

#! Hypothesis Three:
    with c7:
        st.subheader('3. Properties without basement are 40% bigger that the others.')

        basement_no = round(df[df['basement'] == "N"]['sqft_lot'].mean(),2)
        basement_yes = round(df[df['basement'] == "S"]['sqft_lot'].mean(),2)

        if basement_no > basement_yes:
            base_no = round(((basement_no-basement_yes)*100/basement_no),2)
            base_ye = 0
            st.write('Hypothesis is true. Properties without basement are',base_no,'% bigger than properties with basement.')
        else:
            base_no = 0
            base_ye = round(((basement_no-basement_yes)*100/basement_yes),2)
            st.write('Hypothesis is false. Properties without basement are',base_no,'% smaller than properties with basement.')
            
        hthree_line = ['Sem Porão','Com Porão']
        hthree_col = [basement_no,basement_yes]
        hthree_res = pd.DataFrame(list(zip(hthree_line,hthree_col)), columns=['Porão','sqft_lot'])

        figthree = px.bar(hthree_res, x='Porão', y='sqft_lot', color='sqft_lot', text='sqft_lot', height=450)
        figthree.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        figthree.update_layout(title_text="Hypothesis 3: With Basement vs Without Basement", title_x=0.5)
        st.plotly_chart(figthree)
    
#! Hypothesis Four:
    with c8:
        st.subheader('4. YoY ( Year over Year ) property price growth is 10%.')

        yr_14 = round(df[df['year'] == 2014]['price'].mean(),2)
        yr_15 = round(df[df['year'] == 2015]['price'].mean(),2)

        if yr_14 > yr_15:
            year_14 = round(((yr_14-yr_15)*100)/yr_14,2)
            year_15 = 0
            st.write('Hypothesis is false. The price did not grew up.')
        else:
            year_14 = 0
            year_15 = round(((yr_15-yr_14)*100)/yr_15,2)
            st.write('Hypothesis is true. The price grew up',year_15,'%.')
            
        htfour_line = ['2014','2015']
        htfour_col = [yr_14, yr_15]
        htfour_res = pd.DataFrame(list(zip(htfour_line,htfour_col)), columns=['Year','Price'])

        figfour = px.bar(htfour_res, x='Year', y='Price',text='Price', color='Price', height=450)
        figfour.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        figfour.update_layout(title_text="Hypothesis 4: Price Growth per Year", title_x=0.45)

        st.plotly_chart(figfour)

#! Hypothesis Five:
    with c9:
        st.subheader('5. Month over Month price growth is 15% for properties with 3 bathrooms.')
        st.write('Hypothesis is false,the price does not show growth.')
        bath = df[(df['bathrooms'] == 3 )]
        bath = bath[['month','price']].groupby('month').sum().reset_index()

        figfive = px.line(bath, x='month', y='price', height=400)
        figfive.update_layout(title_text="Hypothesis 5: Bathrooms vs Price Growth by Month", title_x=0.55)
        
        st.plotly_chart(figfive)

#! Hypothesis Six:
    with c10:
        st.subheader('6. Properties in bad conditions but is water front are more expensive thant properties in good condition but is not water front.')
        st.write('Hypothesis is true. Water front properties in bad conditions are more expensive than properties in good condition but are not water front.')

        water_bad = round(df[(df['waterfront'] == 1) & ( df['condition'] <= 3)]['price'].mean())
        nowater_good = round(df[(df['waterfront'] == 0) & ( df['condition'] >= 3)]['price'].mean())

        htsix_line = ['Bad & Water','Good & Not Water']
        htsix_col = [water_bad, nowater_good]
        htsix_res = pd.DataFrame(list(zip(htsix_line, htsix_col)), columns=['Caracteristica','Price'])

        figsix = px.bar(htsix_res, x='Caracteristica', y='Price', text='Price', color='Price', height=450)
        figsix.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        figsix.update_layout(title_text="Hypothesis 6: Feature vs Price", title_x=0.45)

        st.plotly_chart(figsix)

#! Hypothesis Seven:
    with c11:
        st.subheader('7. Properties that are not waterfront are smaller than the properties that are water front.')
        st.write('Hypothesis is true. Properties that are water front are bigger than properties that are not water front.')

        is_water = round(df[(df['waterfront'] == 1)]['sqft_lot'].mean())
        is_not_water = round(df[(df['waterfront'] == 0)]['sqft_lot'].mean())

        htseven_line = ['Is Water Front','Is Not Water Front']
        htseven_col = [is_water,is_not_water]
        htseven_res = pd.DataFrame(list(zip(htseven_line, htseven_col)), columns=['Caracteristica','Size'])

        figseven = px.bar(htseven_res, x='Caracteristica', y='Size', text='Size', color='Size', height=450)
        figseven.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        figseven.update_layout(title_text="Hypothesis 7: Size vs Water Front", title_x=0.45)

        st.plotly_chart(figseven)

#! Hypothesis Eight:
    with c12:
        st.subheader('8. Properties renovated are 20% more expensive than the properties that are not renovated.')

        avg_not_reno = round(df[df['yr_renovated'] == 0]['price'].mean())
        avg_reno = round(df[df['yr_renovated'] != 0]['price'].mean())

        if avg_not_reno > avg_reno:
            renovated=((avg_not_reno-avg_reno)*100)/avg_not_reno
            original=0
            st.write('Hypothesis is true. Properties that was renovated are',renovated,'% more expensive than properties that was not renovated.')
        else:
            renovated=0
            original=round(((avg_reno-avg_not_reno)*100)/avg_reno,2)
            st.write('Hypothesis is false. Properties not renovated are',original,'% more expensive than the properties that was renovated.')

        hteig_line = ['Renovated','Original']
        hteig_col = [avg_reno, avg_not_reno]
        hteig_res = pd.DataFrame(list(zip(hteig_line,hteig_col)), columns=['Caracteristica','Price'])

        figeig = px.bar(hteig_res, x='Caracteristica', y='Price', color='Price', text='Price', height=450)
        figeig.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        figeig.update_layout(title_text="Hypothesis 8: Price vs Renovation", title_x=0.45)

        st.plotly_chart(figeig)

#! Hypothesis Nine:
    with c13:
        st.subheader('9. Houses with more than 3 bedrooms cost 40% more than properties that have less bedrooms.')

        bed_more = df[df['bedrooms'] >= 3]['price'].mean()
        bed_less = df[df['bedrooms'] < 3]['price'].mean()

        if bed_more > bed_less:
            bedmore = round(((bed_more-bed_less)*100)/bed_more,2)
            bedless = 0
            st.write('Hypothesis is true. Properties with more than 3 bedrooms costs',bedmore,'% more than the properties with less than 3 bedrooms.')
        else:
            bedmore = 0
            bedless = round(((bedless-bedmore)*100)/bedless,2)
            st.write('Hypothesis is false. Properties not renovated are',bedless,'% more expensive than the properties that was renovated.')

        htnine_line = ['More than 3 bedrooms','Less than 3 bedrooms']
        htnine_col = [bed_more,bed_less]
        htnine_res = pd.DataFrame(list(zip(htnine_line, htnine_col)), columns=['bedrooms','price'])

        fignine = px.bar(htnine_res, x='bedrooms', y='price', text='price', color='price', height=450)
        fignine.update_traces(texttemplate='%{text:.2s}', textposition='outside')
        fignine.update_layout(title_text="Hypothesis 9: Size vs Price", title_x=0.45)

        st.plotly_chart(fignine)

#! Hypothesis Ten:
    with c14:
        st.subheader('10. At the winter there are 35% more properties to sell than the summer.')

        seas = df[['season','id']].groupby('season').count().reset_index()

        wint = round(df[df['season'] == 'winter']['id'].count())
        summ = round(df[df['season'] == 'summer']['id'].count())

        if wint > summ:
            winter=round(((wint-summ)*100)/wint)
            summer=0
            st.write('Hypothesis is true. At the winter there are',winter,'% more properties to sell than the summer.')
        
        else:
            winter=0
            summ=round(((summ-wint)*100)/summ)
            st.write('No verão tem-se',summ,'% mais imóveis a venda do que no inverno.')
            
        figten = px.line(seas, x='season', y='id', height=450)
        figten.update_layout(
                title_text="Hypothesis 10: Properties sales vs Year", title_x=0.45)

        st.plotly_chart(figten)

    return(None)

#! ETL

if __name__ == '__main__':

    #! Data Extraction
    path = '/home/reng/Documentos/ds_repos/House_Rocket_Insights/data/kc_house_data.csv'
    df = get_data(path)
    url = 'https://opendata.arcgis.com/datasets/83fc2e72903343aabff6de8cb445b81c_2.geojson'
    geofile = get_geofile( url )
    
    #! Transformation
    set_new_columns(df)
    features(df)
    data_correct(df)

    #! Load
    description(df)
    business_problems(df, geofile)
    hipothesys(df)