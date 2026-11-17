"""Day 1 Gemini smoke test."""

import os
import time

from dotenv import load_dotenv

load_dotenv()


def main() -> None:
    model = os.getenv("LLM_MODEL", "").strip()
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not model:
        raise SystemExit("Missing required environment variable: LLM_MODEL")
    if not api_key or api_key == "PASTE_KEY_HERE":
        raise SystemExit("Missing required environment variable: GEMINI_API_KEY")

    from google import genai

    client = genai.Client(api_key=api_key)
    start = time.perf_counter()
    response = client.models.generate_content(
        model=model, contents="Reply with the single word: ok"
    )
    latency_ms = (time.perf_counter() - start) * 1000
    print(
        f"provider=gemini model={model} latency={latency_ms:.0f}ms "
        f"output={response.text!r}"
    )


if __name__ == "__main__":
    main()
