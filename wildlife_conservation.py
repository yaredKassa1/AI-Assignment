# Species Data
species_data = {
    "ethiopian_wolf": {
        "status": "endangered",
        "threats": ["habitat_loss", "disease"],
        "habitat": "highlands",
    },
    "mountain_nyala": {
        "status": "endangered",
        "threats": ["habitat_loss", "hunting"],
        "habitat": "moorland",
    },
    "bale_monkey": {
        "status": "endangered",
        "threats": ["habitat_loss"],
        "habitat": "bamboo_forest",
    },
    "gelada_baboon": {
        "status": "near_threatened",
        "threats": ["habitat_loss"],
        "habitat": "grasslands",
    },
    "meneliks_bushbuck": {
        "status": "vulnerable",
        "threats": ["habitat_loss", "hunting"],
        "habitat": "moist montane forests",
    },
    "african_wild_dog": {
        "status": "endangered",
        "threats": ["habitat_loss", "human_wildlife_conflict"],
        "habitat": "savannah",
    },
}

# Human Activities that can harm species
human_activities = ["poaching", "deforestation", "urbanization", "climate_change"]

# Conservation Measures
conservation_measures = {
    "ethiopian_wolf": "habitat_protection",
    "mountain_nyala": "habitat_protection",
    "bale_monkey": "bamboo_forest_protection",
    "gelada_baboon": "habitat_restoration",
    "meneliks_bushbuck": "habitat_protection",
    "african_wild_dog": "wildlife_corridor",
}

# Function to determine if a species is at risk
def is_at_risk(species):
    if species not in species_data:
        return None  # Species not found
    status = species_data[species]["status"]
    if status in ["endangered", "critically_endangered"]:
        return True
    if status in ["vulnerable", "near_threatened"]:
        threats = species_data[species]["threats"]
        if "poaching" in threats or "habitat_loss" in threats:
            return True
    return False

# Function to recommend conservation strategies based on threats
def recommended_conservation_strategy(species):
    threats = species_data[species]["threats"]
    if "poaching" in threats:
        return "anti_poaching"
    
    habitat = species_data[species]["habitat"]
    if "habitat_loss" in threats:
        if habitat == "bamboo_forest":
            return "bamboo_forest_protection"
        else:
            return "habitat_protection"
    return None

# Function to mitigate human activities
def mitigate_human_activity(species):
    mitigations = []
    for activity in human_activities:
        if activity in species_data[species]["threats"] or is_at_risk(species):
            mitigations.append(activity)
    return mitigations

# User Input and Output
def main():
    while True:
        animal_name = input("Enter the name of the animal (or -1 to exit): ").strip().lower()
        if animal_name == "-1":
            print("Exiting the program.")
            break
        
        risk_status = is_at_risk(animal_name)
        
        if risk_status is None:
            print(f"The species '{animal_name}' is not found in the database.")
        elif risk_status:
            print(f"The {animal_name} is at risk.")
            strategy = recommended_conservation_strategy(animal_name)
            if strategy:
                print(f"Recommended conservation strategy for {animal_name}: {strategy}.")
            mitigations = mitigate_human_activity(animal_name)
            if mitigations:
                print(f"To protect the {animal_name}, mitigate the following human activities: {', '.join(mitigations)}.")
        else:
            print(f"The {animal_name} is not endangered.")

if __name__ == "__main__":
    main()