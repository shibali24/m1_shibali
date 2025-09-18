import numpy as np
import soundfile as sf
import random

# ok so first, define the transition probabilities
# basically telling the chain how likely it is to hop from one sound to another
transition_matrix = {
    "candy_unwrapping": {"candy_unwrapping": 0.3, "fire_cackling": 0.2, "keyboard_typing": 0.2, "running_water": 0.2, "splashing_water": 0.1},
    "fire_cackling": {"candy_unwrapping": 0.2, "fire_cackling": 0.4, "keyboard_typing": 0.1, "running_water": 0.2, "splashing_water": 0.1},
    "keyboard_typing": {"candy_unwrapping": 0.2, "fire_cackling": 0.1, "keyboard_typing": 0.4, "running_water": 0.2, "splashing_water": 0.1},
    "running_water": {"candy_unwrapping": 0.1, "fire_cackling": 0.2, "keyboard_typing": 0.1, "running_water": 0.4, "splashing_water": 0.2},
    "splashing_water": {"candy_unwrapping": 0.1, "fire_cackling": 0.2, "keyboard_typing": 0.2, "running_water": 0.2, "splashing_water": 0.3},
}

states = list(transition_matrix.keys())

# helper function to pick next sound based on probability
def next_state(current):
    options = list(transition_matrix[current].keys())
    probs = list(transition_matrix[current].values())
    return np.random.choice(options, p=probs)

# load up all your mp3 files 
def load_samples():
    samples = {}
    for s in states:
        filename = f"assets/{s}.mp3"  
        data, sr = sf.read(filename)
        samples[s] = (data, sr)
    return samples

# generate the final audio track
def generate_asmr(length=20, start="candy_unwrapping"):
    samples = load_samples()
    current = start
    sr = samples[current][1]  
    track = []

    for _ in range(length):
        data, _ = samples[current]
        track.append(data)
        # move to the next sound
        current = next_state(current)  

    # smush them all into one big audio file
    full_track = np.concatenate(track)
    sf.write("asmr_output.wav", full_track, sr)
    print("done! saved to asmr_output.wav")

# run the main thing!
if __name__ == "__main__":
    generate_asmr(length=30, start="fire_cackling")
