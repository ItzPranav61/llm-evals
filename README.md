# Day 1 Gemini smoke test

1. Set up `.env` with your Gemini API key and selected model:

   ```text
   LLM_PROVIDER=gemini
   LLM_MODEL=your-selected-model
   GEMINI_API_KEY=your-key
   ```

2. List available Gemini models:

   ```powershell
   uv run list_models.py
   ```

3. Run the smoke test:

   ```powershell
   uv run hello_llm.py
   ```
