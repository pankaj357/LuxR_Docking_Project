# Molecular Docking of LuxR Protein with Octylbenzene

This repository contains all data, results, and configuration files associated with the study:

**"Molecular Docking of LuxR Protein with Octylbenzene"**  
*by Pankaj and Srishti Singh*  
Affiliation: ICAR - Indian Agricultural Research Institute, New Delhi, India  
Website: [https://www.iari.res.in](https://www.iari.res.in)

---
## Description
Note: The manuscript based on this work is currently being finalized and has not yet been submitted. This repository is made public for transparency and reproducibility.

---
## 🧬 Project Summary

This study investigates the interaction of the LuxR quorum-sensing transcription factor with **Octylbenzene**, a non-canonical, hydrophobic compound. The goal is to evaluate its potential to mimic natural acyl-homoserine lactones (AHLs) and disrupt bacterial quorum sensing.

---

## 📁 Repository Structure

```
LuxR_Docking_Project/
├── Data/
│   ├── ahl_3d.mol2
│   ├── ahl_fixed.pdb
│   ├── ahl.pdbqt
│   ├── ahl.sdf
│   ├── config.txt
│   ├── docked_luxr_ahl.pdbqt
│   ├── luxr_clean.pdbqt
│   ├── luxr_structure.pdb
│   ├── luxr_full.pdbqt
│   ├── luxr.fasta
│   ├── prep_ligand.py
│   └── vina_log.txt
├── Docking/
│   └── config.txt
├── Figures/
│   ├── luxr_docking_final.png
│   └── luxr_docking_final.tiff
└── README.md
```

---

## 🛠️ Tools and Software Used

- **AutoDock Vina v1.1.2** – Molecular docking
- **Open Babel v3.1.1** – File format conversion
- **PyMOL v2.5** – 3D visualization
- **Discovery Studio Visualizer 2021** – 2D interaction mapping

---

## ⚙️ Docking Protocol Summary

- **Ligand**: Octylbenzene (CID: 16607), prepared using Open Babel
- **Receptor**: LuxR modeled from PDB template 3QP5
- **Docking Software**: AutoDock Vina
- **Grid Box**:
  - Center: X = –3.793, Y = –3.755, Z = 15.901
  - Size: 20 × 20 × 20 Å
- **Affinity**: –3.0 kcal/mol
- **Output Pose**: `docked_luxr_ahl.pdbqt`

---

## 📊 Key Residue–Ligand Interactions

| Residue | Type      | Role in Interaction                   |
|---------|-----------|----------------------------------------|
| TYR40   | Aromatic  | π–π stacking                           |
| ASN61   | Polar     | Possible H-bond acceptor               |
| TYR62   | Aromatic  | π–π stacking / H-bond                  |
| PRO63   | Nonpolar  | Van der Waals                          |
| GLU64   | Charged   | Electrostatic stabilization            |
| LYS65   | Charged   | May stabilize ligand edge              |
| TRP66   | Aromatic  | π–π stacking / hydrophobic             |
| GLU115  | Charged   | Distant stabilizer or steric limiter   |
| SER116  | Polar     | Hydrogen bond donor                    |
| GLY117  | Neutral   | Structural support                     |

---

## 🖼️ Figures

- `luxr_docking_final.tiff` – Publication-quality figure (300 DPI, uncompressed)
- `luxr_docking_final.png` – Web-friendly preview image

---

## 📜 How to Use

To replicate or build upon this work:

1. Clone this repository or download the ZIP.
2. Prepare receptor and ligand using the files in `/Data/`.
3. Run docking using the `config.txt` inside `/Docking/`.
4. Visualize results in PyMOL or Discovery Studio.
5. Refer to `vina_log.txt` for docking summary.

---

## 🔗 Data Access and Citation

This repository provides full access to data and visual assets for transparency and reproducibility.  
If used in your research or presentations, please cite as:

> Pankaj & Srishti Singh, *Molecular Docking of LuxR Protein with Octylbenzene*, submitted to **Bioinformation**, 2025.

📧 Contact:
- *Pankaj*: ft.pank@gmail.com  
- *Srishti Singh*: srishtisingh5433@gmail.com

---

## 📘 License

This repository is distributed under the [MIT License](https://opensource.org/licenses/MIT).  
Free for academic and research use.
