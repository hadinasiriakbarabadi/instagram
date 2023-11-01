import os
import openai
openai.api_key=""
class AIGEenerator:
    def __init__(self,api_key):
        self.api_key=api_key
        pass
    
    def generate_prompt(self):
        response=openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt="create a alien planet image promptcreate a alien planet image prompt\n\nThe sky was an eerie shade of violet on the alien planet, an effect caused by the planet's three suns constantly setting and rising in quick succession. The air was thick and humid, with a green mist floating just above the ground. This mist was the planet's primary source of oxygen, making it difficult for any outsiders to survive without the proper equipment.\n\nAs I gazed upon the landscape, I was mesmerized by the unusual plants that seemed to glow in the dim light. The trees were a neon shade of blue, with leaves that appeared to be made of a metallic material. Small orbs of light floated around them, emitting a soft humming noise.\n\nIn the distance, I could see a herd of alien creatures grazing on the luminescent pink grass. Their bodies were slender and covered in a shimmering silver fur, with long antenna-like ears waving in the gentle breeze. As they moved, the ground beneath them seemed to light up, leaving a trail of glowing footsteps behind.\n\nAs I continued to explore, I came across a crystal-clear lake that seemed to stretch on for miles. But upon closer inspection, I realized it was not water, but a thick substance that emitted a soft blue light. I watched as small aquatic creatures swam in the substance,",
            temperature=1.4,
            max_tokens=60,
            top_p=1,
            frequency_penalty=0.5,
            presence_penalty=0.5
            )
        res_text=response.choices[0].text
        return res_text
    def generate_images(sef,prompt):
        response=openai.Image.create(
            prompt=prompt,
            n=3,
            size='512x512'
        )
        images_urls=[
            response['data'][0]['url'],
            response['data'][1]['url'],
            response['data'][2]['url']
        ]
        return images_urls
    def generate_prompt_and_image(self):
        prompt=self.generate_prompt()
        images=self.generate_images(prompt)
        return prompt,images

    