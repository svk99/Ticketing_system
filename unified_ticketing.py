import streamlit as st

st.subheader('Pune Unified Ticket System')

# Initialize session state variables
if 'counter' not in st.session_state:
    st.session_state.counter = 100
if 'list_of_ticket_ids' not in st.session_state:
    st.session_state.list_of_ticket_ids = []

t1, t2 = st.tabs(['Generate Ticket', 'Cancel Ticket'])

with t1:
    journey_from = st.selectbox('From', ['Swargate', 'FC Road', 'Deccan', 'Camp'])
    journey_destination = st.selectbox('To', ['Swargate', 'FC Road', 'Deccan', 'Camp'])
    if st.button('Submit'):
        if journey_from != journey_destination:
            ticket_id = journey_from[0] + journey_destination[0] + str(st.session_state.counter + 1)
            st.session_state.list_of_ticket_ids.append(ticket_id)
            st.session_state.counter += 1
            st.write('The ticket id is', ticket_id)
            st.write('The fare is Rs.10')
        else:
            st.write('Journey from and destination cannot be the same.')

with t2:
    if st.session_state.list_of_ticket_ids:
        id_to_cancel = st.selectbox('Select ticket to be cancelled', st.session_state.list_of_ticket_ids)
        if st.button('Cancel Ticket'):
            st.session_state.list_of_ticket_ids.remove(id_to_cancel)
            st.write('Ticket cancelled. Updated list:', st.session_state.list_of_ticket_ids)
    else:
        st.write('No tickets to cancel.')
