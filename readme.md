# LangChain Examples

A collection of working code examples using LangChain for natural language processing tasks. This repository provides implementations of various tutorials found online. Please refer to the acknowledgments section for the source tutorials.

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

To set up the project, follow these steps:
1. Set up a Python virtual environment
2. Set up the Python dependencies

pip install python-dotenv
pip install langchain
pip install openai

3. Create your .env file, and copy your own OPEN_API_KEY 

OPENAI_API_KEY="copy your key material here"

4. Copy the examples to a python file and run them, start experimenting with your own variations

## Usage and Examples

Describe how to use the project. Include code examples, usage scenarios, or sample commands to demonstrate the project's functionality.

## Features

- simple_prompt_template: Create a prompt object that takes a question as an input variable, and returns an answer. Instantiate an LLM, and create a chain using the instantiated LLM and the prompt object. Finally, run the chain by passing chain.run funtion an input question, and print the output. 

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