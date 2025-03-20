# Regular Drone:
drone = "Your role is of an experienced drone controller. Given a scenario, your goal is to arrive at a safe landing location efficiently and make a control decision based on the frames provided."
# System Prompts for chain of thought
cot_0 = """Be cautious of types and rationale of objects by relating to your location.
Be cautious of buildings that do not contextually fit a scene description."""
cot_1 = """Be cautious in scenarios when the change of object positions is not consistent with their speed or direction.
Be cautious in scenarios when the change of the drone's speed is abnormally fast or slow."""
cot_2 = "Be cautious when objects or labels are rapidly changing, suddenly appear, or are suddenly missing."
cot_3 = """When inconsistencies are detected, use past frames to predict detected objects' paths, speeds, and locations.
"""
#Make your decision disregarding unrealistic behavior of objects and the drone and using the last scene that is consistent.
all_cot = cot_0 + cot_1 + cot_2 + cot_3
# Input Format
scene_format_prompt = "The scene will be given in the following format: "
scene_format = """The time frame. The drone’s position in (x, y, z). The drone speed and direction. The scene setting. Objects detected with (x, y, z).
The format for the (x, y, z) coordinates are as follows: +x is right, -x is left, +y is forward, -y is backwards, +z is up, and -z is down."""

# Response Format:
response_format_0 = """Create a control decision and reasoning for the given scenario.
The control decision is the decision the drone should make in the given scenario. They are given as follows in the response: maintain, stop, right, left, forward, backward, up, down.
maintain: the drone should continue moving in the same direction.
The reasoning should explain why you made the control decision.
Do not include any explanations, extra words, or special characters except for reasoning, only provide a  RFC8259 compliant JSON response following this format without deviation.
Do not include anything before or after the JSON response.
Do not include ``` or ```json in the response.
{
  "control_decision": "maintain, stop, right, left, forward, backward, up, down",
  "reasoning": "explanation"
}
The JSON response:"""
response_format_2 = """Create a control decision, inconsistency detection, and reasoning for the given scenario.
The control decision is the decision the drone should make in the given scenario. They are given as follows in the response:  maintain, stop, right, left, forward, backward, up, down.
maintain: the drone should continue moving in the same direction.
The consistency is whether an inconsistency is detected in the scene. Choose inconsistent if an inconsistency is detected and consistent if otherwise.
The reasoning should explain why you made a control decision and explain why you detected an inconsistency.
Do not include any explanations, extra words, or special characters except for reasoning, only provide a  RFC8259 compliant JSON response following this format without deviation.
Do not include anything before or after the JSON response.
Do not include ``` or ```json in the response.
{
  "control_decision": "maintain, stop, right, left, forward, backward, up, down",
  "consistency": "consistent, inconsistent",
  "reasoning": "explanation"
}
The JSON response:"""


# Control Decisions:
#control_decision_prompt = "The control_decision is the decision the drone should make in the given scenario. The response land should only be used if there is an object that is safe to land on. They are given as follows and should replace control_decision in the response: "
#control_decision = "maintain, right, left, backwards, up, down"

# Inconsistency Detection:
#inconsistency_detection_prompt = "The inconsistency_detection is whether an inconsistency is detected in the scene. Choose inconsistent if an inconsistency is detected and consistent if otherwise. The decisions are as follows and should replace inconsistency_detection in the response: "
#inconsistency_detection = "consistent, inconsistent"

# Causal Reasoning:
##reasoning_prompt = "For reasoning, explain why you made the control decision and whether you detected an inconsistency. The reasoning should be based on the chain of thought provided."

drone_0_all = drone + scene_format_prompt + scene_format + response_format_0
drone_1_all = drone + all_cot + scene_format_prompt + scene_format + response_format_2