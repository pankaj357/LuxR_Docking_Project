
from rdkit import Chem
from rdkit.Chem import AllChem
import os

# Load ligand
mol = Chem.MolFromPDBFile("/Users/admin/Desktop/LuxR_Docking_Project/Data/ahl_fixed.pdb", removeHs=False)

if mol is None:
    raise ValueError("Failed to load PDB file. Check ahl_fixed.pdb")

# Add hydrogens
mol = Chem.AddHs(mol)

# Generate 3D conformer
result = AllChem.EmbedMolecule(mol, randomSeed=42)

if result != 0:
    raise RuntimeError("⚠️  Could not embed 3D coordinates. Structure may be invalid.")

# Optimize geometry
opt_result = AllChem.UFFOptimizeMolecule(mol)
if opt_result != 0:
    print("⚠️  Optimization failed or incomplete. Proceeding anyway.")

# Write MOL2 file for Open Babel conversion
Chem.MolToMolFile(mol, "ahl_fixed.mol")

# Convert to PDBQT
os.system("obabel ahl_fixed.mol -O ahl.pdbqt --partialcharge gasteiger")

print("✅ Ligand saved as ahl.pdbqt")
