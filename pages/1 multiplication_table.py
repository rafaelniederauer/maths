import streamlit as st
import random

def generate_question():
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    return a, b, a * b

def main():
    times = 10
  
    st.title("Multiplication Table Quiz")
    st.write(f"Answer {times} questions correctly to complete the quiz.")

    if 'questions' not in st.session_state:
        st.session_state.questions = [generate_question() for _ in range(times)]
        st.session_state.current_question = 0
        st.session_state.correct_answers = 0
        st.session_state.user_answers = [""] * times
        st.session_state.quiz_completed = False

    if not st.session_state.quiz_completed:
        question = st.session_state.questions[st.session_state.current_question]
        st.write(f"Question {st.session_state.current_question + 1}: What is {question[0]} x {question[1]}?")
        user_answer = st.text_input("Your answer:", value=st.session_state.user_answers[st.session_state.current_question])
        
        if st.button("Submit"):
            if user_answer.isdigit() and int(user_answer) == question[2]:
                st.session_state.correct_answers += 1
            st.session_state.user_answers[st.session_state.current_question] = user_answer
            st.session_state.current_question += 1
            
            if st.session_state.current_question == times:
                st.session_state.quiz_completed = True
                st.write("Quiz completed!")
                st.write(f"You answered {st.session_state.correct_answers} out of {times} questions correctly.")
            else:
                st.experimental_rerun()
    else:
        st.write(f"Quiz completed! You answered {st.session_state.correct_answers} out of {times} questions correctly.")
        if st.button("Restart Quiz"):
            st.session_state.questions = [generate_question() for _ in range(times)]
            st.session_state.current_question = 0
            st.session_state.correct_answers = 0
            st.session_state.user_answers = [""] * times
            st.session_state.quiz_completed = False
            st.experimental_rerun()

if __name__ == "__main__":
    main()
