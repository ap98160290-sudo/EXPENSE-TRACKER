import streamlit as st
import pandas as pd
from storage import load_data,save_data
from tracker import create_transaction
from datetime import date
st.set_page_config(page_title="EXPENSE TRACKER",layout='wide')
st.title("💰💰 PERSONAL EXPENSE TRACKER 💰💰 ")

transactions=load_data()

AMOUNT=st.number_input("AMOUNT(in ₹)",min_value=0.00,step=100.00)
CATEGORY=st.text_input("CATEGORY")
DATE=st.date_input("TRANSACTION DATE",value=date.today())
NOTE=st.text_area("NOTE(optional)")

TYPE=st.selectbox("TRANSACTION TYPE",["INCOME","EXPENSE"])
TYPE=TYPE.upper()


can_submit=(AMOUNT>0,CATEGORY.strip()!="")

btn=st.button("ADD TRANSACTION",disabled=not can_submit)

if btn:
    try:
        transaction=create_transaction(AMOUNT,TYPE,CATEGORY,str(DATE),NOTE)
        transactions.append(transaction)
        save_data(transactions)
        st.success("TRANSACTION SUCCESSFULLY ADDED")
        st.rerun()

    except ValueError as e:
        st.error(str(e))

    

st.subheader(" ALL TRANSACTIONS ")
if not transactions:
    st.info("NO TRANSACTIONS FOUND")
else:
    df=pd.DataFrame(transactions)
    st.dataframe(df,width="stretch")

    st.subheader("DELETE TRANSACTION")

    index_to_delete=st.number_input("ENTER ROW NUMBER TO DELETE (starting from zero)",
    min_value=0,max_value=len(transactions)-1,step=1)


    btn1=st.button("DELETE TRANSACTIONS")
    if btn1:
        st.session_state["delete_index"]=index_to_delete

if "delete_index" in st.session_state:
    idx=st.session_state["delete_index"]

    st.warning(f"ARE YOU SURE TO DELETE THE TRASNSACTION AT ROW {idx}")

    col_yes,col_no=st.columns(2)


    with col_yes:
        if st.button("✅ DELETE"):
            transactions.pop(idx)
            save_data(transactions)
            del st.session_state["delete_index"]
            st.success("TRANSACTION SUCCESSFULLY DELETED")
            st.rerun()

    with col_no:
        if st.button("❌ CANCEL"):
            del st.session_state["delete_index"]