from anthropic import Anthropic
from dotenv import load_dotenv
from pydantic import BaseModel
from sys import stdin

load_dotenv()  # reads variables from a .env file and sets them in os.environ

class SomeText(BaseModel):
    text: str

def main():
    # This program will be called as a Vim filter, so the input will be visually selected text from the editor. The goal is to correct the grammar and spelling of the text using an LLM, and then return the corrected text back to Vim.
    client = Anthropic()
    corrected = client.messages.parse(
            model="claude-opus-4-7",
            max_tokens=1024,
            messages=[
                {
                    "role": "user",
                    "content": "Output the following text (which is either EN-US or DE-DE) with correct grammar and spelling, but do not change the meaning of the text: " + str(stdin.read()),
                }
                ],
            output_format=SomeText, # Tells the API to return output as the Pydantic model defined above
            ).parsed_output
    print(corrected.text, end="")  # end="" prevents adding a trailing newline character

if __name__ == "__main__":    main()
