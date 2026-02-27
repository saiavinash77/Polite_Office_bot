import streamlit as st
from elasticsearch import Elasticsearch

# 1. SETUP PAGE
st.set_page_config(page_title="The Polite Office Bot", page_icon="👔")
st.title("👔 The Polite Office Bot")
st.subheader("Turn your anger into corporate success.")

# 2. CONNECT TO ELASTIC (Replace these!)
# You get Cloud ID from your deployment page
# You get Password from when you created the deployment
CLOUD_ID = "https://my-elasticsearch-project-e2a9d4.es.us-central1.gcp.elastic.cloud:443"
API_KEY = "U3BMRW41d0J4SnpSQjdRRktNWk46OHFWTVd0THA4VW9TeDdBTmtGTDhjdw==" # Or use basic_auth=("elastic", "YOUR_PASSWORD")

# Try to connect
try:
    es = Elasticsearch(
        cloud_id=CLOUD_ID,
        basic_auth=("elastic", "YOUR_PASSWORD_HERE")
    )
except:
    st.error("Could not connect to Elastic. Check your ID and Password.")

# 3. THE INPUT BOX
angry_text = st.text_area("Enter your angry email here:", height=100)

if st.button("Translate to Corporate Speak"):
    if angry_text:
        with st.spinner("Consulting HR..."):

            # 4. SEARCH ELASTIC
            # We search for the closest matching angry phrase in your database
            response = es.search(
                index="polite-index",
                body={
                    "query": {
                        "match": {
                            "angry": angry_text
                        }
                    }
                }
            )

            # 5. DISPLAY RESULT
            if response['hits']['hits']:
                # Get the best match
                best_match = response['hits']['hits'][0]['_source']
                polite_version = best_match['polite']
                category = best_match.get('category', 'General')

                st.success("✅ Professional Translation:")
                st.code(polite_version, language="text")

                st.info(f"Detected Category: {category}")
                st.caption(f"Matched based on: '{best_match['angry']}'")
            else:
                st.warning("No exact match found in database, but here is a generic safe response:")
                st.code("I will take this under advisement and get back to you.", language="text")
    else:
        st.warning("Please enter some text first.")

# Footer
st.markdown("---")
st.markdown("Built with **Elasticsearch** & **Streamlit**")
