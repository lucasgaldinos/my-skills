#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "google-genai",
#     "python-dotenv",
# ]
# ///

# pyright: reportUnknownMemberType=false, reportUnknownVariableType=false, reportUnknownArgumentType=false, reportMissingTypeStubs=false, reportMissingImports=false

import sys
import time
import os
from datetime import datetime
from typing import Any, Literal
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load variables from a global ~/.<your-skills-folder>/.env if it exists, and fallback to local .env
load_dotenv(os.path.expanduser("~/.agents/.env"))
load_dotenv()

def run_research(query: str, file_paths: list[str] | None = None):
    """
    Executes a Deep Research query using Google Gemini and saves the output to a local markdown file.

    Args:
        query (str): The research query or topic.
        file_paths (list[str] | None): Optional list of file paths to upload as context before running.
    """
    # The client automatically picks up os.environ["GEMINI_API_KEY"]
    if not os.environ.get("GEMINI_API_KEY"):
        print("❌ Error: GEMINI_API_KEY environment variable is missing.")
        print("   Please create a ~/.<your-skills-folder>/.env file containing: GEMINI_API_KEY=your_key")
        print("   Or add it to a .env file in your current directory.")
        sys.exit(status=1)

    client = genai.Client()

    print(f"🔍 Starting Deep Research for: '{query}'")

    parts = [types.Part.from_text(text=query)]
    if file_paths:
        print(f"📤 Uploading {len(file_paths)} context files...")
        for file_path in file_paths:
            if not os.path.exists(file_path):
                print(f"⚠️ Warning: File not found: {file_path}")
                continue
            print(f"   Uploading {file_path}...")
            try:
                uploaded_file = client.files.upload(file=file_path)
                while uploaded_file.state.name == "PROCESSING":
                    time.sleep(2)
                    uploaded_file = client.files.get(name=uploaded_file.name)
                if uploaded_file.state.name == "FAILED":
                    print(f"❌ Failed to process file {file_path}")
                    continue
                parts.append(types.Part.from_uri(uri=uploaded_file.uri, mime_type=uploaded_file.mime_type))
            except Exception as e:
                print(f"❌ Failed to upload {file_path}: {e}")

    # Build the Content object required by interactions.create
    interaction_input = types.Content(role="user", parts=parts) if file_paths else query

    try:
        # Trigger the background research agent directly at Google
        interaction = client.interactions.create(
            agent="deep-research-preview-04-2026", # Or deep-research-max-preview-04-2026
            input=interaction_input,
            agent_config={
                "type": "deep-research",
                "thinking_summaries": "auto",
                "visualization": "off"
            },
            background=True
        )
    except Exception as e:
        print(f"❌ Failed to start research. API Error: {e}")
        sys.exit(1)

    print(f"⏳ Job ID [{interaction.id}] running. Polling Google API...")

    seen_step_ids = set()

    # Poll until completion
    while True:
        try:
            result = client.interactions.get(id=interaction.id)

            # Print intermediate steps safely
            if hasattr(result, 'steps') and result.steps:
                for step in result.steps:
                    step_id: Any | str = getattr(step, 'id', str(id(step)))
                    if step_id not in seen_step_ids:
                        seen_step_ids.add(step_id)

                        step_type: Any | str = getattr(step, 'type', getattr(step, 'step_type', 'unknown'))
                        if step_type == 'action':
                            # typically represents tool executions / searches
                            action_name: Any | str = getattr(getattr(step, 'action', None), 'name', 'Tool Call')
                            print(f"  [Action] {action_name}")
                        elif step_type == 'thought':
                            # represents internal reasoning
                            text: Any | str = getattr(step, 'text', '')
                            # Truncate long thoughts for terminal readability
                            if len(text) > 200:
                                text = text[:197] + "..."
                            print(f"  [Thinking] {text}")
                        elif getattr(step, 'text', None):
                            # fallback for generic text steps that are not the final output
                            # print(f"  [Step] {step.text[:100]}...")
                            pass

            if result.status == "completed":
                print("\n✅ Research Complete!\n")
                print("="*80)

                final_text = ""
                # Safely extract the final text from the outputs or steps array
                if hasattr(result, 'outputs') and result.outputs:
                    for output in result.outputs:
                        out_type = getattr(output, 'type', getattr(output, 'output_type', None))
                        if out_type == "text":
                            final_text += output.text + "\n"
                elif hasattr(result, 'output_text'):
                    final_text = result.output_text
                elif hasattr(result, 'steps'):
                    # if standard properties fail, extract the last valid text from step sequence
                    for step in reversed(result.steps):
                        step_type = getattr(step, 'type', getattr(step, 'step_type', 'unknown'))
                        if step_type not in ['action', 'thought'] and hasattr(step, 'text'):
                            final_text = step.text
                            break

                if not final_text:
                    final_text = "⚠️ Research completed, but no text output could be extracted from the API response."

                print(final_text)
                print("="*80)

                # Save to file
                cwd: str = os.getcwd()
                docs_dir: str = os.path.join(cwd, "docs", "deep-research")
                os.makedirs(docs_dir, exist_ok=True)

                timestamp: str = datetime.now().strftime("%Y%m%d_%H%M%S")
                save_path: str = os.path.join(docs_dir, f"research_{timestamp}.md")

                with open(save_path, "w", encoding="utf-8") as f:
                    f.write(f"# Deep Research: {query}\n\n")
                    f.write(final_text)

                print(f"📁 Research saved to: {save_path}")
                break

            elif result.status == "failed":
                print("\n❌ Research Failed on Google's backend!")
                break

        except Exception as e:
            print(f"⚠️ Polling error: {e}. Retrying in 15 seconds...")

        time.sleep(15)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: uv run deep-research.py \"Your complex query here\" [file1] [file2] ...")
        sys.exit(status=1)

    user_query: str = sys.argv[1]
    files_to_upload: list[str] = sys.argv[2:] if len(sys.argv) > 2 else []
    run_research(query=user_query, file_paths=files_to_upload)