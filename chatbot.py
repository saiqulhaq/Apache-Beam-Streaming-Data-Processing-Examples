import json
from concurrent import futures
from typing import Callable

import streamlit as st
from google.cloud import pubsub_v1

project_id = "sandbox-boxsand"
topic = "chatbot-pycon2024"
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project=project_id, topic=topic)
publish_futures = []


def get_callback(publish_future: pubsub_v1.publisher.futures.Future,
                 data: str) -> Callable[[pubsub_v1.publisher.futures.Future], None]:
    def callback(publish_future: pubsub_v1.publisher.futures.Future) -> None:
        try:
            # Wait 60 seconds for the publish call to succeed
            print(publish_future.result(timeout=60))
        except futures.TimeoutError:
            print(f"Publishing {data} timed out")

    return callback


def main():
    st.title('Chatbot')

    if "message" not in st.session_state:
        st.session_state["message"] = [
            {"role": "assistant", "content": "Hi, I'm a calculator bot. I'll sum your input number"}]

    for msg in st.session_state.message:
        st.chat_message(msg["role"]).write(msg["content"])

    prompt = st.chat_input("What number do you have?")
    if prompt:
        st.session_state["message"].append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        try:
            number = int(prompt)
            data = json.dumps({"number": number})
            publish_future = publisher.publish(topic_path, data.encode("utf-8"))
            publish_future.add_done_callback(get_callback(publish_future, data))
            publish_futures.append(publish_future)

        except ValueError:
            st.session_state["message"].append({"role": "assistant", "content": prompt})
            with st.chat_message("assistant"):
                st.write("Hmmm... seems your input is not a number. Any mistakes?")

        finally:
            futures.wait(publish_futures, return_when=futures.ALL_COMPLETED)


if __name__ == '__main__':
    main()
