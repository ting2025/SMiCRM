import os
import csv
from rdkit import Chem
from rdkit.Chem import AllChem

input_folder = '/Users/tinaleung/Desktop/mechanism'
csv_file = '/Users/tinaleung/Desktop/mechanism/mechanism.csv'
output_folder = os.path.join(input_folder, 'mechanism_SD')

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open(csv_file, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Extract image name and SMILES from current row
        image_name = os.path.splitext(os.path.basename(row['\ufefffile_path']))[0]
        smiles = row['SMILES']

        mol = Chem.MolFromSmiles(smiles)

        # Check if molecule is valid
        if mol is None:
            print(f'Error: unable to generate molecule from SMILES "{smiles}" for image {image_name}')
            continue

        Chem.Kekulize(mol)
        sd_file = os.path.join(output_folder, f'{image_name}.sdf')
        w = Chem.SDWriter(sd_file)
        w.write(mol)
        w.close()
