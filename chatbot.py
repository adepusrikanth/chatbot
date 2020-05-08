from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import nltk
from nltk.corpus import stopwords
set(stopwords.words('english'))
 
# Creating ChatBot Instance
chatbot = ChatBot(
    'CoronaBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
) 
 # Training with Personal Ques & Ans 
conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome.",
	"What is corona virus?",
	"Corona viruses are a large family of viruses which may cause illness in animals or humans. In humans several coronaviruses are known to cause respiratory infections ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS)and Severe Acute Respiratory Syndrome (SARS.The most recently discovered coronavirus causes coronavirus disease COVID-19. ",
	"How does COVID-19 spread?",
	"COVID-19 is most likely to spread from person-to-person through: 1.close contact with a person while they are infectious or in the 24 hours before their symptoms appeared 2.close contact with a person with a confirmed infection who coughs or sneezes 3.touching objects or surfaces (such as door handles or tables) contaminated from a cough or sneeze from a person with a confirmed infection and then touching your mouth or face.",
	"What is corona virus?","Corona viruses are a large family of viruses which may cause illness in animals or humans. In humans several coronaviruses are known to cause respiratory infections ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS)and Severe Acute Respiratory Syndrome (SARS.The most recently discovered coronavirus causes coronavirus disease COVID-19. ",
    "How does COVID-19 spread?","COVID-19 is most likely to spread from person-to-person through: 1.close contact with a person while they are infectious or in the 24 hours before their symptoms appeared 2.close contact with a person with a confirmed infection who coughs or sneezes 3.touching objects or surfaces (such as door handles or tables) contaminated from a cough or sneeze from a person with a confirmed infection and then touching your mouth or face.",
    "Can I leave home?","All people are required to stay home unless it is absolutely necessary to go outside.",
    "Should I be tested for COVID-19?","Your doctor will tell you if you should be tested. They will arrange for the test.",
    "Should I wear a face mask?","You do not need to wear a mask if you are healthy. For more information on the use of surgical masks visit this page on the Health website",
    "Should I be taking my kids out of childcare or school?","Schools and childcare are compeletly closed till furthure order.",
    "What about working from home?","Indians are encouraged to work from home where they can.",
    "What about public transport like planes buses trains ride shares and taxis?","The Government recommends that employers offer flexible working arrangements to minimise the number of people catching public transport at any one time. Long distance services carry a higher risk of infection and should be reconsidered at this time.",
    "What is the government doing to contain the spread of COVID-19?","The government is following the instructions of the WHO carefully and every level of public health machinery is aligned to it. The ministry of health is constantly updated about the numbers of cases and provides instructions to doctors and hospitals regarding the isolation and treatment of patients with the disease. The government has stopped the entry of people from countries affected by this disease by cancelling visas. Those who are suspected of having the disease are being tested. Quarantine facilities have been put into place in multiple locations. Ideally a mechanism for testing anyone who suspects they have the disease should be put in place but this is yet to happen.",
    "Is this infection going to stay or disappear? Will warmer weather help to contain the virus spread? Will it reappear once colder weather returns?","This is particularly hard to predict. Some viral diseases (e.g. flu) are largely seasonal and tend to spread more easily in winters rather than in the heat of the summer. We have no idea as of now whether COVID-19 will fall into this category. It could vanish altogether after the summer or  perhaps more likely scenarioâ€‰â€”â€‰it could appear again in a second wave. We simply donâ€™t know yet.",
    "Is there a vaccine against it or a medicine I can take if I get infected?","No not yet although many laboratories around the world are working on this. There are a number of vaccine candidates that are being developed and a number of existing medicines for other diseases are being tested on COVID-19 patients to see if they will work. Making a safe vaccine available takes time up to a year or two at best.",
    "Can I get the infection from eating say meat or by using products from China?","No not at all. First of all this is a virus that is being transmitted between humans through a respiratory route; just any animal you might encounter wonâ€™t harbour it. So eating meat has nothing to do with getting a coronavirus infection. Also viruses such as this one donâ€™t last long on exposed surfaces and donâ€™t tolerate high temperatures very well. The delays in a package reaching from China to India will ensure that no virus will survive the journey to infect you. It is thus safe to use products from China without fear of infection.",
    "what is indian government official website for coronavirus"," Here it is - https://www.mohfw.gov.in/index.html",
    "What is COVID-19","COVID-19 is the infectious disease caused by the most recently discovered corona virus. This new virus and disease were unknown before the outbreak began in Wuhan China in December 2019.",
    "What are the symptoms of COVID-19","The most common symptoms of COVID-19 are fever tiredness and dry cough. Some patients may have aches and pains nasal congestion runny nose sore throat or diarrhea. These symptoms are usually mild and begin gradually  Some people become infected but donâ€™t develop any symptoms and don't feel unwell. Most people (about 80%) recover from the disease without needing special treatment.Around 1 out of every 6 people who gets COVID-19 becomes seriously ill and develops difficulty breathing",
    "Can the virus that causes COVID-19 be transmitted through the air?","Studies to date suggest that the virus that causes COVID-19 is mainly transmitted through contact with respiratory droplets rather than through the air. See previous answer on â€œHow does COVID-19 spread?â€",
    "Can CoVID-19 be caught from a person who has no symptoms?","The main way the disease spreads is through respiratory droplets expelled by someone who is coughing. The risk of catching COVID-19 from someone with no symptoms at all is very low.However many people with COVID-19 experience only mild symptoms.",
    "Can I catch COVID-19 from the feces of someone with the disease? ","The risk of catching COVID-19 from the feces of an infected person appears to be low  While initial investigations suggest the virus may be present in feces in some cases spread through this route is not a main feature of the outbreak The ongoing research on the waysCOVID-19 is spread and will continue to share new findings",
    "What can I do to protect myself and prevent the spread of disease","1.Regularly and thoroughly clean your hands with an alcoholbased hand rub\nMaintain at least 1 metre (3 feet) distance between yourself andanyone who is coughing or sneezing\nAvoid touching eyes nose and mouth\n Make sure you and the people around you follow good respiratory hygiene. This means covering your mouth and nose with your bent elbow or tissue when you cough or sneeze\nStay home if you feel unwell\n Keep up to date on the latest COVID-19 hotspots (cities or local areas where COVID-19 is spreading widely).",
    "How likely am I to catch COVID-19?","The risk depends on where you are - and more specifically whether there is a COVID-19 outbreak unfolding there.",
    "Should I worry about COVID-19?","Illness due to COVID-19 infection is generally mild especially for children and young adults",
    "Who is at risk of developing severe illness","While we are still learning about how COVID-2019 affects people older persons and persons with pre-existing medical conditions (such as high blood pressure heart disease lung disease cancer or diabetes) appear to develop serious illness more often than others.",
    "Are antibiotics effective in preventing or treating the COVID-19?","No. Antibiotics do not work against viruses they only work on bacterial infections",
    "Are there any medicines or therapies that can prevent or cure COVID-19","While some western traditional or home remedies may provide comfort and alleviate symptoms of COVID-19 there is no evidence that current medicine can prevent or cure the disease",
    "Is there a vaccine drug or treatment for COVID-19","Not yet  However those affected should receive care to relieve symptoms.",
    "Is COVID-19 the same as SARS?","No. The virus that causes COVID-19 and the one that caused the outbreak of Severe Acute Respiratory Syndrome (SARS) in 2003 are related to each other genetically",
    "How long is the incubation period for COVID-19?","The â€œincubation periodâ€ means the time between catching the virus and beginning to have symptoms of the disease Most estimates of the incubation period for COVID-19 range from 1-14 days most commonly around five days. These estimates will be updated as more data become available. ",
    "Can humans become infected with the COVID-19 from an animal source?","To protect yourself such as when visiting live animal markets avoid direct contact with animals and surfaces in contact with animals. Ensure good food safety practices at all times",
    "Can I catch COVID-19 from my pet?","While there has been one instance of a dog being infected in Hong Kong  to date there is no evidence that a dog cat or any pet can transmit COVID-19 COVID-19 is mainly spread through droplets produced when an infected person coughs sneezes or speaks.",
    "How long does the virus survive on surfaces?","It is not certain how long the virus that causes COVID-19 survives on surfaces but it seems to behave like other corona viruses  Studies suggest that corona viruses (including preliminary information on the COVID-19 virus) may persist on surfaces for a few hours or up to several days",
    "Is it safe to receive a package from any area where COVID-19 has been reported?","Yes. The likelihood of an infected person contaminating commercial goods is low and the risk of catching the virus that causes COVID-19 from a package that has been moved travlled and exposed to different conditions and temperature is also low.",
    "Is there anything I should not do?","Smoking and  Wearing multiple masks and  Taking antibiotics."

	


]

trainer = ListTrainer(chatbot)
trainer.train(conversation)



# Training with English Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.english'
) 