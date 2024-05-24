import os, logging
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, executor
from langchain_community.llms.ctransformers import CTransformers
from langchain_core.prompts import PromptTemplate
from langchain.chains.llm import LLMChain
from langchain_community.llms.ollama import Ollama

load_dotenv()

TELEGRAM_API_TOKEN = os.getenv("TOKEN")
MODEL = os.getenv("MODEL_LOCATION")


bot = Bot(token=TELEGRAM_API_TOKEN)
disp = Dispatcher(bot)

@disp.message_handler(commands=['start', 'help'])
async def command_start_handler(messages:types.Message):
    """This handler receives messages from '/start' or '/help' command

    Args:
        message(types.Message):_description_
    """
    await messages.reply("Hi!\nI am a chatter bot.")

@disp.message_handler()
async def echo(message: types.Message):

    B_INST, E_ISNT = "[INST]","[/INST]"
    B_SYS, E_SYS = "<<SYS>>\n", "\n<<SYS>>\n\n"
    CUSTOM_SYSTEM_PROMPT = """\
        You are a software product support consultant for a product known as AI-Spy. Answer the user quesries!
        """
    SYSTEM_PROMPT = B_SYS+CUSTOM_SYSTEM_PROMPT+E_SYS

    instruction = f"reply user for his message: {message.text}"

    template = B_INST+SYSTEM_PROMPT+instruction+E_ISNT

    
    prompt = PromptTemplate(template=template, input_variables=["message"])


    model = CTransformers(model=MODEL,
                    model_type = "llama",
                    config={'max_new_tokens':250,
                        'temperature':0.01})
    
    #model = Ollama(model="llama3")
    
    llm_chain = LLMChain(prompt=prompt, llm=model)
    input_data = {
            "input": message.text
        }

    response = llm_chain.invoke(input=input_data)
    print(response)

    await message.reply(response['text'])

if __name__ == "__main__":
    executor.start_polling(disp, skip_updates=True)
    