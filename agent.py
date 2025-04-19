from emotionalAnalysis import generate
from mvpagent import generate as responseAi

def Ai_Pipeline(name,age,gender,input):
    EmotionalAnalysis=generate(age=age,user_input=input,gender=gender)

    return responseAi(EmotionalAnalysis,name)