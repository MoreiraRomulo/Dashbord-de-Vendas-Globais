import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


# Carregar os dados:
@st.cache_data
def load_data():
    df = pd.read_csv('dataset2.csv')
    df = df.drop('Unnamed: 0', axis=1)
    return df

df = load_data()


# Configurações da página
st.set_page_config(layout='wide',initial_sidebar_state='collapsed')




# Título
st.title("_Dashbord Analítico de Vendas Globais_",
         text_alignment= "center",
         help = "Por padrão o dashbord exibe as informações de todo o período. Abra a janela lateral para escolher um período específico.")

# 1° Filtro: Anos
ano_inicial = df['Ano'].unique().min()
ano_final = df['Ano'].unique().max()
ano = st.sidebar.slider('Ano', min_value= ano_inicial, max_value= ano_final, value = (ano_inicial,ano_final)  )

df_filtro = df[ (df['Ano']>=ano[0]) &  (df['Ano']<=ano[1]) ]


# 2° Filtro: Países
pais = st.sidebar.multiselect('País', df['Pais'].unique())

if pais:
    df_filtro = df_filtro[df_filtro['Pais'].isin(pais)]
elif len(pais)==1:
    pais_unico= pais[0]
    
# 3° Filtro: Segmento
segmento = st.sidebar.multiselect('Segmento', df['Segmento'].unique())
if segmento:
    df_filtro = df_filtro[df_filtro['Segmento'].isin(segmento)]
    if len(segmento)==1:
        segmento_unico=segmento[0]


# Layout da página
col1, col0 = st.columns(2, border = True)
col2 = st.container(border=True)
col3, col4 = st.columns([0.60,0.40],border = True)
col5 = st.container(border=True)



# 1° gráfico: número total de vendas
col1.metric(label = '**Total de Vendas:**',value = f"US$ {df_filtro['Total_Vendas'].sum():,.0f}".replace(",","."))

# col0 = SubCategoria mais vendida
df_subcatg = df_filtro.groupby(['SubCategoria'], as_index=False)['Total_Vendas'].sum().sort_values(by='Total_Vendas', ascending = False).head(1)

col0.metric(label = f"**Produto mais vendido:** :red-background[{df_subcatg.iloc[0,0]}]", 
            value = f"US$ {df_subcatg.iloc[0,1]:,.0f}".replace(",","."))


# 2° gráfico: 
df_seg = df_filtro.groupby(['Ano','Segmento'],as_index = False)['Total_Vendas'].sum()

fig2 = px.bar(df_seg, x='Ano', y='Total_Vendas', color='Segmento', 
              category_orders={'Segmento':['Home Office','Corporativo','Consumidor']} ,
               text=['US$ {:,.0f}'.format(x).replace(",",".") for x in df_seg['Total_Vendas']])
fig2.update_layout(yaxis_title = None)
col2.subheader('Vendas por *:blue[Segmento]*')
col2.plotly_chart(fig2,theme="streamlit")



# 3° gráfico: Vendas realizadas por categoria
df_catg = df_filtro.groupby(['Ano','Categoria'],as_index=False)['Total_Vendas'].sum()
fig3 = px.bar(df_catg, x = 'Total_Vendas', y = 'Ano', color = 'Categoria', 
              category_orders={'Categoria':['Suprimentos','Moveis','Tecnologia']}, orientation='h' ,
              text=['US$ {:,.0f}'.format(x).replace(",",".") for x in df_catg['Total_Vendas']])
fig3.update_layout(yaxis_title = None)
fig3.update_layout(xaxis_title = None)
col3.subheader('Vendas por *:blue[Categoria]*')
col3.plotly_chart(fig3)


# MAPA DE ÁRVORE:
df_pais = df_filtro.groupby(['Pais'],as_index = False)['Total_Vendas'].sum().sort_values(by='Total_Vendas',ascending=False).head(20)
fig5 = px.treemap(df_pais,path=['Pais'],values='Total_Vendas',color='Total_Vendas')
col5.subheader('Maiores mercados consumidores')
col5.plotly_chart(fig5)


# 5° gráfico: Vendas por SubCategoria(deixar claro a classificação 'Categoria' -> 'SubCategoria')
df_subc = df_filtro.groupby(['Categoria','SubCategoria'],as_index=False)['Total_Vendas'].sum().sort_values(by='Total_Vendas',ascending=False)
fig4 = px.bar(df_subc, x ='Total_Vendas', y='SubCategoria', color = 'Categoria',
              category_orders={'Categoria':['Suprimentos','Moveis','Tecnologia']} ,orientation='h')
col4.subheader('Vendas por *:blue[SubCategoria]*')
fig4.update_layout(yaxis_title = None)
fig4.update_layout(xaxis_title = None)
col4.plotly_chart(fig4)



