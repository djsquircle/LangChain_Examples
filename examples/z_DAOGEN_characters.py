from y_web_character_summarizer import generate_character_profile_summary

# List of character profile URLs
character_urls = [
        'https://daogen.ai/dj-squircle/',
        'https://daogen.ai/zoe-austeen/',
        'https://daogen.ai/falcon-a-quest/',
        'https://daogen.ai/luna-vega/',
        'https://daogen.ai/orion-galileo/',
        'https://daogen.ai/harmonic-cipher/',
        'https://daogen.ai/kauper/',
        'https://daogen.ai/professor-starling/',
        'https://daogen.ai/apollo/',
        'https://daogen.ai/draco-novastorm/',
        'https://daogen.ai/yasuke/',
        'https://daogen.ai/universal-sonicboom/',
        'https://daogen.ai/cornelius-franklin/',
        'https://daogen.ai/lee-jenkins/',
        'https://daogen.ai/valerian-skymane/',
        'https://daogen.ai/0ppenheimer/',
        'https://daogen.ai/fayrion-the-enchanter/',
        'https://daogen.ai/bobbycina-dribblybottom/',
        'https://daogen.ai/vito-provolone/'
]

# Iterate over the character URLs and generate summaries
for url in character_urls:
    summary = generate_character_profile_summary(url)
    print(f"Character Profile Summary for {url}:")
    print(summary)
    print("-------------------------------------")
