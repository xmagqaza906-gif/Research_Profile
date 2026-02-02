# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Research Profile",
    layout="wide"
)


st.markdown("""
<style>

.name-title {
    font-size: 32px;
    font-weight: bold;
    color: #1f4e79;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 18px;
    color: #555;
    margin-bottom: 15px;
}


img {
    border-radius: 50%;
    border: 3px solid #1f4e79;
}

</style>
""", unsafe_allow_html=True)


st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Research Profile", "Publications", "Projects", "Contact"]
)

if menu == "Research Profile":

    st.markdown('<div class="profile-container">', unsafe_allow_html=True)

    # Top section (Image + Name aligned)
    col1, col2 = st.columns([1, 4])

    with col1:
        st.image("pic.jpg", width=100)  # Replace with your image

    with col2:
        st.markdown(
            '<div class="name-title">Mr Xolani Magqaza</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="subtitle">Biostatistics | University of Fort Hare</div>',
            unsafe_allow_html=True
        )

    st.markdown("---")

    # Research Areas
    col3, col4 = st.columns(2)

    with col3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Research Focus")
        st.markdown("""
        - Clinical Trials & Experimental Design  
        - Genetic & Genomic Statistics  
        - Statistical Modeling in Health Sciences  
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Technical Expertise")
        st.markdown("""
        - Survival Analysis & Time-to-Event Data  
        - Biomedical Imaging & Diagnostics  
        - Data Analytics & Statistical Computing  
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    st.image(
        "data_analytics.jpg",
        caption="Statistical Data Analytics & Modeling",
        use_container_width=True
    )

elif menu == "Publications":

    st.title("Publications")

    uploaded_file = st.file_uploader(
        "Upload a CSV file of publications",
        type="csv"
    )

    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications, use_container_width=True)

        keyword = st.text_input("Filter by keyword")

        if keyword:
            filtered = publications[
                publications.apply(
                    lambda row: keyword.lower() in row.astype(str).str.lower().values,
                    axis=1
                )
            ]
            st.write(f"Results for '{keyword}':")
            st.dataframe(filtered, use_container_width=True)

        if "Year" in publications.columns:
            st.subheader("Publication Trends")
            year_counts = publications["Year"].value_counts().sort_index()
            st.bar_chart(year_counts)

elif menu == "Projects":

    st.title("Research Projects")

    st.subheader(
        "Investigating the Effect of the Step Size–Line Search Parameter "
        "for the Damped Newton Algorithm in Empirical Likelihood Ratio-Based Tests"
    )

    st.markdown("""
    This study examined how the **step size (line search parameter)** influences 
    the performance of the **Damped Newton Algorithm** in 
    **Empirical Likelihood Ratio (ELR)-based statistical tests**.

    **Key Areas:**
    - Convergence speed  
    - Numerical stability  
    - Accuracy of test statistics  
    - Computational efficiency  

    **Contribution:**
    - Guidance on optimal step size selection  
    - Improved reliability of ELR tests  
    - Enhanced computational performance  
    """)

    st.subheader("Astronomy Observations")
    st.write("Brightness and celestial observation data studies.")

    st.subheader("Weather Data Modeling")
    st.write("Temperature and humidity data analysis.")

elif menu == "Contact":

    st.title("Please get in touch")

    st.markdown("""
    📧 **Email:** xmagqaza906@gmail.com  
    📱 **Phone:** 0790488317  
    """)

