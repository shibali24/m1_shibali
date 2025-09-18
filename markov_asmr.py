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

def next_state(current):
    """
    Pick the next sound state based on transition probabilities.

    Args:
        current (str): the current sound state (e.g., "fire_cackling")

    Returns:
        str: the next state chosen according to the Markov transition probabilities
    """
    options = list(transition_matrix[current].keys())
    probs = list(transition_matrix[current].values())
    return np.random.choice(options, p=probs)

def read_and_flatten(path):
    """
    Load an audio file and convert to mono if needed.

    Args:
        path (str): path to the .wav file

    Returns:
        tuple: (numpy array of audio samples in mono, sample rate)
    """
    data, sr = sf.read(path)
    if data.ndim > 1:       # if stereo, average channels → mono
        data = data.mean(axis=1)
    return data, sr

def load_samples():
    """
    Load all ASMR sound samples from the assets folder into memory.
    Ensures audio is flattened to mono for consistency.

    Returns:
        dict: mapping of sound state → (audio samples, sample rate)
    """
    samples = {}
    samples["candy_unwrapping"] = read_and_flatten("assets/candy_unwrapping.wav")
    samples["fire_cackling"]    = read_and_flatten("assets/fire_cackling.wav")
    samples["keyboard_typing"]  = read_and_flatten("assets/keyboard_typing.wav")
    samples["running_water"]    = read_and_flatten("assets/running_water.wav")
    samples["splashing_water"]  = read_and_flatten("assets/splashing_water.wav")
    return samples

def generate_asmr(length=20, start="candy_unwrapping"):
    """
    Generate an ASMR audio track using a Markov chain to sequence sounds.

    Args:
        length (int): number of sound clips to include in the sequence
        start (str): the starting sound state

    Side effects:
        Writes an output file 'asmr_output.wav' to the working directory.
    """
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

if __name__ == "__main__":
    generate_asmr(length=30, start="fire_cackling")