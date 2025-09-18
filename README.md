# Markov ASMR Generator

This project is a simple experiment in using Markov chains to create generative ASMR audio. Instead of composing music, the system strings together everyday sounds like fire crackling or typing on a keyboard. Each new sound is chosen based on probabilities, so the final output always comes out a little different.

The program works by starting from one sound and then letting the Markov chain decide which sound should follow. Sometimes the next clip is simply placed after the last one. Other times the sounds are overlapped with a small fade or even layered on top of each other. This keeps the track from feeling too mechanical and gives it a more natural ASMR texture.

---

## Why this project is meaningful to me

I’ve always used ASMR to help me relax before bed. Sometimes it is the crackle of a fire or the sound of running water that makes it easier to fall asleep. For this project, I decided to collect a small set of sounds that feel personal. A few are mine and a few came from asking friends what noises they found calming. I spent the week recording and gathering them, which made the project feel less like writing code and more like building something I would actually use.  

Working with these sounds reminded me of the way small, everyday noises can have such a strong effect on mood. Letting a Markov chain shuffle and overlap them is a playful way of turning something simple and familiar into a track that is never exactly the same twice.  

---

## Sound States

These are the sound “states” the system can be in. At each step, one of these is chosen:

| State             | Example sound it represents |
|-------------------|-----------------------------|
| candy_unwrapping  | crinkle of a wrapper        |
| fire_cackling     | soft fireplace crackles     |
| keyboard_typing   | keyboard ASMR               |
| running_water     | flowing water in the river  |
| splashing_water   | water splashes in bucket    |

---

## How the chain works

The system keeps track of how likely it is to move from one state to another. For example, if it is currently in `fire_cackling`, there might be a 40% chance it stays there, a 20% chance it moves to `running_water`, and smaller chances for the other sounds. These probabilities are all written into the transition matrix at the top of the code.

---

## Combination modes

When adding a new sound, the program also decides how to combine it with the track so far. There are three possible modes:

1. **Concat** – the new sound plays fully after the old one  
2. **Overlap** – the new sound fades in while the old one fades out  
3. **Mix** – both sounds are layered together  

This is chosen randomly, which makes the output feel less repetitive.

---

## Length of the output

The `length` parameter controls how many sound clips are chained together. It does not mean seconds but rather the number of clips. So `length=30` means 30 clips are chosen one after another. If each clip is around 5 seconds, the result would be about 2 and a half minutes long. You can adjust this value depending on how long you want your ASMR track to run.

---

## Next steps

Going forward, I’d like to:  
- Record more sounds to expand the state space beyond five  
- Adjust transition probabilities to reflect smoother or more surprising sequences  
- Add more control over the combination modes (so I can choose how often overlaps or mixes happen) as opposed to just choosing it randomly. 

---

## Running the program

Make sure your `.wav` files are in an `assets/` folder. Then run:

```bash
python3 markov_asmr.py


---
Citations

Numpy Documentation – random sampling with probabilities: https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html

SoundFile Documentation – reading and writing WAV files: https://pysoundfile.readthedocs.io/en/latest/

Python Official Documentation – working with arrays and audio data: https://docs.python.org/3/library/array.html

Overlap and mixing logic inspired by audio handling discussions on Stack Overflow (e.g., averaging stereo channels to mono): https://stackoverflow.com/questions/32174978/average-numpy-array-columns