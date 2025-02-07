# AIOS-LSFS
From Commands to Prompts: LLM-based Semantic File System for AIOS

## 🏠 Architecture of LSFS
<p align="center">
<img src="assets/lsfs-arc.png">
</p>

## 🚀 Quickstart

### Installation
```
conda create -n lsfs python=3.11
conda activate lsfs
pip install -r requirements.txt
```

### Run
Please make sure you have read the instructions in AIOS to set up the environment and launch the AIOS kernel. 

After that, you can run the following command to start the LSFS terminal.

```
python scripts/run_terminal.py
```

Then you can start interacting with the LSFS terminal by typing natural language commands. 

## Reference
If you find this project useful, please cite our paper:
```
@article{shi2024commands,
  title={From Commands to Prompts: LLM-based Semantic File System for AIOS},
  author={Shi, Zeru and Mei, Kai and Jin, Mingyu and Su, Yongye and Zuo, Chaoji and Hua, Wenyue and Xu, Wujiang and Ren, Yujie and Liu, Zirui and Du, Mengnan and others},
  journal={arXiv preprint arXiv:2410.11843},
  year={2024}
}
```