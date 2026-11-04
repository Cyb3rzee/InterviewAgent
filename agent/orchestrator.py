import ollama
from memory.retrieval import ProfileRetriever

class InterviewAgent:
    def __init__(self, model_name: str = "llama3.2:3b"):
        self.model_name = model_name
        self.retriever = ProfileRetriever()

    def stream_answer(self, question: str):
        context = self.retriever.get_context(question)
        
        system_prompt = (
            "You are an interview assistant representing the candidate. "
            "STRICT RULE: Use ONLY the provided candidate background to answer questions. "
            "Keep your response concise and focused (100–150 words max). "
            "Do NOT fabricate experience."
        )

        user_prompt = f"{context}\nINTERVIEWER QUESTION: {question}"

        response_stream = ollama.chat(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            options={"num_predict": 250, "temperature": 0.5},
            stream=True
        )

        for chunk in response_stream:
            yield chunk["message"]["content"]
