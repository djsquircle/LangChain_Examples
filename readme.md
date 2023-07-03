# LangChain Examples

A collection of working code examples using LangChain for natural language processing tasks. This repository provides implementations of various tutorials found online. Please refer to the acknowledgments section for the source tutorials where most of the code examples originated and were inspired from.

## Table of Contents

- [Project Setup and Installation](#project-setup-and-installation)
- [Usage and Examples](#usage-and-examples)
- [Features](#features)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)
- [Support and Contact](#support-and-contact)
- [Acknowledgments](#acknowledgments)

## Project Setup and Installation

You can use markdown formatting to make the steps in the "Project Setup and Installation" section look cleaner. Here's an example:

## Project Setup and Installation

To set up the project, follow these steps:

1. Set up a Python virtual environment:

   ```shell
   # Create a virtual environment
   python3 -m venv myenv
   
   # Activate the virtual environment
   source myenv/bin/activate
   ```

2. Install the Python dependencies:

   ```shell
   # Install required packages
   pip install python-dotenv langchain openai newspaper3k pypdf
   ```

3. Create your `.env` file:

   ```shell
   # Create a new file named .env
   touch .env
   
   # Open the .env file in a text editor and add the following line:
   OPENAI_API_KEY="copy your key material here"
   ```

4. Copy the examples to a Python file and run them. Start experimenting with your own variations.

   ```shell
   # Copy the example code to a Python file, e.g., example.py
   cp examples.py example.py
   
   # Run the Python file
   python example.py
   ```


## Usage and Examples

This project provides small examples of working with LangChain using Python.

## Features

01.00_surferbro_prompt_template.py
01.01_simple_prompt_template.py
01.02_simple_prompt_template.py
01.03_simple_naming_assistant.py
01.04_simple_summarizer.py
01.05_simple_prompt_template.py
02.01_simple_movie_assistant.py
02.02_simple_movie_assistant.py
03.01_dj_squircle_life_coach_with_few_shot_example_step_by_step.py
03.02_dj_squircle_life_coach_with_few_shot_examples.py
04.01_save_few_shot_example_prompts.py
04.02_load_few_shot_example_prompts.py
04.03_save_several_few_shot_example_prompts.py
04.04_load_several_few_shot_examples.py
05.01_few_shot_example_prompt.py
06.01_how_many_tokens_whats_it_cost.py
07.01_output_parser_csv.py
07.02_output_parser_structured_with_validation.py
08.01_language_translate_and_summarize.py
09.01_prompt_chaining.py
10.01_pdf_summarizing.py
11.01_web_article_summarizer.py
y_web_character_summarizer.py
z_DAOGEN_characters.py

## Documentation

This is all documented in this readme, more documentation and details can be found at our substack: https://substack.com/@djsquircle

## Contributing

We welcome contributions from the community! If you'd like to contribute to this project please e-mail djsquircle@gmail.com

## License

This project is licensed under the MIT License.


## Support and Contact

For support or inquiries, please contact djsquircle@gmail.com.


## Acknowledgments

Special thanks to Mostafa Ibrahim for his invaluable [tutorial](https://pub.towardsai.net/how-to-create-your-own-llm-powered-slackbot-with-langchain-on-your-own-private-data-f435c422696) on connecting a local host run LangChain chat to the Slack API. Your expertise and guidance have been instrumental in integrating Falcon A. Quest with the dynamic Slack platform, enabling seamless interactions and real-time communication within our community.

I would also like to extend my gratitude to the incredible team at Activeloop for their [comprehensive course](https://learn.activeloop.ai/courses/langchain) on LangChain and Vector Databases in Production. Your course has provided invaluable insights and a solid foundation for implementing LangChain's powerful capabilities, empowering us to leverage large language models like never before.

A heartfelt thank you to DigitalOceanv for their exceptional [tutorials](https://docs.digitalocean.com/tutorials/enable-push-to-deploy/) on setting up containers and Kubernetes. Your resources have been crucial in orchestrating the infrastructure needed to support Falcon A. Quest's seamless deployment and scalability, ensuring a smooth user experience.

Lastly, a special shout-out to ChatGPT 4 for its invaluable support throughout the entire process. Its advanced capabilities, guidance, and debugging assistance have been pivotal in bringing Falcon A. Quest to life and refining its interactions with the DAOGEN community.