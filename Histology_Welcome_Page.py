
import streamlit as st

# Configuração inicial
st.set_page_config(
    page_title="Boas-vindas à Histologia I",
    layout="centered"
)

# Cabeçalho Institucional
st.markdown('''
<div style='text-align: center; font-family: Arial;'>
    <h2>UNIVERSIDADE FEDERAL DE CAMPINA GRANDE</h2>
    <h3>CENTRO DE FORMAÇÃO DE PROFESSORES</h3>
    <h4>UNIDADE ACADÊMICA DE ENFERMAGEM</h4>
</div>
''', unsafe_allow_html=True)

# Título da página
st.title("Bem-vindos à Disciplina de Histologia I")

# Mensagem de boas-vindas
st.markdown('''
<div style='text-align: justify; font-size: 18px; line-height: 1.6;'>
    <p>Queridos alunos,</p>
    <p>É com grande alegria que damos início à nossa jornada na disciplina de <strong>Histologia I</strong>. Aqui, exploraremos juntos o fascinante universo das células e dos tecidos, compreendendo como suas estruturas e funções moldam os organismos vivos.</p>
    <p>Sejam curiosos, questionem, descubram e mergulhem profundamente neste campo essencial para a compreensão da saúde e do funcionamento do corpo humano. Cada aula será uma oportunidade para crescermos juntos, conectando teoria à prática e transformando conhecimento em aprendizado significativo.</p>
    <p>Preparem-se para um semestre repleto de descobertas, desafios e conquistas!</p>
    <p><strong>Bem-vindos e sucesso nesta jornada!</strong></p>
</div>
''', unsafe_allow_html=True)

# Rodapé
st.markdown('''
<div style='text-align: center; font-size: small; color: gray; margin-top: 50px;'>
    Desenvolvido pelo Prof. Dr. Fábio Marques
</div>
''', unsafe_allow_html=True)
