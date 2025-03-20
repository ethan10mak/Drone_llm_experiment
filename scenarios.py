## TODO, maybe define the correct inconsistency detection for testing
## Definition of a correct scene decision
## A correct scene decision is a decision that is considered safe and not abrupt.
## maintain is considered a safe decision if the drone can not collide with an object.
## stop is considered a safe decision if the drone can collide with an object.
## land is considered a safe decision if the drone can land on a safe object.

# Benign Scene 0
benign_scene0_t_0 = "Frame t. The drone’s position is (0, 0, 100). The drone is moving forward. The scene is a city. A flat roof is detected at (0, 0, 50) and is not moving."
benign_scene0_t_1 = "Frame t + 1. The drone’s position is (0, 2, 100). The drone is moving forward. The scene is a city. A flat roof is detected at (0, 0, 50) and is not moving."
benign_scene0_t_2 = "Frame t + 2. The drone’s position is (0, 4, 100). The drone is moving forward. The scene is a city. A flat roof is detected at (0, 0, 50) and is not moving."
benign_scene0_t_3 = "Frame t + 3. The drone’s position is (0, 6, 100). The drone is moving forward. The scene is a city. A flat roof is detected at (0, 0, 50) and is not moving."
# Disturbed Frames
benign_scene0_t_4 = "Frame t + 4. The drone’s position is (0, 8, 100). The drone is moving forward. The scene is a city. A flat roof is detected at (0, 0, 50) and is not moving."
benign_scene0_t_5 = "Frame t + 5. The drone’s position is (0, 10, 100). The drone is moving forward. The scene is a city. A flat roof is detected at (0, 0, 50) and is not moving."
benign_scene0_t_6 = "Frame t + 6. The drone’s position is (0, 12, 100). The drone is moving forward. The scene is a city. A flat roof is detected at (0, 0, 50) and is not moving."
benign_scene0_all = benign_scene0_t_0 + benign_scene0_t_1 + benign_scene0_t_2 + benign_scene0_t_3 + benign_scene0_t_4 + benign_scene0_t_5 + benign_scene0_t_6
benign_scene0_3 = benign_scene0_t_1 + benign_scene0_t_2 + benign_scene0_t_3 + benign_scene0_t_4 + benign_scene0_t_5 + benign_scene0_t_6
benign_scene0_2 = benign_scene0_t_2 + benign_scene0_t_3 + benign_scene0_t_4 + benign_scene0_t_5 + benign_scene0_t_6
benign_scene0_1 = benign_scene0_t_3 + benign_scene0_t_4 + benign_scene0_t_5 + benign_scene0_t_6
correct_benign_scene0_decisions = ["down"]

# Benign Scene 1
benign_scene1_t_0 = "Frame t. The drone’s position is (0, 0, 100). The drone is moving forward. The scene is an ocean. No building is detected."
benign_scene1_t_1 = "Frame t + 1. The drone’s position is (0, 2, 100). The drone is moving forward. The scene is an ocean. No building is detected."
benign_scene1_t_2 = "Frame t + 2. The drone’s position is (0, 4, 100). The drone is moving forward. The scene is an ocean. No building is detected."
benign_scene1_t_3 = "Frame t + 3. The drone’s position is (0, 6, 100). The drone is moving forward. The scene is an ocean. No building is detected."
# Disturbed Frames
benign_scene1_t_4 = "Frame t + 4. The drone’s position is (0, 8, 100). The drone is moving forward. The scene is an ocean. No building is detected."
benign_scene1_t_5 = "Frame t + 5. The drone’s position is (0, 10, 100). The drone is moving forward. The scene is an ocean. No building is detected."
benign_scene1_t_6 = "Frame t + 6. The drone’s position is (0, 12, 100). The drone is moving forward. The scene is an ocean. No building is detected."
benign_scene1_all = benign_scene0_t_0 + benign_scene0_t_1 + benign_scene0_t_2 + benign_scene0_t_3 + benign_scene0_t_4 + benign_scene0_t_5 + benign_scene0_t_6
benign_scene1_3 = benign_scene0_t_1 + benign_scene0_t_2 + benign_scene0_t_3 + benign_scene0_t_4 + benign_scene0_t_5 + benign_scene0_t_6
benign_scene1_2 = benign_scene0_t_2 + benign_scene0_t_3 + benign_scene0_t_4 + benign_scene0_t_5 + benign_scene0_t_6
benign_scene1_1 = benign_scene0_t_3 + benign_scene0_t_4 + benign_scene0_t_5 + benign_scene0_t_6
correct_benign_scene1_decisions = ["maintain"]

# Benign Scene 2
benign_scene2_t_0 = "Frame t. The drone’s position is (0, 0, 100). The drone is moving forward. The scene is a city. A tree is detected at (0, 15, 100) and is not moving."
benign_scene2_t_1 = "Frame t + 1. The drone’s position is (0, 2, 100). The drone is moving forward. The scene is a city. A tree is detected at (0, 15, 100) and is not moving."
benign_scene2_t_2 = "Frame t + 2. The drone’s position is (0, 4, 100). The drone is moving forward. The scene is a city. A tree is detected at (0, 15, 100) and is not moving."
benign_scene2_t_3 = "Frame t + 3. The drone’s position is (0, 6, 100). The drone is moving forward. The scene is a city. A tree is detected at (0, 15, 100) and is not moving."
# Disturbed Frames
benign_scene2_t_4 = "Frame t + 4. The drone’s position is (0, 8, 100). The drone is moving forward. The scene is a city. A tree is detected at (0, 15, 100) and is not moving."
benign_scene2_t_5 = "Frame t + 5. The drone’s position is (0, 10, 100). The drone is moving forward. The scene is a city. A tree is detected at (0, 15, 100) and is not moving."
benign_scene2_t_6 = "Frame t + 6. The drone’s position is (0, 12, 100). The drone is moving forward. The scene is a city. A tree is detected at (0, 15, 100) and is not moving."
benign_scene2_all = benign_scene0_t_0 + benign_scene0_t_1 + benign_scene0_t_2 + benign_scene0_t_3 + benign_scene0_t_4 + benign_scene0_t_5 + benign_scene0_t_6
benign_scene2_3 = benign_scene0_t_1 + benign_scene0_t_2 + benign_scene0_t_3 + benign_scene0_t_4 + benign_scene0_t_5 + benign_scene0_t_6
benign_scene2_2 = benign_scene0_t_2 + benign_scene0_t_3 + benign_scene0_t_4 + benign_scene0_t_5 + benign_scene0_t_6
benign_scene2_1 = benign_scene0_t_3 + benign_scene0_t_4 + benign_scene0_t_5 + benign_scene0_t_6
correct_benign_scene0_decisions = ["stop"]

# Temporal Inconsistency Scene 0
# Undisturbed Frames
temporal_scene0_t_0 = "Frame t. The drone’s position is (0, 0, 100). The drone is not moving. The scene is a city. A flat roof is detected at (0, 0, 50) and is not moving."
temporal_scene0_t_1 = "Frame t + 1. The drone’s position is (0, 0, 100). The drone is not moving. The scene is a city. A flat roof is detected at (0, 0, 50) and is not moving."
temporal_scene0_t_2 = "Frame t + 2. The drone’s position is (0, 0, 100). The drone is not moving. The scene is a city. A flat roof is detected at (0, 0, 50) and is not moving."
temporal_scene0_t_3 = "Frame t + 3. The drone’s position is (0, 0, 100). The drone is not moving. The scene is a city. A flat roof is detected at (0, 0, 50) and is not moving."
# Disturbed Frames
temporal_scene0_t_4 = "Frame t + 4. The drone’s position is (0, 0, 100). The drone is not moving. The scene is a forest. No building is detected."
temporal_scene0_t_5 = "Frame t + 5. The drone’s position is (0, 0, 100). The drone is not moving. The scene is a forest. No building is detected."
temporal_scene0_t_6 = "Frame t + 6. The drone’s position is (0, 0, 100). The drone is not moving. The scene is a forest. No building is detected."

temporal_scene0_all = temporal_scene0_t_0 + temporal_scene0_t_1 + temporal_scene0_t_2 + temporal_scene0_t_3 + temporal_scene0_t_4 + temporal_scene0_t_5 + temporal_scene0_t_6
temporal_scene0_3 = temporal_scene0_t_1 + temporal_scene0_t_2 + temporal_scene0_t_3 + temporal_scene0_t_4 + temporal_scene0_t_5 + temporal_scene0_t_6
temporal_scene0_2 = temporal_scene0_t_2 + temporal_scene0_t_3 + temporal_scene0_t_4 + temporal_scene0_t_5 + temporal_scene0_t_6
temporal_scene0_1 = temporal_scene0_t_3 + temporal_scene0_t_4 + temporal_scene0_t_5 + temporal_scene0_t_6
correct_temporal_scene0_decisions = ["maintain", "stop", "down"]
# contextual Inconsistency Scene 0
# Undisturbed Frames
contextual_scene_t_0 = "Frame t. The drone’s position is (0, 0, 100). The drone is not moving. The scene is an ocean. No object is detected."
contextual_scene_t_1 = "Frame t + 1. The drone’s position is (0, 0, 100). The drone is not moving. The scene is an ocean. No object is detected."
contextual_scene_t_2 = "Frame t + 2. The drone’s position is (0, 0, 100). The drone is not moving. The scene is an ocean. No object is detected."
contextual_scene_t_3 = "Frame t + 3. The drone’s position is (0, 0, 100). The drone is not moving. The scene is an ocean. No object is detected."
# Disturbed Frames
contextual_scene_t_4 = "Frame t + 4. The drone’s position is (0, 0, 100). The drone is not moving. The scene is an ocean. A flat-roof building is detected at (0, 0, 50) and is not moving."
contextual_scene_t_5 = "Frame t + 5. The drone’s position is (0, 0, 100). The drone is not moving. The scene is an ocean. A flat-roof building is detected at (0, 0, 50) and is not moving."
contextual_scene_t_6 = "Frame t + 6. The drone’s position is (0, 0, 100). The drone is not moving. The scene is an ocean. A flat-roof building is detected at (0, 0, 50) and is not moving."

contextual_scene0_all = contextual_scene_t_0 + contextual_scene_t_1 + contextual_scene_t_2 + contextual_scene_t_3 + contextual_scene_t_4 + contextual_scene_t_5 + contextual_scene_t_6
contextual_scene0_3 = contextual_scene_t_1 + contextual_scene_t_2 + contextual_scene_t_3 + contextual_scene_t_4 + contextual_scene_t_5 + contextual_scene_t_6
contextual_scene0_2 = contextual_scene_t_2 + contextual_scene_t_3 + contextual_scene_t_4 + contextual_scene_t_5 + contextual_scene_t_6
contextual_scene0_1 = contextual_scene_t_3 + contextual_scene_t_4 + contextual_scene_t_5 + contextual_scene_t_6
correct_contextual_scene0_decisions = ["maintain", "stop"]

# Undisturbed Frames
spatial_scene_t_0 = "Frame t. The drone’s position is (0, 0, 100). The drone is moving forward. The scene is a city. A flat-roof building is detected at (0, 50, 100) and is not moving."
spatial_scene_t_1 = "Frame t + 1. The drone’s position is (0, 2, 100). The drone is mvoing forward. The scene is a city. A flat-roof building is detected at (0, 50, 100) and is not moving."
spatial_scene_t_2 = "Frame t + 2. The drone’s position is (0, 4, 100). The drone is moving forward. The scene is a city. A flat-roof building is detected at (0, 50, 100) and is not moving."
spatial_scene_t_3 = "Frame t + 3. The drone’s position is (0, 6, 100). The drone is moving forward. The scene is a city. A flat-roof building is detected at (0, 50, 100) and is not moving."
# Disturbed Frames
spatial_scene_t_4 = "Frame t + 4. The drone’s position is (0, 8, 100). The drone is moving forward. The scene is a city. A flat-roof building is detected at (50, 50, 100) and is moving right."
spatial_scene_t_5 = "Frame t + 5. The drone’s position is (0, 10, 100). The drone is moving forward. The scene is a city. A flat-roof building is detected at (100, 50, 100) and is moving right."
spatial_scene_t_6 = "Frame t + 6. The drone’s position is (0, 12, 100). The drone is moving forward. The scene is a city. A flat-roof building is detected at (150, 50, 100) and is moving right."

spatial_scene0_all = spatial_scene_t_0 + spatial_scene_t_1 + spatial_scene_t_2 + spatial_scene_t_3 + spatial_scene_t_4 + spatial_scene_t_5 + spatial_scene_t_6
spatial_scene0_3 = spatial_scene_t_1 + spatial_scene_t_2 + spatial_scene_t_3 + spatial_scene_t_4 + spatial_scene_t_5 + spatial_scene_t_6
spatial_scene0_2 = spatial_scene_t_2 + spatial_scene_t_3 + spatial_scene_t_4 + spatial_scene_t_5 + spatial_scene_t_6
spatial_scene0_1 = spatial_scene_t_3 + spatial_scene_t_4 + spatial_scene_t_5 + spatial_scene_t_6
correct_spatial_scene0_decisions = ["down", "forwards", "maintain"]

# Scene lists for all disturbed scenes
all_scenes = [temporal_scene0_all, contextual_scene0_all, spatial_scene0_all]
all_scenes_3 = [temporal_scene0_3, contextual_scene0_3, spatial_scene0_3]
all_scenes_2 = [temporal_scene0_2, contextual_scene0_2, spatial_scene0_2]
all_scenes_1 = [temporal_scene0_1, contextual_scene0_1, spatial_scene0_1]
all_scenes_last_frame = [temporal_scene0_t_6, contextual_scene_t_6, spatial_scene_t_6]
all_correct_decisions = [correct_temporal_scene0_decisions, correct_contextual_scene0_decisions, correct_spatial_scene0_decisions]

# Scene lists for benign scenes
all_benign_scenes = [benign_scene0_all, benign_scene1_all, benign_scene2_all]
all_benign_scenes_3 = [benign_scene0_3, benign_scene1_3, benign_scene2_3]
all_benign_scenes_2 = [benign_scene0_2, benign_scene1_2, benign_scene2_2]
all_benign_scenes_1 = [benign_scene0_1, benign_scene1_1, benign_scene2_1]