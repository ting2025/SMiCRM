
# SMiCRM
Optical chemical structure recognition (OCSR) systems aim to understand such diagrams computationally. However, developing methods for complex reaction schemes remains an outstanding challenge due to a lack of annotated datasets mapping molecular images and their identity in SMILES. We introduce SMiCRM, a Structural molecular identifier of Molecular images in Chemical Reaction Mechanisms, a dataset designed to benchmark machine recognition capabilities of chemical molecules within named reaction mechanisms. Comprising 454 images, it spans various organic reactions, each illustrated with molecular structures and mechanistic arrows. SMiCRM addresses this gap by offering a rich collection of annotated molecule images, enhancing the benchmarking process for OCSR methods. This dataset includes a machine-readable molecular identity for each image and integrates mechanistic arrows, adding a layer of complexity absent in previous datasets. By doing so, SMiCRM provides a more authentic and challenging framework for testing molecular recognition technologies, fostering advancements in accurately interpreting complex chemical reaction mechanisms.

<img width="512" alt="image" src="https://github.com/ting2025/SMiCRM/assets/147067583/fa1f9b5f-cc4e-4023-901b-dbb64e885407">

# Structural molecular identities
SDF for molecules are a unique file representing the molecular identity in rdkit. This repo contains a file on how to translate SMILES into SDF files and save into original file path.

# Use and Reuse
Feel free to use this benchmark dataset to test out your OCSR model. 

## DOI of this dataset
10.5281/zenodo.10811653
## Dataset link of this dataset
https://zenodo.org/records/10811653
## Paper access
Paper: arxiv
## Citation 💌
If you use our code or our dataset please cite the paper or this github page with
```
@misc{leung2024smicrmbenchmarkdatasetmechanistic,
      title={SMiCRM: A Benchmark Dataset of Mechanistic Molecular Images}, 
      author={Ching Ting Leung and Yufan Chen and Hanyu Gao},
      year={2024},
      eprint={2407.18338},
      archivePrefix={arXiv},
      primaryClass={cs.CV},
      url={https://arxiv.org/abs/2407.18338}, 
}
```
