# File Management System
The file management system is a set of rules and guidelines for managing digital files.<br>
It contains two connected subsystems: a system for organizing files and a system for backing up files.<br>
This document is a guide for setting up your file management system and documentation to reference when maintaining it.

## Contents
- [SETUP GUIDE](#setup-guide)
  - [IDENTIFY SYSTEM DEVICES](#identify-system-devices)
  - [ADDING SETUP FILES](#adding-setup-files)
  - [ORGANIZING YOUR FILES](#organizing-your-files)
    - [IDENTIFYING DEFAULT DIRECTORIES](#identifying-default-directories)
    - [CREATING CUSTOM DIRECTORIES](#creating-custom-directories)
  - [BACKING UP YOUR FILES](#backing-up-your-files)
    - [IDENTIFY SYSTEM DATA](#identify-system-data)
    - [ALLOCATING STORAGE SPACE](#allocating-storage-space)
    - [CREATING YOUR BASE COPY](#creating-your-first-copy-of-system-data)
    - [FILLING UNUSED SPACE](#filling-unused-space)
      - [ADDING FULL COPIES](#adding-full-copies)
      - [ADDING PARTIAL COPIES](#adding-partial-copies)
      - [ADDING TO PARTIAL COPIES](#add-to-partial-copies)
  - [MAINTAINING YOUR NETWORK](#maintaining-your-network)
- [DOCUMENTATION](#documentation)
  - [ADD FULL COPY ALGORITHM](#add-full-copy-algorithm)
  - [ADD PARTIAL COPY ALGORITHM](#add-partial-copy-algorithm)
  - [ADD TO PARTIAL COPY ALGORITHM](#add-to-partial-copy-algorithm)
  - [ARCHIVE INSTANCE](#archive-instance)
  - [BASE COPY](#base-copy)
  - [BREAKAWAY COPY](#breakaway-copy)
  - [CUSTOM DIRECTORIES](#custom-directories)
    - [BACKUP-STORAGE](#backup-storage)
    - [STORAGE-EXTENSION](#storage-extension)
    - [FILE-MANAGEMENT-SYSTEM](#file-management-system-1)
      - [GLOBAL](#global)
      - [INSTANCE-INFORMATION](#instance-information)
      - [SAVE](#save)
      - [WRITABLE-DIRECTORIES](#writable-directories)
  - [DEFAULT DIRECTORIES](#default-directories)
  - [DEVICES](#devices)
    - [STANDARD DEVICES](#standard-devices)
    - [SIMPLE DEVICES](#simple-devices)
  - [DOCUMENTATION FILE](#documentation-file)
  - [FILE MANAGEMENT SYSTEM](#file-management-system-2)
  - [FILE MANAGEMENT SYSTEM INSTANCE](#file-management-system-instance)
  - [FILL UNUSED SPACE ALGORITHM](#fill-unused-space-algorithm)
  - [FOLDER TRACKING DIRECTORIES](#folder-tracking-directories)
  - [INSTANCE NETWORKS](#instance-networks)
  - [INSTANCE CONTAINER DIRECTORY](#instance-container-directory)
  - [INSTANCE PRESERVATION DIRECTORIES](#instance-preservation-directories)
  - [INSTANCE TRACKING DIRECTORIES](#instance-tracking-directories)
  - [NETWORK REFRESH ALGORITHM](#network-refresh-algorithm)
  - [PLACEHOLDERS](#placeholders)
  - [STALE FOLDER](#stale-folder)
  - [USER CONTROLLED FILES AND FOLDERS](#user-controlled-file--user-controlled-folder)

# Setup Guide
## Identify System Devices
Identify every device you use that meets one or more of the following criteria:
- You want to organize files on the device
- You want to backup files from the device
- You want to store backups on the device
These will be referred to as your system devices.

## Adding Setup Files
From your system devices, select the device you use most or the device that is easiest to access.<br>
This will be referred to as your controller device.
On your controller device:
- If the device has an operating system, go to your user directory.
- If the device does not have an operating system, go to the root directory.
- Copy the files from Setup/Controller into whichever directory you're in.
- Open the file File-Management-System/Instance-Information/name.txt.
- Choose a name for your controller and save it in the file.
- Write and save your controller name in File-Management-System/Instance-Information/controller.txt.
- In File-Management-System/Global, rename the folder 'This-Instance' to the name of your controller.
- In File-Management-System/Writable-Directories, delete the three empty folders and add shortcuts to the 'Backup-Storage', 'File-Management-System', and 'Storage-Extension' folders.
- If the device has a Desktop folder, I recommend adding to it a shortcut to the 'File-Management-System' folder.

System devices that are not your controller device will be referred to as your standard devices.<br>
Repeat the following on all of your standard devices:
- If the device has an operating system, go to your user directory.
- If the device does not have an operating system, go to the root directory.
- Copy the files from Setup/Standard into whichever directory you're in.
- Open the file File-Management-System/Instance-Information/name.txt.
- Choose a unique name for this device and save it in the file.
- Write and save your controller name in File-Management-System/Instance-Information/controller.txt.
- In File-Management-System/Writable-Directories, delete the three empty folders and add shortcuts to the 'Backup-Storage', 'File-Management-System', and 'Storage-Extension' folders.
- If the device has a Desktop folder, I recommend adding to it a shortcut to the 'File-Management-System' folder.

On your controller device:
- For each standard device 'D', copy Setup/Templates/Instance-Tracking-Directory/Instance-Name to File-Management-System/Global and rename it to 'D'.

## Adding Concepts
In the previous step, every time you copied the folders in Setup/Controller or Setup/Standard into a user or root directory, you created a 'file management system instance' in that directory.<br>
A 'file management system instance' or 'instance' for short, is an imaginary structure that contains part of the file system on a device.<br>
Specifically, an instance contains everything inside of the folder in which the File-Management-System directory resides.<br>
The purpose of defining the instance structure on a device is to artificially restrict your activity on that device to the smallest area that contains all of your files.<br>
The reason you created an instance in each of your user directories is because this is where people keep the vast majority of their files.<br>
On your devices without an operating system, the reason you created an instance at the root directory is because devices without an operating system are likely pure storage devices with no existing file system.<br>
Thus, it is likely your files are stored directory at the root.<br>
The expectation from this point is that you will avoid modifying any files or folders outside of your instances whenever possible.<br>
If after reading this you feel that your instances should be placed elsewhere, you are free to do so, but consider using multiple instances on a device first as some locations may not be supported (see documentation).<br>

On your controller device, you created a special type of instanced called a 'controller instance' or 'controller' for short.<br>
To differentiate controller instances from other instances, any instance that is not a controller instance will be referred to as a 'standard instance'.<br>
The purpose of a controller instance is to connect a group of instances into a 'file management system instance network' or 'instance network' or just 'network' for short.<br>
The purpose of an instance network is to facilitate coordinated data storage across a group of related instances.

Moving forward, we will no longer need to concept of 'system devices'.<br>
Instead, the instructions will refer to your 'instance network', its 'controller instance', and its 'standard instances'.

## Organizing Your Files
### Identifying Default Directories
For this next part, you will need to be familiar with the following terminology:
- The 'top level' of an instance is the location in which its File-Management-System folder is stored.
- A file or folder 'F' in a directory 'D' is a user controlled file if every directory in the path of 'F' after 'D' was created by you.

For each instance in your network:
- At the top level, identify the folders that:
  - Contain some of your files that you want to organize and/or save, and
  - You did not create, and
  - Are not the File-Management-System, Backup-Storage, Storage-Extension, Downloads, or Desktop folders.
  - Note: This will usually include folders like Documents, Pictures, Videos, etc.
- For each folder 'F' you identify:
  - Create a folder at the top level of the instance called 'Protected-F'.
  - In Protected-F, create a file called README.md and write in it: 'The purpose of this folder is to store user controlled F files.'
  - In File-Management-System/Default-Directories, create a shortcut to 'F'.
  - In File-Management-System/Writable-Directories, create a shortcut to Protected-F.
  - Move your user controlled files and folders in 'F' from 'F' to Protected-F.
  - If at this point you realize that 'F' does not have many user controlled files or folders, you can delete Protected-F and its shortcut in Writable-Directories.
- If the instance has a Desktop folder:
  - Create a file in it called README.md and write in it: 'The purpose of this folder is to store shortcuts and folders to group shortcuts.'
  - In File-Management-System/Writable-Directories, create a shortcut to Desktop.
- If the instance has a Downloads folder:
  - Create a file in it called README.md and write in it: 'The purpose of this folder is to temporarily store downloaded files until they can be stored elsewhere.'
  - In File-Management-System/Writable-Directories, create a shortcut to Downloads.

### Adding Concepts
The folders 'F' that you just identified are called 'default directories'.<br>
The folders 'Protected-F' that you just created are called 'custom directories'.

The first purpose of these classifications is to enable you to separate your files from files that are managed by other people's programs.<br>
You did this when you moved your user controlled files from default directories to custom directories.

The second purpose is to group your files into units that can be easily accessed, tracked, and stored.<br>
This will be especially useful if you want to create backup copies of your data.

The third purpose is to further artificially restrict your activity.<br>
The expectation from this point on is that you will avoid modifying files and folders outside of custom directories whenever possible.

### Creating Custom Directories
In this section, you will create more custom directories to clean up your instance network.<br>
For the best results, adhere to the custom directory principles and strictly follow the custom directory rules, all of which can be found [here](#custom-directories).

For each instance in your network, at the top level:
- Create custom directories for any remaining user controlled files and folders in the instance that are not already in a custom directory.
  - This includes things like loose files and folders at the top level of the instance.
  - You may also want to temporarily break the rules and bring in content from outside the instance.
- Create custom directories for your files that do not belong in or would be more appropriately stored outside of an existing custom directory.
  - For example:
    - Create a custom directory to store random executables and installers from your downloads and desktop folders.
    - Move work and school files from 'Protected-Documents' to custom directories called 'Work' and 'School' respectively.
- For each custom directory 'C' that you made:
  - Create a file in C called README.md and write the purpose of C in it.
  - Go to File-Management-System/Writable-Directories and create a shortcut to C.

## Adding Concepts
Now that your network is fully set up and organized, you're ready to back up your data.<br>
Doing this requires an understanding of what data you want to back up.<br>
To aid in this, I'm introducing the concept of 'system data'.<br>
The system data of your instance network is simply the set of files and folders in your network that you want to back up.<br>
The goal of the following section is to maximize the number of copies of system data stored across your instance network.

## Backing Up Your Files
If you do not have any files in your instance network that you want to back up, you can skip this section.<br>
Otherwise, keep your controller instance available as you will need to use it frequently from here onwards.

### Identify System Data
The first step in backing up your data is to figure out what data you want to back up.<br>
Fortunately, each file management system instance has a folder 'File-Management-System/Save' to make this process easier.<br>
The Save folder stores shortcuts to folders you want to back up in an instance.<br>
It has a strict rule that it may only store shortcuts to default and custom directories from the instance in which it resides.<br>
This is mainly to prevent you from backing up parts of folders, which are difficult to work with.

For each instance 'I' in your network:
- Add a shortcut to every folder you want to back up from 'I' to the File-Management-System/Save folder of 'I'.
  - Every shortcut you need should already be in File-Management-System/Default-Directories and File-Management-System/Writable-Directories.
- For every folder 'F' with a shortcut in File-Management-System/Save:
  - Confirm that 'F' does not contain any shortcuts to folders that are not contained within a folder with a shortcut in File-Management-System/Save.
    - There is no official procedure for fixing this, as it should not happen if you follow the [custom directory rules](#rules-1).
  - In your network's controller instance, create a [placeholder](#placeholders) for 'F' and add it to File-Management-System/Global/I/Save.

### Allocating Storage Space
The next step is to figure out where you want to store back up copies of system data.

For each instance 'I' in your network:
- If you want to use some amount of space 'S' on the device that 'I' is on to store back up copies of system data:
  - Set the value in Backup-Storage/capacity.txt to 'S'.
  - In your network's controller instance, set the value in File-Management-System/Global/I/Backup-Storage/capacity.txt to 'S'.

### Adding Concepts
You are almost ready to start making back up copies of system data.<br>
But before you do, you need to know how you will manage these copies.<br>
Any instance that stores part of a system data copy will be assigned a 'copy id'.<br>
If an instance stores a full copy of system data, its copy id will be unique in its network.<br>
If an instance stores part of a copy of system data, its copy id will be shared with other instances in its network that store other parts of the same copy.<br>
The controller instance of a network knows the copy id of every instance in its network and which system data folders each instance stores.<br>
This allows you to use your controller to analyze the state of each copy in your network before you make any modifications.

### 'Creating' Your First Copy of System Data
Your instance network already contains a full copy of system data stored at the top level of one or more instances.
This is called your network's 'base copy'.

For each instance 'I' in your network:
- If 'I' contains any shortcuts in its File-Management-System/Save folder:
  - Change the value in Backup-Storage/copy_id.txt to 0.
  - In your network's controller instance, change the value in File-Management-System/Global/I/Backup-Storage/copy_id.txt to 0.

### Adding Concepts
You are now ready to start making 'real' copies of system data.<br>
In an instance, any files that are part of a 'real' copy are stored in the [Backup-Storage directory](#backup-storage).<br>
Because this directory is going to store files from different instances, there needs to be a way to keep files from different instances separate.<br>
To do this this, files in Backup-Storage will be exclusively stored in '[instance preservation directories](#instance-preservation-directories)'.<br>
Whenever you add folders to an instance preservation directory in Backup-Storage, you must ensure that you are following both the instance preservation directory rules and the Backup-Storage directory rules.<br>
Read the Backup-Storage directory and instance preservation directory sections in the documentation before reading further.

The process of making 'real' copies is handled entirely by the '[fill unused space](#fill-unused-space-algorithm)' algorithm.<br>
As its name suggest, the fill unused space algorithm will eliminate any 'remaining capacity' in your instance network.<br>
The remaining capacity of an instance is its capacity - the size of its Backup-Storage folder.

### Filling Unused Space
This section will introduce you to the fill unused space algorithm.<br>
The algorithm you will use has been modified slightly to make it easier to understand.<br>
After completing this guide, use the algorithm as it is described in the documentation.

#### Adding Full Copies
For each instance 'I' in your network:
- If 'I's' capacity >= system data size - the sum of the size of all system data folders in 'I':
  - In Backup-Storage, add all system data folders that are not already in I.
  - If the value in Backup-Storage/copy_id.txt is not unique within your network, change it to be unique.
  - For each folder 'F' you created in/added to Backup-Storage:
    - If 'F' is not in system data: in your network's controller instance, create 'F' in/add 'F' to File-Management-System/Global/'I'/Backup-Storage.
    - Otherwise: in your network's controller instance, create a placeholder for 'F' and add it to File-Management-System/Global/'I'/Backup-Storage.
  - If you changed the value in Backup-Storage/copy_id.txt: update File-Management-System/Global/'I'/Backup-Storage/copy_id.txt in your network's controller instance to have the same value.

#### Adding Concepts
In the next section you will deal with copies of system data stored across multiple instances.<br>
These copies are referred to as 'fragmented copies'.<br>
It is possible you have already encountered these when you set up your network's base copy.<br>
Working with fragmented copies requires heavy use of your network's controller instance.<br>
One of the most important functions of the controller instance is to allow you to determine which folders a fragmented copy contains.<br>
This allows you to continue an incomplete copy from a different instance than it was started on without duplicating any folders.

#### Adding Partial Copies
For each instance 'I' in your network:
- If 'I's' capacity < system data size - the sum of the size of all system data folders in 'I' and 'I's' remaining capacity > 0 and 'I' does not have a copy id:
  - If there are any incomplete copies of system data in the same instance network as 'I':
    - Let COPY be the copy id of any incomplete copy.
    - For each folder 'F' in system data:
      - If 'F' is not in the copy with id COPY and the remaining capacity of 'I' is not 0:
        - If 'F' can be added to the Backup-Storage folder of 'I': add it.
    - If any folder was added to 'I':
      - Set the value in Backup-Storage/copy_id.txt to COPY.
  - Else:
    - Let 'L' be a list of folders in system data.
    - While 'L' is not empty and the remaining capacity of 'I' is not 0:
      - If the next folder 'F' in 'L' can be added to the Backup-Storage folder of 'I': add it and remove it from 'L'.

#### Adding Concepts
At this point, your network contains as many copies as it can.<br>
However, it is possible that some of the instances storing your base copy have unused capacity.<br>
To address this, we will use a new branch of the fill unused space algorithm.

#### Add to Partial Copies
For each instance 'I' in your network:
- If 'I' does not store a full copy of system data and 'I's' remaining capacity > 0:
  - Let 'eligible_folders' be a list of system data folders that are not stored anywhere in 'I'.
  - let 'copy_folders' be a list of all folders in the copy that 'I' stores part of.
  - Sort 'copy_folders' in ascending order of frequency.
    - The frequency of an element of 'copy_folders' is the number of times it appears in the list.
  - Remove the duplicate entries from 'copy_folders'.
  - If there are any folders in system data that are not in 'copy_folders': add them to the front of the list.
  - For each folder 'F' in 'copy_folders':
    - If the remaining capacity of 'I' > 0 and 'F' is in 'eligible_files':
      - If 'F' can be added to the Backup-Storage folder of 'I': add it.

## Maintaining Your Network
If you have completed all previous sections of this guide, then your network is completely set up.<br>
For further learning, please refer to the documentation below.

# Documentation
The file management system acknowledges and accounts for the fact that some of its rules will need to be broken at times in practice.<br>
These rules will be clearly marked as 'Soft'.

## Add Full Copy Algorithm
### Inputs
- An instance I.

### Pseudocode
Remove all stale files from the Backup-Storage directory of I.<br>
For every folder F in system data:
- If F [can be added](#backup-storage-property-4) to the Backup-Storage directory of I, add it.<br>

If I does not have a unique copy id, give it one.

### Outputs
- None.

## Add Partial Copy Algorithm
### Inputs
- An instance I.

### Pseudocode
If there is one or more incomplete copies of system data in the same instance network as I:
- Let COPY be the copy id of any incomplete copy.
- For each folder F in system data:
  - If F is not in the copy with id COPY and the remaining capacity of I is not 0:
    - If F can be added to the Backup-Storage folder of I: add it.
- If any folder was added to I:
  - Set the copy id of I to COPY.
Else:
- Let L be a list of folders in system data.
- While L is not empty and the remaining capacity of I is not 0:
  - If the next folder F in L can be added to the Backup-Storage folder of I: add it and remove it from L.

### Outputs
- None.

## Add to Partial Copy Algorithm
### Inputs
- An instance I.

### Pseudocode
Let eligible_folders be a list of system data folders that do not have a shortcut in the File-Management-System/Save folder of I and are not stored in the Backup-Storage folder of I.<br>
Let copy_folders be a list of all folders in the copy that I stores part of.<br>
The frequency of an element of copy_folders is the number of times it appears in the list.<br>
Sort copy_folders in ascending order of frequency.<br>
Remove the duplicate entries from copy_folders.<br>
If there are any folders in system data that are not in copy_folders: add them to the front of the list.<br>
For each folder F in copy_folders:
- If the remaining capacity of I > 0 and F is in eligible_files:
  - If F can be added to the Backup-Storage folder of I: add it.

### Outputs
- None.

## Archive Instance
Archive is an imaginary instance used to 'store' files that cannot be easily incorporated into a real instance.<br>
In practice, this allows users to store these files in an instance preservation directory.

### Rules
1. The Archive instance exists in every instance network.

## Base Copy
The base copy of an instance network N is the copy of system data made of folders that each have a shortcut in one of the File-Management-System/Save directories of N.

## Breakaway Copy
A breakaway copy in an instance I is a complete copy of system data that is stored partially in I's Backup-Storage directory and partially in I's Instance-Container directory.

## Custom Directories
Custom directories are folders made by a user as part of a file management system instance.

### Principles
1. The number of custom directories in an instance should be kept relatively small.
2. Custom directories should group content into categories that are approximately as broad as the categories of default directories.
3. If there is a program controlled file or folder 'F' that thematically belongs in a custom directory 'D', add a shortcut to 'F' in 'D'.

### Rules
1. Custom directories must be stored at the same level as the File-Management-System directory of the instance they reside in.
2. For each custom directory in an instance, there must a shortcut in the File-Management-System/Writable-Directories folder of that instance.
3. Custom directories may only store the following:
    - User controlled files and folders.
    - Shortcuts to default folders and other custom directories.
    - Shortcuts to files and folders within default folders and other custom directories.

### Backup-Storage
Stores instance preserving directories associated with different instances in the network in which the containing instance resides.

#### Rules
1. Excluding the documentation file, copy id file, and capacity file, the top level the Backup-Storage directory must only contain instance preservation directories.
2. The copy_id file of the Backup-Storage directory contains a copy id if and only if Backup-Storage is storing system data files.
3. A storage device cannot contain any empty directories in its Backup-Storage folder.
4. <span id="backup-storage-property-4"> A folder F is eligible to be added to instance preservation directory P in instance I if:
    - The remaining capacity of I >= the size of F.
    - F does not have a shortcut in the File-Management-System/Save directory of I and is not stored in the Backup-Storage directory of I.
    - F is in system data.
   </span>

### Storage-Extension
Stores files from different instances in the network in which the containing instance resides.

#### Rules
1. Excluding the documentation file, the top level the Storage-Extension directory must only contain instance preservation directories.
2. Do not store backups in the Storage-Extension directory.

### File-Management-System
The file management system instance folder is part of a file management system instance.

#### Global
The global directory is used by a controller instance to track the contents of the Backup-Storage and File-Management-System/Save directories of all instances in the instance network it resides in.

##### Rules
1. The Global directory may only be stored in a controller instance at File-Management-System/Global.
2. Except for the documentation file, all children of the global directory are instance tracking directories.
3. For each instance A in an instance network, there is an instance tracking directory in the Global directory named 'A'.

#### Instance-Information
The Instance-Information folder, unsurprisingly, stores information about the file management system instance it resides in.

##### Controller.txt
Stores the name of the controller instance of the network to which the instance in which the file resides belongs.

##### Name.txt
Stores the name of the instance in which the file resides.

#### Save
Stores a shortcut to every folder that should be backed up from the instance.

##### Rules
1. With the exception of its documentation file, the Save directory may only contain shortcuts to default and custom directories.
    - A consequence of this is that you cannot back up only part of a directory. This limitation greatly simplifies file tracking.
2. The Save directory cannot contain shortcuts to Backup-Storage or Storage-Extension.

#### Writable-Directories
Stores a shortcut to every custom directory in the instance it resides in.

##### Rules
1. With the exception of its documentation file, the Writable-Directories directory may only contain shortcuts to directories.
2. Soft: Only shortcuts to custom directories and special case default directories are permitted.

## Default Directories
Default directories are any directories that are children of an instance container directory and are not custom directories.<br>
It is important to identify these, as default directories form an integral part of many user's organization strategy, which needs to be accounted for.<br>
Some of the more important default directories include Documents, Music, Pictures, and Videos.<br>
As part of the instance creation process, users identify important default directories and move their user controlled files out into custom directories that serve the same function, but cannot be written to by programs.

### Special Cases
The Desktop and Downloads folders are special cases because while programs do write to them, they do so in very predicable ways.<br>
This makes it easy for users to organize these folders however they want.

## Devices
### Standard Devices
Devices with an operating system.

### Simple Devices
Devices without an operating system.

## Documentation File
A documentation file is a file that documents the purpose of a directory.

### Rules
1. The documentation file F of a directory D must be stored at D/F.
2. Each of the following folders must contain a documentation file:
    - Every custom directory.
    - Every child directory of File-Management-System.

## File Management System
The file management system is a set of instructions for organizing and saving the files of a file tree.

### Instructions
1. Locate the files to organize and save.
2. Restrict activity to the smallest subtree that contains all of these files.
3. Isolate the files from existing organization schemes.
4. Group the files into easily manageable units.
5. Create a structure to categorize, track, and interact with these units.
6. Add parts to the structure that enable it to coordinate with other structures.

## File Management System Instance
A file management system instance is an implementation of the file management system instructions.<br>
Because it is difficult to determine when some instructions are fully implemented, a file management instance is considered complete when its initial structure is complete.

### Initial Structure
#### Controller Instance
```
Instance-Container/
├── Backup-Storage/
|   ├── capacity.txt
|   ├── copy_id.txt
|   └── README.md
|
├── File-Management-System/
│   ├── Default-Directories/
|   |   └── README.md
│   ├── Global/
│   |   ├── Archive/
│   |   |    └── Save/
|   |   └── README.md
│   ├── Instance-Information/
│   |   ├── controller.txt
│   |   ├── name.txt
|   |   └── README.md
│   ├── Save/
|   |   └── README.md
|   ├── Writable-Directories/
|   |   └── README.md
|   └── README.md
|
├── Storage-Extension/
|   └── README.md
```

#### Standard Instance
```
Instance-Container/
├── Backup-Storage/
|   ├── capacity.txt
|   ├── copy_id.txt
|   └── README.md
|
├── File-Management-System/
│   ├── Default-Directories/
|   |   └── README.md
│   ├── Instance-Information/
│   |   ├── controller.txt
│   |   ├── name.txt
|   |   └── README.md
│   ├── Save/
|   |   └── README.md
|   ├── Writable-Directories/
|   |   └── README.md
|   └── README.md
|
├── Storage-Extension/
|   └── README.md
```

### Properties
1. The location and scope of an instance is the directory in which its File-Management-System folder resides.
2. <span id="instance-property-2"> An instance I is eligible to add a partial copy of system data to its Backup-Storage directory if:
    - System data is not empty.
    - I cannot store a full copy of system data.
    - I's remaining capacity > 0.
    - I does not have a copy id.
   </span>
3. <span id="instance-property-3"> An instance I is eligible to add a full copy of system data to its Backup-Storage directory if:
    - System data is not empty.
    - I does not store a full copy of system data.
    - I can store a full copy of system data (see [property 5](#instance-property-5)).
   </span>
4. <span id="instance-property-4"> An instance I is eligible to add system data folders to its Backup-Storage directory if:
    - System data is not empty.
    - I does not store a full copy of system data.
    - I's remaining capacity > 0.
   </span>
5. <span id="instance-property-5"> An instance I can store a full copy of system data if I's capacity >= system data size - I's system data size.
   </span>

### Implementation Details
#### Instruction 1
Select an instance container directory.

#### Instruction 2
Create the File-Management-System directory and document its purpose by adding this file to it.

#### Instruction 3
Identify important default directories in the instance container directory.
For each important default directory A:
  - Create a custom directory named 'Protected-A'.
  - Move user controlled files from A to Protected-A.

#### Instruction 4
Create custom directories to store remaining user controlled files.

#### Instruction 5
Create the following directories and add a documentation file to each:
- Backup-Storage
- File-Management-System/Save
- File-Management-System/Writable-Directories
- Storage-Extension

#### Instruction 6
Create the following directories and add a documentation file to each:
- File-Management-System/Global
- File-Management-System/Instance-Information

### Rules
1. If an instance exists in a directory D, then there can be no other instance in D or its descendants.
2. Soft: Do not modify the file tree outside the scope of the instance.
3. Soft: Within the scope of the instance, do not move folders that you did not create. If you need to do this, create a shortcut for that folder to use in its place.
4. An instance may not store more than one copy of any file in system data.

## Fill Unused Space Algorithm
### Inputs
- An instance I

### Pseudocode
If I is [eligible](#instance-property-2) to add a partial copy of system data: [add a partial copy](#add-partial-copy-algorithm) with inputs = I.<br>
Else, if I is [eligible](#instance-property-3) to add a full copy of system data: call the [add full copy algorithm](#add-full-copy-algorithm) with inputs = I.<br>
Else, if I is [eligible](#instance-property-4) to add system data folders: call the [add to partial copy algorithm](#add-to-partial-copy-algorithm) with inputs = I.

### Outputs
- None

## Folder Tracking Directories
Folder tracking directories are a special type of directory used to track some or all of the contents of a specific custom or default directory.<br>
Currently, these are only found in the instance tracking directories in File-Management-System/Global.

### Properties
1. The 'limit' of a folder tracking directory is the last level in its file tree.

### Rules
1. The name of an folder tracking directory must match the name of the folder it tracks.
2. Store shortcuts as empty directory placeholders.
3. When tracking Backup-Storage, the limit of the tracking directory is fixed at the level of the 'File-Management-System' directories in Backup-Storage, if it contains any. Otherwise, the limit is fixed at the last level of Backup-Storage.
4. When tracking Save, the limit of the tracking directory is fixed at the last level of Save.

## Instance Networks
A group of related file management system instances or a standalone instance is called a file management system network.

### Instances
The instances of an instance network is a set containing all instances that are part of the network.<br>
This set is sorted by increasing order of available space.

### System Data
The system data of an instance network is a set containing all and only folders with a shortcut in some File-Management-System/Save folder in the network.

### System Data Copies
The system data copies of an instance network is a set of proper and improper subsets and multisets of system data stored within the Backup-Storage folders of the network's instances.

### Rules
1. In a file management system network, there can be no two instances with the same name.
2. In a group of networks, there can be no two networks with the same name.

## Instance Container Directory
Any directory that contains an instance and the File-Management-System directory of that instance is its child.

### Supported Options
- Standard devices: user profile directories
- Simple devices: root directory

## Instance Preservation Directories
Instance preservation directories are a special type of directory used to organize files in the Backup-Storage and Storage-Extension directories.<br>
An instance preservation directory preserves the following information about each file 'F' that it stores:
- The instance 'I' that 'F' originated from.
- The location of 'F' on the device that contains 'I'.

### Rules
1. The name of an instance preservation directory must be the same as the name of the file management system instance it stores files for.
2. Files inside of an instance preservation directory need to be stored so that every part of their absolute paths after the device root is preserved.
    - This gives users the ability to store files from anywhere in the instance.

## Instance Tracking Directories
Instance tracking directories are a special type of directory used to track the contents of select folders in an instance.<br>
Currently, these are only found in File-Management-System/Global.

### Rules
1. The name of an instance tracking directory must match the name of the instance it tracks.
2. All child directories of an instance tracking directory are folder tracking directories.

## Network Refresh Algorithm
### Inputs
- An instance network N.

### Pseudocode
In the Global directory, sort the instance tracking directories in ascending order of capacity.<br>
Give the base copy of N a unique id if it doesn't already have one.

### Outputs
- None.

## Placeholders
In the file management system, a placeholder for a file or folder named F is an empty folder named PLACEHOLDER-F.

## Stale Folder
A stale folder is a folder that has been removed from system data, but remains in one or more copies in a network.<br>
Officially, stale folders in a copy are classified as duplicates.<br>
Stale folders can be safely ignored. Because they are not in system data, the fill unused space algorithm will not interact with them.<br>
They can also be removed just like any other folder in Backup-Storage.

## User Controlled File / User Controlled Folder
### Strict
A file or folder F in a directory D is a user controlled file if every directory in the path of F after D was created by the user.

### Flexible
A file or folder F in a directory D is a user controlled file if for every directory P in the path of F after D, there is no program that relies on P being in its current location to perform any current functions.<br>
The purpose of this definition is to allow users to classify some files or folders that they did not create as 'user controlled'.<br>
On my own machine for example, I did not create the folder 'Pictures/Screenshots', but I fully control its content via the Snipping Tool program, so I classified it as a user controlled folder, moved it to Protected-Pictures, and changed the Snipping Tool's save folder to Protected-Pictures/Screenshots.