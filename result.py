import streamlit as st

def show_result_page():
    st.title('チューリングテスト - 判定結果')

    # セッションステートの初期化
    if 'evaluation_submitted' not in st.session_state:
        st.session_state.evaluation_submitted = False

    # フォームの作成
    with st.form("evaluation_form"):
        # 人間かロボットかの選択
        identity = st.radio(
            "判定結果を選択してください：",
            ["人間", "AI（ロボット）"],
            index=None
        )

        # 確信度のスライダー
        confidence = st.slider(
            "判断の確信度（1-10）：",
            min_value=1,
            max_value=10,
            value=5
        )

        # 判断理由のテキストエリア
        reason = st.text_area(
            "判断理由を詳しく説明してください：",
            height=150
        )

        # 送信ボタン
        submitted = st.form_submit_button("結果を送信")

        if submitted:
            if not identity:
                st.error("判定結果を選択してください。")
            elif not reason:
                st.error("判断理由を入力してください。")
            else:
                st.session_state.evaluation_submitted = True
                st.session_state.evaluation_result = {
                    "identity": identity,
                    "confidence": confidence,
                    "reason": reason
                }

    # 送信後の結果表示
    if st.session_state.evaluation_submitted:
        st.success("評価が送信されました！")

        st.subheader("提出された評価：")
        st.write(f"判定結果： {st.session_state.evaluation_result['identity']}")
        st.write(f"確信度： {st.session_state.evaluation_result['confidence']}/10")
        st.write("判断理由：")
        st.write(st.session_state.evaluation_result['reason'])

        # Display the time taken for the conversation
        if 'end_time' in st.session_state and 'start_time' in st.session_state:
            time_taken = st.session_state.end_time - st.session_state.start_time
            minutes, seconds = divmod(int(time_taken), 60)
            st.write(f"会話にかかった時間： {minutes}分 {seconds}秒")
