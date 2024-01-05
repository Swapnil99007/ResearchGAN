import os
import time
from openai import OpenAI

client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])

assistant = client.beta.assistants.create(
  name="Researcher",
  instructions="""You are a research scientist assistant, skilled in explaining complex academic \\
  concepts with simplicity and creative flair. When given the title and abstract from any academic 
  research paper, you are able to easily break down research paper abstracts into several parts 
  to help others understand what the research paper is all about. I will be giving you a abstract from a
  research paper and you need to present it in 10 points.""",
  model="gpt-3.5-turbo-1106",
)
thread = client.beta.threads.create()

# thread = client.beta.threads.create(
#     messages=[
#         {
#             "role":"user",
#             "content":
#             """
#             Title: A benchmark for extreme conditions of the multiphase interstellar medium in the most luminous hot dust-obscured galaxy at z = 4.6
#             Abstract: WISE J224607.6-052634.9 (W2246-0526) is a hot dust-obscured galaxy at z = 4.601, and the most luminous obscured quasar known to date. W2246-0526 harbors a heavily obscured supermassive black hole that is most likely accreting above the Eddington limit. We present observations with the Atacama Large Millimeter/submillimeter Array (ALMA) in seven bands, including band 10, of the brightest far-infrared (FIR) fine-structure emission lines of this galaxy: [OI]63μm, [OIII]88μm, [NII]122μm, [OI]145μm, [CII]158μm, [NII]205μm, [CI]370μm, and [CI]609μm. A comparison of the data to a large grid of Cloudy radiative transfer models reveals that a high hydrogen density (nH∼3×103 cm−3) and extinction (AV∼300 mag), together with extreme ionization (log(U)=−0.5) and a high X-ray to UV ratio (αox≥−0.8) are required to reproduce the observed nuclear line ratios. The values of αox and U are among the largest found in the literature and imply the existence of an X-ray-dominated region (XDR). In fact, this component explains the a priori very surprising non-detection of the [OIII]88μm emission line, which is actually suppressed, instead of boosted, in XDR environments. Interestingly, the best-fitted model implies higher X-ray emission and lower CO content than what is detected observationally, suggesting the presence of a molecular gas component that should be further obscuring the X-ray emission over larger spatial scales than the central region that is being modeled. These results highlight the need for multiline infrared observations to characterize the multiphase gas in high redshift quasars and, in particular, W2246-0526 serves as an extreme benchmark for comparisons of interstellar medium conditions with other quasar populations at cosmic noon and beyond.
#             """,
#         },
#     ]
# )

message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=
    """
    Title: A benchmark for extreme conditions of the multiphase interstellar medium in the most luminous hot dust-obscured galaxy at z = 4.6
    Abstract: WISE J224607.6-052634.9 (W2246-0526) is a hot dust-obscured galaxy at z = 4.601, and the most luminous obscured quasar known to date. W2246-0526 harbors a heavily obscured supermassive black hole that is most likely accreting above the Eddington limit. We present observations with the Atacama Large Millimeter/submillimeter Array (ALMA) in seven bands, including band 10, of the brightest far-infrared (FIR) fine-structure emission lines of this galaxy: [OI]63μm, [OIII]88μm, [NII]122μm, [OI]145μm, [CII]158μm, [NII]205μm, [CI]370μm, and [CI]609μm. A comparison of the data to a large grid of Cloudy radiative transfer models reveals that a high hydrogen density (nH∼3×103 cm−3) and extinction (AV∼300 mag), together with extreme ionization (log(U)=−0.5) and a high X-ray to UV ratio (αox≥−0.8) are required to reproduce the observed nuclear line ratios. The values of αox and U are among the largest found in the literature and imply the existence of an X-ray-dominated region (XDR). In fact, this component explains the a priori very surprising non-detection of the [OIII]88μm emission line, which is actually suppressed, instead of boosted, in XDR environments. Interestingly, the best-fitted model implies higher X-ray emission and lower CO content than what is detected observationally, suggesting the presence of a molecular gas component that should be further obscuring the X-ray emission over larger spatial scales than the central region that is being modeled. These results highlight the need for multiline infrared observations to characterize the multiphase gas in high redshift quasars and, in particular, W2246-0526 serves as an extreme benchmark for comparisons of interstellar medium conditions with other quasar populations at cosmic noon and beyond.
    """
)

run = client.beta.threads.runs.create(
  thread_id=thread.id,
  assistant_id=assistant.id,
)

messages = client.beta.threads.messages.list(
  thread_id=thread.id
)

while True:
    sleep_time = 3
    print(f"Sleeping for {sleep_time} seconds")
    time.sleep(sleep_time)
    run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
    )
    print("Current Status: ", run.status)
    if run.status != 'in_progress':
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        print(messages.data[0].content[0].text.value)
        break
