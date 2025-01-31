% --- Facts ---

% Species
species(ethiopian_wolf).
species(mountain_nyala).
species(bale_monkey).
species(gelada_baboon).
species(meneliks_bushbuck).
species(african_wild_dog).

% Conservation Status
conservation_status(ethiopian_wolf, endangered).
conservation_status(mountain_nyala, endangered).
conservation_status(bale_monkey, endangered).
conservation_status(gelada_baboon, near_threatened).
conservation_status(meneliks_bushbuck, vulnerable).
conservation_status(african_wild_dog, endangered).

% Threats to Species
threat(ethiopian_wolf, habitat_loss).
threat(ethiopian_wolf, disease).
threat(mountain_nyala, habitat_loss).
threat(mountain_nyala, hunting).
threat(bale_monkey, habitat_loss).
threat(gelada_baboon, habitat_loss).
threat(meneliks_bushbuck, habitat_loss).
threat(meneliks_bushbuck, hunting).
threat(african_wild_dog, habitat_loss).
threat(african_wild_dog, human_wildlife_conflict).

% Habitat Requirements
requires(ethiopian_wolf, highlands).
requires(mountain_nyala, moorland).
requires(bale_monkey, bamboo_forest).
requires(gelada_baboon, grasslands).
requires(meneliks_bushbuck, moist_montane_forests).
requires(african_wild_dog, savannah).

% Human-Wildlife Interaction: Activities that can harm species
human_activity(poaching).
human_activity(deforestation).
human_activity(urbanization).
human_activity(climate_change).

% Conservation Measures
conservation_measure(ethiopian_wolf, habitat_protection).
conservation_measure(mountain_nyala, habitat_protection).
conservation_measure(bale_monkey, bamboo_forest_protection).
conservation_measure(gelada_baboon, habitat_restoration).
conservation_measure(meneliks_bushbuck, habitat_protection).
conservation_measure(african_wild_dog, wildlife_corridor).

% --- Rules ---

% Rule: If a species is endangered or critically endangered, it's at risk.
at_risk(Species) :-
    conservation_status(Species, endangered).

% Rule: If a species is vulnerable or near threatened and faces poaching or habitat loss, it's also at risk.
at_risk(Species) :-
    conservation_status(Species, vulnerable),
    (threat(Species, poaching); threat(Species, habitat_loss)).
at_risk(Species) :-
    conservation_status(Species, near_threatened),
    (threat(Species, poaching); threat(Species, habitat_loss)).

% Rule: Recommend conservation strategies based on the threats faced by a species
recommended_conservation_strategy(Species, habitat_protection) :-
    threat(Species, habitat_loss).

recommended_conservation_strategy(Species, bamboo_forest_protection) :-
    requires(Species, bamboo_forest).

recommended_conservation_strategy(Species, wildlife_corridor) :-
    threat(Species, habitat_loss).

% Rule: If the human activity harms a species, provide suggestions for mitigating the activity.
mitigate_human_activity(Species, Activity) :-
    human_activity(Activity),
    (threat(Species, Activity); at_risk(Species)),
    format('To protect the ~w, mitigate the human activity: ~w.~n', [Species, Activity]).
