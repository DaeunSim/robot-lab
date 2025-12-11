### Configuration ###   

#### Install Conda

1. create a new directory (lerboot_lab)        

2. locate setup_conda.yaml and requirements_conda.txt in the directory    

3. open a new terminal as an amdin from the directory    

4. set up conda    
(git repo: https://github.com/jeongeun980906/lerobot-mujoco-tutorial#)
```
user # conda env create -f setup_conda.yaml
user # conda activate lerobot_lab
(lerobot_lab) user # pip install -r requirement_conda.txt
(lerobot_lab) user # git clone https://github.com/jeongeun980906/lerobot-mujoco-tutorial.git
(lerobot_lab) user # python -m ipykernel install --user --name=lerobot_lab --display-name 'Python (lerobot_lab)'
```

5. open jupyter notebook
```
(lerobot_lab) user # jupyter notebook --browser=chrome
```

    
#### Mujoco Tutorial    

1. collect_data.ipynb
   - When the cup is moved to the left side of the plate, one episode is finished,    
     then a data sample is generated and located in lerobot-mujoco-tutorial/demo_data/data/chunk-000/
   - NUMBER_DEMO=1 this specifies the number of demonstrations for data collection.
     If this is set to 3, three episodes will run, and a dataset containing three episodes will be created.

2. visualize_data.ipynb
   - It is to visualize the generated dataset from the collect_data.ipynb.
   - LeRobotDataset('omy_pnp', root='./demo_data') specifies the path and name of the dataset.    

3. training process    
   - Skip the training stage in this tutorial.
   - Relevant tools: WandB (logging/monitoring), data augmentation(add noise)

4. deploy.ipynb
   - ckpt refers to the checkpoint resulting from training.
     The robot arm moves based on the inference results from this model.    


