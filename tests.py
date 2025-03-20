import prompts as p
import scenarios as s
import sys
import json
import matplotlib.pyplot as plt
import os
from openai import OpenAI
## NEED TO REPLACE API with api key:
api = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=api)
import csv

# Function that runs the model with a given scene and outputs a json result
def test(model_text = "gpt-4o", drone = p.drone_1_all, scene = s.temporal_scene0_all):
    completion = client.chat.completions.create(
        model=model_text,
        store=False,
        messages=[
            {"role": "developer", "content": drone},
            {
                "role": "user",
                "content": scene
            }
        ]
    )
    #print(completion.choices[0].message.content)
    return json.loads(completion.choices[0].message.content)

# Function to run n number of tests and puts it into output.json
# Returns the list of results
def run_test(n, model_text = "gpt-4o", drone = p.drone_1_all, scene = s.temporal_scene0_all):
    list_of_results = []
    for i in range(n):
        results = {}
        results.update(test(model_text, drone, scene))
        list_of_results.append(results)
        try:
            with open('output.json', 'r') as f:
                data = json.load(f)
        except FileNotFoundError:
            print("FileNotFoundError")
            data = []
        except json.JSONDecodeError:
            print("Empty JSON File")
            data = []
        
        if isinstance(data, list):
            data.append(results)
        elif isinstance(data, dict):
            data.update(results)
        else:
            print("Error")
            return
        #data.update(results)
        with open('output.json', 'w') as f:
            json.dump(data, f, indent=4)
    return list_of_results

def print_results():
    with open('output.json') as f:
        data = json.load(f)
    print(json.dumps(data, indent = 4))

def plot_results():
    with open('output.json') as f:
        data = json.load(f)
    # Extract the data for plotting

# Next Step, create a function to run all of the scenarios with different history frames
# Runs tests for all scenarios with ideal number of history frames
# Collects data and plots it somewhere
# Runs all scenes with both drones
def run_all_tests(n = 2):
    result_0 = 0
    result_1 = 0
    result_1_inc = 0
    i = 0
    for scene in s.all_scenes_last_frame:
        # o1-2024-12-17
        r = run_test(n, "gpt-4o", p.drone_0_all, scene)
        for x in r:
            if x.get("control_decision") in s.all_correct_decisions[i]:
                #print(x.get("control_decision"), s.all_correct_decisions[i])
                result_0 += 1
        i += 1

    i = 0
    for scene in s.all_scenes:
        r = run_test(n, "gpt-4o", p.drone_1_all, scene)
        for x in r:
            if x.get("control_decision") in s.all_correct_decisions[i]:
                #print(x.get("control_decision"), s.all_correct_decisions[i])
                result_1 += 1
            if x.get("consistency") == "inconsistent":
                result_1_inc += 1
        i += 1
    i = 0
    total = n * len(s.all_scenes)
    #print(result_0, result_1)
    #print(total)
    plt.bar(["drone_0_safe", "drone_1_safe", "drone_1_inc."],[result_0/total, result_1/total, result_1_inc/total])
    plt.xlabel("Drones")
    plt.ylabel("Success Rate")
    plt.title("Success Rate of Drones")
    plt.savefig("drone_graph_comparison.png")
    plt.show()
    return result_0, result_1

# Runs all scenes with different number of history frames
# TODO, change to only run drone 1
def run_history_tests(n = 5):
    result_1_all = 0
    result_1_h3 = 0
    result_1_h2 = 0
    result_1_h1 = 0
    result_1_all_inc = 0
    result_1_h3_inc = 0
    result_1_h2_inc = 0
    result_1_h1_inc = 0
    i = 0
    # 4 history frames for both drones
    for scene in s.all_scenes:
        r = run_test(n, "gpt-4o", p.drone_1_all, scene)
        for x in r:
            if x.get("control_decision") in s.all_correct_decisions[i]:
                result_1_all += 1
            if x.get("consistency") == "inconsistent":
                result_1_all_inc += 1
        i += 1
    i = 0

    # 3 History frames for both drones
    for scene in s.all_scenes_3:
        r = run_test(n, "gpt-4o", p.drone_1_all, scene)
        for x in r:
            if x.get("control_decision") in s.all_correct_decisions[i]:
                result_1_h3 += 1
            if x.get("consistency") == "inconsistent":
                result_1_h3_inc += 1
        i += 1
    i = 0

    # 2 History frames for both drones
    for scene in s.all_scenes_2:
        r = run_test(n, "gpt-4o", p.drone_1_all, scene)
        for x in r:
            if x.get("control_decision") in s.all_correct_decisions[i]:
                result_1_h2 += 1
            if x.get("consistency") == "inconsistent":
                result_1_h2_inc += 1
        i += 1
    i = 0

    # 1 History frame for both drones
    for scene in s.all_scenes:
        r = run_test(n, "gpt-4o", p.drone_1_all, scene)
        for x in r:
            if x.get("control_decision") in s.all_correct_decisions[i]:
                result_1_h1 += 1
            if x.get("consistency") == "inconsistent":
                result_1_h1_inc += 1
        i += 1
    i = 0
    # Creates the graph
    total = n * len(s.all_scenes)
    plt.bar(["drone_1_4H", "drone_1_4H_inc", "drone_1_3H,", "drone_1_3H_inc", "drone_1_2H", "drone_1_2H_inc", "drone_1_1H", "drone_1_1H_inc"],
            [result_1_all/total, result_1_all_inc/total, result_1_h3/total, result_1_h3_inc/total, result_1_h2/total, result_1_h2_inc/total, result_1_h1/total, result_1_h1_inc/total])
    plt.xlabel("Drones with number of history frames")
    plt.ylabel("Success Rate")
    plt.title("Success Rate of Drones with Different History Frames")
    plt.savefig("drone_graph_history_frames.png")
    plt.show()
    return

# Runs multiple benign tests
# Tests for false-positives
def run_benign_tests(n = 2):
    result_0 = 0
    result_1 = 0
    i = 0
    # 4 history frames for both drones
    for scene in s.all_scenes:
        r = run_test(n, "gpt-4o", p.drone_0_all, scene)
        for x in r:
            if x.get("control_decision") in s.all_correct_decisions[i]:
                result_0 += 1
        i += 1

    i = 0
    for scene in s.all_scenes:
        r = run_test(n, "gpt-4o", p.drone_1_all, scene)
        for x in r:
            if x.get("control_decision") in s.all_correct_decisions[i]:
                result_1 += 1
        i += 1
    i = 0
    # Creates the graph
    total = n * len(s.all_scenes)
    plt.bar(["drone_0", "drone_1"],[result_0/ total, result_1/total])
    plt.xlabel("Drones")
    plt.ylabel("Success Rate")
    plt.title("Success Rate of Drones with Benign Scenes")
    plt.savefig("drone_graph_benign.png")
    plt.show()
    return result_0, result_1
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        match sys.argv[1]:
            ## TODO, Create more system argument cases for different kinds of tests,
            ## Make sure that case 'h' works properly
            ## Tests for something with the HUDSON paper
            ## False positive analysis
            ## Add onto the current tests to see number of inconsistencies
            case 'a':
                ## Run tests with all scenes (regular amount of history frames)
                print("do all")
                run_all_tests(n = 5)
                # Success Drone 0 = 0.4
                # Success Drone 1 = 0.6666666666666666
                # Success Drone 1 Inc = 1.0
            case 'h':
                ## Run tests with all scene changing the number of history frames
                ## Less tests per scene
                print("do history frame test")
                run_history_tests(n = 5)
            case 'b':
                ## Run tests with benign scenes
                print("do benign test")
                run_benign_tests(n = 2)
            case 't':
                ## Run tests with temporal scenes
                print("do temporal test")
                print(run_test(1, "gpt-4o", p.drone_1_all, s.benign_scene1_all))
            case _:
                print("Invalid Input")
    else:
        print("No argument provided.")
    
    
    #run_test(2, "gpt-4o", p.drone_1_all, s.contextual_scene0_1)
    #run_test(2, "gpt-4o", p.drone_1_all, s.spatial_scene0_1)
    #run_test(2, "gpt-4o", p.drone_1_all, s.temporal_scene0_1)
    #run_test(2, "gpt-4o", p.drone_1_all, s.benign_scene0_1)
    #print(run_all_tests(2))
    #print_results()