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
   pip install python-dotenv langchain openai newspaper3k
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

- 1.1 simple_prompt_template: Create a prompt object that takes a question as an input variable, and returns an answer. Instantiate an LLM, and create a chain using the instantiated LLM and the prompt object. Finally, run the chain by passing chain.run funtion an input question, and print the output. 
- 1.2 simple_movie_assistant
- 1.3 simple_naming_assistant
- 1.4 simple_summarizer
- 1.5 simple_prompt_template
- 2.1 surferbro_prompt_template
- 3.1 dj_squircle_life_coach_with_few_shot_example_step_by_step
- 3.2 dj_squircle_life_coach_with_few_shot_examples
- 4.1 save_few_shot_example_prompts
- 4.2 load_few_shot_example_prompts
- 4.3 save_several_few_shot_example_prompts
- 4.4 load_several_few_shot_examples
- 5.1 few_shot_example_prompt
- 6.1 how_many_tokens_whats_it_cost
- 7.1 output_parser_csv
- 7.2 output_parser_structured_with_validation
- 8.1 language translation
- 9.1 prompt_chaining
- 10.1 pdf_summarizing
- 11.1 web_article_summarizer

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