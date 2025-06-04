You're deep in the classic **post-dig chaos** — 50 folders from 10 Splice packs, each with their own random structure? Here are ** examples** of what that mess looks like, and how this tool helps:

---

### 🎯 The Problem: Typical Sample Pack Mess

You just downloaded packs like:

```
Splice/Samples/packs/
├── Elite Percussion Vol.2/
│   └── loops/drum_loops/full_loops/
│       └── 128bpm_funky_perc_loop.wav
│
├── Analog Heat/
│   └── one_shots/kicks/
│       └── kick_dirty_01.wav
│
├── Cloudy Keys Vol.1/
│   └── instruments/piano_loops/
│       └── dreamy_piano_loop_01.wav
│
├── FX Toolkit/
│   └── risers/sweeps/
│       └── riser_white_noise.wav
│
...and 46 more folders.
```

You’re clicking and clicking, just to find or sort and still can’t remember where that punchy snare was.

---

### ✅ After Running This Tool

You now have a clean structure like:

```
merged/__sorted/
├── kick/
│   └── kick_dirty_01.wav
│
├── perc/
│   └── 128bpm_funky_perc_loop.wav
│
├── piano/
│   └── dreamy_piano_loop_01.wav
│
├── fx/
│   └── riser_white_noise.wav
│
├── _unsorted/
│   └── weirdly_named_loop_abc123.wav
```

No more clicking through endless nested folders.
Everything is sorted. Anything ambiguous? It’s in `_unsorted/`, ready for review.

---

# 🛠 Configuration

Here's the formatted version for the README:

---

### 🛠 Configuration

Open `config_user.py` and tweak the following:

* **`SOURCE_DIR` / `TARGET_DIR`** – Set your input and output folders
* **`COPY_FILES`** – Toggle between copying (`True`) or moving (`False`) files
* **`CATEGORIES`** – Add or remove keywords for sorting

then run
```bash
python sort_samples.py
```

(Optional: run utils/flatten_folders.py if you just want to flatten the nested folders)

And get back to making music. 🎛️🎚️
