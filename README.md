## Key Features of Qt Template

### 1. File Editor
Compose and edit text files with ease! The **File Editor** allows you to:
- Open existing text files.
- Save your work effortlessly to preserve your compositions.

**Demo**:  

https://github.com/user-attachments/assets/4fa1dc9a-c8c9-4cd6-be1c-78cc40675824


### 2. Rotate 3D
Visualize and interact with 3D objects! The **Rotate 3D** feature includes:
- Smoothly rotating 3D models in OpenGL.
- Switching between multiple predefined objects.
- Loading and viewing custom STL files for a personalized experience.

**Demo 1**:  

https://github.com/user-attachments/assets/77d8ff96-aa22-40ae-800f-07075b2e73fd

**Demo 2**:  

https://github.com/user-attachments/assets/2de6f3bd-50d8-4059-8470-222393f56a4f

### 3. Tic Tac Toe
Challenge yourself or a friend with the classic **Tic Tac Toe** game:
- Enjoy an interactive user interface.
- Fun and intuitive gameplay.

**Demo**:  

https://github.com/user-attachments/assets/cbc7e14e-1a9f-4316-ba7a-927a9bea7f53

### 4. Image Draw
Unleash your creativity with **Image Draw**, a drawing application reminiscent of MS Paint:
- Sketch and draw freely on a blank canvas.
- Save your artistic creations as PNG files.

**Demo**:  

https://github.com/user-attachments/assets/02438ea1-f87c-4e15-9a86-a55f3192b2d4


## Directory Structure

The project is organized into the following directories and files:

- `main.py`: The primary entry point of the application.
- `config/`: This folder contains adjustable parameters, constants, and settings for the project.
- `resources/`: This folder stores non-code materials such as icons, sounds, and other resources.
- `src/`: This folder contains the source code for the project.
- `tests/`: This folder mirrors the structure of the `src` folder and contains tests for the capabilities stored within `src`.
- `environment.yaml`: This file is used to set up the developer environment.
- `README.md`: This file describes how to work within and run the project.

## Setting Up the Development Environment

This project uses Miniconda to manage the development environment.  Miniconda can be downloaded from https://www.anaconda.com/docs/getting-started/miniconda/install.  Follow the steps below to create and manage the environment using `environment.yaml`.

### Creating the Environment

To create the environment from the `environment.yaml` file, run the following command:

```sh
conda env create -f environment.yaml -n <environment_name>
conda activate <environment_name>
```

This will create a new conda environment with all the dependencies specified in the `environment.yaml` file.  By default, this QtTemplate has a placeholder name which can be optionally set using the `-n` flag in the `conda env create` command.

### Updating Packages

To update the packages in the environment to their latest versions, use the following command:

```sh
conda activate <environment_name>
conda update --all
```

### Installing New Packages

To install new packages into the environment, activate the environment and use the `conda install` command:

```sh
conda activate <environment_name>
conda install <package_name>
```

Some packages may not be available in the default Conda channels.  conda-forge can be included during the installation step to potentially resolve this:

```sh
conda install -c conda-forge <package_name>
```

### Updating `environment.yaml`

After installing new packages or making changes to the environment, you should update the `environment.yaml` file to reflect these changes.  To export the current state of the environment to `environment.yaml`, use the following command:

```sh
conda env export --no-builds > environment.yaml
```

This will overwrite the existing `environment.yaml` file with the current environment configuration, excluding build-specific details.  Note that the "prefix" field within `environment.yaml` can simply be removed.

## Running the Code

To run the code, ensure that the conda environment is activated and then execute the `main.py` script. Use the following commands:

```sh
conda activate <environment_name>
python ./main.py
```

This will start the application using the environment and dependencies specified in the `environment.yaml` file.

## Creating an Executable

To create a standalone executable of the application, you can use PyInstaller.  PyInstaller bundles a Python application and all its dependencies into a single package.  To create an executable, run the following command:

```sh
pyinstaller --noconsole --onefile --name QtTemplate --add-data "resources/*;resources" ./main.py
```

This command will generate a single executable file named `QtTemplate`. The executable will be located in the `dist` directory. You can distribute this executable to users who do not have Python installed.
