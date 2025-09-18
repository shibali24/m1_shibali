import numpy as np
import soundfile as sf
import random

# transition probabilities (how the chain hops from one sound to another)
transition_matrix = {
    "candy_unwrapping": {"candy_unwrapping": 0.3, "fire_cackling": 0.2, "keyboard_typing": 0.2, "running_water": 0.2, "splashing_water": 0.1},
    "fire_cackling": {"candy_unwrapping": 0.2, "fire_cackling": 0.4, "keyboard_typing": 0.1, "running_water": 0.2, "splashing_water": 0.1},
    "keyboard_typing": {"candy_unwrapping": 0.2, "fire_cackling": 0.1, "keyboard_typing": 0.4, "running_water": 0.2, "splashing_water": 0.1},
    "running_water": {"candy_unwrapping": 0.1, "fire_cackling": 0.2, "keyboard_typing": 0.1, "running_water": 0.4, "splashing_water": 0.2},
    "splashing_water": {"candy_unwrapping": 0.1, "fire_cackling": 0.2, "keyboard_typing": 0.2, "running_water": 0.2, "splashing_water": 0.3},
}

states = list(transition_matrix.keys())

# helper function to pick next sound based on probabilities
def next_state(current):
    options = list(transition_matrix[current].keys())
    probs = list(transition_matrix[current].values())
    return np.random.choice(options, p=probs)

# helper: always flatten to mono so arrays line up
def read_and_flatten(path):
    data, sr = sf.read(path)
    if data.ndim > 1:       # if stereo, average channels
        data = data.mean(axis=1)
    return data, sr

# load wav files from assets folder (hardcoded)
def load_samples():
    samples = {}
    samples["candy_unwrapping"] = read_and_flatten("assets/candy_unwrapping.wav")
    samples["fire_cackling"]    = read_and_flatten("assets/fire_cackling.wav")
    samples["keyboard_typing"]  = read_and_flatten("assets/keyboard_typing.wav")
    samples["running_water"]    = read_and_flatten("assets/running_water.wav")
    samples["splashing_water"]  = read_and_flatten("assets/splashing_water.wav")
    return samples

# stitch the sequence together into one track
def generate_asmr(length=20, start="candy_unwrapping"):
    samples = load_samples()
    current = start
    sr = samples[current][1]  
    track = []

    for _ in range(length):
        data, _ = samples[current]
        track.append(data)
        current = next_state(current)  # move chain forward

    full_track = np.concatenate(track)
    sf.write("asmr_output.wav", full_track, sr)
    print("done! saved to asmr_output.wav")

# run it
if __name__ == "__main__":
    generate_asmr(length=30, start="fire_cackling")