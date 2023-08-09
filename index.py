import streamlit as st
import pandas as pd
import plotly.express as px

def main():

    df = pd.read_csv('DF_REE.csv')
    dfEmis = pd.read_csv('Emisiones.csv')
    dfEmisA = pd.read_csv('Emisiones_anhos.csv')
    st.header('Generación y emisiones del sistema eléctrico de España')

    st.image("Imgn_REE.JPG")

    st.write('A continuación se pueden ver los datos en crudo:')

    with st.expander('Dataframes del Proyecto', False):
        st.dataframe(dfEmis)
        st.dataframe(dfEmisA)
        st.dataframe(df)
    
    st.write('---')


    renovables = ['Hidroeólica',
                  'Solar fotovoltaica',
                  'Solar térmica',
                  'Otras renovables',
                  'Eólica',
                  ]
    
    ####################################################################
    ####################################################################
    ####################################################################
    
    st.write('##### Generación energética por tipo de tecnología utilizada')
    st.write('Filtrado por años y tipo de energía (renovable vs no renovable)')

    with st.expander('Filtros'):
        selected = st.multiselect(label = 'Tipo de energía',
                    options = ['Renovables', 'No renovables'],
                    default = ['Renovables','No renovables'],
                    key = 'generación'
                    )
        
        from_ = st.slider('Desde', 2014, 2022, 2014, key = 'generación_from')
        to = st.slider('Hasta', from_, 2022, 2022, key = 'generación_to')

    columns_gen = [x for x in df.columns if 'Generación' in x]

    empty = False

    if len(selected) == 2:
        columns = [x for x in columns_gen] + ['Años']
    elif len(selected) == 0:
        empty = True
    elif selected[0] == 'Renovables':
        columns = [x for x in columns_gen if x[11:-4] in renovables] + ['Años']
    elif selected[0] == 'No renovables':
        columns = [x for x in columns_gen if x[11:-4] not in renovables] + ['Años']

    if not empty:

        generacion = df[columns]
        generacion = generacion[generacion['Años'].between(from_, to)]

        fig=px.bar(data_frame = generacion,
        x          = "Años",
        y          = generacion.columns[1:],
        title      ="")

        st.plotly_chart(figure_or_data = fig, use_container_width = True)

    ####################################################################
    ####################################################################
    ####################################################################

        año_max = sum([generacion.iloc[-1][x+1] for x in range(generacion.shape[1]-1)])

        porcentajes_generaciones = [round(generacion.iloc[-1][x+1]/año_max*100,2) for x in range(generacion.shape[1]-1)]

        energias = [generacion.columns[1:]][0]

        gen_100 = pd.DataFrame({"Tecnologías" : energias, "% Generación" : porcentajes_generaciones})
        
        gen_100 = gen_100[gen_100['Tecnologías'] != 'Años']

        fig = px.pie(data_frame = gen_100,
        names      = "Tecnologías",
        values     = "% Generación")

        st.plotly_chart(figure_or_data = fig, use_container_width = True)
    
    ####################################################################
    ####################################################################
    ####################################################################
    st.write('##### Emisiones de CO2 por tipo de tecnología utilizada')

    fig2=px.pie(data_frame = dfEmis,
       names      = "Tecnologías",
       values     = "% Emisiones")
    
    st.plotly_chart(figure_or_data = fig2, use_container_width = True)

    st.write('##### Emisiones de Co2 por tipo de energía utilizada y año')

    fig3=px.bar(data_frame = dfEmisA,
       x          = "Años",
       y          = dfEmisA.columns[1:-2],)
    
    st.plotly_chart(figure_or_data = fig3, use_container_width = True)







    
if __name__ == '__main__':
    main()