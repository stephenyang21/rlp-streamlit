
from utils import decode_raw_tx
from dataclasses import asdict  
from hex_json import hex_deserialize
import streamlit as st

st.title("RLP Decoder")

message = st.text_input("Enter the message to decode:")

okButtom = st.button("OK")

if okButtom:
    res = decode_raw_tx(message)
    message_decode = asdict(res)  
    st.subheader("JSON Message:")

    st.json((message_decode))