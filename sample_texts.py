"""
Sample texts for testing the AI Text Summarizer API
Copy and paste these into your API requests for quick testing
"""

# Technology Examples
TECH_EXAMPLES = {
    "ai_intro": """
    Artificial intelligence (AI) is intelligence demonstrated by machines, in contrast to 
    the natural intelligence displayed by humans and animals. Leading AI textbooks define 
    the field as the study of intelligent agents: any device that perceives its environment 
    and takes actions that maximize its chance of successfully achieving its goals. 
    Colloquially, the term "artificial intelligence" is often used to describe machines 
    (or computers) that mimic "cognitive" functions that humans associate with the human 
    mind, such as "learning" and "problem solving".
    """,
    
    "quantum_computing": """
    Quantum computing is a type of computation that harnesses the collective properties 
    of quantum states, such as superposition, interference, and entanglement, to perform 
    calculations. The devices that perform quantum computations are known as quantum 
    computers. Though current quantum computers are too small to outperform usual 
    (classical) computers for practical applications, they are believed to be capable 
    of solving certain computational problems, such as integer factorization, 
    substantially faster than classical computers.
    """,
    
    "blockchain": """
    Blockchain is a distributed ledger technology that maintains a continuously growing 
    list of records, called blocks, which are linked and secured using cryptography. 
    Each block typically contains a cryptographic hash of the previous block, a timestamp, 
    and transaction data. By design, a blockchain is resistant to modification of the data. 
    It is an open, distributed ledger that can record transactions between two parties 
    efficiently and in a verifiable and permanent way.
    """,
    
    "machine_learning": """
    Machine learning (ML) is a field of inquiry devoted to understanding and building 
    methods that 'learn', that is, methods that leverage data to improve performance 
    on some set of tasks. It is seen as a part of artificial intelligence. Machine 
    learning algorithms build a model based on sample data, known as training data, 
    in order to make predictions or decisions without being explicitly programmed to 
    do so. Machine learning algorithms are used in a wide variety of applications, 
    such as in medicine, email filtering, speech recognition, and computer vision, 
    where it is difficult or unfeasible to develop conventional algorithms to perform 
    the needed tasks.
    """
}

# Science Examples
SCIENCE_EXAMPLES = {
    "climate_change": """
    Climate change refers to long-term shifts in temperatures and weather patterns. 
    These shifts may be natural, such as through variations in the solar cycle. 
    But since the 1800s, human activities have been the main driver of climate change, 
    primarily due to burning fossil fuels like coal, oil and gas. Burning fossil fuels 
    generates greenhouse gas emissions that act like a blanket wrapped around the Earth, 
    trapping the sun's heat and raising temperatures. Examples of greenhouse gas emissions 
    that are causing climate change include carbon dioxide and methane.
    """,
    
    "photosynthesis": """
    Photosynthesis is a process used by plants and other organisms to convert light 
    energy into chemical energy that, through cellular respiration, can later be released 
    to fuel the organism's activities. This chemical energy is stored in carbohydrate 
    molecules, such as sugars and starches, which are synthesized from carbon dioxide 
    and water. In most cases, oxygen is also released as a waste product. Most plants, 
    algae, and cyanobacteria perform photosynthesis; such organisms are called 
    photoautotrophs. Photosynthesis is largely responsible for producing and maintaining 
    the oxygen content of the Earth's atmosphere.
    """,
    
    "black_holes": """
    A black hole is a region of spacetime where gravity is so strong that nothing, 
    including light and other electromagnetic waves, has enough energy to escape it. 
    The theory of general relativity predicts that a sufficiently compact mass can 
    deform spacetime to form a black hole. The boundary of no escape is called the 
    event horizon. Although it has an enormous effect on the fate and circumstances 
    of an object crossing it, it has no locally detectable features according to 
    general relativity. In many ways, a black hole acts like an ideal black body, 
    as it reflects no light.
    """
}

# Business Examples
BUSINESS_EXAMPLES = {
    "remote_work": """
    Remote work, also known as telecommuting or work from home, is a working style 
    that allows professionals to work outside of a traditional office environment. 
    It is based on the concept that work does not need to be done in a specific place 
    to be executed successfully. The COVID-19 pandemic accelerated the adoption of 
    remote work across many industries. Companies have discovered that remote work 
    can lead to increased productivity, reduced overhead costs, and improved work-life 
    balance for employees. However, it also presents challenges such as communication 
    difficulties, feelings of isolation, and the need for better digital security.
    """,
    
    "startup_culture": """
    Startup culture refers to the environment and set of values that characterize 
    young, fast-growing companies. This culture typically emphasizes innovation, 
    rapid growth, and taking risks. Startups often have flat organizational structures, 
    flexible work arrangements, and a focus on disrupting traditional industries. 
    Employees in startup environments are usually expected to wear multiple hats, 
    work long hours, and be comfortable with uncertainty. While this culture can be 
    exciting and rewarding, it can also be stressful and may not be suitable for everyone. 
    The startup culture has significantly influenced how modern businesses operate.
    """
}

# Historical Examples
HISTORY_EXAMPLES = {
    "industrial_revolution": """
    The Industrial Revolution was the transition to new manufacturing processes in 
    Great Britain, continental Europe, and the United States, in the period from 
    about 1760 to sometime between 1820 and 1840. This transition included going 
    from hand production methods to machines, new chemical manufacturing and iron 
    production processes, the increasing use of steam power and water power, the 
    development of machine tools and the rise of the mechanized factory system. 
    The Industrial Revolution also led to an unprecedented rise in the rate of 
    population growth and helped create the modern economic world we live in today.
    """,
    
    "space_race": """
    The Space Race was a 20th-century competition between two Cold War adversaries, 
    the Soviet Union and the United States, to achieve superior spaceflight capability. 
    It had its origins in the ballistic missile-based nuclear arms race between the 
    two nations following World War II. The technological advantage demonstrated by 
    spaceflight achievement was seen as necessary for national security and became 
    part of the symbolism and ideology of the time. The Space Race brought pioneering 
    launches of artificial satellites, uncrewed space probes, and human spaceflight. 
    It effectively began with the Soviet launch of Sputnik 1 on October 4, 1957.
    """
}

# Health & Wellness Examples
HEALTH_EXAMPLES = {
    "meditation": """
    Meditation is a practice where an individual uses a technique – such as mindfulness, 
    or focusing the mind on a particular object, thought, or activity – to train attention 
    and awareness, and achieve a mentally clear and emotionally calm and stable state. 
    Meditation has been practiced since antiquity in numerous religious traditions and 
    beliefs. Since the 19th century, it has spread from its origins to other cultures 
    where it is commonly practiced in private and business life. Studies have shown that 
    meditation may reduce stress, anxiety, depression, and pain, and enhance peace, 
    perception, self-concept, and well-being.
    """,
    
    "nutrition": """
    Nutrition is the science that interprets the nutrients and other substances in food 
    in relation to maintenance, growth, reproduction, health and disease of an organism. 
    It includes ingestion, absorption, assimilation, biosynthesis, catabolism and excretion. 
    The diet of an organism is what it eats, which is largely determined by the availability 
    and palatability of foods. For humans, a healthy diet includes preparation of food 
    and storage methods that preserve nutrients from oxidation, heat or leaching, and 
    that reduce risk of foodborne illnesses. Nutritional science is the study of nutrition.
    """
}


def print_all_examples():
    """Print all example texts organized by category"""
    categories = {
        "Technology": TECH_EXAMPLES,
        "Science": SCIENCE_EXAMPLES,
        "Business": BUSINESS_EXAMPLES,
        "History": HISTORY_EXAMPLES,
        "Health & Wellness": HEALTH_EXAMPLES
    }
    
    print("="*70)
    print("SAMPLE TEXTS FOR AI TEXT SUMMARIZER API")
    print("="*70)
    
    for category, examples in categories.items():
        print(f"\n{'='*70}")
        print(f"📚 {category.upper()}")
        print('='*70)
        
        for title, text in examples.items():
            print(f"\n🔹 {title.upper().replace('_', ' ')}")
            print("-"*70)
            print(text.strip())
            print()


if __name__ == "__main__":
    print_all_examples()
