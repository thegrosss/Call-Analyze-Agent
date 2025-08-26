import streamlit as st

from integration import giga, get_prompt

# Название чата
st.title("Агент оценки звонков")

# Список всех состояний
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role" : "ai",
            "content" : "Предоставьте текстовую запись телефонного разговора, а я проведу его анализ"
        }
    ]

# Отображение всех состояний в чате
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

if user_prompt := st.chat_input():
    # Ввод пользовательского запроса
    st.chat_message("user").write(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    with st.spinner("Анализирую 🤔"):
        # Получение ответа от GigaChat
        response = giga.chat(get_prompt(user_prompt))
        ai_answer = response.choices[0].message.content

        # Запись в список состояний ответ от GigaChat
        st.chat_message("ai").write(ai_answer)
        st.session_state.messages.append({"role": "ai", "content": ai_answer})